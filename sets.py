def union(A, B):
    join = [x for x in B if x not in A]
    return A + join

def intersect(A, B):
    return[x for x in B if x in A]
    
def setdiff(A, B):
    return[x for x in A if x not in B]

def symdiff(A, B):
    return union(setdiff(A,B), setdiff(B,A))  

def cartprod(A, B):
    return[[x,y] for x in A for y in B]


    
print union([1,2,3],[2,3,4])
print intersect([1,2,3],[2,3,4])
print setdiff([1,2,3],[2,3,4])
print symdiff([1,2,3],[2,3,4])
print cartprod([1,2,3],[2,3,4])
