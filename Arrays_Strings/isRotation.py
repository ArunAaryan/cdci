def isRotation(str1, str2):
    if(not len(str1)== len(str2) and len(str1) > 0):
        return False
    str1 *= 2 
    if str2 in str1:
        return True
print(isRotation('Mango','goMan'))
