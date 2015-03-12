# coding: UTF-8

s = "パタトクカシーー"
ans = ""

for x in range(0, len(s)):
    if x % 2 != 0:
        ans += s[x]

print(ans)
