from numpy import *
from measure_state import generate_state_count

def hadamard_gate_1(state_in):
    H1 = (1 / sqrt(2)) * array([[1, 0, 0, 0, 1, 0, 0, 0],
                                [0, 1, 0, 0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0, 0, 1, 0],
                                [0, 0, 0, 1, 0, 0, 0, 1],
                                [1, 0, 0, 0, -1, 0, 0, 0],
                                [0, 1, 0, 0, 0, -1, 0, 0],
                                [0, 0, 1, 0, 0, 0, -1, 0],
                                [0, 0, 0, 1, 0, 0, 0, -1]])
    final_state = dot(H1, state_in)
    return final_state


def hadamard_gate_2(state_in):
    H2 = (1 / sqrt(2)) * array([[1, 0, 1, 0, 0, 0, 0, 0],
                                [0, 1, 0, 1, 0, 0, 0, 0],
                                [1, 0, -1, 0, 0, 0, 0, 0],
                                [0, 1, 0, -1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 0, 1, 0],
                                [0, 0, 0, 0, 0, 1, 0, 1],
                                [0, 0, 0, 0, 1, 0, -1, 0],
                                [0, 0, 0, 0, 0, 1, 0, -1]])
    final_state = dot(H2, state_in)
    return final_state


def hadamard_gate_3(state_in):
    H3 = (1 / sqrt(2)) * array([[1, 1, 0, 0, 0, 0, 0, 0],
                                [1, -1, 0, 0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0, 0, 0, 0],
                                [0, 0, 1, -1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 1, -1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 1, 1],
                                [0, 0, 0, 0, 0, 0, 1, -1]])
    final_state = dot(H3, state_in)
    return final_state


def driver():
    state_1 = hadamard_gate_1([0, 0, 0, 0, 1, 0, 0, 0])
    state_2 = hadamard_gate_2(state_1)
    state_3 = hadamard_gate_3(state_2)
    print(generate_state_count(state_1, 1000, True))
    print(generate_state_count(state_3, 1000, True))


if __name__ == '__main__':
    driver()
