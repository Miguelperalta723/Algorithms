#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #hard code min price to be first item at index 0
  #max profit so far would be second item - first item
  current_min_price_so_far = prices[0]
  max_profit_so_far = prices[1] - prices[0]
  #loop through prices starting with second item
  for i in range(1, len(prices)):
      #if any item is less than min price then make min price that item
      if prices[i] < current_min_price_so_far:
          current_min_price_so_far = prices[i]
      #if current price - min price is greather than max profit then make max profit price - min price
      elif prices[i] - current_min_price_so_far > max_profit_so_far:
          max_profit_so_far = prices[i] - current_min_price_so_far


  return max_profit_so_far 



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



  # Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here. 

# iterate to list
#find highest number
#find lowest number in an index lower than the highest number
#return the difference

# current_min_price_so_far = 0
#     max_profit_so_far = 0