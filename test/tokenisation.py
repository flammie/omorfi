from argparse import ArgumentParser
from omorfi.omorfi import Omorfi

WEIRD_TOK = "(OA,...)."


def main():
    a = ArgumentParser()
    a.add_argument('-f', '--fsa', metavar='FSAFILE', required=True,
                   help="HFST's optimised lookup binary data for the "
                        "transducer to be applied")
    options = a.parse_args()
    omorfi = Omorfi()
    omorfi.load_from_dir(options.fsa, analyse=True, accept=True)

    tokens = omorfi.python_tokenise(WEIRD_TOK)
    # Check tokens are in same order as text
    start = 0
    for token in tokens:
        start = WEIRD_TOK.index(token['surf'], start)


if __name__ == '__main__':
    main()
