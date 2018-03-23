"""
Выполните следующие шаги:

DONE Скачайте файл с предложениями (sentences.txt).
DONE Каждая строка в файле соответствует одному предложению. Считайте их, приведите каждую к нижнему регистру с помощью строковой функции lower().
DONE Произведите токенизацию, то есть разбиение текстов на слова. Для этого можно воспользоваться регулярным выражением, которое считает разделителем любой символ, не являющийся буквой: re.split('[^a-z]', t). Не забудьте удалить пустые слова после разделения.
DONE Составьте список всех слов, встречающихся в предложениях. Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. Для этого удобно воспользоваться структурой dict.
DONE Создайте матрицу размера n * d, где n — число предложений. Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. У вас должна получиться матрица размера 22 * 254.
Найдите косинусное расстояние от предложения в самой первой строке (In comparison to dogs, cats have not undergone...) до всех остальных с помощью функции scipy.spatial.distance.cosine. Какие номера у двух предложений, ближайших к нему по этому расстоянию (строки нумеруются с нуля)? Эти два числа и будут ответами на задание. Само предложение (In comparison to dogs, cats have not undergone... ) имеет индекс 0.
Запишите полученные числа в файл, разделив пробелом. Обратите внимание, что файл должен состоять из одной строки, в конце которой не должно быть переноса. Пример файла с решением вы можете найти в конце задания (submission-1.txt).
Совпадают ли ближайшие два предложения по тематике с первым? Совпадают ли тематики у следующих по близости предложений?
"""
import re
import numpy as np
import scipy
file = open('sentences.txt')
text = file.read().lower()
#text = text.lower()
#print(text)
words = re.split('[^a-z]', text)
#words = words.remove('')
#print(len(words))
only = []
#print(len(words))
for i in range(0, len(words)):
    #print(words[i])
    #print(len(words[i]))
    if len(words[i]) > 0 and only.count(words[i]) == 0:
        only.append(words[i])
    i += 1
#print(only)
ourdict ={}
for i in range(0, len(only)):
    if only[i] in ourdict.keys():
        pass
    else:
        ourdict[i] = only[i]
#print(ourdict)
#numwords = 0
#sent = 'In comparison to dogs, cats have not undergone major changes during the domestication process.'
#for key,value in ourdict.items():
#    if key in text:
#        numwords +=1
#print(numwords)
#print(file)
sent = {}
with open("sentences.txt") as f:
    for j in range (0, 22):
        for i in f:
            if i.strip('\n') in sent.values():
                pass
            else:
                sent[j] = i.strip('\n')
            j += 1
#print(sent)
mat = np.zeros((len(sent),len(ourdict)))
#print(mat.shape)
#print(len(sent))
for key,value in sent.items():
    #print(sent.get(key))
    for newkey, value in ourdict.items():
        #print(j)
        #print(ourdict.get(key))
        #print(sent.get(key).count(str(ourdict.get(newkey))))
            #print(sent[i].count(ourdict[j]))
        mat[key,newkey] = sent.get(key).count(str(ourdict.get(newkey)))
        #j += 1
    #i += 1
print(mat.shape)
print(mat)
scipy.spatial.distance.cosine
