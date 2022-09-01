_ = input()
cards_sangun_possess = set(input().split())
_ = input()
cards_shown = list(input().split())
res = map(lambda x: str(int((x in cards_sangun_possess))) + ' ', cards_shown)

print(''.join(list(res)))