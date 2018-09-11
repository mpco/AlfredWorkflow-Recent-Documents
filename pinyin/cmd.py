import argparse
from pinyin import get

from pinyin._compat import u


def pinyin():
    parser = argparse.ArgumentParser()
    parser.add_argument("chars", help="Input chinese words")
    args = parser.parse_args()

    if not args.chars:
        parser.print_help()
        return

    print(get(u(args.chars)))
