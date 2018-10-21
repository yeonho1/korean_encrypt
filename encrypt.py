#-*coding:utf-8-*
import sys
from hangultoolkit import hgtk
import core


letters = core.getLetters(reverse=False)
def encrypt(toEncrypt):
    checkingStr = toEncrypt
    otherLetters = core.getOtherLetters()
    
    for x in otherLetters.keys():
        checkingStr = checkingStr.replace(x, "")
    if hgtk.checker.is_hangul(checkingStr):
        sepText = list(hgtk.text.decompose(toEncrypt))
        enchr = ''
        for x in sepText:
            if ord(x) != 0x1d25:
                if x in otherLetters:
                    enchr += otherLetters[x] + ','
                elif x == ' ':
                    enchr += ' ,'
                else:
                    enchr += letters[x] + '+'
            else:
                enchr = enchr[:-1] + ','
        try:
            return enchr[:-1]
        except:
            return ''
    else:
        return ''

