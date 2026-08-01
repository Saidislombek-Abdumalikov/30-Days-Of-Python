letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I am enjoying 30 days of Python Challenge"
print(sentence)



'''///////////////////////////////////////////////////////'''



multiline_string = '''I am a student and enjoy learning.
I didn't find anything as rewarding as learning to code.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a student and enjoy learning.
I didn't find anything as rewarding as learning to code.
That is why I created 30 days of python.'''"""
print(multiline_string)


'''//////////////////////////////////////////////////////////////'''


first_name = 'Saidislom'
last_name = 'Abdumalikov'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Saidislom Abdumalikov
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16