import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "[]{}();:.,@#$%&*-_"

length = random.randint(8,16)
pas = lower + upper + numbers + symbols

password = "".join(random.sample(pas,length))

print(password)