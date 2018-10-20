#-*coding:utf-8-*
import sys
from hangultoolkit import hgtk
import core


letters = core.getLetters(reverse=False)
def encrypt(toEncrypt):
    sepText = list(hgtk.text.decompose(toEncrypt))
    enchr = ''
    for x in sepText:
        if ord(x) != 0x1d25:
            if x == ' ':
                enchr += ' '
            else:
                enchr += letters[x] + '+'
        else:
            enchr = enchr[:-1] + ','
    try:
        return enchr[:-1]
    except:
        return ''

