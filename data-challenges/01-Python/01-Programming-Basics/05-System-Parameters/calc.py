# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys

def main():
    """Implement the calculator"""
    args = sys.argv
    if args[2] == "+":
        out = int(args[1]) + int(args[3])
    elif args[2] == "-":
        out = int(args[1]) - int(args[3])
    elif args[2] == "*":
        out = int(args[1]) * int(args[3])
    else:
        out = None
    return out

if __name__ == "__main__":
    print(main())
