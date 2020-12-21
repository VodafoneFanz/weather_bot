#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from  nonebot.adapters.cqhttp import Bot
from nonebot.log import logger, default_format

# Custom your logger
# 
# from nonebot.log import logger, default_format
logger.add("error.log",
           rotation="00:00",
           diagnose=False,
           level="ERROR",
           format=default_format)

# You can pass some keyword args config to init function
# 初始化
nonebot.init()
app = nonebot.get_asgi()
# 全局Driver
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", Bot)
# 加载插件
nonebot.load_builtin_plugins()
nonebot.load_plugins("src/plugins")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.run(app="bot:app")
