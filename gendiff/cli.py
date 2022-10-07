import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('filename1', metavar='first_file')
    parser.add_argument('filename2', metavar='second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish')

    return parser.parse_args()
