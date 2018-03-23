"""
Выполните следующие шаги:

DONE Скачайте файл с предложениями (sentences.txt).
DONE Каждая строка в файле соответствует одному предложению. Считайте их, приведите каждую к нижнему регистру с помощью строковой функции lower().
DONE Произведите токенизацию, то есть разбиение текстов на слова. Для этого можно воспользоваться регулярным выражением, которое считает разделителем любой символ, не являющийся буквой: re.split('[^a-z]', t). Не забудьте удалить пустые слова после разделения.
DONE Составьте список всех слов, встречающихся в предложениях. Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. Для этого удобно воспользоваться структурой dict.
DONE Создайте матрицу размера n * d, где n — число предложений. Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. У вас должна получиться матрица размера 22 * 254.
DONE Найдите косинусное расстояние от предложения в самой первой строке (In comparison to dogs, cats have not undergone...) до всех остальных с помощью функции scipy.spatial.distance.cosine. Какие номера у двух предложений, ближайших к нему по этому расстоянию (строки нумеруются с нуля)? Эти два числа и будут ответами на задание. Само предложение (In comparison to dogs, cats have not undergone... ) имеет индекс 0.
DONE Запишите полученные числа в файл, разделив пробелом. Обратите внимание, что файл должен состоять из одной строки, в конце которой не должно быть переноса. Пример файла с решением вы можете найти в конце задания (submission-1.txt).
Совпадают ли ближайшие два предложения по тематике с первым? Совпадают ли тематики у следующих по близости предложений?
"""
import re
import numpy as np
import scipy.spatial.distance as ssd
file = open('sentences.txt')
text = file.read().lower()
words = re.split('[^a-z]', text)
only = []
for i in range(0, len(words)):
    if len(words[i]) > 0 and only.count(words[i]) == 0:
        only.append(words[i])
    i += 1
ourdict = {}
for i in range(0, len(only)):
    if only[i] in ourdict.keys():
        pass
    else:
        ourdict[i] = only[i]
sent = {}
with open("sentences.txt") as f:
    for j in range(0, 22):
        for i in f:
            if i.strip('\n') in sent.values():
                pass
            else:
                sent[j] = i.strip('\n')
            j += 1
mat = np.zeros((len(sent), len(ourdict)))
for key, value in sent.items():
    for newkey, value in ourdict.items():
        mat[key, newkey] = sent.get(key).count(str(ourdict.get(newkey)))
result = {}
for row in mat:
    print(ssd.cosine(row, mat[0]))
