import os
import time

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 107, 144]
b = []
ln = len(a)
i = 0

while(i <= len(a) - 1):
    if(a[i] % 2 == 0):
        b.append(a[i])
    
    i += 1
#--

print b  
