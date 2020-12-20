# -*- coding: utf-8 -*-

from nonebot import on_command
from nonebot.rule import regex
from nonebot.adapters.cqhttp import Bot, Event
from .gacha import *

arknights = on_command("抽卡", rule=regex(r"\d{1,2}$"), priority=4)


@arknights.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数 1, 10
    if args:
        state["roll_times"] = args  # 如果用户发送了参数则直接赋值


@arknights.got("roll_times", prompt="单抽输入1, 十连输入10")
async def handle_city(bot: Bot, event: Event, state: dict):
    roll_times = state["roll_times"]
    # 在这里对参数进行验证
    if state["roll_times"] not in ["1", "10"]:
        await arknights.finish("不支持自定义次数抽卡")

    result_list = await arknights_gacha(int(roll_times))
    await arknights.finish(result_list)
