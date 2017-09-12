# 第二周记录
## 170828 3wd1
### 探索记录
探索4h，其中2h完成大作业收尾工作
1. 使用session存储历史数据
2. 使用CSS对网页布局
3. 对flask响应POST方法和GET方法
4. 使用flask模板功能

### 经验与收获
1. 使用session时应当设置app.secret_key = 'any random string'，可以用任意字符串，os.urandom(24)
2. session['var'] = var 中的var数据，若是object时需要是可以被转换为json的，否则会报错
3. CSS中的设置可以直接抄比较流行的网站
4. 使用{{outputdata|safe}}格式的写法使文本不会被转码，保持HTML代码形式
调试时打开bebug模式app.run(debug = True)
