# 選択ソート
def sort(A):
    for i in range(0, len(A)):
        print('i:', i)
        select_min(A, i)

def select_min(A, i):
    print('A:', A)
    min = i
    for j in range(i + 1, len(A)):
        if A[min] > A[j]:
            min = j
    A[i], A[min] = A[min], A[i]