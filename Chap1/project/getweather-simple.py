#! python3
"""
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""
from textwrap import dedent


weather_info = open("weather_info.txt", 'r', encoding = "utf-8")
weather_dic = {}

for line in weather_info:
    templist = line.split(',')
    weather_dic[templist[0]] = templist[1].strip()

weather_info.close()

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
        print(f"历史查询记录：{','.join(i for i in history)}")
        break

    elif userinput == "history":
        print(f"历史查询记录：{','.join(i for i in history)}")

    else:
        print(weather_dic.get(userinput, f"不存在{userinput}的天气记录！"))
        history.append(userinput)
