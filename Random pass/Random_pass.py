import random
symbols = "abcdefghiklmnopqrstuvwxyz0123456789"
# +-/*?`~!@#$%^&*|\
password = ""
c = 0
print("Enter quantitu of symbols")
n = int(input())
for c in range(0, n):
    i = random.randint(0, len(symbols))
    password = password + symbols[i]
print(password)