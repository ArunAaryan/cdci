def checkPermutations(str1, str2):
    if len(str1) != len(str2):
        return False
    charset = [0]*128
    for i in str1:
        val = ord(i)
        charset[val]+=1
    for i in str2:
        val = ord(i)
        charset[val]-=1
        if charset[val]<0:
            return False
    return True
result = checkPermutations(input(),input())
print(result)