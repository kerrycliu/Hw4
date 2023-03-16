'''Create a file named double.py and create a decorator inside called double.
• Your decorator can assume the function using it has no arguments.
• The decorator should run the function once, print “Let’s try that again!”, then run the function
once again.
• Do not keep any test code when you submit your code. We only want the decorator.
Examples: Input (in file called test.py):
from double import double
@timestamp
def greet():
print('Hello World!')
def main():
greet()
main()'''

def double(func):
    def wrapper():
        func()
        print("Let's try that again")
        func()
    return wrapper



    
