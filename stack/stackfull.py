# # Top Operation with class :-

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             print("Stack is Empty")

#     def top(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             print("Stack is Empty")
    
#     def is_empty(self):
#         if len(self.stack)==0:
#             print('true')
#         else:
#             print('false')




# obj = Stack()
# obj.push(10)
# # obj.pop()
# # obj.top()
# obj.push('python')
# # print(obj.top())
# # obj.is_empty()

class stack():
    def __init__(self,capacity):
        self.stack=[]
        self.c=capacity
    capacity=10
    def push(self,element):
        if self.stack is not None: 
            if len(self.stack)>=self.c:
                print(' stack overflowed')
            else:
                self.stack.append(element)
                print(stack)
obj=stack()
obj.push(20)-
