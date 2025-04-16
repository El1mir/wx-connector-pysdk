# wx-connector-pysdk
## 写在前面
欢迎各位给项目提出建议和问题，欢迎提出 issue 和 pr

主操作封装库：[GitHub | WxConnectorLib](https://github.com/El1mir/WxConnector)

Api提供连接件：[GitHub | WxConnectorProvider](https://github.com/El1mir/WxConnectorProvider)

求佬们给用的到的项目点点 Star 谢谢喵

## 项目介绍
本项目是 WxConnector 系列项目的 python 开发 sdk

对 WxConnectorProvider 提供的 api 进行封装，提供了简单易用的接口

PyPi 包页面：
[PYPI | wx-connector-pysdk](https://pypi.org/project/wx-connector-pysdk/)
## 使用方法
### 环境安装
我们需要先安装 dotnet 8.0 runtime 环境

可以在
[Download Dotnet 8.0](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
该URL中的 `.NET Desktop Runtime 8.0.x`中获取

也可以在 
[123云盘文件分享 | Dotnet-Runtime-8.0.15-win-x64](https://www.123912.com/s/trNHjv-Ai9GA)
中获取
### 安装主程序
在 
[GitHub | WxConnectorProvider](https://github.com/El1mir/WxConnectorProvider)
的 `Release` 页面中下载最新版的安装包安装

使用前双击启动主程序即可
### 在 python 项目中安装 sdk
使用pip
```
pip install wx-connector-pysdk
```
或使用 uv
```
uv add wx-connector-pysdk
```
### 使用示例
```python
# 设置 WxConnectorProvider 的 Url
set_url("localhost:8022")
# 启动 WeChat
strat_wx(r"C:\Program Files\Tencent\WeChat\WeChat.exe")
# 启动监听并添加监听事件
start_listeners(["小米"])
# 启动本地事件监听
start_event_listen()

# 添加事件处理函数
@event.on("NewMessageWithoutSelfEvent")
def handle_new_msg(msg: WMessage) -> None:
    print(f"从{msg.MsgFromWindow}窗口收到{msg.MsgSenderName}的信息说：{msg.MsgContent}")

time.sleep(30)
# 发送测试消息
send_text("测试消息","小米")
```
### 开发文档
开发文档还在路上喵，请各位小看一下只有100行的简单代码凑合一下喵

on 方法支持的事件列表请看 

[ApiFox | WxConnectorProvider](https://3rr385280j.apifox.cn/3621830w0)
