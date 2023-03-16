'''Create a file named log.py and create decorator inside called timestamp
• The decorator should print the current time then afterwards print anything the is being decorated (see
examples below)
Hint: - Use time.ctime()
Examples: Input (in file called test.py):
from log import timestamp
@timestamp
def hi():
print('hi')
def main():
hi()
main()
Output:
$ python3 test.py
Wed Oct 19 17:27:12 2022
hi'''

import time

def timestamp(func):
    def wrapper():
        print(time.ctime())
        func()
    return wrapper