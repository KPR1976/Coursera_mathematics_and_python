import re
import numpy as np
import scipy.spatial.distance as ssd

"""
Скачайте файл с предложениями (sentences.txt).
"""
file = open('sentences.txt', 'r')
sentences = file.readlines()
print(sentences)
"""
Каждая строка в файле соответствует одному предложению. Считайте их, приведите каждую к нижнему регистру с помощью строковой функции lower().
Произведите токенизацию, то есть разбиение текстов на слова. Для этого можно воспользоваться регулярным выражением, которое считает разделителем любой символ, не являющийся буквой: re.split('[^a-z]', t). Не забудьте удалить пустые слова после разделения.
"""
i = 0
for sentence in sentences:
    sentence = re.split('[^a-z]', sentence.lower())  # split sentence to words using lower
    sentences[i] = [x for x in sentence if len(x) > 0]  # remove empty words
    i += 1
print(sentences)
"""
Составьте список всех слов, встречающихся в предложениях. Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. Для этого удобно воспользоваться структурой dict.
"""
wordindex = dict()
i = 0
for sentence in sentences:
    for word in sentence:
        if word not in wordindex:
            wordindex[word] = i
            i += 1
print(wordindex)
"""
Создайте матрицу размера n * d, где n — число предложений. Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. У вас должна получиться матрица размера 22 * 254.
"""
mat = np.zeros((len(sentences), len(wordindex)))
print(mat.shape)
for sentencei in range(0, len(sentences)):
    for word in sentences[sentencei]:
        wordi = wordindex[word]
        mat[sentencei][wordi] += 1
print(mat)
"""
Найдите косинусное расстояние от предложения в самой первой строке (In comparison to dogs, cats have not undergone...) до всех остальных с помощью функции scipy.spatial.distance.cosine. Какие номера у двух предложений, ближайших к нему по этому расстоянию (строки нумеруются с нуля)? Эти два числа и будут ответами на задание. Само предложение (In comparison to dogs, cats have not undergone... ) имеет индекс 0.
"""
for row in mat:
    print(ssd.cosine(row, mat[0]))
