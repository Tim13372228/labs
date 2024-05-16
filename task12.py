#Сибагатов Тимур ИПМбд 01-23 (лаб 12)

#Задание1
def HYPERgrasshopper(n):
    GH = [None] + ([0] * max(3, n))
    GH[1] = 1
    GH[2] = 1
    for i in range(3, n + 1):
        GH[i] = GH[i - 1] + GH[i - 2]
        if i % 3 == 0:
            GH[i] += GH[i // 3]
    return GH[n]
print('Количество способов достичь её:',HYPERgrasshopper(int(input('Введите конечную точку: '))))




#Задание2
import numpy as np

def max_common_sequence(first_seq, second_seq):
    common_sequences = []
    i = 0
    while i < len(first_seq) - 1:
        j = 0
        while j < len(second_seq) - 1:
            if first_seq[i] == second_seq[j]:
                current_sequence = first_seq[i]
                k = 1
                while (i + k < len(first_seq)) and (j + k < len(second_seq)) and (first_seq[i + k] == second_seq[j + k]):
                    current_sequence += first_seq[i + k]
                    k += 1
                common_sequences.append(current_sequence)
            j += 1
        i += 1
    if not common_sequences:
        return ''
    return max(common_sequences, key=len)

def max_common_sequence_dynamically(first_seq, second_seq):
    first_seq = ' ' + first_seq  # Добавляем пробел для индексации
    second_seq = ' ' + second_seq  # Добавляем пробел для индексации
    lengths = np.zeros((len(first_seq), len(second_seq)))
    directions = np.zeros((len(first_seq), len(second_seq)))

    for i in range(1, len(first_seq)):
        for j in range(1, len(second_seq)):
            if first_seq[i] == second_seq[j]:
                lengths[i][j] = lengths[i-1][j-1] + 1
                directions[i][j] = -1  # Диагональ
            elif lengths[i-1][j] >= lengths[i][j-1]:
                lengths[i][j] = lengths[i-1][j]
                directions[i][j] = 2  # Вверх
            else:
                lengths[i][j] = lengths[i][j-1]
                directions[i][j] = 1  # Влево

    i, j = len(first_seq) - 1, len(second_seq) - 1
    common_sequence = []

    while i > 0 and j > 0:
        if directions[i][j] == -1:
            common_sequence.append(first_seq[i])
            i -= 1
            j -= 1
        elif directions[i][j] == 2:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(common_sequence))

first_input = input('Введите первую последовательность: ')
second_input = input('Введите вторую последовательность: ')

print(max_common_sequence(first_input, second_input))
print(max_common_sequence_dynamically(first_input, second_input))




#Задание3
def is_subsequence(first_sequence, second_sequence):
    match_count = 0
    j = 0

    for i in range(len(first_sequence)):
        if first_sequence[i] == second_sequence[j]:
            match_count += 1
            if j < len(second_sequence) - 1:
                j += 1
            elif match_count < len(second_sequence):
                return False
        if match_count == len(second_sequence):
            return True
    return False

first_input = input('Введите первую последовательность: ')
second_input = input('Введите вторую последовательность: ')

print('Является ли вторая последовательность подпоследовательностью первой? Ответ:', is_subsequence(first_input, second_input))

