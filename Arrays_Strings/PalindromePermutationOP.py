# This is the easy implementation.
def checkPalindrome(str):
    table = [0] * 26
    countOdd=0
    for char in str:
        charNum = getChar(char)
        if charNum!=-1:
            table[charNum]+=1
            if table[charNum] %2 == 1:
                countOdd+=1
            else:
                countOdd-=1
    return countOdd<=1




def getChar(char):
    aNum = ord('a')
    valNum = ord(char) - (aNum)
    if 0 <= valNum <= 26:
        return valNum
    else:
        return -1 
print(checkPalindrome('cocoa'))
