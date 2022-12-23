import random

# arr_repr = [[2, 2, 2, 2],
#             [0, 2, 0, 0],
#             [0, 2, 2, 2],
#             [2, 2, 2, 0]]


# right swipe function
def right(arr_repr):
    for i in range(0,4):
        arr = arr_repr[i]
        j=0
        count=0
        while j<len(arr):
            if arr[j] == 0:
                arr.pop(j)
                count+=1
            else:
                j+=1
        arr=[0]*count + arr
        new_arr=[]
        j=3
        while j>0:
            if arr[j]!=arr[j-1]:
                new_arr.append(arr[j])
                j-=1
            else:
                new_arr.append(arr[j]+arr[j-1])
                new_arr.append(0)
                j-=2
        if len(new_arr)<4:
            new_arr.append(arr[0])
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
        arr_repr[i] = new_arr

# left swipe function
def left(arr_repr):
    for i in range(0,4):
        arr = arr_repr[i]
        j = 0
        count = 0
        while j < len(arr):
            if arr[j] == 0:
                arr.pop(j)
                count += 1
            else:
                j += 1
        arr = arr + [0] * count
        new_arr=[]
        j=0
        while j<3:
            if arr[j]!=arr[j+1]:
                new_arr.append(arr[j])
                j+=1
            else:
                new_arr.append(arr[j]+arr[j+1])
                new_arr.append(0)
                j+=2
        if len(new_arr)<4:
            new_arr.append(arr[3])
        j=0
        count=0
        while j<len(new_arr):
            if new_arr[j] == 0:
                new_arr.pop(j)
                count+=1
            else:
                j+=1
        new_arr=new_arr + [0]*count
        arr_repr[i] = new_arr

# up swipe function
def up(arr_repr):
    j = 0
    while j < 4:
        arr = []
        for i in range(0, 4):
            arr.append(arr_repr[i][j])
        i = 0
        count = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop(i)
                count += 1
            else:
                i += 1
        arr = arr + [0] * count
        new_arr = []
        i = 0
        while i < 3:
            if arr[i] != arr[i+1]:
                new_arr.append(arr[i])
                i += 1
            else:
                new_arr.append(arr[i] + arr[i+1])
                new_arr.append(0)
                i += 2
        if len(new_arr) < 4:
            new_arr.append(arr[3])
        i = 0
        count = 0
        while i < len(new_arr):
            if new_arr[i] == 0:
                new_arr.pop(i)
                count += 1
            else:
                i += 1
        new_arr = new_arr + [0] * count
        for i in range(0, 4):
            arr_repr[i][j] = new_arr[i]
        j += 1

# down swipe function
def down(arr_repr):
    j = 0
    while j < 4:
        arr = []
        for i in range(0, 4):
            arr.append(arr_repr[i][j])
        i = 0
        count = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop(i)
                count += 1
            else:
                i += 1
        arr = [0] * count + arr
        new_arr = []
        i = 3
        while i > 0:
            if arr[i] != arr[i-1]:
                new_arr.append(arr[i])
                i -= 1
            else:
                new_arr.append(arr[i] + arr[i-1])
                new_arr.append(0)
                i -= 2
        if len(new_arr) < 4:
            new_arr.append(arr[0])
        new_arr = new_arr[::-1]
        i = 0
        count = 0
        while i < len(new_arr):
            if new_arr[i] == 0:
                new_arr.pop(i)
                count += 1
            else:
                i += 1
        new_arr = [0] * count + new_arr
        for i in range(0, 4):
            arr_repr[i][j] = new_arr[i]
        j += 1

def random_insert(arr_repr):
    random_number = random.randint(1, 10)
    if random_number in range(1, 8):
        insert = 2
    else:
        insert = 4
    candidates = []
    for i in range(0, 4):
        for j in range(0, 4):
            if arr_repr[i][j] == 0:
                candidates.append(str(i)+str(j))
    n = len(candidates)
    random2 = random.randint(0, n-1)
    pos = candidates[random2]
    arr_repr[int(pos[0])][int(pos[1])] = insert



# down(arr_repr)
# print(arr_repr)




