arr_repr = [[2, 2, 2, 2],
            [8, 2, 2, 2],
            [0, 256, 2048, 2048],
            [0, 64, 0, 1024]]

def right(arr_repr):

    for i in range(0,4):
        new_arr=[]
        j=3
        while j>0:
            if arr_repr[i][j]!=arr_repr[i][j-1]:
                new_arr.append(arr_repr[i][j])
                j-=1
            else:
                new_arr.append(arr_repr[i][j]+arr_repr[i][j-1])
                new_arr.append(0)
                j-=2
        if len(new_arr)<4:
            new_arr.append(arr_repr[i][0])
        new_arr=new_arr[::-1]
        j=0
        count=0
        while j<len(new_arr):
            if new_arr[j] == 0:
                new_arr.pop(j)
                count+=1
            else:
                j+=1
        new_arr=[0]*count + new_arr




        print(new_arr)



right(arr_repr)











