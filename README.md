# AndroidProjectNameCounter
### 获取你的安卓项目有多少字，支持智能分类代码文件进行统计

###

## 使用方法：
### 1. 从[Github Release](https://github.com/wanxiaoT/AndroidProjectNameCounter/releases/tag/1.0) 将 AndroidProjectNameCounter.py 下载到你的电脑
### 2. cmd运行```py AndroidProjectNameCounter.py```
### 3. 以[wanxiaoT/TChat: 开源的AI聊天软件](https://github.com/wanxiaoT/TChat)为例，运行结果如下：
```C:\1Git\AndroidProjectNameCounter>py AndroidProjectNameCounter.py
    Android Studio 项目代码量统计工具
    By wanxiaoT
    Github: https://github.com/wanxiaoT

📁 请输入 Android Studio 项目路径: C:\Users\Administrator\AndroidStudioProjects\TChat

🔍 正在扫描项目: C:\Users\Administrator\AndroidStudioProjects\TChat

============================================================
文件类型            文件数        行数           字符数             字符(无空格)
------------------------------------------------------------
Kotlin          171        44,371       1,577,865       948,419
XML             16         269          13,187          11,119
Gradle KTS      7          280          7,209           5,771
Properties      2          40           2,096           1,826
JSON            1          44           2,137           1,788
============================================================
📊 总计            197        45,004       1,602,494       968,923
============================================================

📈 详细统计:
   • 总文件数: 197 个
   • 总代码行数: 45,004 行
   • 总字符数: 1,602,494 字符
   • 总字符数(不含空格): 968,923 字符

💡 提示: 如果代码主要是英文，约等于 968,923 个字符

✅ 统计完成！

按 Enter 键退出...```