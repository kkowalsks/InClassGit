import random

def password(a):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    p = "".join(random.sample(chars, a))
    print(p)

