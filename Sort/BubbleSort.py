"""
冒泡排序
比较稳定的排序方法
时间复杂度O(n^2)
"""


def bubble_sort(arr):
    for i in range(len(arr)-1):
        status = False     # 标示符，如果某一次比较没有发生任何改变，则停止循环
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                status = True
        if not status:
            break


if __name__ == '__main__':
    array = [1, 4, 7, 2, 8, 5, 9, 3, 6]
    bubble_sort(array)
    print(array)
