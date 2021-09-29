#WRITE YOUR CODE IN THIS FILE
#define share fair
def shareFair(x,y):
    
    #if no remainder
    if (x%y) == 0:
        return True

    #if there is remainder
    else:
        return False

    #print share fair
print(shareFair(10, 5))