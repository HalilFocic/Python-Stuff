#Input:
#solution.solution(3, [7, 3, 5, 1])
#Output:
#    -1,7,6,3

#Input:
#solution.solution(5, [19, 14, 28])
#Output:
#    21,15,29

def getNextRazlika(vrh,number):
    return vrh//(2**number)

def advancedSearch(value,currentNode,height,level):
    if value==currentNode-1:
        return currentNode
    if value==currentNode-1-getNextRazlika(2**height-1,level):
        return currentNode
    if value>currentNode-1-getNextRazlika(2**height-1,level):
        return advancedSearch(value,currentNode-1,height,level+1)
    else:
        return advancedSearch(value,currentNode-1-getNextRazlika(2**height-1,level),height,level+1)
def solution(h, q):
    solve=[]
    for item in q:
        if item<1 or item>=2**h-1:
            solve.append(-1)
            continue
        solve.append(advancedSearch(item,2**h-1,h,1))
    return solve
    
    
print(solution(3, [7, 3, 5, 1]))
print(solution(5,[19,14,28]))
