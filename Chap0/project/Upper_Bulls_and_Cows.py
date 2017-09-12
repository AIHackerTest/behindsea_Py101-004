"""
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
"""

import random

# 一大串说明文字
print("Wellcome to Super Bulls and Cows!")
print("You have 10 chance to guess a four-digit number. The numbers no repeat and not begin with 0.")
print("Now let's go!\n")
print("Please type in your answer and press Enter.")

def input_format_right(answer_str):
    """用于判断是否为四位、不重复、数字、首位非零"""
    if len(answer_str) != 4 or answer_str[0] == "0" or not answer_str.isdecimal():
        return False
    else:
        answer_list = [i for i in answer_str]
        for ans in answer_list:
            if answer_list.count(ans) != 1:
                return  False
    return True

# 确定10以内数字作为候选
int_list = [str(i) for i in range(0, 10)]

# 一直取，直至选出首位不为零的四位数取样
while True:
    number =random.sample(int_list, 4)
    if number[0] !="0":
        break
# 转换为string
number_str = "".join(num for num in number)

#开始循环输入答案
for i in range(0, 10):
    # 相同位置和仅包含的个数初始化
    same = 0
    include = 0

    #获取输入数字
    answer_str = input("> ")
    # 判断输入的字符是否为四位数字首位非零，符合规则就转换为list类型
    if input_format_right(answer_str):
        pass
    else:
        print("Please input four-digit with no repeat and not begin with 0.")
        print(f"You have {9-i} chance left.")
        continue

    # 判断是否相等，或者输出相符的位数
    if answer_str == number_str:
        print(f"Yes. You win!")
        break
    else:
        for j in range(0, 4):
            # 对于answer_str中每个元素逐一核对是否与number_str同位置元素相同，否则遍历number_str查找是否存在；对应分别统计same和include个数
            if answer_str[j] == number_str[j]:
                same += 1
            else:
                for num in number_str:
                    if answer_str[j] == num:
                        include +=1
                    else:
                        pass

        # 输出说明文字及剩下次数
        print(f"Sorry. Your answer's reply is {same}A{include}B.")
        print(f"You have {9-i} chance left.")

# 最终无论是否猜出，均输出谜底number_str
print(f"The number is {number_str}")
