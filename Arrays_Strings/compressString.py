def compressString(ustr):
    countConsecutive = 0
    new_string=''
    for i in range(len(ustr)):
        countConsecutive+=1
        if i+1 >= len(ustr) or ustr[i] != ustr[i+1]:
            new_string += ustr[i]+str(countConsecutive)
            countConsecutive = 0
    
    return new_string if len(ustr) > len(new_string) else new_string 

print(compressString('aaaaabbbbbccc'))


    