def oneEditReplace(str1, str2):
    foundEdit = False
    index = 0   
    while index < len(str1): 
        if str1[index] != str2[index]:
            if foundEdit:
                return False
            foundEdit = True
        index+=1
    return True 
def oneEditInsert(str1, str2):
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    return True

def oneEditAway(str1, str2):
    if len(str1) == len(str2):
        return oneEditReplace(str1, str2)
    elif len(str1)+1 == len(str2):
        return oneEditInsert(str1, str2)
    elif len(str1) == len(str2)+1:
        return oneEditInsert(str2, str1) 
    else:
        return False

print(oneEditAway('baile','bail'))