'''result = ""
while True:
    try:
        a = raw_input()
        result += a
    except(EOFError):
        break
print (result)'''

import string
import sys

a = open("3_source.txt")

while True:
    try:
        long_string = a.readline()
        if long_string == "":
            break
        for i, c in enumerate(long_string):
            if i > 3 and i <= len(long_string)-5 and c in string.lowercase:
                count = 0
                for j in [-3,-2,-1,1,2,3]:
                    if long_string[i+j] in string.uppercase:
                        count += 1
                    else:
                        break
                for k in [-4,4]:
                    #print i+k
                    #print len(long_string)
                    if long_string[i+k] not in string.uppercase:
                        count += 1
                    else:
                        break
                if count == 8:
                    sys.stdout.write(c)
    except(EOFError):
        break

