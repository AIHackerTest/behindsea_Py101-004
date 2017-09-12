# 第一周日记

前五天就略，之前已经写过的第一周复盘算是前四天的任务了

## 170811 0wd5

### 探索记录：

1. 1h 完成了第一周的作业提交，写了完成作业过程中的收获
- 30min 查看issue中问题  
- 2h 查看开智学习卡片，杨志平对编程学习的建议及对本课程的定义
- 1h 查看Learn Python 3 The Hard Way第43讲内容，手动输入代码

### 复盘 & 改进：
今天有哪些收获？

有哪些有用的经验、技巧可以在未来复用？

哪些地方做得不好？打算如何改进？

#### 收获和经验：
1. 首先是对本周课程作业中涉及到的重要知识点进行了回顾和加深印象：如list、random、join等

2. 查看其他人的作业，发现了set()函数，用作将集合中的元素分组，编程无重复的内容。这是在编程设想中需要的函数，但并没有查到。

3. 学习exercise 43 前面的说明内容。get到“自顶向下”的设计技能：
  - 尽可能的去想象，并用文字、图表、图像等一切形式记录下所有的需求和设想。包括场景，功能，动作等一切能够想到的事物，并用文字记录下来

  - 将所有的描述归纳，成为较为系统的说明

  - 提炼说明中的名词、动词。名词用作类名，动词作为函数（方法）名。

  - 提炼这些名词之间的联系，以图形、或者表格的形式记录成树状图。确立继承关系。

  - 写下程序的骨架，仅仅包括类名、继承关系、函数和方法名等，然后调试。调试成功之后就继续加上核心执行代码继续调试……以此类推，直至完成整个程序。

#### 不好的地方
1. 观看视频之后没有及时复盘记录所看到的东西，好多东西都忘记了。

2. 作息饮食紊乱。中午吃饭后一点多，没有及时午休，导致下午15时以后困顿睡到18点过，而且睡眠质量并不好。晚上吃太多，导致身体躁动，不能静下来好好写代码。以后尽量调整好作息和饮食，使自己能够有更好的状态进行工作和学习。


## 170812 0wd6
### 探索记录
花费时间1h30min，照着书修改完成exercise 43
  - 1h 对照书输入代码
  - 30min 查找错误
### 收获和经验
1. 类的方法中存在不能使用self的方式。当调用类未实例化的情况下，定义方法时不能在方法中添加self参数。

```python
  class Dog(object):
    def walk():
      print("I' walking")

  Dog.walk()  

  # 输出结果I' walking.已测试。
  ```
2. 字典不仅可以用来存储静态的变量，甚至可以用来存储实例化的类。参见：

```Python
# 带括号的都是类
scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
}
```
3. 调试方法：`print()`当前位置的变量内容

### 不好的地方
遇到问题时不是第一时间看代码，查错误，而是重复操作好多遍。没有第一时间反应过来需要将错误信息放到Google中去查。因此浪费了许多时间。

今后遇到错误后处理步骤：

1. 根据命令行中提示的错误行去查看指定行是否有错误；
2. 在程序运行的路径上安插`print()`打印变量值或者类名；
3. 在Google中输入错误信息，查找可能存在的问题；
4. 在GitHub中发issue向同学提问。

## 170813 0wd7
### 探索记录
1. 30min 分析并写下ex43的组织结构。
2. 1h20min 完成第二周作业，查询天气程序。

### 收获与经验

1. open()函数打开文件时，可以直接指定字符编码；
2. 声明字典类型用{}(大括号)
3. `for x in xs`类型迭代可以嵌套
4. file逐行遍历可以用`for line in file`,也可以用`file.readline() `加while循环
### 不好的地方
1. 似乎太过于需要外界的赞赏了。本就比别人多很多的编程经验，轻松完成任务是很正常的事情。如此似乎有些过了。
2. 查询python的documentation似乎不太熟练。大多数方法在此均有记录，但是每次使用时不能清楚的查到，导致浪费很多时间。