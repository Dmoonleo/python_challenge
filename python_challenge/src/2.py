import string

def file_process():
    result = ""
    while True:
        try:
            a = raw_input()
            result += a
        except(EOFError):
            break
    print (result)

a = open("2_out.txt")
long_string = a.readline()
result = ""
for i in long_string:
    if i in string.letters:
        result += i
print(result)