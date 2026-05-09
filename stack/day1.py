# Stack :-
'''
# Operation :- 1) push
               2) pop 
               3) top
               4) isempty
               5) isfull
               6) under flow
               7) over flow


'''

# Push :- 
'''stack=[]
n=int(input("enter number of element : "))
for i in range(n):
    element = eval(input("Enter any value : "))
    stack.append(element)
print(stack)'''


# Pop :-
'''stack=[]
n=int(input("enter number of element : "))
for i in range(n):
    element = eval(input("Enter any value : "))
    stack.append(element)
print(stack)
x=stack.pop(0)  # pop return in value
print(x,stack)'''


# Top :-
'''stack=[]
n=int(input("enter number of element : "))
for i in range(n):
    element = eval(input("Enter any value : "))
    stack.append(element)
print(stack)
t=stack[-1]
print(t)'''

# Isempty :-  Return is True/False
'''stack=[]
n=int(input("enter number of element : "))
for i in range(n):
    element = eval(input("Enter any value : "))
    stack.append(element)
print(stack)
if len(stack) == 0:
    print(" Stack is Empty")'''



# Isfull :- Return is True/False
'''max_stack_len =5
stack =[]
total_element= int(input("enter total number of element : "))
i =1
while i<total_element:
    if len(stack) == max_stack_len:
        print("Stack is Full !")
        break
    else:
        e=int(input("enter element : "))
        stack.append(e)
    i = i+1
print(stack)
'''


# USING FUNCTION :- Try to create using function.

# Create Push using function :-
'''stack = []
MAX = 5

def push():
    if len(stack) == MAX:
        print("Overflow! Stack is full")
    else:
        x = int(input("Enter element: "))
        stack.append(x)
        print("Stack:", stack)
push()'''

'''
def stack():
    stack =[]
    return stack
def push (stack,element):
    if stack is not None:
        stack.append(element)
        return
stack = stack()
element=int(input(" Enter any number : "))
push(stack,element)
print(stack)
'''
# Create Pop using function :-

'''stack = [10, 20, 30]
def pop():
    if len(stack) == 0:
        print("Underflow! Stack is empty")
    else:
        print("Popped element:", stack.pop())
        print("Stack:", stack)
pop()
'''

'''stack = []
n = int(input("Enter number of elements: "))
for i in range(n):
    element = eval(input("Enter any value: "))
    stack.append(element)

print("Stack:", stack)

def pop(stack):
    if len(stack) > 0:
        return stack.pop()
    else:
        return "Underflow! Stack is empty"
result = pop(stack)
print("Popped element:", result)
print("Stack after pop:", stack)
'''

# Create Top using function :-

'''stack = [10, 20, 30]
def top():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])
top()
'''

'''stack = []
n = int(input("Enter number of elements: "))
for i in range(n):
    element = eval(input("Enter any value: "))
    stack.append(element)
print("Stack:", stack)
def top(stack):
    if len(stack) > 0:
        return stack[-1]
    else:
        return "Underflow! Stack is empty"
result = top(stack)
print("Top element:", result)
'''

# Create isempty using function :-

'''stack = []
def isempty():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")
isempty()
'''


'''stack = []
n = int(input("Enter number of elements: "))
for i in range(n):
    element = eval(input("Enter any value: "))
    stack.append(element)
print("Stack:", stack)
def isempty(stack):
    if len(stack) == 0:
        return "Stack is empty"
    else:
        return "Stack is not empty"
print(isempty(stack))
'''

# Create isfull using function :-
'''
stack = [10, 20, 30, 40, 50]
MAX = 5
def isfull():
    if len(stack) == MAX:
        print("Stack is full")
    else:
        print("Stack is not full")
isfull()
'''
'''
stack = []
MAX = 5
n = int(input("Enter number of elements: "))
for i in range(n):
    element = eval(input("Enter any value: "))
    stack.append(element)

print("Stack:", stack)

def isfull(stack):
    if len(stack) == MAX:
        return True
    else:
        return False
print(isfull(stack))
'''



# Add to card operation prerfrom