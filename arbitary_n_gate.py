import numpy as np
import math
from utils import kronecker_delta, gen_binary, hadamard_gate, get_decimal


def cnot_gate_func(row_arr, col_arr):
    cnot_matrix = [[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 0, 1],
                            [0, 0, 1, 0]]
    row_index = get_decimal(row_arr)
    col_index = get_decimal(col_arr)
    return cnot_matrix[row_index][col_index]


def hadamard_arbitrary_gate(n, qubit_index):
    num_dimension = 2 ** n
    gate_matrix = np.array(
        np.zeros((num_dimension, num_dimension), dtype=complex))
    for row_index in range(len(gate_matrix)):
        row_binary = gen_binary(row_index, n)
        for col_index in range(len(gate_matrix[row_index])):
            col_binary = gen_binary(col_index, n)
            state = 1
            for comp_index in range(n):
                row_split = row_binary[comp_index]
                col_split = col_binary[comp_index]
                if comp_index == qubit_index:
                    state *= hadamard_gate(row_split, col_split)
                else:
                    state *= kronecker_delta(row_split, col_split)
            gate_matrix[row_index][col_index] = complex(state)
    return gate_matrix

def apply_arbitrary_hadamard(n, state):
    for counter in range(n):
        hadamard_gate_to_use = hadamard_arbitrary_gate(n, counter)
        state = np.dot(hadamard_gate_to_use, state)
    return state

def controlled_gate_arbitrary(n, master_index, slave_index, gate_func):
    # Assume that gate_func takes master, slave
    num_dimension = 2 ** n
    gate_matrix = np.array(
        np.zeros((num_dimension, num_dimension), dtype=complex))
    for row_index in range(len(gate_matrix)):
        row_binary = gen_binary(row_index, n)
        for col_index in range(len(gate_matrix[row_index])):
            col_binary = gen_binary(col_index, n)
            state = 1
            control_col_value = [col_binary[master_index],
                                 col_binary[slave_index]]
            control_row_value = [row_binary[master_index],
                                 row_binary[slave_index]]
            controlled_comp = gate_func(control_row_value, control_col_value)
            for comp_index in range(n):
                if (comp_index != master_index) and (comp_index != slave_index):
                    row_split = row_binary[comp_index]
                    col_split = col_binary[comp_index]
                    state *= kronecker_delta(row_split, col_split)
            state *= controlled_comp
            gate_matrix[row_index][col_index] = state
    return gate_matrix


def driver():
    print(controlled_gate_arbitrary(7, 3, 4, cnot_gate_func))


if __name__ == '__main__':
    driver()
