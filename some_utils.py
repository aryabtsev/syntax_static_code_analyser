import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', '-p')
parser.add_argument('--size', '-s')
parser.add_argument('--term', '-t')
namespace = parser.parse_args()


def flat(list_with_tuples):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""

    return sum([list(item) for item in list_with_tuples], [])
