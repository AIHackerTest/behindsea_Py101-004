import requests
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

    def trantemper(self, temperature):
        """转换温度单位"""
        if self.unit == 'c':
            return f"{temperature}°C"
        elif self.unit == 'f':
            temper = float(temperature)
            f = temper * 9 / 5 + 32
            return f"{f}°F"

    def printnow(self, weath_dic):
        """根据字典参数打印返回的数据，若有错误则打印错误信息"""
        htmldata = ''
        location = weath_dic['results'][0]['location']
        now = weath_dic['results'][0]['now']
        last_update = weath_dic['results'][0]['last_update']

        htmldata += f"{location['name']}当前天气信息<br/>"
        htmldata += "  天气：{}，风向：{}，温度：{}。<br/>".format(
            now['text'],
            now['wind_direction'],
            self.trantemper(now['temperature']))
        htmldata += f"更新时间:{last_update}"
        return htmldata

    def printdaily(self, weath_dic):
        htmldata = ''
        location = weath_dic['results'][0]['location']
        daily = weath_dic['results'][0]['daily']
        last_update = weath_dic['results'][0]['last_update']

        htmldata += f"{location['name']}天气预报信息<br/>"

        for day in daily:
            htmldata += "日期：{}, 白天：{}, 夜晚：{}, 风向：{}, 温度：{}-{}<br/>".format(
                day['date'],
                day['text_day'],
                day['text_night'],
                day['wind_direction'],
                self.trantemper(day['low']),
                self.trantemper(day['high']))

        htmldata += f"更新时间:{last_update}<br/>"
        return htmldata
