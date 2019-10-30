# Intern Level Interview Question
# Question:
# Using python syntax show as many possible ways of printing the reverse of a given string using python

# Text to reverse
txt = "Hello World"


# 1 - Using slicing

print(txt[::-1])


# 2 - Using recursion

def recursion_reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return recursion_reverse(s[1:]) + s[0] 

print(recursion_reverse(txt))


# 3 - Using a loop

def loop_reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

print (loop_reverse(txt))


# 4 - Using 'reversed'

print("".join(reversed(txt)))


# 5 - Using a stack

# Function to create an empty stack. It  
# initializes size of stack as 0 
def createStack(): 
    stack=[] 
    return stack 
   
# Function to determine the size of the stack 
def size(stack): 
    return len(stack) 
   
# Stack is empty if the size is 0 
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
   
# Function to add an item to stack . It 
# increases size by 1     
def push(stack,item): 
    stack.append(item) 
   
# Function to remove an item from stack.  
# It decreases size by 1 
def pop(stack): 
    if isEmpty(stack): return
    return stack.pop() 

# Function to reverse a string
def stack_reverse(string): 
    n = len(string) 
       
    # Create a empty stack 
    stack = createStack() 
   
    # Push all characters of string to stack 
    for i in range(0,n,1): 
        push(stack,string[i]) 
   
    # Making the string empty since all 
    # characters are saved in stack     
    string="" 
   
    # Pop all characters of string and put 
    # them back to string 
    for i in range(0,n,1): 
        string+=pop(stack) 
           
    return string

print(stack_reverse(txt))  
