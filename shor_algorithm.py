import numpy as np

from arbitary_n_gate import hadamard_arbitrary_gate, controlled_gate_arbitrary
from matrix_l import matrix_l
from utils import get_decimal, gen_binary, generate_dict_keys, print_dictionary
from measure_state import measure_state
import math

N = 7
C = 15
A = 2
N_MEAS = 200


def controlled_phase(phase, row_arr, col_arr):
    phase_matrix = [[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, complex(math.cos(phase), math.sin(phase))]]
    row_index = get_decimal(row_arr)
    col_index = get_decimal(col_arr)
    return phase_matrix[row_index][col_index]

def perform_shor_analysis(final_state, N_meas):
    x_tilde_measured_dict = {}
    f_measured = {}

    for count in range(N_meas):
        measured_state = gen_binary(measure_state(final_state), 7)
        x_tilde_measured = get_decimal(measured_state[0:3][::-1]) / 8
        f = get_decimal(measured_state[3:])
        x_tilde_measured_dict[x_tilde_measured] = x_tilde_measured_dict[x_tilde_measured] + 1 if x_tilde_measured in x_tilde_measured_dict.keys() else 0
        f_measured[f] = f_measured[f] + 1 if f in f_measured.keys() else 0

    for key, values in x_tilde_measured_dict.items():
        x_tilde_measured_dict[key] /= N_meas

    for key, values in f_measured.items():
        f_measured[key] /= N_meas

    print('x/2l', '  ', 'probability')
    print_dictionary(x_tilde_measured_dict)
    print_dictionary(f_measured)


def driver():
    # Hadamard Gate Definitions
    hadamard_gate_0 = hadamard_arbitrary_gate(N, 0)
    hadamard_gate_1 = hadamard_arbitrary_gate(N, 1)
    hadamard_gate_2 = hadamard_arbitrary_gate(N, 2)

    # L0, L1, L2 matrix definitions
    matrix_l0 = matrix_l(N, C, A, 0)
    matrix_l1 = matrix_l(N, C, A, 1)
    matrix_l2 = matrix_l(N, C, A, 2)

    # controlled_phase
    matrix_0_1_pi_2 = controlled_gate_arbitrary(N, 0, 1, lambda row, col: controlled_phase(math.pi/2, row, col))
    matrix_0_2_pi_4 = controlled_gate_arbitrary(N, 0, 2, lambda row, col: controlled_phase(math.pi/4, row, col))
    matrix_1_2_pi_2 = controlled_gate_arbitrary(N, 1, 2, lambda row, col: controlled_phase(math.pi/2, row, col))

    initial_state = np.zeros(2**N, dtype=complex)
    initial_state[1] = 1

    #Entire Circuit

    next_state = np.dot(hadamard_gate_0, initial_state)
    next_state = np.dot(hadamard_gate_1, next_state)
    next_state = np.dot(hadamard_gate_2, next_state)

    next_state = np.dot(matrix_l0, next_state)
    next_state = np.dot(matrix_l1, next_state)
    next_state = np.dot(matrix_l2, next_state)

    next_state = np.dot(hadamard_gate_0, next_state)
    next_state = np.dot(matrix_0_1_pi_2, next_state)
    next_state = np.dot(matrix_0_2_pi_4, next_state)
    next_state = np.dot(hadamard_gate_1, next_state)
    next_state = np.dot(matrix_1_2_pi_2, next_state)

    final_state = np.dot(hadamard_gate_2, next_state)
    perform_shor_analysis(final_state, N_MEAS)



if __name__ == '__main__':
    driver()



