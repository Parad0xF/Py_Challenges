def merge_the_tools(string, k):

    lst = []
    start = 0

    while start < len(string):
        lst.append(string[start:start+k])
        start += k

    for i in lst:
        temp = []
        for x in range(len(i)):
            if i[x] not in temp:
                temp.append(i[x])
        print(''.join(temp))

if __name__ == '__main__':

    string = "AABCAAADA"    
    k =3
    merge_the_tools(string, k)