# ch1 学习日记

## 170814 1wd1
### 探索记录
今天学习编程2h，完成任务：提交完成任务issue并且对前两位同学的代码作出评判。

### 收获和经验
1. 再次被提醒open的文件需要close。这对于文件读写是一项很重要的操作。
2. 知道了with...as...语句，似乎可以用在指定名称上。
3. 知道了if x in y的判断操作可以用在分支if...else...操作上。

### 不好的地方
对于打开的文件不知道close，这是个很不好的习惯，以后要注意改正。对于所有open的对象需要使用close方法关闭释放资源。

## 170815 1wd2
### 探索记录
昨天练习编程1h，回答同学的提问。并查看相关资源。

### 收获和经验
1. 了解了with...as...语句。与C#中Using语句类似。打开的资源就不需要close了，而且如果出现错误，就直接exit了

## 170816 1wd3

### 探索记录
查看仓库issue，大约花费1h，帮助同学解决代码结果不符合想象问题

### 收获和经验

变量要先赋值后使用才会得到相应结果。

## 170817 1wd4
### 探索记录
花费1h，查看learn python 3 the hard way第46将文字内容，发现主要任务就是写下python project的模板，方便以后取用。
### 收获和经验
没有具体的收获。

## 170818 1wd5
### 探索记录
这几天状态一直不太好，无所事事中。

1h，根据教练的评价修改代码，结果修改过程中造成死循环，经过查看代码找出bug。经过简化，错误结构大致如下：

```python
for city in list:
  list.append(city)
```
在循环中不停地给list加码，导致永远不能完成。

另1h，无所事事瞎逛中。

### 收获与经验
知道for x in list 中，list不是作为固定的值存在，可以被动态更改而造成死循环或者其它意外情况。

## 170819 1wd6
### 探索记录
1. 1h 练习lpthw ex46 项目框架 ex47单元测试内容
2. 2h 安装探索Ubuntu 16.04 系统

### 收获与经验

1. 系统还是熟悉的好，具有趁手的工具，方便实现复杂动作。
2. 安装使用virtualenv包可以创建镜像python运行环境，与主目录具有不同的安装包。
  - 使用virtualenv -system-site-packages (dirpath)命令可以在dirpath中镜像一个python运行环境，并且安装指定的包，专门用于开发某一项目。
  - 可用于指定不同的python版本开发。
3. 单元测试模块nose
  - cd到项目根目录，使用nosetests命令执行单元测试
  - 注意要将文件名命名为NAME_tests.py并保存到tests目录下才能执行
  - 如果要在NAME_test.py中使用import Name.packagename需要在NAME文件夹下放置\__init\__.py文件

### 不好的地方

1. 对单元测试nose模块尚不清楚
2. virtualenv模块使用不熟练，没有查到如何虚拟不同版本的python
3. 探索Ubuntu花费太多时间，没有预料到转换系统后很多工具没有了，尤其是必备的工具有没有替代等事宜。导致措手不及。

## 170820 1wd7

### 探索记录
1. 2h 编写最基本的查询功能
  - 2min requests模块安装
  - 50min 天气查询API寻找，注册账号获取key，研究API的调用方法。
  - 20min json类型探索(后来证明并不需要那么久)，结果是知道了object类型会被转换成字典，使用字典的取数方法可以得到相应的值
  - 40min 修改weather类的getdata方法，确定返回值类型，并根据返回值类型确定打印方式。
2. 1h 修改程序并调试错误
  - 30min 调试程序
  - 30min 重组程序，新增Action类，将打印天气数据的代码封装到Weather类的printdata方法中
3. 30min 编写程序说明及写日志
## 收获与经验
1. 新技能get。
2. 知道了json数据的转换方法，object数据会被转换为字典。使用字典的操作方式就可以获取想要的数据。
3. 知道了requests模块的简单操作方法。直接requests.get就可以。不知道是不是还有post方法。
4. 错误处理，get到了KeyError和requests.exceptions.ReadTimeout两个错误，并输出处理代码。
