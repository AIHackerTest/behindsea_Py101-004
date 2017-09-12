# super()的作用和变化
## super()作用
super()在类的继承中起到调用父类的作用。

在初始化类时非常有用，可以直接调用父类的初始化函数不用再次写相关代码。这样做的好处是提高了代码复用率，同时也给维护增加了很大的便利性。例如：

```python
class A(object):
  def __init__(self, argv1, argv2):
    self.thing1 = argv1 * 10 / 2
    self.thing2 = f"this is {argv2}"

class B(A):
  def __init__(self, argv1, argv2, argv3):
    super().__init__(argv1, argv2)
    self.thing3 = int(argv3)
```
可以看到，如果不使用super()，那么就需要将复杂的定义操作在写一遍，某种意义上来说继承的实质性作用就没有了。
## 在Python3和Python2中区别
在Python3中调用方法：
```python
 super()```
 在Python2中调用方法：
 ```python
 super(Currentclassname,self)
 ```
 二者区别是不用输入当前类名和self参数，在理解上可以更加直观，并且减少了重复输入，更便于维护。

**官方推荐使用Python3的写法。**
