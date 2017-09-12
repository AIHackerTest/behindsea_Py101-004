# 天气查询程序（终端版）使用说明

## 一、运行环境
本程序需要在python3.6环境中运行，除了python自带包外需安装requests包。

requests包安装方法：使用pip安装，在终端输入以下代码：
```
pip install requests
```
如果没有安装pip，请先安装pip。

pip安装方法：下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py),并在终端中使用以下命令运行。
```
python get-pip.py
```

## 二、使用方法和结果说明
### 简单版本getweather.py
1. 使用方法
  终端运行getweather.py
  打开终端，切换到getweather.py所在目录，运行以下命令：
```
python getweather.py
```
2. 查询帮助
  运行程序后会输出以下帮助信息：
```
输入城市名，返回该城市的天气数据；
输入help指令，获取帮助文档；
输入history指令，获取历史查询信息；
输入quit指令，退出程序。
```

3. 结果说明

  1. 正常结果

    正常情况下，程序返回结果类型如下：
    ```
    北京的天气为多云，风向为南，温度为27摄氏度。
    更新时间：2017-08-20T21:20:00
    ```
  2. 异常结果

    1. 根据输入的城市名没有查询到对应的天气数据，返回以下异常：
    ```
    城市名错误或不存在该城市的天气数据！
    ```

    2. 网络情况较差，或者数据提供商的服务器出了问题，导致查询超时，返回以下异常结果：
    ```
    查询超时...请稍后再试！
    ```

### 进阶版本superweather.py


1. 使用方法
终端运行superweather.py
```
python superweather.py
```
2. 程序帮助

  进入程序后会输出以下帮助信息：

  - 输入城市名，返回该城市的天气数据；
  - 输入"城市名/起始天/天数，查询该城市从起始天开始指定天数的天气预报信息。(起始天为0-15的数字，天数为1-3的数字)
  - 输入unit指令，可修改温度单位(c代表摄氏温度/f代表华氏温度)；
  - 输入help指令，获取帮助文档；
  - 输入history指令，获取历史查询信息；
  - 输入quit指令，退出程序。

3. 结果说明
  正常情况下，程序会返回类似的结果：
  ```
  纽约天气预报信息：
    日期：2017-09-02, 白天：晴, 夜晚：晴, 风向：西北, 温度：19°C~27°C
    日期：2017-09-03, 白天：晴, 夜晚：晴, 风向：西北, 温度：20°C~28°C
    日期：2017-09-04, 白天：晴, 夜晚：晴, 风向：东北, 温度：17°C~25°C
    日期：2017-09-05, 白天：晴, 夜晚：晴, 风向：西南, 温度：19°C~28°C
    日期：2017-09-06, 白天：小雨, 夜晚：小雨, 风向：北, 温度：22°C~29°C
    日期：2017-09-07, 白天：未知, 夜晚：未知, 风向：, 温度：°C~°C
    更新时间: 2017-08-23T12:49:31-04:00
  ```
  异常结果：
  ```
  请输入正确格式的参数.
  ```
  查询起始时间或者查询天数输入不正确
  ```
  查询超时...请稍后再试！
  ```
  网络或服务器问题，导致查询时间超过1s，返回超时
  ```
  ErrorCode:AP010010 Error:The location can not be found.
  ```
  没有查询到指定的城市