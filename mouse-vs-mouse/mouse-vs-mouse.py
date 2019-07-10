import argparse

from wordset import WordSet



def mouse_vs_mouse(computer_mouse_wordset, animal_wordset, input_iterable):
    for sentence in input_iterable:
        if computer_mouse_wordset.count_occurrences(sentence) >= animal_wordset.count_occurrences(sentence):
            yield 'computer_mouse'
        else:
            yield 'animal'


def file_reader(file_name):
    with open(file_name, 'rt') as input_file:
        n = int(input_file.readline())  # TODO: handle if not a integer
        for _ in range(n):
            yield input_file.readline()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mouse vs Mouse')
    parser.add_argument('input', help='input file')
    parser.add_argument('--animal', help='animal set', default='animal.txt')
    parser.add_argument('--computer_mouse', help='computer mouse set', default='computer-mouse.txt')

    args = parser.parse_args()

    computer_mouse_wordset = WordSet(open(args.computer_mouse, 'rt').readlines())
    animal_wordset = WordSet(open(args.animal, 'rt').readlines())

    for output in mouse_vs_mouse(computer_mouse_wordset, animal_wordset, file_reader(args.input)):
        print(output)
