#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos,neg,zero=0,0,0
    for num in arr:
        if num >0:
            pos=pos+1
        elif num==0:
            zero=zero+1
        else:
            neg=neg+1
    total = pos+zero+neg
    if total>0:
        print(pos/total,"\n",neg/total,"\n",zero/total)
    else:
        print(0,"\n",0,"\n",0)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
