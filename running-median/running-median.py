import argparse


def running_median(input_iterable):
    """Calculate a running median for input_iterable and return it as generator
    :param input_iterable: iterable with numbers to calculate a running median
    :return a running_median as generator
    """
    acc = []
    for number in input_iterable:
        acc.append(number)
        acc.sort()
        if len(acc) % 2 == 1:
            yield float(acc[len(acc) // 2])
        else:
            yield (acc[len(acc) // 2 - 1] + acc[len(acc) // 2]) / 2


def file_reader(file_name):
    """Return N rows of the file, where N is in first row of the file (N is not included)
    :param file_name: absolute or relative file name
    :return: content of the file as integers
    """
    with open(file_name, 'rt') as input_file:
        n = int(input_file.readline())  # TODO: handle if not a integer
        for _ in range(n):
            yield int(input_file.readline())  # TODO: handle if not a integer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Running Median')
    parser.add_argument('input', help='input file')

    args = parser.parse_args()
    for median in running_median(file_reader(args.input)):
        print(f'{median:.1f}')
