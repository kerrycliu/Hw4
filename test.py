from cacti import cacti_number
from log import timestamp

@cacti_number
def main(arry):
   pass

plot = [ [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 0, 1] ]

print(main(plot))