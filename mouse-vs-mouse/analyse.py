import os
from collections import Counter

from common import filter_dots

if __name__ == '__main__':
    computer_mouse = Counter()
    animal = Counter()
    multisets = {
        'computer-mouse': computer_mouse,
        'animal': animal,
    }

    for i in range(100):
        input_file_name = f'input{i:02}.txt'
        output_file_name = f'output{i:02}.txt'
        if not os.path.isfile(input_file_name) or not os.path.isfile(output_file_name):
            break

        with open(input_file_name, 'rt') as input_file, open(output_file_name, 'rt') as output_file:
            lines = int(input_file.readline())
            for _ in range(lines):
                multisets[output_file.readline().strip()].update(
                    elem.lower() for elem in filter_dots(input_file.readline()).strip().split()
                )

    for key, multiset in multisets.items():
        print(key)
        print()
        for word, occurrences in multiset.most_common():
            print(f'{occurrences}\t{word}')

        print()