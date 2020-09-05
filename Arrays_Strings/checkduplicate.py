def findDuplicate(str):
    arr = [False]*128
    for i in str:
        val = ord(i)
        if arr[val]:
            return False
        arr[val] = True
    return True
stringToBeChecked = input()
result = findDuplicate(stringToBeChecked)
print(result)
        