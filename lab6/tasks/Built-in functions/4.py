#Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:") 
print(delay(lambda x: math.sqrt(x), 2123, 25100))
