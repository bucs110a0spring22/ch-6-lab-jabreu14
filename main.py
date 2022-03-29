import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        if(n % 2) == 0:        # n is even
            n = n // 2
            count += 1
        else:                 # n is odd
            n = n * 3 + 1
            count += 1
    return count 
  
                    # the last print is 1

def main(): 
  value = int(input("Insert upper bound "))
  if(value <= 0):
    return True
  for start in range(1,value+1): 
    count = seq3np1(start)
    print("With a start value of", start, "the number of iterations is",count)
  graph(value)
  
def graph(iteration):
  mywindow = turtle.Screen()
  leonardo = turtle.Turtle()
  donatello = turtle.Turtle()
  mywindow.setworldcoordinates(0,0,10,10)
  max_so_far = 0
  for iteration in range(1, iteration+1):
    result = seq3np1(iteration)
    donatello.goto(iteration, result)
    if result > max_so_far:
      max_so_far = result
    leonardo.up()
    leonardo.goto(0, max_so_far)
    mywindow.setworldcoordinates(0,0,iteration+10,max_so_far+10)
  write = "Maximum so far:",iteration, result
  leonardo.write(write)
  mywindow.exitonclick()

main()