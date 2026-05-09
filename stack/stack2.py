# # """
# # Basic stack operations using push, pop, and top.
# # """
""" 


"""


# # stack = []


# # def push():
# # 	value = int(input("Enter element to push: "))
# # 	stack.append(value)
# # 	print("Pushed successfully.")


# # def pop():
# # 	if len(stack) == 0:
# # 		print("Stack is empty. Nothing to pop.")
# # 		return

# # 	value = stack.pop()
# # 	print("Popped value:", value)


# # def top():
# # 	if len(stack) == 0:
# # 		print("Stack is empty. No top element.")
# # 		return

# # 	print("Top element:", stack[-1])


# # def show_menu():
# # 	print("\nStack Operations")
# # 	print("1. Push")
# # 	print("2. Pop")
# # 	print("3. Top")
# # 	print("4. Exit")


# # while True:
# # 	show_menu()
# # 	choice = input("Enter your choice: ")

# # 	if choice == "1":
# # 		push()
# # 	elif choice == "2":
# # 		pop()
# # 	elif choice == "3":
# # 		top()
# # 	elif choice == "4":
# # 		print("Exiting program.")
# # 		break
# # 	else:
# # 		print("Invalid choice. Please try again.")

# class stack:
#     def __init__(self):
#         self.stack=[]

# obj=stack()
# print(obj.stack)        



# # Push Operation with class
# class stack:
#     def __init__(self):
#         self.stack=[]

#     def push (self, element):
      
#       if self.stack is not None:
#          self.stack.append(element) 
#     #   else:
#     #      print("Stack is not Initialize")    

# obj=stack()
# item=input("Enter any value")
# obj.push(item)
# print(obj.push(item))
# print(obj.stack)     



# # POP Operation with class

# class stack:
#     def __init__(self):
#         self.stack=[]

#     def pop(self):
#         if len(self.stack)>0:
#             return self.stack.pop()
#         else:
#             # raise IndexError ("Stack is Empty")   
#             # raise Exception ("Stack is Empty") 
#             print("Stack is Empty") 

# obj=stack()
# print(obj.stack)  
# print(obj.pop())