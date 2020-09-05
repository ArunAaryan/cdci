# This is the easy implementation.
def checkPalindrome(str):
    table = [0] * 26
    for char in str:
        charNum = getChar(char)
        if(charNum>=0):
            table[charNum]+=1
    flag = False
    for val in table:
        if val%2 == 1:
            if flag:
                return False
            flag = True
    return True




def getChar(char):
    aNum = ord('a')
    valNum = ord(char) - (aNum)
    if 0 <= valNum <= 26:
        return valNum
    else:
        return -1 
print(checkPalindrome('coacoa'))
