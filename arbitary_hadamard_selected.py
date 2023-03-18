import numpy as np
import math
from utils import gen_binary, kronecker_delta


def predict_hadamard(row_indexes, col_indexes):
    predicted_hadamard = 1
    for counter in range(len(row_indexes)):
        # lol
        predicted_hadamard *= -1 if (
                row_indexes[counter] + col_indexes[counter] == 2) else 1
    return predicted_hadamard


def arbitrary_hadamard_selected(num_qubits, selected_indexes):
    num_dimension = 2 ** num_qubits
    gate_matrix = np.array(
        np.zeros((num_dimension, num_dimension), dtype=float))
    for row_index in range(num_dimension):
        row_binary = gen_binary(row_index, num_qubits)
        for col_index in range(num_dimension):
            col_binary = gen_binary(col_index, num_qubits)
            col_selected = []
            row_selected = []
            state = 1
            for comp_index in range(num_qubits):
                if comp_index in selected_indexes:
                    row_selected.append(row_binary[comp_index])
                    col_selected.append(col_binary[comp_index])
                else:
                    state *= kronecker_delta(row_binary[comp_index],
                                             col_binary[comp_index])
            state *= predict_hadamard(row_selected, col_selected)
            gate_matrix[row_index][col_index] = float(state)
    return math.pow((1 / math.sqrt(2)), len(selected_indexes)) * gate_matrix


def driver():
    mat1 = np.matmul(
        arbitrary_hadamard_selected(10, [0, 3, 5]),
        arbitrary_hadamard_selected(10, [4, 7, 8])
    )
    mat2 = (arbitrary_hadamard_selected(10, [0, 3, 4, 5, 7, 8]))

    print(np.array_equal(mat1, mat2))


if __name__ == '__main__':
    driver()
