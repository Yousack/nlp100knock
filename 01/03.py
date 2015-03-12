import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(list(map(len, re.sub(r'[,.]', '', s).split(' '))))
