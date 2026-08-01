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


'''////////////////////////////////////////////////////////////////'''


print('I am enjoying the Python Challenge.\nI am ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
'''I am enjoying the Python Challenge.
I am ?
Days  Topics  Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"'''


'''////////////////////////////////////////////////////////////////////// '''