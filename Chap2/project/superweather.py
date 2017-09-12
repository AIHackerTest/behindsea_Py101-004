#! python3
"""
任务：
1.输入城市名，返回该城市的天气数据；
2.输入指令，打印帮助文档（一般使用 h 或 help）；
3.输入指令，退出程序的交互（一般使用 quit 或 exit）；
4.在退出程序之前，打印查询过的所有城市。
5.查询指定日期的天气信息
6.转换温度单位
7.分别使用不同（国外）API完成以上类似动作
"""
from textwrap import dedent
import requests
from sys import exit


class Weather(object):
    """天气类，用于查询和打印天气数据"""

    def __init__(self):
        """用于初始化API设置"""
        self.nowapi = 'https://api.seniverse.com/v3/weather/now.json'
        self.dailyapi = 'https://api.seniverse.com/v3/weather/daily.json'
        self.key = '4r9bergjetiv1tsd'
        self.language = 'zh-Hans'
        self.unit = 'c'
        self.timeout = 1
        self.history = {}

    def getnow(self, city):
        """根据输入参数名查询天气数据，返回字典"""
        result = requests.get(self.nowapi, params={
            'key': self.key,
            'location': city,
            'language': self.language,
            'unit': 'c'
        }, timeout=self.timeout)
        return ['00', result.json()]

    def getdaily(self, city, start, days):
        """根据输入参数查询指定日期段的天气预报"""
        result = requests.get(self.dailyapi, params={
            'key': self.key,
            'location': city,
            'language': self.language,
            'unit': 'c',
            'start': start,
            'days': days
        }, timeout=self.timeout)
        return ['10', result.json()]

    def printnow(self, weath_dic):
        """根据字典参数打印返回的数据，若有错误则打印错误信息"""
        location = weath_dic['results'][0]['location']
        now = weath_dic['results'][0]['now']
        last_update = weath_dic['results'][0]['last_update']

        print(f"{location['name']}当前天气信息：")
        print("  天气：{}，风向：{}，温度：{}。".format(
            now['text'],
            now['wind_direction'],
            self.trantemper(now['temperature'])))
        print("  更新时间:", last_update)

    def printdaily(self, weath_dic):
        location = weath_dic['results'][0]['location']
        daily = weath_dic['results'][0]['daily']
        last_update = weath_dic['results'][0]['last_update']

        print(f"{location['name']}天气预报信息：")

        for day in daily:
            print("  日期：{}, 白天：{}, 夜晚：{}, 风向：{}, 温度：{}~{}".format(
                day['date'],
                day['text_day'],
                day['text_night'],
                day['wind_direction'],
                self.trantemper(day['low']),
                self.trantemper(day['high'])))

        print("  更新时间:", last_update)

    def trantemper(self, temperature):
        if self.unit == 'c':
            return f"{temperature}°C"
        elif self.unit == 'f':
            temper = float(temperature)
            f = temper * 9 / 5 + 32
            return f"{f}°F"


class Action(object):
    """用于执行指定指令，包括help、history"""
    def help():
        print(dedent("""
            ----本程序数据由心知天气提供------
            输入城市名，返回该城市的天气数据；
            输入"城市名/起始天/天数，查询该城市15天内天气预报信息。(起始天为0-14的数字，天数为1-7的数字)
            输入unit指令，可修改温度单位(c代表摄氏温度/f代表华氏温度)；
            输入help指令，获取帮助文档；
            输入history指令，获取历史查询信息；
            输入quit指令，退出程序。"""))

    def history(weather):
        if len(weather.history) > 0:
            print("历史查询数据如下：")
            for h_weather in weather.history.values():
                if h_weather[0] == '00':
                    weather.printnow(h_weather[1])
                elif h_weather[0] == '10':
                    weather.printdaily(h_weather[1])
        else:
            print('尚未查询过任何城市')

    def quit():
        exit(0)



# 以下是运行程序，当直接执行本文件时执行，被引用时不执行
if __name__ == '__main__':
    weath = Weather()
    startRange = [str(i) for i in range(1, 15)]
    daysRange = [str(i) for i in range(1, 8)]

    Action.help()

    while True:

        userinput = input("请输入指令或您要查询的城市名：")

        if userinput == "help":
            Action.help()

        elif userinput == "quit":
            Action.quit()

        elif userinput == "history":
            Action.history(weath)

        elif userinput == 'unit':
            uin = input("请输入温度单位(c/f)：")
            if uin == 'c':
                weath.unit = 'c'
                print("温度单位修改为摄氏温度")
            elif uin == 'f':
                weath.unit = 'f'
                print("温度单位设置为华氏温度")
            else:
                print("指定的单位类型错误")

        else:
            args = userinput.split('/')
            if len(args) == 1:
                try:
                    city_weath = weath.getnow(userinput)
                    # 若返回的是错误代码则报错
                    if 'status_code' in city_weath[1]:
                        print(
                            f"ErrorCode:{city_weath[1]['status_code']} Error:{city_weath[1]['status']}")
                    else:
                        weath.printnow(city_weath[1])
                        weath.history[userinput] = city_weath

                except requests.exceptions.ReadTimeout:
                    print("查询超时...请稍后再试！\n")
            elif len(args) == 3 and args[1] in startRange and args[2] in daysRange:
                city = args[0]
                start = args[1]
                days = args[2]

                try:
                    daily_weath = weath.getdaily(city, start, days)
                    # 若返回错误信息则打印错误信息与代码
                    if 'status_code' in daily_weath[1]:
                        print(
                            f"ErrorCode:{daily_weath[1]['status_code']} Error:{daily_weath[1]['status']}")
                    else:
                        weath.printdaily(daily_weath[1])
                        weath.history[userinput] = daily_weath
                except requests.exceptions.ReadTimeout:
                    print("查询超时...请稍后再试！\n")
            else:
                print("请输入正确格式的参数.")
