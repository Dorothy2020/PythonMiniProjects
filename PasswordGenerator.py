import random

passlen = int(input("enter the length of password"))
s = "abcdefghijkl04236ABCDG!$%^()?"
p = "".join(random.sample(s, passlen))

print(p)
