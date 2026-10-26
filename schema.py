# 作者：小明
# 项目：day21
# 文件：schema.py
# 时间：2026/10/26 10:55
# pydantic 主要用于数据格式验证
from pydantic import BaseModel, Field
import json
import re


class Ticket(BaseModel):
    intent: str = Field(description='工单意图')
    time: str | None = Field(None, description='时间')
    people: int = Field(1, description='人数')
    position: str | None = Field(None, description='地点')


def parse_json(text: str):
    """容错解析：优先 json.loads，失败则正则截取首个 {...} 块。"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        try:
            return json.loads(m.group(0)) if m else None
        except:
            return None
