import time
from color import*

def partition(data, start, end, drawData, timeTick):
    
    pivot_index = start
    pivot = data[pivot_index]
    
    while start < end:
         
        while start < len(data) and data[start] <= pivot:
            start += 1
             
        while data[end] > pivot:
            end -= 1
        
        if(start < end):
            data[start], data[end] = data[end], data[start]
     
   
    data[end], data[pivot_index] = data[pivot_index], data[end]
    
    return end
     

def quick_sort(data, start, end, drawData, timeTick):
    if start < end:
        pivot_position = partition(data, start, end, drawData, timeTick)
        quick_sort(data, start, pivot_position-1, drawData, timeTick)
        quick_sort(data, pivot_position+1, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)
        
    drawData(data, [BLUE for x in range(len(data))])