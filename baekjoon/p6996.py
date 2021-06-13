for _ in range(int(input())):
    s, t = input().split()
    print(s + " & " + t + " are " + "NOT " * (1 - int(sum(hash(c) for c in s) == sum(hash(c) for c in t))) + "anagrams.")