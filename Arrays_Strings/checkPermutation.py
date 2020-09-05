def checkPermutations(str1, str2):
    if len(str1)!= len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1==str2:
        return True
    return False
res = checkPermutations(input(), input()) 
print(res)