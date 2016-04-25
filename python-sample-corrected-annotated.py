# Sample Python program

# "your_name" is a variable that we set equal to whatever the user types.
your_name = raw_input( "First thing's first.  What is your name? " )

# "print" is an example of one of Python's built-in functions.  Everything inside the parentheses will get printed
# to the console below.  This usage of "print" also uses the variable "your_name" that we defined above.  
print( "Welcome to Mars Cafe, " + your_name + "!" )
print("\n\nThis program will try to do a few things, but it may need your help.  Let's get started.\n\n")



# Variables can be used and manipulated in a program.  So far we have one variable, "your_name".  This is useful
# to have since the user supplies the value for "your_name", so the programmer doesn't need to have
# any prior knowledge of who might be using the program.  

# In the line directly below, we do something interesting with the name that the user provided us: we count 
# how many letters it has!  How does this happen?  First, we need a basic understanding of variable "types".  
# Many programming languages have "strong typing", meaning that whenever you define a variable you must also define
# that variable's type.  Common variable types are "integer", "string" (meaning a string of letters - anything 
# inside quotation marks), and "decimal".  Python has so-called "weak typing" or "implicit typing" (or "duck 
# typing" - if it looks like a duck and quacks like a duck, then it's a duck), which means that the type of a 
# variable is implied when the program is run.  Notice that we never defined "your_name" to be a string, but since 
# it was set equal to input that the user typed in line 4, the program implies that the data stored inside 
# "your_name" is of type "string".

# Whew!  Now that that's out of the way, we can understand what's going on when we find the number of letters in our
# user's name.  You'll see that "your_name" is wrapped inside two different functions.  "len" and "str" are 
# built-in functions just like "print" is.  "len" finds the length of a string and returns an integer value.  "str"
# converts an integer value into a string value.  The functions are executed from the inside out, so we first get the
# length of "your_name" and then convert that number back into a string in order to be printed with the "print"
# function.  Try removing the "str" function and the program will throw an error.  That's because, in the computer's
# eyes, it doesn't make sense to add a number to a string.  When the integer is converted back into a string, the "+"
# operation no longer means "addition", but rather, "concatenation."
print( "1) Your name is " + str(len(your_name)) + " letters long." )



# What's with this funky "\n" character that pops up all over?  Don't pay it much attention, all it does is 
# denote a carriage return inside a string.  They have been added for readability's sake.
print( "\n2) Let's find out how many days old you are." )

# Here we're defining another variable, "your_age", in the same way that we defined "your_name" above.
# "raw_input" is a built-in python function that collects a line of text that the user types in on the command 
# line below.
your_age = raw_input( "How many years old are you? " )

# Another instance of a variable being wrapped in a few of Python's built-in functions before being printed to 
# the console.  As you likely noticed, not using the wrapping functions "str" and "int" results in a really wonky
# output.  In the original code, printing "your_age * 365" along with the two other strings "You are approximately "
# and " days old." printed out the number you typed in 365 times in a row.  The reason is that, even if you typed
# in a number for "your_age", the "raw_input" function interperets any typed input as a string.  Thus if enter "21"
# for this prompt, your_age would be equal to "21" the string of characters, not 21 the number.  In the corrected
# code below, the "int" funciton first converts "your_age" into an integer, and that integer is then multiplied 
# by 365.  Then the result of that calculation is convertet back into a string with "str".

# Can you make that number any more precise? Think about how long it's been since your last birthday, leap
# years, et cetera.
print( "You are approximately " + str(int(your_age) * 365) + " days old." )



# One of the basic conceptual building blocks of programs, along with variables, is "loops".  The most common type
# of loop is a "for-loop", and those are the kind we use in this program.  The idea is that a computer can do 
# repetitive tasks much faster than a human, so we ought to use that to our advantage.  With a for-loop, we tell
# the program how many times to execute some section of code.  In the example below, we want to print out the 
# numbers 1 through 10.  We could very easily write:
#       print("1")
#       print("2")
#       print("3")
#       etc...
# but that seems like a horrible waste of time.  Especially if instead we wanted to print out, say, the numbers
# 1 through 200.  Or the first ten thousand primes.  You get the idea.  Instead, the for-loop below lets us write:
#       for i in range(10):
# to accomplish the same task.  This line is a bit of shorthand.  It defines a temporary variable "i" to be used
# inside the loop.  "i" won't be available outside the loop unless we redefine it elsewhere.  The built-in "range"
# function builds a list of numbers up to 10 (the number we passed into the function), and it sets "i" to be equal
# to each number in that list successively.  So on the first iteration of the for-loop, "i" is equal to 0.  The next
# iteration, "i" is 1, on the next iteration "i" is equal to "2", and so on.  
print( "\n3) Print out the numbers 1-10:" )
for i in range(10):
    # Most programming languages are zero-indexed, meaning they start counting up from zero instead of one.
    # Another option would be to call an alternate version of the "range" function, whose format 
    # is "range(start, stop)"". To use it to print out the numbers 1-10, you'd write:
    #           for i in range(1,11):
    # Notice that we go from 1 to 11, not 1 to 10.  A quirk of this version of the range function is that
    # we go *to* the "stop" argument, not *through* it.  
    print(i+1)
    


print( "\n4) Print out the first 10 Fibonacci numbers:" )
def fibonacci(n):
    # Python, unlike many other programming languages, has strict rules on indentation.  Lines of code are 
    # executed one after another as long as they're on the same indentation level.  So the code that is considered
    # "inside" a function (like this fibonacci function), or "inside" a for-loop, is all a level more indented than
    # the loop or function itself.  
    a,b = 1,1
    for i in range(n):
        print(a)
        a,b = b,a+b
        
# Remember Python's built-in functions?  "print", "str", "len", et al?  Well, we can define our own custom functions
# too.  That's exactly what we do above with the line "def fibonacci(n):", where we define a function named
# "fibonacci" that accepts one argument.  In the function definition itself, that argument is a variable that we
# call "n", although we could have named it anything else.  Inside the function we define two more variables, "a"
# and "b", set them both equal to 1, and then use a for-loop to generate the fibonacci sequence for "n" terms and
# print out each term along the way with a call to the "print" function.

# After the function is defined, we can call it just like we've been calling Python's built-in functions.  Directly
# below, we have "fibonacci(10)".  This calls the fibonacci function that we wrote, and sets "n" equal to 10.  If
# we call the function again, but pass in a different number, the function's variable "n" will be set to that new
# number and either a longer or shorter fibonacci sequence will be printed out.

# Try calling the fibonacci function again, only this time print out the first 50 terms.  Think about the limitations
# of Python's "duck typing" in a function like this.  Would it make sense to print out the first 3.14 terms of the
# fibonacci sequence?  What if we called fibonacci("happy birthday")?  Feel free to experiment with the fibonacci
# function that we've defined above, extend or alter what it prints out or the types of input it accepts.  
fibonacci(10)
