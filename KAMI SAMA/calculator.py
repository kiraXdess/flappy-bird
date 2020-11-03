import math

x = input("> ")
y = input("> ")
Float = (float(x) - math.floor(float(x))) + (float(y) - math.floor(float(y)))
answer = float(x) + float(y)
if Float < 0.60:
    print(answer)
else:
    print(answer + 0.4)
