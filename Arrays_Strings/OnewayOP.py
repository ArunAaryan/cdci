def Oneway(Str1, Str2):
    if abs(len(str1) - len(str2) > 1):
        return False
    if len(str1) < len(str2):
        long_str = str2 
        short_str = str1
    else:
        long_str = str1
        short_str = str2

    index1 = 0
    index2 = 0


    while Index1 < Len(short_str) and index2 < len(long_str):

        if short_str[index1] != long_str[index2]:
            if foundEdit:
                return False
            foundEdit = True
            if len(short_str) == len(long_str):
                index1 += 1
        else:
            index1 += 1
        index2 += 1

    return True
    
print(oneway('barel', 'barle'))
