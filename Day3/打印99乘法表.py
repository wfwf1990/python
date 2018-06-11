'''
1 * 1 =  1
2 * 1 = 2   2 * 2 = 4
3 * 1 = 3   3 * 2 = 6  3 * 3 = 9
'''
'''
col = 1
while col <= 9:
    num = 1
    while num <= col:
        print("%d * %d = %d\t" %(col,num,col*num),end="")
        num += 1
    print()
    col += 1
'''

'''
1 * 1 =  1
2 * 1 = 2   2 * 2 = 4
3 * 1 = 3   3 * 2 = 6  3 * 3 = 9
'''
for col in range(1,10):
    num = 1
    while num <= col:
        print("%d * %d = %d\t" % (col, num, col * num), end="")
        num +=1
    print()
    col +=1
