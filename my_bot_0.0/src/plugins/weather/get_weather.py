# -*- coding: utf-8 -*-

import urllib.request
import json
import gzip


def judge_city(city: str):
    # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city)
    # 发出请求并读取到weather_data
    weather_data = urllib.request.urlopen(url).read()
    # 以utf-8的编码方式解压数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    # 将json数据转化为dict数据
    weather_dict = json.loads(weather_data)

    if weather_dict.get('desc') == 'OK':
        return True
    else:
        return False


async def get_weather(city: str):
    """
    :param city: 城市名称
    :return: 搜索成功=>天气信息 搜索失败=>有误信息
    """

    # judge_city(city)
    # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city)
    # 发出请求并读取到weather_data
    weather_data = urllib.request.urlopen(url).read()
    # 以utf-8的编码方式解压数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    # 将json数据转化为dict数据
    weather_dict = json.loads(weather_data)

    forecast = weather_dict.get('data').get('forecast')

    today = '城市：' + weather_dict.get('data').get('city') + '\n' \
            + '日期：' + forecast[0].get('date') + '\n' \
            + '温度：' + weather_dict.get('data').get('wendu') + '℃\n' \
            + '高温：' + forecast[0].get('high') + '℃\n' \
            + '低温: ' + forecast[0].get('low') + '℃\n' \
            + '风向：' + forecast[0].get('fengxiang') + '\n' \
            + '风力：' + forecast[0].get('fengli') + '\n' \
            + '天气：' + forecast[0].get('type') + '\n' \
            + '感冒：' + weather_dict.get('data').get('ganmao') + '\n'

    return today
