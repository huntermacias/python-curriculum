# Python Program to 
# demonstrate stack implementation
# using list 

stack = []

# append() function to push
stack.append('h')
stack.append('u')
stack.append('n')
stack.append('t')
stack.append('e')
stack.append('r')

print("Initial Stack: ")
print(stack)

#pop() function to pop
# LIFO Order
# print("\nElement poped from stack: ")
# print("[",stack.pop(), "]")
reverse_stack = []
for i in stack[::-1]: 
	popped = stack.pop()
	reverse_stack.append(popped)

print("\nReverse Stack: ")
print(reverse_stack)

# print("\nStack after element popped: ")
# print(stack)
