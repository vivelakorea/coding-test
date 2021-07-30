def P2(s: str) -> int:
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1

# print(P2('loveprogram'))
# print(P2('llooveeprogram'))
# print(P2('computingfoundationfordatascience'))