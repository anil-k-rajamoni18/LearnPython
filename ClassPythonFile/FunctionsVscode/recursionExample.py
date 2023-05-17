# count = 0
# def printName(fname,lname): 
#     global count 
#     count+=1
#     print(count ,end = " : ")
#     print(fname+' '+lname )
#     printName('Akumar' , "K") #recursive calls / functions 

    

# printName('Kumar','R') 


def sumRecur(num): 
    if num == 1:
        return num
    else:
        return num+sumRecur(num-1)
    
    
if __name__ == '__main__':
    print(sumRecur(5))


# IDE  Intergrated Development Env
# Auto terminal 
# syntax highlight
# auto completion
# debugging and testing
# embeded git 
# extension support 