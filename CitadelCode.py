import random

def main(cost):
  balance = 0
  for i in range(1000000): # (game played 1 million times)
    prize = random.randint(0,3) # generate index of prize.
    boxes = [0,0,0,0] # initialise each box as elemnt of the array/list.
    boxes[prize] = 100 # randomly assign prize to a box.

    while True: # (loop removing each box out of game until £100 found.)
      balance -= cost # pay to open box.
      choice = random.randint(0,len(boxes)-1) # randomly pick box.
      if boxes[choice] == 100: # if box is prize, 
        balance += 100 # add £100 to balance.
        break # break out of loop.
      else: # if not,
        boxes.pop(choice) # remove chosen box.

  print(f' Final Balance: £{balance} with cost £{cost} and 1m played games')

main(40)
main(39)
main(41)
