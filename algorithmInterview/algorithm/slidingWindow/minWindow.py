import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def includes(dic1, dic2):
            for c in dic2:
                if c not in dic1 or dic2[c] > dic1[c]:
                    return False
            return True


        # 만족하는 substring이 없는 경우, len(t) == 1인 경우 예외적 처리
        need = collections.Counter(t)
        s_have = collections.Counter(s)
        if not includes(s_have, need):
            return ""
        if len(t) == 1:
            return t
        
        # 리턴할 문자열 mw
        mw = ""
        have = collections.defaultdict(int)
        positions = collections.deque()
        left, right = 0, 0
        for i, c in enumerate(s):
            if c in t:
                left = right = i
                break
        positions.append(right)
        have[s[right]] += 1
        while True:
            # t를 모두 포함할때까지 right를 오른쪽으로 한칸씩 옮김
            while right < len(s) - 1 and not includes(have, need):
                right += 1
                if s[right] in need:
                    positions.append(right)
                    have[s[right]] += 1
                
            # 반복문 탈출 조건: 위에서 고정된 left를 가지고 right를 오른쪽으로 끝까지 옮겼는데 윈도우가 need를 모두 가지지 못한 경우
            if not includes(have, need):
                break
            # window 왼쪽의 t가 아닌 문자를 제외하기 위해 left를 옮김
            left = positions[0]
            # mw 기록
            if includes(have, need): # 이 부분 최적화 필요
                if mw == "":
                    mw = s[left:right+1]
                else:
                    mw = min(mw, s[left:right+1], key=len)
            # positions에 기록되어있던 위치로 현재 window 내 t와 매치되는 문자들 중 두번째 부분으로 left를 오른쪽으로 옮김
            have[s[positions.popleft()]] -= 1
            left = positions[0]
        return mw
            
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("abc", "bc"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))