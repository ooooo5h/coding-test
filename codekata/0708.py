"""
strs은 단어가 담긴 배열입니다.

공통된 시작 단어(prefix)를 반환해주세요.

예를 들어

strs = ['start', 'stair', 'step']
return은 'st'
strs = ['start', 'wework', 'today']
return은 ''
"""

strs = ['start', 'wework', 'today']

def get_prefix(strs):

    if len(strs) == 0:
      return ''

    strs.sort()  # 기존 리스트를 알파벳순으로 정렬하여 값을 수정시킨다
    res = ''
    # 맨 앞의 알파벳과 맨 뒤의 알파벳이 같은 순서라면!?그것이 정답아닌가.
    for s in strs[0]:
        # s = s,t,a,r,t
        if strs[-1].startswith(res+s):
            # print(s)
            res += s    # res = st
        else:
            pass

    return res