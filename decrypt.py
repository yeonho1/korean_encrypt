#-*coding:utf-8-*
import sys
from hangultoolkit import hgtk
import core

try:
    sep = unichr(0x1d25)
except:
    sep = chr(0x1d25)
letters = core.getLetters(reverse=True)

def decrypt(toDecrypt):
    decrypted = ''
    letterSplit = toDecrypt.split(',')
    for letter in letterSplit:
        if letter == ' ':
            decrypted += ' '
        else:
            for seq in letter.split('+'):
                decrypted += letters[seq.lstrip().rstrip()]
        decrypted += sep
    print(decrypted)
    return hgtk.text.compose(decrypted)


