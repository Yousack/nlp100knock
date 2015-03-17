# coding: UTF-8

s = "パタトクカシーー"
ans = ""

for x in range(len(s)):
    if x % 2 != 0:
        ans += s[x]

print(ans)
