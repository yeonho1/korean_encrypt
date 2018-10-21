﻿#-*coding:utf-8-*

def getLetters(reverse=False):
    letters = {
           u'ㄱ': '0',
           u'ㄴ': '1',
           u'ㄷ': '2',
           u'ㄹ': '3',
           u'ㅁ': '4',
           u'ㅂ': '5',
           u'ㅅ': '6',
           u'ㅇ': '7',
           u'ㅈ': '8',
           u'ㅊ': '9',
           u'ㅋ': 'a',
           u'ㅌ': 'b',
           u'ㅍ': 'c',
           u'ㅎ': 'd',
           u'ㅏ': '0a',
           u'ㅑ': '1a',
           u'ㅓ': '2a',
           u'ㅕ': '3a',
           u'ㅗ': '4a',
           u'ㅛ': '5a',
           u'ㅜ': '6a',
           u'ㅠ': '7a',
           u'ㅡ': '8a',
           u'ㅣ': '9a',
           u'ㄲ': '0b',
           u'ㄸ': '1b',
           u'ㅃ': '2b',
           u'ㅆ': '3b',
           u'ㅉ': '4b',
           u'ㅐ': '0c',
           u'ㅒ': '1c',
           u'ㅔ': '2c',
           u'ㅖ': '3c',
           u'ㅘ': '4c',
           u'ㅙ': '5c',
           u'ㅚ': '6c',
           u'ㅝ': '7c',
           u'ㅞ': '8c',
           u'ㅟ': '9c',
           u'ㅢ': '10c',
           u'.' : '.',
           u',' : '11c',
           u'!' : '!',
           u'@' : '@',
           u'#': '#',
           u'$': '$',
           u'%': '%',
           u'^': '^',
           u'&': '&',
           u'*': '*',
           u'(': '(',
           u')': ')',
           u'~': '~',
           u'`': '`',
           u'\\': '\\',
           u'-': '-',
           u'_': '_',
           u'+': '+',
           u'=': '=',
           u'[': '[',
           u']': ']',
           u'{': '{',
           u'}': '}',
           u';': ';',
           u':': ':',
           u'<': '<',
           u'>': '>',
           u'/': '/',
           u'?': '?',
           u'"': '"',
           u"'": "'",
           u'0': '0d',
           u'1': '1d',
           u'2': '2d',
           u'3': '3d',
           u'4': '4d',
           u'5': '5d',
           u'6': '6d',
           u'7': '7d',
           u'8': '8d',
           u'9': '9d'
        }
    
    if reverse:
        try:
            result = {v: k for k, v in letters.iteritems()}
        except: 
            result = {v: k for k, v in letters.items()}
    else:
        result = letters
    return result

def getOtherLetters():
    letters = {
           u'.' : '.',
           u',' : '11c',
           u'!' : '!',
           u'@' : '@',
           u'#': '#',
           u'$': '$',
           u'%': '%',
           u'^': '^',
           u'&': '&',
           u'*': '*',
           u'(': '(',
           u')': ')',
           u'~': '~',
           u'`': '`',
           u'\\': '\\',
           u'-': '-',
           u'_': '_',
           u'+': '+',
           u'=': '=',
           u'[': '[',
           u']': ']',
           u'{': '{',
           u'}': '}',
           u';': ';',
           u':': ':',
           u'<': '<',
           u'>': '>',
           u'/': '/',
           u'?': '?',
           u'"': '"',
           u'\'': u'\'',
           u'0': '0d',
           u'1': '1d',
           u'2': '2d',
           u'3': '3d',
           u'4': '4d',
           u'5': '5d',
           u'6': '6d',
           u'7': '7d',
           u'8': '8d',
           u'9': '9d',
           '.' : '.',
           ',' : '11c',
           '!' : '!',
           '@' : '@',
           '#': '#',
           '$': '$',
           '%': '%',
           '^': '^',
           '&': '&',
           '*': '*',
           '(': '(',
           ')': ')',
           '~': '~',
           '`': '`',
           '\\': '\\',
           '-': '-',
           '_': '_',
           '+': '+',
           '=': '=',
           '[': '[',
           ']': ']',
           '{': '{',
           '}': '}',
           ';': ';',
           ':': ':',
           '<': '<',
           '>': '>',
           '/': '/',
           '?': '?',
           '"': '"',
           '\'': u'\'',
           '0': '0d',
           '1': '1d',
           '2': '2d',
           '3': '3d',
           '4': '4d',
           '5': '5d',
           '6': '6d',
           '7': '7d',
           '8': '8d',
           '9': '9d',
           ' ': ' '
    }
    return letters