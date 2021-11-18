#linear serach algorithum function
def linear_search(list ,target):
    #finding target value using for loop
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    """
        verify result
    """
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("target not found")

#Target List
numbers = [1,2,3,4,5,6,7,8,9]
#calling linear search function
result = linear_search(numbers,5) #linear_search(numbers,put target value here)
#verify search result using verify function
verify(result)