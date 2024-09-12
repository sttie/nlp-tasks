"""
Задача: Лемматизировать текст (привести к словарной форме) и приписать леммам частеречные теги. 
Для решения задачи вы можете использовать данные, которые упоминались в лекциях: например, словарь oDict, разметку OpenCorpora и др. Для решения задачи нельзя использовать существующие морфологические анализаторы (mystem, pymorphy и т.п.).
Ввод: предложения вида " токен1 токен2 ... токенN" с расставленными знаками препинания, разделенные переносом строки. Из знаков препинания в предложениях могут содержаться только запятая, точка, вопросительный и восклицательный знаки.
Вывод: для каждого предложения из входных данных вывод в виде " токен1{лемма1=тег1} токен2{лемма2= тег2} ... токенN{леммаN=тегN}" без исходных знаков препинания. Разделитель между токенами -- пробельный символ.
Замечание: При лемматизации буквы е и ё, а также написание с прописной/строчной буквы признаются равноправными.
Пример: 
Input:
Стала стабильнее экономическая и политическая обстановка, предприятия вывели из тени зарплаты сотрудников.
Все Гришины одноклассники уже побывали за границей, он был чуть ли не единственным, кого не вывозили никуда дальше Красной Пахры.
Output:
Стала{стать=V} стабильнее{стабильный=A} экономическая{экономический=A} и{и=CONJ} политическая{политический=A} обстановка{обстановка=S} предприятия{предприятие=S} вывели{вывести=V} из{из=PR} тени{тень=S} зарплаты{зарплата=S} сотрудников{сотрудник=S}
Все{весь=NI} Гришины{гришин=A} одноклассники{одноклассник=S} уже{уже=ADV} побывали{побывать=V} за{за=PR} границей{граница=S} он{он=NI} был{быть=V} чуть{чуть=ADV} ли{ли=ADV} не{не=ADV} единственным{единственный=A} кого{кто=NI} не{не=ADV} вывозили{вывозить=V} никуда{никуда=NI} дальше{далеко=ADV} Красной{красный=A} Пахры{Пахра=S}


От меня:
В русском языке нормальными формами (то, к чему слово приводится при лемматизации) считаются следующие морфологические формы:
    для существительных — именительный падеж, единственное число;
    для прилагательных — именительный падеж, единственное число, мужской род;
    для глаголов, причастий, деепричастий — глагол в инфинитиве (неопределённой форме) несовершенного вида.
"""

import grammemes
import tokenization

GRAMMEMES = grammemes.parse_grammemes("./grammemes.txt")

class Word:
    def __init__(self, primary_form: str, tags: str):
        self.primary_form = primary_form
        self.tags = tags.split(",")
    
    def __repr__(self):
        return f"primary={self.primary_form}, tags={self.tags}"

def has_all_tags(words, form, tags):
    return set(tags) == set.intersection(words[form], set(tags))

def parse_opcorpora_part(words, opcorpora_file, i):
    line = opcorpora_file.readline()
    if len(line) == 0:
        return False

    assert line[:-1].isnumeric(), f"{line}"

    amount, line, primary_form = 0, opcorpora_file.readline(), None
    while line != "\n":
        form, tags = line.split("\t")
        tags = ",".join((tags[:-1]).split(" "))

        if amount == 0:
            primary_form = form
        words[form] = Word(primary_form, tags)
        
        line = opcorpora_file.readline()
        amount += 1
    
    if i == 100000:
        print(f"last form: {form}")

    return True

def parse_opcorpora(opcorpora_path):
    words = {}

    opcorpora_file = open(opcorpora_path, "r", encoding="utf-8")
    
    i = 0
    while True:
        stopped = parse_opcorpora_part(words, opcorpora_file, i)
        if not stopped:
            break

        if i == 100000:
            i = 0
        i += 1

    opcorpora_file.close()

    return words

forms = parse_opcorpora("./dict.opcorpora.txt")
with open("./input.txt") as input_file:
    text = input_file.read()
    tokens = tokenization.tokenizate(forms, text)
    print(" ".join([str(token) for token in tokens]))
