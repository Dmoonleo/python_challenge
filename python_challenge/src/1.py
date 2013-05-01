from string import maketrans

def string_trans(string):
    result = ""
    for i in range(0, len(string)):
        if ord(string[i]) >= ord("a") and ord(string[i]) <= ord("z"):
            result += chr((ord(string[i])-ord("a")+2)%26 + ord("a"))
        else:
            result += string[i]
    print(result)
string_trans("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

trantab = maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(a.translate(trantab))
#print(str.ascii_lowercase())