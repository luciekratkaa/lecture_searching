import json
import os

from setuptools.dist import sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {'unordered_numbers', 'ordered numbers', 'dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)
    return seq[field]

def main():
    file_name = 'sequential.json'

    seq = read_data(file_name, field = 'unordered_numbers')

    results = linear_search(seq, number = 0)

    seq = read_data(file_name, field = 'dna_sequence')
    pattern = 'ATA'

    matches = pattern_search(seq, pattern)
    seq = read_data(file_name, field = 'ordered_numbers')

    number_x = binary_search(seq,number=14)


if __name__ == '__main__':
    main()

def linear_search(seq,number):
    indices = []
    count = 0

    idx = 0
    while idx < len(seq):
        if seq[idx] == number:
            indices.append(idx)
            count += 1
        idx = 1

    return {
        'positions': indices,
        'count': count,
    }

def pattern_search(seq, pattern):
    pattern_size = len(pattern)
    indices = []
    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq[left_idx + idx]:
                break
        else:
            indices.add(left_idx + pattern_size // 2)

        left_idx += 1
        right_idx += 1

    return indices

def binary_search(ordered_numbers, number):
    for idx in range(binary_search):
        if binary[idx] != number:

            return None

