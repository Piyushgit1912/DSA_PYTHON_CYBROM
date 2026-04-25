'''
#  PUSH OPERATION 
stack=[]

stack_size= int(input('ENTER THE MAX LENTH FOR THE STACK--- '))
for i in range(stack_size):
     element=int(input(f'enter element no. {i+1} --- '))
     stack.append(element)

print('CURRENT STACK--:', stack)
'''


#  POP 
stack=[]

stack_size= int(input('ENTER THE MAX LENTH FOR THE STACK--- '))
for i in range(stack_size):
     element=int(input(f'enter element on INDEX no. {i} --- '))
     stack.append(element)

x= stack.pop()
print('\n',' popped vlue= ',x, 'CURRENT STACK--:', stack)


# 
