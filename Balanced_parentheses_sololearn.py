#Balanced parentheses:
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.insert(0,item)
        
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
        
s = Stack()

def balanced(expression):
    
    try:
        for i in expression:
            if i == '(':
                s.push('(')
            elif i == ')':
                s.pop()
            else:
                continue
            
        if len(s.items) == 0:
            print(True)
        else:
            print(False)
    except:
        print(False)
    
balanced('gh(65(jh(fdc))(76h))')
balanced(input('Enter your mathematical expression: '))
"""
Here, first a stack is created so that we can take requiredcharacters from our
expression and put it inside our stack using push and then we will pop it out 
if it's counter balanced character gets detected. If it's a balanced parenthesis 
expression then we will get True else for unbalanced we will get False, and if
there is any error in our expression which will also refer to unbalanced
expression we have to use exceptions.
Stack --> function --> required character --> push --> counter character --> 
pop --> balanced --> True --> unbalanced --> False --> all in try --> 
exceptipon/error --> False
"""
        
#Wrong approach:      
"""
def balanced(expression):
    #your code goes here
    indices1 = []
    for i in range(len(expression)):
        if expression[i] == '(':
            indices1.append(i)

    indices2 = []
    for i in range(len(expression)):
        if expression[i] == ')':
            indices2.append(i)

    if len(indices1) == len(indices2):
        for x in range(len(indices1)) :
            if indices1[x] < indices2[len(indices1)-1-x]:
                return True
            else:
                return False
    else:
        return False

print(balanced(input()))
"""






