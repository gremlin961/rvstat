import os
import sys

var1 = "internal var"

exvar1 = sys.argv[1]
exvar2 = sys.argv[2]

def external(test1, test2):
    test1 = test1
    test2 = test2
    print(test1+' and '+test2)
    print('collected external vars')
    return test1, test2;

test1, test2 = external(exvar1, exvar2)
print('The internal var is: '+var1)

print('The external vars are: '+test1+' and '+test2)
