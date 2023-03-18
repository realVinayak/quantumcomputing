import numpy as np
from utils import gen_binary, get_decimal


def matrix_l(n, C, a, l_index):
    A_resolved = (a ** (2 ** l_index)) % C
    n_dim = 2 ** n
    gate_matrix = np.array(
        np.zeros((n_dim, n_dim), dtype=float))
    for col_index in range(n_dim):
        col_binary = gen_binary(col_index, n)
        l_resolved = 2 - l_index
        if col_binary[l_resolved] == 0:
            row_index = col_index
        else:
            m_decimal = get_decimal(col_binary[3:])
            if m_decimal >= C:
                row_index = col_index
            else:
                new_f = (A_resolved * m_decimal) % C
                new_f_binary = gen_binary(new_f, 4)
                row_index = get_decimal(col_binary[0:3] + new_f_binary)
        gate_matrix[row_index][col_index] = 1
    return gate_matrix


def driver():
    print(matrix_l(7, 15, 7, 2))


if __name__ == '__main__':
    driver()
