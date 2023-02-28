import math


def kronecker_delta(i, j):
    if i == j:
        return 1
    else:
        return 0


def gen_binary(x, n):
    binary = []
    binary_eff = []
    quotient = 10
    while quotient > 0:
        remainder = x % 2
        quotient = (x - remainder) / 2
        x = quotient
        binary.append(remainder)
    while (len(binary) < n):
        binary.append(0)
    binary = binary[::-1]
    for t in range(len(binary)):
        binary_eff.append(int(binary[t]))
    return binary_eff


def hadamard_gate(row, col):
    state = 1
    if row == 1 and col == 1:
        state = -1
    return state / math.sqrt(2)


def get_decimal(binary_arr):
    decimal_value = 0
    for power, bin_ in enumerate(binary_arr[::-1]):
        decimal_value += ((2 ** power) * bin_)
    return decimal_value

def generate_dict_keys(dict_to_apply, max_num):
  for x in range(max_num):
    dict_to_apply[x] = 0

def print_dictionary(dict):
    for key, value in dict.items():
        print(key, '  ', value)


def print_measurement_result(measurement_result, num_qubits):
    for key, value in measurement_result.items():
        print('state: ', key if key < 0 else gen_binary(key, num_qubits), 'probability: ', value)

if __name__ == '__main__':
  print(get_decimal(gen_binary(24, 7)))
