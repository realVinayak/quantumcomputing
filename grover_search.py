import numpy as np
from arbitary_n_gate import hadamard_arbitrary_gate, apply_arbitrary_hadamard
from utils import print_measurement_result
from measure_state import generate_state_count


FIND_INDEX = 15
NUM_QUBITS = 7
NUM_DIF = 6


hadamard_gate_0 = hadamard_arbitrary_gate(NUM_QUBITS, 0)
hadamard_gate_1 = hadamard_arbitrary_gate(NUM_QUBITS, 1)
hadamard_gate_2 = hadamard_arbitrary_gate(NUM_QUBITS, 2)

def oracle_matrix(n, found_index):
    num_dim = 2 ** n
    om = np.zeros((num_dim, num_dim))
    for index in range(num_dim):
        om[index][index] = 1 if index != found_index else -1
    return om


def diffusion_matrix(n):
    return oracle_matrix(n, 0)

def apply_diffusion(state):
    oracle_matrix_to_apply = oracle_matrix(NUM_QUBITS, FIND_INDEX)

    diffusion_matrix_to_apply = diffusion_matrix(NUM_QUBITS)

    next_state = np.dot(oracle_matrix_to_apply, state)
    next_state = apply_arbitrary_hadamard(NUM_QUBITS, next_state)
    next_state = np.dot(diffusion_matrix_to_apply, next_state)
    next_state = apply_arbitrary_hadamard(NUM_QUBITS, next_state)

    return next_state

def driver():
    initial_state = np.zeros(2 ** NUM_QUBITS, dtype=complex)
    initial_state[0] = 1
    next_state = apply_arbitrary_hadamard(NUM_QUBITS, initial_state)
    for counter in range(NUM_DIF):
        next_state = apply_diffusion(next_state)

    print_measurement_result(generate_state_count(next_state, 5000, True), NUM_QUBITS)


def tests():
    initial_state = [1/2, 1/2, -1/2, 1/2]
    hadamard_gate_trial_0 = hadamard_arbitrary_gate(2, 0)
    hadamard_gate_trial_1 = hadamard_arbitrary_gate(2, 1)
    print(np.dot(hadamard_gate_trial_1, (np.dot(hadamard_gate_trial_0, initial_state))))


if __name__ == '__main__':
    driver()




