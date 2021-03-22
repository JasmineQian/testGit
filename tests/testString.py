## check two charcters in or not in
string1 = "hello122"
string2 = "hello"
if string2 in string1:
    print("OK")
else:
    print("string2 is not in string1")

## according to Charcters Case
string3 = "Hello"
string4 = "hello"


name ="DS20210318production"
name2="20210319"
name1 =name[2:10]
print("heelo zhr {}".format(name1))
if name1>name2:
    print("name1 is bigger")
else:
    print("sorry")


if string3.lower() in string4.lower():
    print("OK")
else:
    print("not in")

fruits = ['banana', 'apple', 'mango']
print(len(fruits))
print(range(len(fruits)))
for index in range(len(fruits)):
    print('当前水果 {}:'.format(index))
    print('当前水果 :', fruits[index])

print("Good bye!")

for ff in fruits:
    print('当前水果 :', ff)

