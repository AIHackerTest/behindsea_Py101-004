#! python3
"""
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""
from textwrap import dedent
import requests
from sys import exit


class Weather(object):
    """天气类，用于查询和打印天气数据"""

    def __init__(self):
        """用于初始化API设置"""
        self.api = 'https://api.seniverse.com/v3/weather/now.json'
        self.key = '4r9bergjetiv1tsd'
        self.language = 'zh-Hans'
        self.unit = 'c'
        self.timeout = 1

    def getdata(self, city):
        """输入城市名查询天气数据，返回字典"""

        result = requests.get(self.api, params={
            'key': self.key,
            'location': city,
            'language': self.language,
            'unit': self.unit
        }, timeout=self.timeout)
        return result.json()

    def printdata(weath_dic):
        """根据字典参数打印返回的数据，若有错误则打印错误信息，无需实例化即可调用"""
        location = weath_dic['results'][0]['location']
        now = weath_dic['results'][0]['now']
        last_update = weath_dic['results'][0]['last_update']

        print(f"{location['name']}当前天气信息：")
        print("  天气：{}，风向：{}，温度：{}°C。".format(
            now['text'],
            now['wind_direction'],
            now['temperature']))
        print("  更新时间:", last_update)

class Action(object):
    """用于执行指定指令，包括help、history"""
    def help():
        print(dedent("""
            ----本程序数据由心知天气提供------
            输入城市名，返回该城市的天气数据；
            输入help指令，获取帮助文档；
            输入history指令，获取历史查询信息；
            输入quit指令，退出程序。"""))

    def history(history):
        if len(history) > 0:
            print("历史查询数据如下：")
            for h_weather in history.values():
                Weather.printdata(h_weather)
        else:
            print('尚未查询过任何城市')

    def quit():
        exit(0)



# 以下是运行程序，当直接执行本文件时执行，被引用时不执行
if __name__ == '__main__':
    weath = Weather()
    history = {}

    Action.help()

    while True:

        userinput = input("请输入指令或您要查询的城市名：")

        if userinput == "help":
            Action.help()

        elif userinput == "quit":
            Action.quit()

        elif userinput == "history":
            Action.history(history)

        else:
            try:
                city_weath = weath.getdata(userinput)

                # 若返回的是错误代码则报错
                if 'status_code' in city_weath:
                    print(f"ErrorCode:{city_weath['status_code']} Error:{city_weath['status']}")
                else:
                    Weather.printdata(city_weath)
                    history[userinput] = city_weath

            except requests.exceptions.ReadTimeout:
                print("查询超时...请稍后再试！\n")
