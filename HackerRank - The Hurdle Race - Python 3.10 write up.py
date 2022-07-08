##    https://www.hackerrank.com/challenges/the-hurdle-race/problem

##    A video player plays a game in which the character competes in a hurdle
##    race. Hurdles are of varying heights, and the characters have a maximum
##    height they can jump. There is a magic potion they can take that will
##    increase their maximum jump height by 1 unit for each dose. How many doses
##    of the potion must the character take to be able to jump all of the
##    hurdles. If the character can already clear all of the hurdles, return 0.

##### ##### ##### #####

#   The above problem description is a lot of words to say:
#   Return the difference between the maximum value of height and k.
#   If this value is negative, return 0.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in height
#   The approach is straight forward: use the max fuction to find the max value
#   of height and subtract k from it.  Use the max function again to find the max
#   of the previous value and 0.
#   The max function call on height will be linear with the number of elements
#   in height.  The outer max function call is constant.

def hurdleRace(k, height): 
    return max(0, max(height) - k)
