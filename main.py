import unittest

import file_permutations


# Задача 2
# № 4

# Создать новый двумерный массив, исключив из переданного массива совпадающие столбцы.
# (Совпадающие столбцы – столбцы, у которых все соответствующие элементы равны друз другу).
# При формировании нового массива оставить только первый из каждого набора совпадающих столбцов

# убрать одинаковые строки
def remove_same_rows(source_matrix):
    unique = []
    for el in source_matrix:
        if el not in unique:
            unique.append(el)

    return unique


def remove_same_cols(source_matrix):
    rotated = rotate_right(source_matrix)

    mid = remove_same_rows(rotated)

    result = rotate_left(mid)

    return result


def rotate_right(src):
    result = create_list(src)

    for i in range(len(src)):
        for j in range(len(src[0])):
            result[j][len(src) - i - 1] = src[i][j]

    return result


def rotate_left(src):
    result = rotate_right(rotate_right(rotate_right(src)))
    return result


def create_list(src):
    result = []
    for elem in range(len(src[0])):
        result.append([0] * len(src))

    return result


def print_matrix(src):
    for i in range(len(src)):
        for j in range(len(src[0])):
            print(str(src[i][j]) + " ", end="")
        print()


# пример с запиcью в файл
nums = file_permutations.read_two_dimensional_list("files/input01.txt")

res = remove_same_cols(nums)

file_permutations.write_two_dimensional_list(res, "files/output01.txt")


# tester
class ListTestCase(unittest.TestCase):
    result_list_1 = [[1, 5, 4],
                     [1, 5, 4],
                     [1, 5, 4],
                     [1, 5, 4],
                     [1, 5, 4]]

    nums_1_1 = [[1, 5, 1, 4, 5],
                [1, 5, 1, 4, 5],
                [1, 5, 1, 4, 5],
                [1, 5, 1, 4, 5],
                [1, 5, 1, 4, 5]]

    result_list_2 = [[1, 3, 4],
                     [1, 5, 4],
                     [1, 5, 4],
                     [1, 5, 4],
                     [1, 5, 4]]

    nums_1_2 = [[1, 3, 1, 4, 4],
                [1, 5, 1, 4, 4],
                [1, 5, 1, 4, 4],
                [1, 5, 1, 4, 4],
                [1, 5, 1, 4, 4]]

    def test_1(self):
        assert self.result_list_1 == remove_same_cols(self.nums_1_1)

    def test_2(self):
        assert self.result_list_2 == remove_same_cols(self.nums_1_2)


unittest.main()

# 1 3 3     4 1 1       4 1 1
# 1 3 3 ->  3 3 7 ->    3 7 7 -> повернуть три раза вправо
# 4 7 7     3 3 7

# Процедура поворота
# 4 1 1  -> 3 4 :     res[0][1] [][x]
# 3 3 7     3 1                 [][]  x = 4
#           7 1                 [][]
#                   res[1][1]   [][]
#                               [][x] x = 1
#                               [][]
# и так далее
