'''
#  PUSH OPERATION 
stack=[]

stack_size= int(input('ENTER THE MAX LENTH FOR THE STACK--- '))
for i in range(stack_size):
     element=int(input(f'enter element no. {i+1} --- '))
     stack.append(element)

print('CURRENT STACK--:', stack)
'''

'''
#  POP 
stack=[]

stack_size= int(input('ENTER THE MAX LENTH FOR THE STACK--- '))
for i in range(stack_size):
     element=int(input(f'enter element on INDEX no. {i} --- '))
     stack.append(element)

x= stack.pop()  
#  pop() auto delete the last element (-1) unless we initialize index number in pop()       [ top element top()]
print('\n',' popped vlue= ',x, 'CURRENT STACK--:', stack)
'''

#  top element
stack=[]
stack_size= int(input('ENTER THE MAX LENTH FOR THE STACK--- '))
for i in range(stack_size):
     element=int(input(f'enter element on INDEX no. {i} --- '))
     stack.append(element)
print(stack,stack[-1])


def is_empty():
    if len(stack) ==0:
        print('Stack is Empty')
