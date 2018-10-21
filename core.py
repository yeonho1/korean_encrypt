#-*coding:utf-8-*

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
           u'.' : '.'
        }
    if reverse:
        try:
            result = {v: k for k, v in letters.iteritems()}
        except: 
            result = {v: k for k, v in letters.items()}
    else:
        result = letters
    return result
