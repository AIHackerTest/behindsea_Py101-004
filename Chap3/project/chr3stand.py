import os
from flask import Flask, request, session, render_template
from Weather.Weather import Weather


app = Flask(__name__)
app.secret_key = os.urandom(24)


def help():
    return """<h3>帮助</h3>
    <p>输入城市名和指定的起始天数，</p>
    <p>并点击查询查询该城市的天气数据；</p>
    <p>点击帮助，获取帮助文档；</p>
    <p>点击历史，获取历史查询信息；</p>"""


@app.route('/', methods=['GET', 'POST'])
def getweather():
    if request.method == "GET":
        startRange = [str(i) for i in range(0, 15)]
        daysRange = [str(i) for i in range(1, 8)]
        return render_template('index.html', outputdata='', startRange=startRange, daysRange=daysRange)

    elif request.method == "POST":
        action = request.form['action']
        startRange = [str(i) for i in range(0, 15)]
        daysRange = [str(i) for i in range(1, 8)]
        weath = Weather()
        try:
            history = session['history']
        except:
            history = {}

        if action == "查询":
            city = request.form['city']
            start = request.form['start']
            days = request.form['days']
            html = ''
            if city != '' and start in startRange and days in daysRange:
                try:
                    daily_weath = weath.getdaily(city, start, days)
                    # 若返回错误信息则打印错误信息与代码
                    if 'status_code' in daily_weath[1]:
                        html = f"没有找到[{city}]的天气信息"
                    else:
                        html = weath.printdaily(daily_weath[1])
                        history[city] = daily_weath[1]
                        session['history'] = history
                except:
                    html = "查询错误！"
            outputdata = html

        elif action == "历史":
            if len(history) > 0:
                html = "<h3>历史查询记录</h3>"
                i = 1
                for h_weather in history.values():
                    html += "<br/>"
                    html += f"{i}. "
                    html += weath.printdaily(h_weather)
                    i += 1
                outputdata = html
            else:
                outputdata = "没有任何记录"

        elif action == "帮助":
            outputdata = help()

        else:
            outputdata = ""

        return render_template('index.html', outputdata=outputdata, startRange=startRange, daysRange=daysRange)


if __name__ == '__main__':
    app.run(debug=True)
