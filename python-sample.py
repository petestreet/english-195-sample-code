# Sample Python program - fix the mistakes!

your_name = raw_input( "First thing's first.  What is your name? ")
print("Welcome to Mars Cafe, " + your_name + "!")
print( "\n\nThis program will try to do a few things, but it may need your help.  Let's get started.\n\n" )


print( "1) Your name is " + str(len(your_name)) + " letters long.")


print( "\n2) Let's find out how many days old you are." )
your_age = raw_input( "How many years old are you? " )
print( "You are approximately " + your_age * 365 + " days old." )
# Can you make that number any more precise? Think about how long it's been since your last birthday, leap 
# years, et cetera.


print( "\n3) Print out the numbers 1-10:" )
for i in range(10):
    print(i)
    

print( "\n4) Print out the first 10 Fibonacci numbers:" )
def fibonacci(n):
    a,b = 1,1
    for i in range(n):
        print(a)
        a,b = b,a+b
fibonacci(10)
