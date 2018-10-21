# korean_encrypt
한국어 암호화(복호화) 알고리즘


**Note**: 이 프로그램은 bluedisk님의 hangul-toolkit을 사용합니다. 더 자세한 내용은 https://github.com/bluedisk/hangul-toolkit 을 참조하세요.

qtgui.py와 qtgui_dec.py 파일은 PyQt5를 사용하여 그래픽사용자인터페이스 윈도우를 생성합니다.
PyQt5를 사용하실 때에는 PyQt5가 포함되어 있는 Anaconda3를 사용하는 것을 추천드립니다.

## 원리
우선 bluedisk님의 hangul-toolkit을 활용해 초/중/종성을 분리합니다. (pip로 설치할 수 있는 모듈이지만 소스가 GitHub에 공개되어 있어 소스를 clone해 사용하는 중입니다.)

`
from hangultoolkit import hgtk
hgtk.text.decompose('한글')
 --> ㅎㅏㄴᴥㄱㅡㄹ
`

그런 다음 해당 문자열을 상대로 for문 (문자열에서 문자가 순서대로 하나씩 나오게 하기 위함)을 실행하며 다음과 같은 동작을 실행합니다.

1. 스페이스, !@#$%^&*()와 같은 특수문자들은 전부 빼고 한글인지 확인한다. (hgtk.checker.is_hangul)
2. core.py에서 구현한 함수로 받은 사전(한글 자모음, 특수문자 등이 키이고 암호화된 문자열이 값인 사전)에서 for문에서 나온 한 글자를 키로 하는 문자를 찾는다.
3. for문에서 나온 한 글자로 찾아 넣는 것이 끝났으면 + (한글 자모 분류)를 넣는다. (한글자모인 경우)
3. 특수문자인 경우 ,(글자구분)을 넣는다.
4. 3이 한글자모였을 경우 한글자모 합친 글자가 끝나면 (unichr(0x1d25)를 만나면) ,를 넣는다.
5. 모든 루프가 끝난 뒤 암호화된 문자열을 리턴한다.
6. PyQt 스크립트(qtgui.py)에서 이를 받아 메시지 박스를 표시한 뒤 텍스트박스에도 값을 넣는다.
