#!/usr/bin/env python

from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff


def main():
    args = parse_args()
    print(generate_diff(args.filename1, args.filename2, args.format))


if __name__ == '__main__':
    main()
