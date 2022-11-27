a = "vishal"
b = "raj"
c = a + b
d = "n"
print("the name is vishal raj" + d)

import sys
max_size = sys.maxsize
min_size = -sys.maxsize - 1
print(max_size,min_size)
class solution:
    def reverse_signed(z):
        x=0
        y=1
        if z<0:
            y = -1
            z = z*-1
        while z>0:
            x = (x*10) + z % 10
            z = z//10
        if not -2147483648<sum<2147483647:
            return 0
        return x*y

obj = solution()
print(obj.reverse(123))



                
        
