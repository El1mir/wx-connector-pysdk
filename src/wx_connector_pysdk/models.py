from typing import List

class WMessage:
    """
    WMessage类是转换后的消息数据结构
    转换自WMessageSource类
    转换了枚举 int 值到好理解的枚举项字面量
    """
    MsgType: str
    MsgSourceType: str
    MsgSenderType: str
    MsgOriginType: str
    MsgContent: List[str]
    MsgSenderName: str
    MsgFromWindow: str

    def __init__(
            self,
            msg_type: str,
            msg_source_type: str,
            msg_sender_type: str,
            msg_origin_type: str,
            msg_content: List[str],
            msg_sender_name: str,
            msg_from_window: str
    ):
        self.MsgType = msg_type
        self.MsgSourceType = msg_source_type
        self.MsgSenderType = msg_sender_type
        self.MsgOriginType = msg_origin_type
        self.MsgContent = msg_content
        self.MsgSenderName = msg_sender_name
        self.MsgFromWindow = msg_from_window


def convert_msg_type(msg_type: int) -> str:
    """将消息类型int转换为对应的字符串"""
    msg_type_map = {
        0: "Text",
        1: "Image",
        2: "Video",
        3: "Emoji",
        4: "File",
        5: "MiniProgramCard",
        6: "MergeForward",
        7: "Voice",
        8: "Transfer",
        9: "Quote"
    }
    return msg_type_map.get(msg_type, "Unknown")

def convert_msg_source_type(msg_source_type: int) -> str:
    """将消息来源类型int转换为对应的字符串"""
    msg_source_type_map = {
        0: "Human",
        1: "System"
    }
    return msg_source_type_map.get(msg_source_type, "Unknown")

def convert_msg_sender_type(msg_sender_type: int) -> str:
    """将消息发送者类型int转换为对应的字符串"""
    msg_sender_type_map = {
        0: "Self",
        1: "Friend"
    }
    return msg_sender_type_map.get(msg_sender_type, "Unknown")

def convert_msg_origin_type(msg_origin_type: int) -> str:
    """将消息原始类型int转换为对应的字符串"""
    msg_origin_type_map = {
        0: "Single",
        1: "Group"
    }
    return msg_origin_type_map.get(msg_origin_type, "Unknown")
