#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = []
    for item in recipe:
      if item not in ingredients:
          return 0
      if ingredients[item] // recipe[item] > 0:
          batches.append(ingredients[item] // recipe[item])
      else: return 0
    
    return min(batches)

      






# check if ingredients value > than recipes value
# if it is greater subract recipes value from ingredients
# if not return iteration number



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


  # Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 

  ## Hints

#  * If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
#  * What's the _minimum_ number of loops we need to perform in order to write a working implementation?