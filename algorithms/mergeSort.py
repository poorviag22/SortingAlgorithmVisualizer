import time
from color import *
      
def merge(data, l, m, r,drawData,timeTick):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
  
    for i in range(0, n1):
        L[i] = data[l + i]
 
    for j in range(0, n2):
        R[j] = data[m + 1 + j]
    
    i = 0     
    j = 0    
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1

def merge_sort(data,start,end,drawData,timeTick):
    if start<end:
        mid=int((start+end)/2) 
        merge_sort(data,start,mid,drawData,timeTick)
        merge_sort(data,mid+1,end,drawData,timeTick)

        merge(data,start,mid,end,drawData,timeTick)
      
        drawData(data, [YELLOW if x==mid else BLUE for x in range(len(data))])
        '''drawData(data,[PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])'''   