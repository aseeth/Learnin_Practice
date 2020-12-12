#################Searching Algorithms#################

###Binary search####

def binSearch(n,num):
    low = 0
    high = len(n)-1
    #mid = 0
    while low<=high:
        mid = (low+high)//2
        if num == n[mid]:
            return mid
        elif num>n[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1
    

num = int(input("enter u r num:"))
n = [11,22,33,44,55,66,77]
res = binSearch(n,num)
if res != -1:
    print("num present at",res,"index")
else:
    print("num not in list")