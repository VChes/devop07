
# A
first = 7
second = 44.3
print(f"\n")
print('answers for A')
print(first+second)
print(first*second)
print(second/first)

# Run for calculations
# END A

# B
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print(f"\n")
print('answers for B')
print(a)
print(b)
print(c)

# Answers:
# value of a is 9
# value of b is 8
# value of c is 15
# the actual value of c would be 17 if last re-declaration would happen
# END B

# C.1
name = "john"
name = 'john'
print(f"\n")
print('answers for C.1')
print(name + " ""\" and \' are the same")
# Answer: " and ' are the same

# C.2
my_number = 5+5
#print("result is: " +my_number)
print(f"\n")
print('answers for C.2')
print("result is: " + str(my_number))
print("Answer: 1.my_number is an integer. 2.convert to string str(my_number)")
# Answer: 1.my_number is an integer. 2.convert to string str(my_number)
# END C

# D
x = 5
y = 2.36
print(f"\n")
print('answers for D.1')
print(x+int(y))
print(x+float(y))
#Answer: 7, Python rounds up / down int numbers will (somewhat) work with second print

a = 8
b = "123"
print(f"\n")
print('answers for Challenge')
#print(a+b) < won't work answer below:
print(a+int(b))
# END D
