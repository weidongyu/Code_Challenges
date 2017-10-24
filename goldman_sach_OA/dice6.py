from random import randint

count = 0
for i in range(0,1000000):
    a = randint(1,6)
    n = 1 
    while a % 6 != 0:
        a = (a + randint(1,6)) % 6
        n += 1
    count += n
print count/1000000
