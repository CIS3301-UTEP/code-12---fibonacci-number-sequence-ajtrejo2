def get_fibonacci_number(position):
  if position == 1 or position == 2:
     return 1
  else:
     return ((get_fibonacci_number(position-1)) + (get_fibonacci_number(position-2)))
  #Remove this line and insert your code here. Do not forget this function implements recursion.

def get_fibonacci_number_sequence(number):
   sequence = []
   for i in range(0, number):
      sequence.append(get_fibonacci_number(i + 1))
   return sequence
    
        

     #Remove this line and insert your code here. Do not forget to use get_fibonacci_number to create your list of numbers.
 
if __name__ == "__main__":
    print(get_fibonacci_number(7))
    print(get_fibonacci_number_sequence(15))
    
    