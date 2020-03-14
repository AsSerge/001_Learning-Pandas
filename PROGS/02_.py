def min(*args):
        res = float('inf')
        for arg in args:
                if arg < res:
                        res = arg
        return res
print(min(12,6,3,0,1,4,3,2,3,45,6,7,6,5))
print(min(1))