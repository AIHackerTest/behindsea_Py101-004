# Python2与Python3主要区别（Windows）
## 开发环境
操作系统：Windows

终端：Cmder

Python版本：3.6.0

## 使用特定版本的Python
场景：同时安装Python2与Python3后，但又要使用不同版本的Python运行程序。

解决方案：当安装Python3时，安装程序会在系统目录下安放一个py.exe文件。这个文件允许我们选择使用特定版本的Python来运行程序。

具体用法如下：
> py -2/-3 codefile.py [argv]
- 第一个参数，选择使用2或3对应相应的Python版本
- 第二个参数，具体需要执行的Python代码文件
- 其余参数，运行所需参数

如果不希望在每次执行时使用-2/-3参数，可以在Python代码文件中最开始加入一行
> #! python2

或者

> #! python3

这样py.exe就会自动选择使用对应的Python版本来执行

## Python3与Python2的一些区别

这里的主要内容摘抄自https://docs.python.org/3/whatsnew/3.0.html

### Python新特性
1. print语句更改为print()函数，要带括号使用。

Python3中，print("a", "b")会输出“a b”，

2. 一些常见的API不再返回List类型：
  - 字典类型的方法dict.keys(),dict.values()返回值为视图（views）,因此对返回值不能使用sort()，使用sorted(dict)代替
  - dict.iterkeys(),dict.iteritems(),dict.itervalues()不再支持
  - map()和filter()返回迭代器。
  - range()的功能更改为类似xrange()，并且可以随意指定数字,后者取消
  - zip()现在返回迭代器
  - 另外,可以使用list()函数将变化后的数据转换为list类型

3. 关于比较运算符(<, >=, <=, >)现在只能用在有意义的比较下，否则会报错

4. 数字类型的变化
  - long数字类型现在合并到int数字类型。
  - 运算符 1 / 2 现在返回float类型，即0.5
  - 使用 1 // 2 来达到舍弃小数位，仅保留整数位的效果。
  - repr()关于长整型的返回值不再包含尾部的L，因此不能手动舍弃最后一位，否则会伤害数据。推荐直接使用str()代替
  - 八进制类型不再使用"0720"格式，而使用"0o720"

5. 所有关于二进制数据和Unicode字符数据均有所改变
