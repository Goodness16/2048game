import random
import pygame



# arr_repr = [[2, 0, 0, 0],
#             [4, 4, 0, 0],
#             [8, 4, 4, 2],
#             [4, 8, 2, 16]]
#
# score = 0

# right swipe function
def right(arr_repr, score=0, changed=False):
    for i in range(0,4):
        arr = arr_repr[i].copy()
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
                score += arr[j]+arr[j-1]
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

        ## New Lines
        if new_arr != arr_repr[i]:
            changed = True
        arr_repr[i] = new_arr
    return (changed, score)

# left swipe function
def left(arr_repr, score=0, changed=False):
    for i in range(0,4):
        arr = arr_repr[i].copy()
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
                score += arr[j]+arr[j+1]
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

        ## New Lines
        if new_arr != arr_repr[i]:
            changed = True
        arr_repr[i] = new_arr
    #print(changed)

    return (changed, score)

# up swipe function
def up(arr_repr, score=0, changed=False):
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
                score += arr[i] + arr[i + 1]
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

        ## New Lines
        arr = []
        for i in range(0, 4):
            arr.append(arr_repr[i][j])
        if arr != new_arr:
            changed = True
        for i in range(0, 4):
            arr_repr[i][j] = new_arr[i]
        j += 1
    return (changed, score)


# down swipe function
def down(arr_repr, score=0, changed=False):
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
                score += arr[i] + arr[i-1]
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

        ## New Lines
        arr = []
        for i in range(0, 4):
            arr.append(arr_repr[i][j])
        if arr != new_arr:
            changed = True
        for i in range(0, 4):
            arr_repr[i][j] = new_arr[i]
        j += 1
    #print(changed)
    return (changed, score)


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

def high(curr_score_value, high_score_value):
    if curr_score_value>high_score_value:
        high_score_value = curr_score_value
        f=open("Highscore.txt", "w")
        f.write(str(high_score_value))
        f.close()














