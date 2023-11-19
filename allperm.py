from itertools import permutations


def allperm(str):

    permlist = permutations(str)

    for perm in list(permlist):
        print(''.join(perm))

if __name__ == "__main__":
    str = "WSA"

    allperm(str)

    