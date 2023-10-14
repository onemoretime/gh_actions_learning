import os
import sys

def main():
    """
    small useless main
    """
    print(os.path.abspath(os.curdir))
    print(sys.platform)

if __name__ == '__main__':
    main()