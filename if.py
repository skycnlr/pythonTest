from os.path import join
print(join('C:\\windows', 'system32'))

age=106
if age>100:
    print ("dddddd:",age)
elif age>0:
    print("xxxxxx")
else:
    print "nn"

print "jjjjj"

if age:
    print ("111111111")


print (1+2+3)
print (list(range(10)))
print list(range(1,10))
print list(range(1,10,4))
for x in range(1,10,2):
    sum = sum + x
    print (sum)
input = input("input num:")
if (input > 0):
    print "input > 0"
else:
    print ("input <= 0")