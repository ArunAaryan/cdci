def urlify(str, true_length):
    space_count = 0
    for i in range(true_length):
        if str[i]==' ':
            space_count+=1
    index = space_count * 2 + true_length
    for i in range(true_length -1, -1, -1):
        if str[i]==' ':
            str[index - 1] = '0'
            str[index - 2] = '2'
            str[index - 3] = '%'
            index -= 3
        else:
            str[index -1 ] = str[i]
            index -= 1
    return str 
str = list('Mr John Smith    ')
result = urlify(str, 13)
print(result)

