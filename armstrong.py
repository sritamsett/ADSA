n = int(input())
s = str(n)
p = len(s)
t = sum(int(d) ** p for d in s)

if t == n:
    print("Armstrong")
else:
    print("Not Armstrong")
