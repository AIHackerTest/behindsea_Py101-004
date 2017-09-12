# 天气查询程序web版说明

## 运行环境
python3.6 + requests + flask

## 使用方法
天气查询程序web版部署在本地，用于查询从起始日期开始的指定天数的天气预报信息。
1. 查询天气
  - 输入城市
  - 选择起始日期（以今天为0）
  - 查询的天数
  - 点击查询按钮
2. 查看历史查询数据
  - 点击历史按钮
3. 查看帮助信息
  - 点击帮助按钮

## 错误信息
1. 没有找到[{city}]的天气信息
  - 即没有找到指定城市的天气信息，可能是城市输入错误，或者天气预报服务未覆盖到该地区
2. 查询错误！
  - 在查询或者显示过程中出现不可预期的错误，可能是网络未连接或者网络服务器没有响应。