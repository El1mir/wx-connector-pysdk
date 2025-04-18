# -*- coding: utf-8 -*-
import json
import time
from threading import Thread
from typing import Callable, Dict, TypeVar, Optional

import requests
import websocket
from websocket import WebSocketApp, WebSocket

from wx_connector_pysdk.models import *

# 定义严格的回调函数类型
WMessageHandler = Callable[[WMessage], None]
# 定义类型变量 T，限定为 WMessageHandler 类型
T = TypeVar('T', bound=WMessageHandler)

"""
url_base 形式为 localhost:port
"""
url_base: str = ""
event: Optional['EventManager'] = None

class EventManager:
    ws: WebSocketApp
    callbacks: Dict[str, List[Callable[[WMessage],None]]]

    def on(self, eventType: str) -> Callable[[T], T]:
        """
        用于定义事件处理函数
        """

        def decorator(func: T) -> T:
            if self.callbacks.get(eventType) is None:
                self.callbacks[eventType] = [func]
            else:
                self.callbacks[eventType].append(func)
            return func

        return decorator

    def __init__(self, base_url: str):
        self.callbacks = {}
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(f"ws://{base_url}/api/Event/ws",
                                    on_message=self._on_message
                                    )
        Thread(target=ws.run_forever).start()

    def _on_message(self, _: WebSocket, message: str) -> None:
        """
        用于接收消息的回调函数
        :param message: 收到的消息
        :return: None
        """
        data = json.loads(message)
        event_type = data['eventType']
        msg = WMessage(
            convert_msg_type(data["data"]["MsgType"]),
            convert_msg_source_type(data["data"]["MsgSourceType"]),
            convert_msg_sender_type(data["data"]["MsgSenderType"]),
            convert_msg_origin_type(data["data"]["MsgOriginType"]),
            data["data"]["MsgContent"],
            data["data"]["MsgSenderName"],
            data["data"]["MsgFromWindow"]
        )
        for callback in self.callbacks.get(event_type, []):
            callback(msg)

def set_url(base_url: str) -> None:
    """
    用于设置包使用的url
    :param base_url: 传入 WxConnectorProvider 启动的url 以 localhost:port 的形式
    :return: None
    """
    global url_base
    url_base = base_url

def start_event_listen() -> None:
    """
    用于启动事件监听器（必须在设置URL之后启动）
    :return: None
    """
    global event
    event = EventManager(url_base)

def strat_wx(wx_path: str) -> None:
    """
    用于启动 WeChat
    :param wx_path: WeChat 主程序的完整路径
    :return: None
    """
    requests.post(
        f"http://{url_base}/api/Wx/startWx",
        json={"WxPath": wx_path}
    )

def start_listeners(listeners: List[str]) -> None:
    """
    用于启动 WxConnectorProvider 的监听
    打开独立监听窗口
    :param listeners: 监听对象（用户备注名和群名备注名）
    :return: None
    """
    requests.post(
        f"http://{url_base}/api/Wx/listen",
        json={"Listeners": listeners}
    )

def send_text(msg: str, send_to: str) -> None:
    """
    用于向指定窗口发送普通文本消息（支持排版和wx表情）
    只能向已经监听的对象发送文本消息（send_to，就是监听的对象名，开始监听时传的什么就用什么）
    send_to 也可以用消息对象的 MsgFromWindow 属性
    wx表情 格式为 [xxx] 可以从 wx 复制得到
    :param msg: 普通文本消息内容
    :param send_to: 用于发送的窗口（同listeners）
    :return: None
    """
    requests.post(
        f"http://{url_base}/api/Action/sendText",
        json={"Msg": msg, "SendWindowTitle": send_to}
    )

def send_file(file_path: str, send_to: str) -> None:
    """
    用于向指定窗口发送本地文件消息
    只能向已经监听的对象发送消息（send_to，就是监听的对象名，开始监听时传的什么就用什么）
    send_to 也可以用消息对象的 MsgFromWindow 属性
    :param file_path: 需要发送的本地文件的完整路径
    :param send_to: 用于发送的窗口（同listeners）
    :return: None
    """
    requests.post(
        f"http://{url_base}/api/Action/sendFile",
        json={"FilePath": file_path, "SendWindowTitle": send_to}
    )

def at_by_username_in_group(username: str, window_title) -> None:
    """
    用于在群聊内通过用户的备注名at用户
    :param username: 要 at 用户的备注名
    :param window_title: 群聊窗口的标题
    :return: None
    """
    requests.post(
        f"http://{url_base}/api/Action/AtByUserNameInGroup",
        json={"UserName": username, "WindowTitle": window_title}
    )
