import random
import numpy as np

NUM_MEAS = 5000


def measure_state(input_state):
    probe_random = random.random()
    amplitude = [abs(base) ** 2 for base in input_state]
    amplitude_cumsum = np.cumsum(amplitude)
    previous_amp = 0
    for index, amp in enumerate(amplitude_cumsum):
        if previous_amp <= probe_random <= amp:
            return index
        previous_amp = amp
    return -1


def generate_state_count(input_state, num_iter, norm=False):
    count_dict = {-1: 0}

    for index in range(len(input_state)):
        count_dict[index] = 0

    for iter_ in range(num_iter):
        sampled_state = measure_state(input_state)
        count_dict[sampled_state] = count_dict[sampled_state] + 1

    if norm:
        for key in count_dict.keys():
            count_dict[key] = count_dict[key]/num_iter

    return count_dict

