# 04 用 SwiftUI 做出你的第一个 App

这一章我们做一个真实的、完整的、可以直接拿去上架的 App：一个倒数日工具。输入「发工资」和日期，它告诉你还有几天；输入「入职」和过去的日期，它告诉你已经过了几天。

为什么选它？因为这类 App 满足第一章说的全部「新手友好」条件：纯本地运行、不要服务器、不碰用户隐私数据、功能边界清晰。而且 App Store 上同类产品（Days Matter 等）常年活在效率榜上——它小，但它是个真产品。

整个 App 的核心代码不到 150 行。**SwiftUI 的杠杆率就在这里：你描述界面长什么样，系统负责把它画出来、管理好。**

---

## 一、SwiftUI 的三个核心概念

写代码前，先用三分钟建立心智模型。SwiftUI 只需要先理解三件事：

**第一，界面是「声明」出来的。** 你不写「创建一个按钮、设置颜色、添加到屏幕」这种指令序列，而是直接描述结果：

```swift
VStack {
    Text("还有 14 天")
        .font(.largeTitle)
    Text("发工资")
        .foregroundStyle(.secondary)
}
```

`VStack` 是竖向排列，`HStack` 是横向排列，`Text` 是一段文字，后面用点语法链式修饰样式。读起来几乎是英文白话。

**第二，界面是状态的函数。** 用 `@State` 标记的变量一旦改变，所有用到它的界面会自动刷新：

```swift
@State private var count = 0

Button("点了 \(count) 次") {
    count += 1   // 改这个变量，按钮文字自动更新
}
```

没有「手动刷新界面」这个操作。你只管改数据，界面跟着数据走。

**第三，一切皆 View，View 可以组合。** 复杂界面就是小 View 拼出来的大 View，像搭积木。

掌握这三点，下面的代码你就能读懂八成。

## 二、创建项目

打开 Xcode，Create New Project → iOS → App，填写配置：

| 字段 | 填什么 | 说明 |
|------|------|------|
| Product Name | DayCount | App 的项目名，之后可以改显示名 |
| Organization Identifier | com.你的名字 | 例如 com.wanghe，构成 Bundle ID 的前缀 |
| Interface | SwiftUI | 界面框架 |
| Language | Swift | 语言 |
| Testing System | None | 第一个项目先不管测试 |

这里的 **Bundle ID**（如 `com.wanghe.DayCount`）值得多看一眼：它是你的 App 在苹果体系里的全球唯一身份证，上架后永远不能改。Organization Identifier 用「倒写的域名」是惯例，没有域名就用 `com.` 加你的常用 ID。

## 三、数据模型：一个倒数日是什么

新建文件 `Event.swift`，定义数据结构：

```swift
import Foundation

struct Event: Identifiable, Codable {
    var id = UUID()
    var title: String
    var date: Date

    // 距今天数：未来为正，过去为负
    var daysFromNow: Int {
        let start = Calendar.current.startOfDay(for: Date())
        let end = Calendar.current.startOfDay(for: date)
        return Calendar.current.dateComponents([.day], from: start, to: end).day ?? 0
    }
}
```

逐行拆解：

- `struct Event` 定义了「一个倒数日」：标题加日期，再加一个自动生成的唯一 id
- `Identifiable` 协议让它能被列表识别，`Codable` 协议让它能被序列化成 JSON 存盘——Swift 里很多能力是靠「声明遵守某个协议」免费获得的
- `daysFromNow` 是计算属性：每次读取时现场计算距离今天多少天。用 `startOfDay` 对齐到零点，避免「还有 0.6 天算不算 1 天」的歧义

## 四、主界面：列表与状态

把项目自带的 `ContentView.swift` 改成下面这样，这是整个 App 的主界面：

```swift
import SwiftUI

struct ContentView: View {
    @State private var events: [Event] = []
    @State private var showingAdd = false

    var body: some View {
        NavigationStack {
            List {
                ForEach(events) { event in
                    HStack {
                        Text(event.title)
                        Spacer()
                        Text(label(for: event))
                            .font(.title3.bold())
                            .foregroundStyle(event.daysFromNow >= 0 ? .blue : .secondary)
                    }
                }
                .onDelete { events.remove(atOffsets: $0); save() }
            }
            .navigationTitle("倒数日")
            .toolbar {
                Button("添加", systemImage: "plus") { showingAdd = true }
            }
            .sheet(isPresented: $showingAdd) {
                AddEventView { newEvent in
                    events.append(newEvent)
                    events.sort { $0.date < $1.date }
                    save()
                }
            }
            .overlay {
                if events.isEmpty {
                    ContentUnavailableView("还没有倒数日",
                        systemImage: "calendar.badge.plus",
                        description: Text("点右上角的 + 添加第一个"))
                }
            }
            .onAppear(perform: load)
        }
    }

    private func label(for event: Event) -> String {
        let d = event.daysFromNow
        if d == 0 { return "今天" }
        return d > 0 ? "还有 \(d) 天" : "已 \(-d) 天"
    }

    private func save() {
        if let data = try? JSONEncoder().encode(events) {
            UserDefaults.standard.set(data, forKey: "events")
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: "events"),
              let saved = try? JSONDecoder().decode([Event].self, from: data)
        else { return }
        events = saved
    }
}
```

这段代码浓缩了一个典型 SwiftUI App 的全部骨架，几个关键点：

- 两个 `@State`：`events` 是数据本身，`showingAdd` 控制「添加」弹窗开关。整个界面就是这两个状态的投影
- `List` 加 `ForEach` 把数组渲染成列表，`.onDelete` 一行就获得了左滑删除
- `.sheet` 是从底部弹出的模态页，绑定在 `showingAdd` 上：状态变 true 它就弹出
- `ContentUnavailableView` 是系统自带的空状态页——**空状态不是装饰，审核员打开你的 App 时看到的第一屏往往就是它**
- `save()` 和 `load()` 用 UserDefaults 存取 JSON。对于几十条以内的小数据，这是最简单可靠的持久化方案，不需要数据库

## 五、添加页面：表单与回调

再新建一个 `AddEventView.swift`：

```swift
import SwiftUI

struct AddEventView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var title = ""
    @State private var date = Date()
    let onSave: (Event) -> Void

    var body: some View {
        NavigationStack {
            Form {
                TextField("名称，例如：发工资", text: $title)
                DatePicker("日期", selection: $date, displayedComponents: .date)
            }
            .navigationTitle("添加倒数日")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("取消") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("保存") {
                        onSave(Event(title: title, date: date))
                        dismiss()
                    }
                    .disabled(title.isEmpty)
                }
            }
        }
    }
}
```

两个新概念：

- `$title` 里的美元符号表示「双向绑定」：输入框改文字，变量跟着变；变量变，输入框也跟着变
- `onSave` 是一个函数类型的属性，子页面填完数据，通过它把结果「回传」给主界面。这是 SwiftUI 里页面间传数据最常用的模式之一

按 ⌘R 运行。添加几条倒数日，左滑删除一条，杀掉 App 重开——数据还在。**这就是一个功能完整的 App 了。**

## 六、收尾：让它从 Demo 变成产品

上架前还差几个小动作，都在项目设置（点导航区最顶上的项目图标）里：

- **Display Name** 改成「倒数日」——桌面图标下显示的名字，可以是中文
- **iPhone Orientation** 只勾 Portrait（竖屏），小工具锁竖屏能省掉一半的布局适配
- **Minimum Deployments** 保持默认或设为前一两个大版本，覆盖绝大多数活跃设备
- 试一下深色模式（模拟器里 ⌘⇧A 切换）：我们全程用的系统颜色（`.blue`、`.secondary`），深色模式自动适配——这是优先用系统样式的红利

另外两个此刻不用做、但要知道的事：图标和截图放在第八章统一处理；如果想加更多功能（通知提醒、小组件），克制住，先把这一版送上架。

## 七、卡住了怎么办

新手三个最高频的报错：

- **「Cannot find 'XXX' in scope」**——名字拼错了，或者那个文件没创建。Swift 区分大小写
- **预览（Canvas）一直转圈**——点预览区的刷新按钮（⌘⌥P）；再不行，⌘R 直接跑模拟器，预览坏了不影响真实运行
- **改了代码没反应**——⌘B 重新构建一次；Xcode 偶尔抽风，重启它是合法手段

更通用的方法：把报错信息原文丢给 AI，附上相关代码。SwiftUI 的报错信息以晦涩著称（一个分号错误可能报在十行之外），AI 解读报错是当下最划算的用法。

---

## 写在最后

这一章的全部代码加起来不到 150 行，但它覆盖了 SwiftUI 的主干道：状态驱动界面、列表、表单、页面跳转、数据持久化。之后做任何 App，都是在这副骨架上换肌肉。

模拟器里它已经跑起来了。下一章，我们把它装进你口袋里的真 iPhone——顺便跨过整条链路上最让人头疼的一关：证书和签名。
