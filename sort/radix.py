# ****************************************************************分割线****************************************************************
# todo 基数排序

# 每循环一次，大位数会向后挤

def radix(input):
    max_val=max(input)
    max_digit=1  # 最大位数
    while max_val//10>0:
        max_digit+=1
        max_val=max_val//10

    digit=0
    while digit<max_digit:
        temp = [[] for i in range(10)]
        # 求每个元素的个十百位值
        for i in input:
            t=(i//10**digit)%10
            temp[t].append(i)

        input=[]
        for bucket in temp:
            for j in bucket:
                input.append(j)
        print("{t} {i}".format(t=temp,i=input))
        digit+=1
    return input

test=[111,100,21,11,10,1]
print(radix(test))
