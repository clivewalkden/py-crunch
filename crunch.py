#! C:\Pythons\Python27

import argparse
import itertools
import sys
import time

__author__ = 'Clive Walkden'


def generate(chrs, min, max, output, duplicates):

    # if os.path.exists(output):
    #     os.makedirs(os.path.dirname(output))

    print ('[+] Generating wordlist in `%s`' % output)
    print ('\n[i] Start time: %s' % time.strftime('%H:%M:%S'))
    start = time.clock()

    output = open(output, 'w')

    for n in range(min, max + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            if duplicates:
                if duplicate_check(chars):
                    continue
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()

    output.close()

    print ('\n[i] End time: %s' % time.strftime('%H:%M:%S'))
    print ('\n[i] Took %s seconds' % round((time.clock() - start), 2))


def duplicate_check(s):
    for i in xrange(len(s)):
        if i != s.rfind(s[i]):
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This is a script to generate wordlists inspired by crunch wordlist generator')
    parser.add_argument(
        '-min', '--min_length',
        help='The minimum character length',
        type=int,
        required=True,
    )
    parser.add_argument(
        '-max', '--max_length',
        help='The minimum character length',
        type=int,
        required=True,
    )
    parser.add_argument(
        '-o', '--output',
        help='Output filename',
        default='data/wl.txt',
    )
    parser.add_argument(
        '-c', '--chars',
        help='The characters to iterate through',
        default=None,
    )
    parser.add_argument(
        '-d', '--duplicates',
        help='Dont save duplicates',
        action="store_true"
    )

    args = parser.parse_args()

    generate(args.chars, args.min_length, args.max_length, args.output, args.duplicates)



