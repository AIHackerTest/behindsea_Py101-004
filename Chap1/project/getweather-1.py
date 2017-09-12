#! python3
"""
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""
from textwrap import dedent

class Weather(object):

    def __init__(self):
        weather_info = open("weather_info.txt", 'r', encoding = "utf-8")
        # 从weather_info 读取数据并放入weather_dic字典中，清除字符两端空白
        self.weather_dic = {city.strip() : weath.strip() for city, weath in (line.split(',')  for line in weather_info)}

        weather_info.close()

    def getweather(self, city):
        return self.weather_dic.get(city, f"不存在{city}的天气记录！")


current_weather = Weather()
history = []

while True:

    userinput = input("请输入指令或您要查询的城市名：")

    if userinput == "help":
        print(dedent("""
        输入城市名，返回该城市的天气数据；
        输入help指令，获取帮助文档；
        输入history指令，获取历史查询信息；
        输入quit指令，退出程序；
        """))

    elif userinput == "quit":
        break

    elif userinput == "history":
        print(f"历史查询记录：{','.join(f'{city}:{current_weather.getweather(city)}' for city in history)}")

    elif userinput in current_weather.weather_dic:
        print(current_weather.getweather(userinput))
        history.append(userinput)
    else:
        print("没有指定地区的天气信息")
