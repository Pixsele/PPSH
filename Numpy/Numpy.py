import numpy as np


def check_magic_square(array):
    sum_of_line = array.sum(axis=1)
    sum_of_column = array.sum(axis=0)
    sum_of_first_diag = array.diagonal().sum()
    sum_of_second_diag = np.flip(array, 1).diagonal().sum()

    if np.unique(sum_of_line).size != 1 or np.unique(
            sum_of_column).size != 1 or sum_of_first_diag != sum_of_second_diag:
        return False

    return True


arr = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])
arr2 = np.array([[2, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]])
print(arr)
print(arr2)

print(check_magic_square(arr))
print(check_magic_square(arr2))