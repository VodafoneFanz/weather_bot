# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import regex
from nonebot.adapters.cqhttp import Bot, Event
from .get_weather import get_weather, judge_city

"""
1   输入/天气
    输入城市，寻找城市，如果存在运行get_weather，如果不存在返回提示
2   输入/天气 [城市名称]
    直接执行 
"""

# 事件响应器
weather = on_command("天气", rule=regex(r"\w{2,5}$"), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    if not judge_city(city):
        await weather.finish("你想查询的城市暂不支持，关闭请求!")
    else:
        city_weather = await get_weather(city)
        await weather.finish(city_weather)

# async def get_weather(city: str):
#     return f"{city}的天气是..."
