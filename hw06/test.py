"""
nums = []
for x in range(8):
    nums.append(x)

print nums

squares = []
for x in range(8):
    squares.append(x**2)

print squares


print [x for x in range(8)]

print [x*x for x in range(8)]

print [ (x, x*x, x*x*x) for x in range(8) ]

p="myNoobPass1234"

print [x for x in p]

print [x for x in "1234"]

UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print [ x for x in p if x in UC_LETTERS ]

print [ 1 for x in p if x in UC_LETTERS ]

print [ 1 if x in UC_LETTERS else 0 for x in p ]
"""

def passwordTest(test):
    UC_LETTERS1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UC_LETTERS2="abcdefghijklmnopqrstuvwxyz"
    UC_NUMBERS="0123456789"
    if len([x for x in test if x in UC_LETTERS1]) > 0:
        if len([x for x in test if x in UC_LETTERS2]) > 0:
            if len([x for x in test if x in UC_NUMBERS]) > 0:
                return True
    return False

"""
print passwordTest("ABCd0")
print passwordTest("ABCD0")
print passwordTest("ABCdO")
print passwordTest("abcd0")
"""

def passwordStrength(test):
    UC_LETTERS1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UC_LETTERS2="abcdefghijklmnopqrstuvwxyz"
    UC_NUMBERS="0123456789"
    UC_CHARACTERS=".?!&#,;:-_*"
    c = 0
    if len([x for x in test if x in UC_LETTERS1]) > 2:
        c+=2
    elif len([x for x in test if x in UC_LETTERS1]) > 0:
        c+=1
    if len([x for x in test if x in UC_LETTERS2]) > 2:
        c+=2
    elif len([x for x in test if x in UC_LETTERS2]) > 0:
        c+=1
    if len([x for x in test if x in UC_NUMBERS]) > 1:
        c+=2
    elif len([x for x in test if x in UC_NUMBERS]) > 0:
        c+=1
    if len([x for x in test if x in UC_CHARACTERS]) > 1:
        c+=2
    elif len([x for x in test if x in UC_CHARACTERS]) > 0:
        c+=1
    if len(test) > 11:
        c+=2
    elif len(test) > 7:
        c+=1
    return c
"""
print passwordStrength("a")
print passwordStrength("B")
print passwordStrength("aaa")
print passwordStrength("BBB")
print passwordStrength("1")
print passwordStrength("22")
print passwordStrength("!")
print passwordStrength("??")
print passwordStrength("aaaaaaaa")
print passwordStrength("aaaaaaaaaaaa")
print passwordStrength("asadBDFS345!!!")
"""
