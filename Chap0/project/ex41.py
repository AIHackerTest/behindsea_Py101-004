import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# 定义模型，用于被替换
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "Form *** get the *** function, call it with params self, @@@",
    "***.*** = '***'":
      "Form *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first，英文=>代码 或者 代码=>英文
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    # 将单词转换为可用于类名或类定义参数的单词（首字母大写），符合命名规则
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    # 选用用于替换 *** 的单词
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    # 随机选用1-2个参数，并用 ，隔开
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(", ".join(
            random.sample(WORDS, param_count)))

    # 执行两次将snippet和phrase分别替换
    for sentence in snippet, phrase:
        #不写数字就是全部，和不带括号一样，和直接换sentence一样
        result = sentence[:]

        # fake class names，伪装成函数名
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names，伪装成其他名称
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists，伪装参数列表
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D，但是Ctrl+D并不能停止
try:
    while True:
        # 取用PHRASES的keys，并且打乱顺序
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        # 对每个key，及其value，分别替换其中的‘@@@’‘###’‘***’形成句子并输出
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            # 停顿等待输入
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    #抓取错误
    print("\nBye")
