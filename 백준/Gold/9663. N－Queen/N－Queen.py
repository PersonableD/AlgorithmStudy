#행이 x, 열이 y, board[y]=x
#x행에 놓고 놓을수없을 때 y+1 시켜준다.
#놓아도 되는지 아닌지 체크
import sys


def check(y, arr):
    for i in range(y):
        if arr[i]==arr[y] or y-i==arr[i]-arr[y] or arr[y]-arr[i]==y-i:
            return False
    return True

def nqueen(x,arr,y):
    global count
    if y==N:
        count+=1
        return
    else:
        while x < N:
            arr[y] = x
            if check(y, arr):
                nqueen(0, arr, y+1)
            x+=1
    return

N = int(sys.stdin.readline())

arr = [0] * N # N : input
x = 0
count = 0
nqueen(0, arr, 0)
print(count)
