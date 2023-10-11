def plusMinus(arr):
    dic = {'nagetive': 0,
            'positive': 0,
            'zero': 0}
    list1 = list(arr)
    for i in list1:
        if i >0:
            dic['positive']+=1
        elif i < 0:
            dic['nagetive']+=1
        else:
            dic['zero']+=1
    length = len(arr)
    p = '{0:.6f}'.format(dic['positive']/length)
    n = '{0:.6f}'.format(dic['nagetive']/length)
    z = '{0:.6f}'.format(dic['zero']/length)
    print(p)
    print(n)
    print(z)

arr1 = (-1,-2,1,2,6,0)
plusMinus(arr1)