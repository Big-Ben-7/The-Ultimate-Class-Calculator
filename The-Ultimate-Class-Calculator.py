from math import *
import random
import cmath
import types

global ans
ans = 0.0
global rl
rl = 0.0
global im
im = 0.0
global im2
im2 = 0.0
global mod
mod = 0.0
global ang
ang = 0.0
global rat
rat = 0.0
global dif
dif = 0.0
global rt
rt = 0.0
global rt2
rt2 = 0.0
global binsum
binsum = ""
global attempts
attempts = 0
global problems
problems = 1
global print_problems
print_problems = 1
global pos
pos = [[1, 1, 1, 8], [1, 1, 1, 11], [1, 1, 1, 12], [1, 1, 2, 6], [1, 1, 2, 7], [1, 1, 2, 8], [1, 1, 2, 9], [1, 1, 2, 10], [1, 1, 2, 11], [1, 1, 2, 12], [1, 1, 3, 4], [1, 1, 3, 5], [1, 1, 3, 6], [1, 1, 3, 7], [1, 1, 3, 8], [1, 1, 3, 9], [1, 1, 3, 10], [1, 1, 3, 11], [1, 1, 3, 12], [1, 1, 4, 4], [1, 1, 4, 5], [1, 1, 4, 6], [1, 1, 4, 7], [1, 1, 4, 8], [1, 1, 4, 9], [1, 1, 4, 10], [1, 1, 4, 12], [1, 1, 5, 5], [1, 1, 5, 6], [1, 1, 5, 7], [1, 1, 5, 8], [1, 1, 6, 6], [1, 1, 6, 8], [1, 1, 6, 9], [1, 1, 6, 12], [1, 1, 7, 10], [1, 1, 8, 8], [1, 1, 10, 12], [1, 1, 11, 11], [1, 1, 11, 12], [1, 1, 12, 12], [1, 2, 2, 4], [1, 2, 2, 5], [1, 2, 2, 6], [1, 2, 2, 7], [1, 2, 2, 8], [1, 2, 2, 9], [1, 2, 2, 10], [1, 2, 2, 11], [1, 2, 2, 12], [1, 2, 3, 3], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 8], [1, 2, 3, 9], [1, 2, 3, 10], [1, 2, 3, 11], [1, 2, 3, 12], [1, 2, 4, 4], [1, 2, 4, 5], [1, 2, 4, 6], [1, 2, 4, 7], [1, 2, 4, 8], [1, 2, 4, 9], [1, 2, 4, 10], [1, 2, 4, 11], [1, 2, 4, 12], [1, 2, 5, 5], [1, 2, 5, 6], [1, 2, 5, 7], [1, 2, 5, 8], [1, 2, 5, 9], [1, 2, 5, 10], [1, 2, 5, 12], [1, 2, 6, 6], [1, 2, 6, 7], [1, 2, 6, 8], [1, 2, 6, 9], [1, 2, 6, 10], [1, 2, 6, 11], [1, 2, 6, 12], [1, 2, 7, 7], [1, 2, 7, 8], [1, 2, 7, 9], [1, 2, 7, 10], [1, 2, 7, 11], [1, 2, 7, 12], [1, 2, 8, 8], [1, 2, 8, 9], [1, 2, 8, 10], [1, 2, 9, 11], [1, 2, 9, 12], [1, 2, 10, 11], [1, 2, 10, 12], [1, 2, 11, 11], [1, 2, 11, 12], [1, 2, 12, 12], [1, 3, 3, 3], [1, 3, 3, 4], [1, 3, 3, 5], [1, 3, 3, 6], [1, 3, 3, 7], [1, 3, 3, 8], [1, 3, 3, 9], [1, 3, 3, 10], [1, 3, 3, 11], [1, 3, 3, 12], [1, 3, 4, 4], [1, 3, 4, 5], [1, 3, 4, 6], [1, 3, 4, 7], [1, 3, 4, 8], [1, 3, 4, 9], [1, 3, 4, 10], [1, 3, 4, 11], [1, 3, 4, 12], [1, 3, 5, 6], [1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 5, 9], [1, 3, 5, 10], [1, 3, 5, 11], [1, 3, 5, 12], [1, 3, 6, 6], [1, 3, 6, 7], [1, 3, 6, 8], [1, 3, 6, 9], [1, 3, 6, 10], [1, 3, 6, 11], [1, 3, 6, 12], [1, 3, 7, 7], [1, 3, 7, 8], [1, 3, 7, 9], [1, 3, 7, 10], [1, 3, 7, 12], [1, 3, 8, 8], [1, 3, 8, 9], [1, 3, 8, 10], [1, 3, 8, 11], [1, 3, 8, 12], [1, 3, 9, 9], [1, 3, 9, 10], [1, 3, 9, 11], [1, 3, 9, 12], [1, 3, 10, 10], [1, 3, 10, 11], [1, 3, 10, 12], [1, 3, 11, 11], [1, 3, 11, 12], [1, 3, 12, 12], [1, 4, 4, 4], [1, 4, 4, 5], [1, 4, 4, 6], [1, 4, 4, 7], [1, 4, 4, 8], [1, 4, 4, 9], [1, 4, 4, 10], [1, 4, 4, 11], [1, 4, 4, 12], [1, 4, 5, 5], [1, 4, 5, 6], [1, 4, 5, 7], [1, 4, 5, 8], [1, 4, 5, 9], [1, 4, 5, 10], [1, 4, 5, 11], [1, 4, 5, 12], [1, 4, 6, 6], [1, 4, 6, 7], [1, 4, 6, 8], [1, 4, 6, 9], [1, 4, 6, 10], [1, 4, 6, 11], [1, 4, 6, 12], [1, 4, 7, 7], [1, 4, 7, 8], [1, 4, 7, 9], [1, 4, 7, 11], [1, 4, 7, 12], [1, 4, 8, 8], [1, 4, 8, 9], [1, 4, 8, 11], [1, 4, 8, 12], [1, 4, 9, 10], [1, 4, 9, 11], [1, 4, 9, 12], [1, 4, 10, 10], [1, 4, 10, 11], [1, 4, 10, 12], [1, 4, 12, 12], [1, 5, 5, 5], [1, 5, 5, 6], [1, 5, 5, 9], [1, 5, 5, 10], [1, 5, 5, 11], [1, 5, 5, 12], [1, 5, 6, 6], [1, 5, 6, 7], [1, 5, 6, 8], [1, 5, 6, 9], [1, 5, 6, 10], [1, 5, 6, 11], [1, 5, 6, 12], [1, 5, 7, 8], [1, 5, 7, 9], [1, 5, 7, 10], [1, 5, 7, 11], [1, 5, 7, 12], [1, 5, 8, 8], [1, 5, 8, 9], [1, 5, 8, 10], [1, 5, 8, 11], [1, 5, 8, 12], [1, 5, 9, 9], [1, 5, 9, 10], [1, 5, 9, 11], [1, 5, 9, 12], [1, 5, 10, 10], [1, 5, 10, 11], [1, 5, 10, 12], [1, 5, 11, 11], [1, 5, 11, 12], [1, 5, 12, 12], [1, 6, 6, 6], [1, 6, 6, 8], [1, 6, 6, 9], [1, 6, 6, 10], [1, 6, 6, 11], [1, 6, 6, 12], [1, 6, 7, 9], [1, 6, 7, 10], [1, 6, 7, 11], [1, 6, 7, 12], [1, 6, 8, 8], [1, 6, 8, 9], [1, 6, 8, 10], [1, 6, 8, 11], [1, 6, 8, 12], [1, 6, 9, 9], [1, 6, 9, 10], [1, 6, 9, 12], [1, 6, 10, 12], [1, 6, 11, 12], [1, 6, 12, 12], [1, 7, 7, 9], [1, 7, 7, 10], [1, 7, 7, 11], [1, 7, 7, 12], [1, 7, 8, 8], [1, 7, 8, 9], [1, 7, 8, 10], [1, 7, 8, 11], [1, 7, 8, 12], [1, 7, 9, 9], [1, 7, 9, 10], [1, 7, 9, 11], [1, 7, 9, 12], [1, 7, 10, 12], [1, 7, 12, 12], [1, 8, 8, 8], [1, 8, 8, 9], [1, 8, 8, 10], [1, 8, 8, 11], [1, 8, 8, 12], [1, 8, 9, 11], [1, 8, 9, 12], [1, 8, 10, 11], [1, 8, 10, 12], [1, 8, 11, 12], [1, 8, 12, 12], [1, 9, 9, 12], [1, 9, 10, 12], [1, 9, 11, 11], [1, 9, 11, 12], [1, 9, 12, 12], [1, 10, 10, 12], [1, 10, 11, 12], [1, 10, 12, 12], [1, 11, 11, 12], [1, 11, 12, 12], [1, 12, 12, 12], [2, 2, 2, 3], [2, 2, 2, 4], [2, 2, 2, 5], [2, 2, 2, 7], [2, 2, 2, 8], [2, 2, 2, 9], [2, 2, 2, 10], [2, 2, 2, 11], [2, 2, 2, 12], [2, 2, 3, 3], [2, 2, 3, 4], [2, 2, 3, 5], [2, 2, 3, 6], [2, 2, 3, 7], [2, 2, 3, 8], [2, 2, 3, 9], [2, 2, 3, 10], [2, 2, 3, 11], [2, 2, 3, 12], [2, 2, 4, 4], [2, 2, 4, 5], [2, 2, 4, 6], [2, 2, 4, 7], [2, 2, 4, 8], [2, 2, 4, 9], [2, 2, 4, 10], [2, 2, 4, 11], [2, 2, 4, 12], [2, 2, 5, 5], [2, 2, 5, 6], [2, 2, 5, 7], [2, 2, 5, 8], [2, 2, 5, 9], [2, 2, 5, 10], [2, 2, 5, 11], [2, 2, 5, 12], [2, 2, 6, 6], [2, 2, 6, 7], [2, 2, 6, 8], [2, 2, 6, 9], [2, 2, 6, 10], [2, 2, 6, 11], [2, 2, 6, 12], [2, 2, 7, 7], [2, 2, 7, 8], [2, 2, 7, 10], [2, 2, 7, 12], [2, 2, 8, 8], [2, 2, 8, 9], [2, 2, 8, 10], [2, 2, 8, 12], [2, 2, 9, 10], [2, 2, 9, 11], [2, 2, 9, 12], [2, 2, 10, 10], [2, 2, 10, 11], [2, 2, 11, 11], [2, 2, 11, 12], [2, 2, 12, 12], [2, 3, 3, 3], [2, 3, 3, 5], [2, 3, 3, 6], [2, 3, 3, 7], [2, 3, 3, 8], [2, 3, 3, 9], [2, 3, 3, 10], [2, 3, 3, 11], [2, 3, 3, 12], [2, 3, 4, 4], [2, 3, 4, 5], [2, 3, 4, 6], [2, 3, 4, 7], [2, 3, 4, 8], [2, 3, 4, 9], [2, 3, 4, 10], [2, 3, 4, 11], [2, 3, 4, 12], [2, 3, 5, 5], [2, 3, 5, 6], [2, 3, 5, 7], [2, 3, 5, 8], [2, 3, 5, 9], [2, 3, 5, 10], [2, 3, 5, 11], [2, 3, 5, 12], [2, 3, 6, 6], [2, 3, 6, 7], [2, 3, 6, 8], [2, 3, 6, 9], [2, 3, 6, 10], [2, 3, 6, 11], [2, 3, 6, 12], [2, 3, 7, 7], [2, 3, 7, 8], [2, 3, 7, 9], [2, 3, 7, 10], [2, 3, 7, 11], [2, 3, 7, 12], [2, 3, 8, 8], [2, 3, 8, 9], [2, 3, 8, 10], [2, 3, 8, 11], [2, 3, 8, 12], [2, 3, 9, 9], [2, 3, 9, 10], [2, 3, 9, 12], [2, 3, 10, 10], [2, 3, 10, 12], [2, 3, 11, 11], [2, 3, 11, 12], [2, 3, 12, 12], [2, 4, 4, 4], [2, 4, 4, 5], [2, 4, 4, 6], [2, 4, 4, 7], [2, 4, 4, 8], [2, 4, 4, 9], [2, 4, 4, 10], [2, 4, 4, 11], [2, 4, 4, 12], [2, 4, 5, 5], [2, 4, 5, 6], [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 5, 9], [2, 4, 5, 10], [2, 4, 5, 11], [2, 4, 5, 12], [2, 4, 6, 6], [2, 4, 6, 7], [2, 4, 6, 8], [2, 4, 6, 9], [2, 4, 6, 10], [2, 4, 6, 11], [2, 4, 6, 12], [2, 4, 7, 7], [2, 4, 7, 8], [2, 4, 7, 9], [2, 4, 7, 10], [2, 4, 7, 11], [2, 4, 7, 12], [2, 4, 8, 8], [2, 4, 8, 9], [2, 4, 8, 10], [2, 4, 8, 11], [2, 4, 8, 12], [2, 4, 9, 9], [2, 4, 9, 10], [2, 4, 9, 12], [2, 4, 10, 10], [2, 4, 10, 11], [2, 4, 10, 12], [2, 4, 11, 11], [2, 4, 11, 12], [2, 4, 12, 12], [2, 5, 5, 7], [2, 5, 5, 8], [2, 5, 5, 9], [2, 5, 5, 10], [2, 5, 5, 11], [2, 5, 5, 12], [2, 5, 6, 6], [2, 5, 6, 7], [2, 5, 6, 8], [2, 5, 6, 9], [2, 5, 6, 10], [2, 5, 6, 11], [2, 5, 6, 12], [2, 5, 7, 7], [2, 5, 7, 8], [2, 5, 7, 9], [2, 5, 7, 10], [2, 5, 7, 11], [2, 5, 8, 8], [2, 5, 8, 9], [2, 5, 8, 10], [2, 5, 8, 11], [2, 5, 8, 12], [2, 5, 9, 10], [2, 5, 9, 11], [2, 5, 9, 12], [2, 5, 10, 10], [2, 5, 10, 11], [2, 5, 10, 12], [2, 5, 11, 12], [2, 5, 12, 12], [2, 6, 6, 6], [2, 6, 6, 7], [2, 6, 6, 8], [2, 6, 6, 9], [2, 6, 6, 10], [2, 6, 6, 11], [2, 6, 6, 12], [2, 6, 7, 8], [2, 6, 7, 9], [2, 6, 7, 10], [2, 6, 7, 11], [2, 6, 7, 12], [2, 6, 8, 8], [2, 6, 8, 9], [2, 6, 8, 10], [2, 6, 8, 11], [2, 6, 8, 12], [2, 6, 9, 9], [2, 6, 9, 10], [2, 6, 9, 11], [2, 6, 9, 12], [2, 6, 10, 10], [2, 6, 10, 11], [2, 6, 10, 12], [2, 6, 11, 12], [2, 6, 12, 12], [2, 7, 7, 8], [2, 7, 7, 10], [2, 7, 7, 11], [2, 7, 7, 12], [2, 7, 8, 8], [2, 7, 8, 9], [2, 7, 8, 11], [2, 7, 8, 12], [2, 7, 9, 10], [2, 7, 9, 11], [2, 7, 10, 10], [2, 7, 10, 11], [2, 7, 10, 12], [2, 7, 11, 12], [2, 7, 12, 12], [2, 8, 8, 8], [2, 8, 8, 9], [2, 8, 8, 10], [2, 8, 8, 11], [2, 8, 8, 12], [2, 8, 9, 9], [2, 8, 9, 10], [2, 8, 9, 11], [2, 8, 9, 12], [2, 8, 10, 10], [2, 8, 10, 11], [2, 8, 10, 12], [2, 8, 11, 11], [2, 8, 11, 12], [2, 8, 12, 12], [2, 9, 9, 11], [2, 9, 9, 12], [2, 9, 10, 10], [2, 9, 10, 11], [2, 9, 10, 12], [2, 9, 11, 11], [2, 10, 10, 11], [2, 10, 10, 12], [2, 10, 11, 11], [2, 10, 11, 12], [2, 11, 11, 11], [2, 11, 11, 12], [2, 11, 12, 12], [2, 12, 12, 12], [3, 3, 3, 3], [3, 3, 3, 4], [3, 3, 3, 5], [3, 3, 3, 6], [3, 3, 3, 7], [3, 3, 3, 8], [3, 3, 3, 9], [3, 3, 3, 10], [3, 3, 3, 11], [3, 3, 3, 12], [3, 3, 4, 4], [3, 3, 4, 5], [3, 3, 4, 6], [3, 3, 4, 7], [3, 3, 4, 8], [3, 3, 4, 9], [3, 3, 4, 11], [3, 3, 4, 12], [3, 3, 5, 5], [3, 3, 5, 6], [3, 3, 5, 7], [3, 3, 5, 9], [3, 3, 5, 10], [3, 3, 5, 12], [3, 3, 6, 6], [3, 3, 6, 7], [3, 3, 6, 8], [3, 3, 6, 9], [3, 3, 6, 10], [3, 3, 6, 11], [3, 3, 6, 12], [3, 3, 7, 7], [3, 3, 7, 8], [3, 3, 7, 9], [3, 3, 7, 11], [3, 3, 7, 12], [3, 3, 8, 8], [3, 3, 8, 9], [3, 3, 8, 10], [3, 3, 8, 12], [3, 3, 9, 9], [3, 3, 9, 10], [3, 3, 9, 11], [3, 3, 9, 12], [3, 3, 11, 12], [3, 3, 12, 12], [3, 4, 4, 4], [3, 4, 4, 5], [3, 4, 4, 6], [3, 4, 4, 7], [3, 4, 4, 8], [3, 4, 4, 9], [3, 4, 4, 10], [3, 4, 4, 11], [3, 4, 4, 12], [3, 4, 5, 5], [3, 4, 5, 6], [3, 4, 5, 7], [3, 4, 5, 8], [3, 4, 5, 9], [3, 4, 5, 10], [3, 4, 5, 11], [3, 4, 5, 12], [3, 4, 6, 6], [3, 4, 6, 8], [3, 4, 6, 9], [3, 4, 6, 10], [3, 4, 6, 11], [3, 4, 6, 12], [3, 4, 7, 7], [3, 4, 7, 8], [3, 4, 7, 9], [3, 4, 7, 10], [3, 4, 7, 11], [3, 4, 7, 12], [3, 4, 8, 9], [3, 4, 8, 10], [3, 4, 8, 11], [3, 4, 8, 12], [3, 4, 9, 9], [3, 4, 9, 11], [3, 4, 9, 12], [3, 4, 10, 10], [3, 4, 10, 12], [3, 4, 11, 12], [3, 4, 12, 12], [3, 5, 5, 6], [3, 5, 5, 7], [3, 5, 5, 8], [3, 5, 5, 9], [3, 5, 5, 11], [3, 5, 5, 12], [3, 5, 6, 6], [3, 5, 6, 7], [3, 5, 6, 8], [3, 5, 6, 9], [3, 5, 6, 10], [3, 5, 6, 11], [3, 5, 6, 12], [3, 5, 7, 8], [3, 5, 7, 9], [3, 5, 7, 10], [3, 5, 7, 11], [3, 5, 7, 12], [3, 5, 8, 8], [3, 5, 8, 9], [3, 5, 8, 11], [3, 5, 8, 12], [3, 5, 9, 9], [3, 5, 9, 10], [3, 5, 9, 12], [3, 5, 10, 10], [3, 5, 10, 11], [3, 5, 10, 12], [3, 5, 11, 11], [3, 5, 11, 12], [3, 5, 12, 12], [3, 6, 6, 6], [3, 6, 6, 7], [3, 6, 6, 8], [3, 6, 6, 9], [3, 6, 6, 10], [3, 6, 6, 11], [3, 6, 6, 12], [3, 6, 7, 7], [3, 6, 7, 8], [3, 6, 7, 9], [3, 6, 7, 10], [3, 6, 7, 12], [3, 6, 8, 8], [3, 6, 8, 9], [3, 6, 8, 10], [3, 6, 8, 12], [3, 6, 9, 9], [3, 6, 9, 10], [3, 6, 9, 11], [3, 6, 9, 12], [3, 6, 10, 10], [3, 6, 10, 11], [3, 6, 10, 12], [3, 6, 11, 11], [3, 6, 11, 12], [3, 6, 12, 12], [3, 7, 7, 7], [3, 7, 7, 8], [3, 7, 7, 9], [3, 7, 7, 10], [3, 7, 7, 12], [3, 7, 8, 8], [3, 7, 8, 9], [3, 7, 8, 11], [3, 7, 8, 12], [3, 7, 9, 9], [3, 7, 9, 10], [3, 7, 9, 11], [3, 7, 9, 12], [3, 7, 10, 10], [3, 7, 10, 11], [3, 7, 11, 11], [3, 7, 11, 12], [3, 7, 12, 12], [3, 8, 8, 8], [3, 8, 8, 9], [3, 8, 8, 10], [3, 8, 8, 11], [3, 8, 8, 12], [3, 8, 9, 9], [3, 8, 9, 10], [3, 8, 9, 11], [3, 8, 9, 12], [3, 8, 10, 10], [3, 8, 10, 11], [3, 8, 10, 12], [3, 8, 11, 11], [3, 8, 11, 12], [3, 8, 12, 12], [3, 9, 9, 9], [3, 9, 9, 10], [3, 9, 9, 11], [3, 9, 9, 12], [3, 9, 10, 10], [3, 9, 10, 11], [3, 9, 10, 12], [3, 9, 11, 11], [3, 9, 11, 12], [3, 9, 12, 12], [3, 10, 10, 12], [3, 10, 11, 12], [3, 11, 11, 12], [3, 11, 12, 12], [3, 12, 12, 12], [4, 4, 4, 4], [4, 4, 4, 5], [4, 4, 4, 6], [4, 4, 4, 7], [4, 4, 4, 8], [4, 4, 4, 9], [4, 4, 4, 10], [4, 4, 4, 11], [4, 4, 4, 12], [4, 4, 5, 5], [4, 4, 5, 6], [4, 4, 5, 7], [4, 4, 5, 8], [4, 4, 5, 10], [4, 4, 5, 11], [4, 4, 5, 12], [4, 4, 6, 8], [4, 4, 6, 9], [4, 4, 6, 10], [4, 4, 6, 11], [4, 4, 6, 12], [4, 4, 7, 7], [4, 4, 7, 8], [4, 4, 7, 9], [4, 4, 7, 10], [4, 4, 7, 12], [4, 4, 8, 8], [4, 4, 8, 9], [4, 4, 8, 10], [4, 4, 8, 11], [4, 4, 8, 12], [4, 4, 9, 11], [4, 4, 9, 12], [4, 4, 10, 10], [4, 4, 10, 12], [4, 4, 11, 12], [4, 4, 12, 12], [4, 5, 5, 5], [4, 5, 5, 6], [4, 5, 5, 7], [4, 5, 5, 8], [4, 5, 5, 9], [4, 5, 5, 10], [4, 5, 6, 6], [4, 5, 6, 7], [4, 5, 6, 8], [4, 5, 6, 9], [4, 5, 6, 10], [4, 5, 6, 11], [4, 5, 6, 12], [4, 5, 7, 7], [4, 5, 7, 8], [4, 5, 7, 9], [4, 5, 7, 10], [4, 5, 7, 11], [4, 5, 7, 12], [4, 5, 8, 8], [4, 5, 8, 9], [4, 5, 8, 10], [4, 5, 8, 11], [4, 5, 8, 12], [4, 5, 9, 9], [4, 5, 9, 10], [4, 5, 9, 12], [4, 5, 10, 10], [4, 5, 10, 11], [4, 5, 10, 12], [4, 5, 11, 11], [4, 5, 11, 12], [4, 5, 12, 12], [4, 6, 6, 6], [4, 6, 6, 7], [4, 6, 6, 8], [4, 6, 6, 9], [4, 6, 6, 10], [4, 6, 6, 12], [4, 6, 7, 7], [4, 6, 7, 8], [4, 6, 7, 9], [4, 6, 7, 10], [4, 6, 7, 12], [4, 6, 8, 8], [4, 6, 8, 9], [4, 6, 8, 10], [4, 6, 8, 12], [4, 6, 9, 9], [4, 6, 9, 10], [4, 6, 9, 12], [4, 6, 10, 10], [4, 6, 10, 11], [4, 6, 10, 12], [4, 6, 11, 11], [4, 6, 11, 12], [4, 6, 12, 12], [4, 7, 7, 7], [4, 7, 7, 8], [4, 7, 7, 11], [4, 7, 8, 8], [4, 7, 8, 9], [4, 7, 8, 10], [4, 7, 8, 11], [4, 7, 8, 12], [4, 7, 9, 9], [4, 7, 9, 10], [4, 7, 9, 11], [4, 7, 9, 12], [4, 7, 10, 10], [4, 7, 10, 11], [4, 7, 10, 12], [4, 7, 11, 11], [4, 7, 11, 12], [4, 7, 12, 12], [4, 8, 8, 8], [4, 8, 8, 9], [4, 8, 8, 10], [4, 8, 8, 11], [4, 8, 8, 12], [4, 8, 9, 9], [4, 8, 9, 10], [4, 8, 9, 11], [4, 8, 9, 12], [4, 8, 10, 10], [4, 8, 10, 11], [4, 8, 10, 12], [4, 8, 11, 11], [4, 8, 11, 12], [4, 8, 12, 12], [4, 9, 9, 10], [4, 9, 9, 12], [4, 9, 10, 11], [4, 9, 10, 12], [4, 9, 11, 11], [4, 9, 11, 12], [4, 9, 12, 12], [4, 10, 10, 11], [4, 10, 10, 12], [4, 10, 11, 12], [4, 10, 12, 12], [4, 12, 12, 12], [5, 5, 5, 5], [5, 5, 5, 6], [5, 5, 5, 9], [5, 5, 5, 12], [5, 5, 6, 6], [5, 5, 6, 7], [5, 5, 6, 8], [5, 5, 6, 11], [5, 5, 7, 7], [5, 5, 7, 8], [5, 5, 7, 10], [5, 5, 7, 11], [5, 5, 8, 8], [5, 5, 8, 9], [5, 5, 8, 10], [5, 5, 8, 11], [5, 5, 8, 12], [5, 5, 9, 9], [5, 5, 9, 10], [5, 5, 9, 11], [5, 5, 10, 10], [5, 5, 10, 11], [5, 5, 11, 11], [5, 5, 11, 12], [5, 5, 12, 12], [5, 6, 6, 6], [5, 6, 6, 7], [5, 6, 6, 8], [5, 6, 6, 9], [5, 6, 6, 10], [5, 6, 6, 12], [5, 6, 7, 7], [5, 6, 7, 8], [5, 6, 7, 9], [5, 6, 7, 12], [5, 6, 8, 8], [5, 6, 8, 9], [5, 6, 8, 10], [5, 6, 8, 12], [5, 6, 9, 9], [5, 6, 9, 10], [5, 6, 9, 11], [5, 6, 9, 12], [5, 6, 10, 10], [5, 6, 10, 11], [5, 6, 10, 12], [5, 6, 11, 11], [5, 6, 11, 12], [5, 6, 12, 12], [5, 7, 7, 9], [5, 7, 7, 10], [5, 7, 7, 11], [5, 7, 8, 8], [5, 7, 8, 9], [5, 7, 8, 10], [5, 7, 9, 10], [5, 7, 9, 11], [5, 7, 9, 12], [5, 7, 10, 10], [5, 7, 10, 11], [5, 7, 10, 12], [5, 7, 11, 11], [5, 7, 12, 12], [5, 8, 8, 8], [5, 8, 8, 9], [5, 8, 8, 10], [5, 8, 9, 11], [5, 8, 9, 12], [5, 8, 10, 11], [5, 8, 10, 12], [5, 8, 11, 12], [5, 8, 12, 12], [5, 9, 9, 11], [5, 9, 9, 12], [5, 9, 10, 10], [5, 9, 10, 11], [5, 9, 12, 12], [5, 10, 10, 11], [5, 10, 10, 12], [5, 10, 11, 11], [5, 11, 12, 12], [6, 6, 6, 6], [6, 6, 6, 8], [6, 6, 6, 9], [6, 6, 6, 10], [6, 6, 6, 11], [6, 6, 6, 12], [6, 6, 7, 9], [6, 6, 7, 10], [6, 6, 7, 11], [6, 6, 7, 12], [6, 6, 8, 8], [6, 6, 8, 9], [6, 6, 8, 10], [6, 6, 8, 11], [6, 6, 8, 12], [6, 6, 9, 10], [6, 6, 9, 11], [6, 6, 9, 12], [6, 6, 10, 12], [6, 6, 11, 12], [6, 6, 12, 12], [6, 7, 7, 10], [6, 7, 7, 11], [6, 7, 8, 9], [6, 7, 8, 10], [6, 7, 8, 11], [6, 7, 8, 12], [6, 7, 9, 9], [6, 7, 9, 12], [6, 7, 10, 10], [6, 7, 10, 12], [6, 7, 11, 11], [6, 7, 11, 12], [6, 7, 12, 12], [6, 8, 8, 8], [6, 8, 8, 9], [6, 8, 8, 10], [6, 8, 8, 11], [6, 8, 8, 12], [6, 8, 9, 9], [6, 8, 9, 10], [6, 8, 9, 11], [6, 8, 9, 12], [6, 8, 10, 11], [6, 8, 10, 12], [6, 8, 11, 11], [6, 8, 11, 12], [6, 8, 12, 12], [6, 9, 9, 10], [6, 9, 9, 11], [6, 9, 9, 12], [6, 9, 10, 11], [6, 9, 10, 12], [6, 9, 11, 12], [6, 9, 12, 12], [6, 10, 10, 10], [6, 10, 11, 12], [6, 10, 12, 12], [6, 11, 11, 12], [6, 11, 12, 12], [6, 12, 12, 12], [7, 7, 7, 12], [7, 7, 8, 11], [7, 7, 9, 10], [7, 7, 11, 12], [7, 7, 12, 12], [7, 8, 8, 9], [7, 8, 8, 10], [7, 8, 8, 11], [7, 8, 8, 12], [7, 8, 9, 10], [7, 8, 9, 12], [7, 8, 10, 10], [7, 8, 10, 11], [7, 8, 11, 12], [7, 8, 12, 12], [7, 9, 10, 11], [7, 9, 10, 12], [7, 9, 11, 11], [7, 9, 11, 12], [7, 9, 12, 12], [7, 10, 10, 11], [7, 10, 10, 12], [7, 10, 12, 12], [8, 8, 8, 10], [8, 8, 8, 11], [8, 8, 8, 12], [8, 8, 9, 11], [8, 8, 9, 12], [8, 8, 10, 12], [8, 8, 11, 12], [8, 8, 12, 12], [8, 9, 9, 12], [8, 9, 10, 12], [8, 9, 11, 11], [8, 9, 11, 12], [8, 9, 12, 12], [8, 10, 10, 12], [8, 10, 11, 11], [8, 10, 12, 12], [8, 11, 12, 12], [9, 9, 9, 12], [9, 9, 11, 12], [9, 9, 12, 12], [9, 10, 11, 12], [9, 10, 12, 12], [9, 11, 11, 11], [9, 11, 12, 12], [9, 12, 12, 12], [10, 10, 10, 12], [10, 10, 11, 12], [10, 10, 12, 12], [10, 11, 11, 12], [10, 11, 12, 12], [10, 12, 12, 12], [11, 11, 11, 12], [11, 11, 12, 12], [11, 12, 12, 12], [12, 12, 12, 12]]
random.shuffle(pos)
global keeps
keeps = ["ans", "pi", "e", "tau", "inf", "nan", "infj", "nanj", "keeps", "rl", "im", "im2", "mod", "ang", "rat", "rt", "rt2", "binsum", "dif", "problems", "print_problems", "pos", "attempts"]
def clear_variables():
    for var in list(globals()):
        if var not in keeps and not isinstance(globals()[var], (types.ModuleType, types.FunctionType, types.BuiltinFunctionType, type)):
            del globals()[var]

def settings():
    global sig
    print()
    print("Welcome to settings!")
    print("Please enter the setting to turn on or off")
    while True:
        print()
        setting = input("Setting (i): ")
        if setting.lower() == "" or setting.lower() == "exit" or setting.lower() == "exi":
            break
        elif setting.lower() == "i" or setting.lower() == "inf" or setting.lower() == "info":
            print()
            print("Settings: ")
            print(f"In development!")
            continue
        else:
            print('Please enter a setting, "i" for info, or return to exit')
            continue
        value = input("On/off: ")
        if value.lower() == "" or value.lower() == "exit" or value.lower() == "exi":
            continue
        elif value.lower() != "on" and value.lower() != "off":
            print('Please enter either "on" or "off", or return to exit')
            continue

def integer(n):
    if round(n) == round(n, 12):
        return n
    
def series_find_constants(iunterm, indexcalc):
    scindex = 0
    while scindex < 2:
        if scindex == 0:
            cstring = "pi"
            constant = pi
        else:
            cstring = "e"
            constant = e
        if iunterm == 0:
            sumindex = f"ix{round(iunterm, 12)}"
            print(sumindex + f" (index of {round(iunterm, 12)}) = {round(indexcalc)}")
            globals()[sumindex] = indexcalc
            keeps.append(sumindex)
            break
        elif iunterm % constant == 0:
            if iunterm / constant > 0:
                if iunterm == constant:
                    sumindex = "ix" + cstring
                    print(sumindex + f" (index of " + cstring + f") = {round(indexcalc)}")
                else:
                    sumindex = f"ix{round(iunterm / constant)}" + cstring
                    print(sumindex + f" (index of {round((iunterm / constant))}" + cstring + f") = {round(indexcalc)}")
                globals()[sumindex] = indexcalc
                keeps.append(sumindex)
                break
            elif iunterm / constant < 0:
                if iunterm / constant == -1:
                    sumindex = f"ix_" + cstring
                    print(sumindex + f" (index of -" + cstring + f") = {round(indexcalc)}")
                else:
                    sumindex = f"ix_{round(abs(iunterm / constant))}" + cstring
                    print(sumindex + f" (index of -{round(abs(iunterm / constant))}" + cstring + f") = {round(indexcalc)}")
                globals()[sumindex] = indexcalc
                keeps.append(sumindex)
                break
        elif constant % iunterm == 0:
            if constant / iunterm < 0:
                sumindex = f"ix_" + cstring + f"_D_{round(abs(constant / iunterm))}"
                print(sumindex + f" (index of -" + cstring + f"/{round(abs(constant / iunterm))}" + f") = {round(indexcalc)}")
                globals()[sumindex] = indexcalc
                keeps.append(sumindex)
                break
            elif constant / iunterm > 0:
                sumindex = f"ix" + cstring + f"_D_{round(constant / iunterm)}"
                print(sumindex + f" (index of " + cstring + f"/{round((constant / iunterm))}" + f") = {round(indexcalc)}")
                globals()[sumindex] = indexcalc
                keeps.append(sumindex)
                break
        elif scindex == 1:
            if round(iunterm, 12) > 0:
                sumindex = f"ix{round(iunterm, 12)}"
            else:
                sumindex = f"ix_{abs(round(iunterm, 12))}"
            print(sumindex + f" (index of {round(iunterm, 12)}) = {round(indexcalc)}")
            globals()[sumindex] = indexcalc
            keeps.append(sumindex)
        scindex += 1

def print_binomial(a, b, c, d, n, k, unterm, x, y):
    global binsum
    co = comb(abs(n), k) * a ** (abs(n) - k) * c ** k
    xpow = round(b * (abs(n) - k), 12)
    ypow = round(d * k, 12)
    if round(co, 12) == 1 and (xpow != 0 or ypow != 0):
        cost = ""
    elif round(co, 12) == -1 and (xpow != 0 or ypow != 0):
        cost = "-"
    else:
        cost = f"{round(co, 12)} "
    if x != y:
        if xpow == 1:
            xpowst = x + " "
        elif xpow == 0:
            xpowst = ""
        elif xpow < 0:
            xpowst = x + f"^({xpow}) "
        else:
            xpowst = x + f"^{xpow} "
        if ypow == 1:
            ypowst = y
        elif ypow == 0:
            ypowst = ""
        elif ypow < 0:
            ypowst = y + f"^({ypow})"
        else:
            ypowst = y + f"^{ypow}"
        combined = cost + xpowst + ypowst
    else:
        vpow = xpow + ypow
        if vpow == 1:
            vpowst = x
        elif vpow == 0:
            vpowst = ""
        elif vpow < 0:
            vpowst = x + f"^({vpow})"
        else:
            vpowst = x + f"^{vpow}"
        combined = cost + vpowst
    if combined[len(combined) - 1] == " ":
        combined = combined[:len(combined) - 1]
    if n >= 0:
        print(f"Term {unterm}: " + combined)
    else:
        print(f"Term {unterm} denominator: " + combined)
    if combined[0] == "-":
        combined = combined[1:]
        binsum = binsum[:len(binsum) - 3] + " - "
    binsum += combined + " + "
    covar = f"cf{unterm}"
    globals()[covar] = co
    keeps.append(covar)
    print(covar+ f" (term {unterm} coefficient) = {round(co, 12)}")

def from_polar():
    global ans
    global rl
    global im
    global ang
    global mod
    print()
    print("Welcome to complex operations in polar form!")
    print("Please enter the modulus/absolute value and angle/argument of the terms")
    while True:
        clear_variables()
        print()
        av = input("Term 1 modulus/absolute value (i): ")
        if av == "" or av == "exit" or av == "exi":
            break
        elif av == "i" or av == "info" or av == "inf":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as terms')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ^ (exponent)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc")
            print('Real constants such as "pi", "e", and "tau" can be entered')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "rl" (real part of previous complex result), "im" (imaginary part of previous complex result), "rt" (1st real solution of previous quadratic), "rt2" (2nd real solution of previous quadratic), "im2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "cf1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation")
            print('Enter "rec" for rectangular form, "r" for real operations, "m" for matrix operations, "s" for summations (this will direct to binomial expansion), "f" for functions (this will direct to polynomials), and "g" for games (this will direct to play Math 24)')
            continue
        elif av == "rec" or av == "rectangular" or av == "rectangular form":
            from_rectangular()
            break
        elif av == "r" or av == "real" or av == "rea" or av == "real operations":
            real_operation()
            break
        elif av == "f" or av == "functions" or av == "fun":
            polynomial()
            break
        elif av == "m" or av == "matrix" or av == "mat" or av == "matrix operations":
            matrix_operation()
            break
        elif av == "s" or av == "sum" or av == "summations":
            binomial_expansion()
            break
        elif av == "g" or av == "gam" or av == "games":
            math24play()
            break
        try:
            av = av.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            av = 0 + eval(av)
            if round(av, 12) < 0:
                print('Absolute values cannot be negative')
                continue
        except:
            print('Please enter a real nonnegative number or expression, "i" for info, or return to exit')
            continue
        inang = input("Term 1 angle/argument: ")
        if inang == "" or inang == "exit" or inang == "exi":
            continue
        try:
            inang = inang.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            inang = 0 + eval(inang)
        except:
            print('Please enter a real number or expression, or return to exit')
            continue
        while True:
            angmode = input("Inputted in (r)adians or (d)egrees? ")
            if angmode.lower() == "radians" or angmode.lower() == "rad" or angmode.lower() == "r":
                ang = inang
                break
            elif angmode.lower() == "degrees" or angmode.lower() == "deg" or angmode.lower() == "d":
                ang = radians(inang)
                break
            else:
                print('Please enter either "r" for radians or "d" for degrees')
        a = av * cos(ang)
        b = av * sin(ang)
        cterm1 = f"{round(av, 12)} cos({round(inang, 12)}) + {round(av, 12)} sin({round(inang, 12)})i"
        print("First term: " + cterm1)
        while True:
            print()
            op = input("Operation (i): ")
            if op.lower() == "info" or op.lower() == "i" or op.lower() == "inf":
                print()
                print('The following operations can be entered: equals (=), add (+), subtract (-), multiply (*), divide (/), exponent (^), rectangular ([])')
                print("The above operations can only be entered as an operation, not as part of an expression")
            else:
                break
        if op.lower() == "" or op.lower() == "exit" or op.lower() == "exi":
            continue
        print()
        if not(op.lower() == "=" or op.lower() == "equals" or op.lower() == "equ" or op.lower() == "rectangular" or op.lower() == "rec" or op.lower() == "rectangular form"):
            av2 = input("Term 2 modulus/absolute value: ")
            if av2 == "" or av2 == "exit" or av2 == "exi":
                continue
            try:
                av2 = av2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                av2 = 0 + eval(av2)
                if round(av2, 12) < 0:
                    print('Absolute values cannot be negative')
                    continue
            except:
                print('Please enter a real number or expression, or return to exit')
                continue                        
            inang2 = input("Term 2 angle/argument: ")
            if inang2 == "" or inang2 == "exit" or inang2 == "exi":
                continue
            try:
                inang2 = inang2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                inang2 = 0 + eval(inang2)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            while True:
                angmode2 = input("Inputted in (r)adians or (d)egrees? ")
                if angmode2.lower() == "radians" or angmode2.lower() == "rad" or angmode2.lower() == "r":
                    ang2 = inang2
                    break
                elif angmode2.lower() == "degrees" or angmode2.lower() == "deg" or angmode2.lower() == "d":
                    ang2 = radians(inang2)
                    break
                else:
                    print('Please enter either "r" for radians or "d" for degrees')
            c = av2 * cos(ang2)
            d = av2 * sin(ang2)
            cterm2 = f"{round(av2, 12)} cos({round(inang2, 12)}) + {round(av2, 12)} sin({round(inang2, 12)})i"
            print("Second term: " + cterm2)
            print()
        try:
            if op.lower() == "=" or op.lower() == "equals" or op.lower() == "equ":
                res = cmath.polar(complex(a, b))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "+" or op.lower() == "add":
                res = cmath.polar(complex(a, b) + complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "-" or op.lower() == "subtract" or op.lower() == "sub":
                res = cmath.polar(complex(a, b) - complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "*" or op.lower() == "multiply" or op.lower() == "mul":
                res = cmath.polar(complex(a, b) * complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "/" or op.lower() == "divide" or op.lower() == "div":
                res = cmath.polar(complex(a, b) / complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "^" or op.lower() == "exponent" or op.lower() == "exp" or op.lower() == "**":
                res = cmath.polar(complex(a, b) ** complex(c, d))
                ares = res[1]
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")
            elif op.lower() == "rectangular" or op.lower() == "rec" or op.lower() == "rectangular form" or op.lower() == "rec for" or op.lower() == "[]":
                res = cmath.rect(av, ang)
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")                
            else:
                print('Please enter a valid operation ("i" for info and return to exit)')
        except:
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms')
            print("Division by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print()

def from_rectangular():
    global ans
    global rl
    global im
    global ang
    global mod
    print()
    print("Welcome to complex operations in rectangular form!")
    print("Please enter the first term in the form a + bi and the second term (if needed) in the form c + di")               
    while True:
        clear_variables()
        print()
        a = input("a (i): ")
        if a == "" or a == "exit" or a == "exi":
            break
        elif a == "i" or a == "info" or a == "inf":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as values')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ^ (exponent)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc")
            print('Real constants such as "pi", "e", and "tau" can be entered')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "rl" (real part of previous complex result), "im" (imaginary part of previous complex result), "rt" (1st real solution of previous quadratic), "rt2" (2nd real solution of previous quadratic), "im2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "cf1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation")
            print('Enter "p" for polar form, "r" for real operations, "m" for matrix operations, "s" for summations (this will direct to binomial expansion), "f" for functions (this will direct to polynomials), and "g" for games (this will direct to play Math 24)')
            continue
        elif a == "p" or a == "polar" or a == "pol" or a == "polar form":
            from_polar()
            break
        elif a == "r" or a == "rea" or a == "real" or a == "real operations":
            real_operation()
            break
        elif a == "f" or a == "fun" or a == "functions":
            polynomial()
            break
        elif a == "s" or a == "summations" or a == "sum":
            binomial_expansion()
            break
        elif a == "m" or a == "mat" or a == "matrix" or a == "matrix operations":
            matrix_operation()
            break
        elif a == "g" or a == "gam" or a == "games":
            math24play()
            break
        try:
            a = a.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            a = 0 + eval(a)
        except:
            print('Please enter a real number or expression, "i" for info, or return to exit')
            continue
        b = input("b: ")
        if b == "" or b == "exit" or b == "exi":
            continue
        try:
            b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            b = 0 + eval(b)
        except:
            print('Please enter a real number or expression, or return to exit')
            continue
        if round(a, 12) != 0 and round(b, 12) > 0:
            if round(b, 12) != 1:
                cterm1 = f"{round(a, 12)} + {round(b, 12)}i"
            else:
                cterm1 = f"{a} + i"
        elif round(a, 12) != 0 and round(b, 12) < 0:
            if round(b, 12) != -1:
                cterm1 = f"{round(a, 12)} - {round(b * -1, 12)}i"
            else:
                cterm1 = f"{round(a, 12)} - i"
        elif round(a, 12) == 0 and round(b, 12) != 0:
            if round(b, 12) != -1 and round(b, 12) != 1:
                cterm1 = f"{round(b, 12)}i"
            elif round(b, 12) == 1:
                cterm1 = "i"
            else:
                cterm1 = "-i"
        elif round(b, 12) == 0:
            cterm1 = f"{round(a, 12)}"
        print("First term: " + cterm1)
        while True:
            print()
            op = input("Operation (i): ")
            if op.lower() == "info" or op.lower() == "i" or op.lower() == "inf":
                print()
                print('The following operations can be entered: equals (=), add (+), subtract (-), multiply (*), divide (/), exponent (^), absolute value or modulus (||), angle or argument (<), polar (|<)')
                print("The above operations can only be entered as an operation, not as part of an expression")
            else:
                break
        if op.lower() == "" or op.lower() == "exit" or op.lower() == "exi":
            continue
        if not(op.lower() == "=" or op.lower() == "equals" or op.lower() == "equ" or op.lower() == "argument" or op.lower() == "arg" or op.lower() == "angle" or op.lower() == "ang" or op.lower() == "phase" or op.lower() == "pha" or op.lower() == "polar" or op.lower() == "pol" or op.lower() == "abs" or op.lower() == "absolute value" or op.lower() == "magnitude" or op.lower() == "mag" or op.lower() == "||" or op.lower() == "modulus" or op.lower() == "mod"):
            print()
            c = input("c: ")
            if c == "" or c == "exit" or c == "exi":
                continue
            try:
                c = c.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                c = 0 + eval(c)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue                        
            d = input("d: ")
            if d == "" or d == "exit" or d == "exi":
                continue
            try:
                d = d.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                d = 0 + eval(d)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            if round(c, 12) != 0 and round(d, 12) > 0:
                if round(d, 12) != 1:
                    cterm2 = f"{round(c, 12)} + {round(d, 12)}i"
                else:
                    cterm2 = f"{round(c, 12)} + i"
            elif round(c, 12) != 0 and round(d, 12) < 0:
                if round(d, 12) != -1:
                    cterm2 = f"{round(c, 12)} - {round(d * -1, 12)}i"
                else:
                    cterm2 = f"{round(c, 12)} - i"
            elif round(c, 12) == 0 and round(d, 12) != 0:
                if round(d, 12) != 1 and round(d, 12) != -1:
                    cterm2 = f"{round(d, 12)}i"
                elif round(d, 12) == 1:
                    cterm2 = "i"
                else:
                    cterm2 = "-i"
            elif round(d, 12) == 0:
                cterm2 = f"{round(c, 12)}"
            print("Second term: " + cterm2)
        try:
            if op.lower() == "=" or op.lower() == "equals" or op.lower() == "equ":
                res = complex(a, b)
                print()
                print(f"Result: {cterm1}")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "+" or op.lower() == "add":
                res = complex(a, b) + complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "-" or op.lower() == "subtract" or op.lower() == "sub":
                res = complex(a, b) - complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "*" or op.lower() == "multiply" or op.lower() == "mul":
                res = complex(a, b) * complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "/" or op.lower() == "divide" or op.lower() == "div":
                res = complex(a, b) / complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "^" or op.lower() == "exponent" or op.lower() == "exp" or op.lower() == "**":
                res = complex(a, b) ** complex(c, d)
                print()
                if round(res.imag, 12) > 0 and round(res.real, 12) != 0:
                    if round(res.imag, 12) != 1:
                        print(f"Result: {round(res.real, 12)} + {round(res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} + i")
                elif round(res.real, 12) == 0 and round(res.imag, 12) != 0:
                    if round(res.imag, 12) != 1 and round(res.imag, 12) != -1:
                        print(f"Result: {round(res.imag, 12)}i")
                    elif round(res.imag, 12) == 1:
                        print(f"Result: i")
                    else:
                        print(f"Result: -i")
                elif round(res.imag, 12) == 0:
                    print(f"Result: {round(res.real, 12)}")
                else:
                    if round(res.imag, 12) != -1:
                        print(f"Result: {round(res.real, 12)} - {round(-1 * res.imag, 12)}i")
                    else:
                        print(f"Result: {round(res.real, 12)} - i")
                rl = res.real
                print(f"rl (real part) = {round(rl, 12)}")
                im = res.imag
                print(f"im (imaginary part) = {round(im, 12)}")
            elif op.lower() == "abs" or op.lower() == "absolute value" or op.lower() == "magnitude" or op.lower() == "mag" or op.lower() == "||" or op.lower() == "modulus" or op.lower() == "mod":
                mod = abs(complex(a, b))
                print()
                print(f"mod (modulus/absolute value) = {round(mod, 12)}")
            elif op.lower() == "<" or op.lower() == "angle" or op.lower() == "ang" or op.lower() == "phase" or op.lower() == "pha" or op.lower() == "argument" or op.lower() == "arg":
                res = cmath.phase(a, b)
                while True:
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(res, 12) < 0:
                                res += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(res, 12) > 0:
                                res -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        res = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(res, 12) < 0:
                                res += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(res, 12) > 0:
                                res -= 360
                        break
                print()                  
                ang = res
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)") 
            elif op.lower() == "|<" or op.lower() == "polar" or op.lower() == "pol" or op.lower() == "polar form":
                res = cmath.polar(complex(a, b))
                ares = res[1]
                while True:
                    print()
                    unit = input("Output in (r)adians or (d)egrees? ")
                    if not(unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg"):
                        print('Please enter either "r" for radians or "d" for degrees')
                        continue
                    while True:
                        angle = input("Output (p)ositive or (n)egative angle? ")
                        if not(angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "+" or angle.lower() == "pos" or angle.lower() == "-" or angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg"):
                            print('Please enter either "p" for positive or "n" for negative')
                            print()
                        else:
                            break
                    if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 2 * pi
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 2 * pi
                        break
                    elif unit.lower() == "d" or unit.lower() == "degrees" or unit.lower() == "deg":
                        ares = degrees(ares)
                        if angle.lower() == "positive" or angle.lower() == "p" or angle.lower() == "pos" or angle.lower() == "+":
                            if round(ares, 12) < 0:
                                ares += 360
                        elif angle.lower() == "negative" or angle.lower() == "n" or angle.lower() == "neg" or angle.lower() == "-":
                            if round(ares, 12) > 0:
                                ares -= 360
                        break
                print()
                print(f"Result: {round(res[0], 12)} cos({round(ares, 12)}) + {round(res[0], 12)} sin({round(ares, 12)})i")
                mod = res[0]
                print(f"mod (modulus/absolute value) = {round(abs, 12)}")
                ang = ares
                if unit.lower() == "r" or unit.lower() == "radians" or unit.lower() == "rad":
                    print(f"ang (angle/argument) = {round(ang, 12)} (radians)")
                else:
                    print(f"ang (angle/argument) = {round(ang, 12)} (degrees)")                    
            else:
                print('Please enter a valid operation ("i" for info and return to exit)')
        except:
            print()
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms')
            print("Division by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print()

def real_operation():
    global ans
    print()
    print("Welcome to real operations!")
    while True:
        clear_variables()
        print()
        n = input('First term (i): ')
        if n == "exit" or n == "" or n == "exi":
            break
        elif n == "i" or n == "inf" or n == "info":
            print()
            print('Real numbers and expressions, such as "3 * sin(pi / 3)", can be entered as terms')
            print("The following non-parenthesized operators and functions can be entered as part of an expression:")
            print("Arithmetic operators: + (add), - (subtract), * (multiply), / (divide), // (integer divide), % (remainder), ^ (exponent)")
            print("Comparison operators: == (equal to), != (not equal to), < (less than), <=, (less than or equal to), > (greater than), >= (greater than or equal to)")
            print("Logic operators: and (true if both are true), or (true if either is true), not() (inverts truth value)")
            print("Functions: eg. abs(x), sqrt(x), cbrt(x), pow(x, y), log(x, base), factorial(x), comb(x, y), perm(x, y), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), degrees(x), radians(x), sum([x, y, z,...]), int(x), round(x), etc")
            print('Real constants such as "pi", "e", and "tau" can be entered')
            print('Real variables can also be entered, for example: "ans" (previous real answer), "rl" (real part of previous complex result), "im" (imaginary part of previous complex result), "rt" (1st real solution of previous quadratic), "rt2" (2nd real solution of previous quadratic), "im2" (imaginary part of 2nd previous quadratic complex solution) "sum" (previous series summation), "rat" (previous geometric series common ratio), "dif" (previous arithmetic series common difference), "term1" (1st term of previous series), "cf1" (1st coefficient of previous binomial expansion), and stored variables')
            print("The above operators and functions can only be entered as part of an expression, not as an operation")
            print('Enter "c" for complex operations (this will direct to rectangular form), "m" for matrix operations, "s" for summations (this will direct to binomial expansion), "f" for functions (this will direct to polynomials), and "g" for games (this will direct to play Math 24)')
            continue
        elif n == "c" or n == "com" or n == "complex" or n == "complex operations":
            from_rectangular()
            break
        elif n == "s" or n == "sum" or n == "summations":
            binomial_expansion()
            break
        elif n == "f" or n == "fun" or n == "functions":
            polynomial()
            break
        elif n == "m" or n == "mat" or n == "matrix" or n == "matrix operations":
            matrix_operation()
            break
        elif n == "g" or n == "gam" or n == "games":
            math24play()
            break
        else:
            try:
                n = n.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                if (eval(n) == True or eval(n) == False) and (n.find("==") != -1 or n.find("<") != -1 or n.find(">") != -1 or n.find("<=") != -1 or n.find(">=") != -1 or n.find("!=") != -1):
                    print()
                    print(eval(n))
                    continue
                n = 0 + eval(n)
                try:
                    roundtry = round(n, 12)
                except:
                    print()
                    print(eval(n))
                    continue
            except:
                print('Please enter a real number or expression, "i" for info, or return to exit')
                continue
            while True:
                op = input('Operation (i): ')
                if op.lower() == "info" or op.lower() == "i" or op.lower() == "inf":
                    print()
                    print("The following operations can be entered:")
                    print('Basic: add (+), subtract (-), multiply (*), divide (/), integer divide or floor divide (//), remainder or modulo (r or %), absolute value or magnitude (||)')
                    print('Power: exponent (^), logarithm (log), square rt (sqrt), cube rt (cbrt)')
                    print('Trigonometry: sine (sin), cosine (cos), tangent (tan), arcsine (asin), arccosine (acos), arctangent (atan), degrees (deg), radians (rad)')
                    print("Combinatorics: factorial (!), choose (cho), permute (per)")
                    print("Comparison: == (equal to), != (not equal to), < (less than), <= (less than or equal to), > (greater than), >= (greater than or equal to)")
                    print("Other: equals (=), store (sto), round (~), integer (int)")
                    print()
                else:
                    break
            if op.lower() == "exit" or op.lower() == "":
                continue
            elif not(op.lower() == "store" or op.lower() == "sto" or op.lower() == "equals" or op.lower() == "=" or op.lower() == "equ" or op.lower() == "factorial" or op.lower() == "fac" or op.lower() == "!" or op.lower() == "sqrt" or op.lower() == "square rt" or op.lower() == "squ" or op.lower() == "cbrt" or op.lower() == "cube rt" or op.lower() == "cub" or op.lower() == "absolute value" or op.lower() == "||" or op.lower() == "abs" or op.lower() == "magnitude" or op.lower() == "mag" or op.lower() == "asin" or op.lower() == "arcsine" or op.lower() == "inverse sine" or op.lower() == "inv sin" or op.lower() == "acos" or op.lower() == "arccosine" or op.lower() == "inverse cosine" or op.lower() == "inv cos" or op.lower() == "atan" or op.lower() == "arctangent" or op.lower() == "inverse tangent" or op.lower() == "inv tan" or op.lower() == "asi" or op.lower() == "aco" or op.lower() == "ata" or op.lower() == "sin" or op.lower() == "sine" or op.lower() == "cos" or op.lower() == "cosine" or op.lower() == "tangent" or op.lower() == "tan" or op.lower() == "int" or op.lower() == "integer" or op.lower() == "radians" or op.lower() == "rad" or op.lower() == "degrees" or op.lower() == "deg"):
                if op.lower() == "exponent" or op.lower() == "^" or op.lower() == "exp" or op.lower() == "**":
                    n2 = input('Exponent: ')
                    if n2 == "" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                        n2 = 0 + eval(n2)
                    except:
                        print('Please enter a real number or expression, or return to exit')
                        continue
                elif op.lower() == "round" or op.lower() == "~" or op.lower() == "rou":
                    n2 = input('Decimals to round (0-12): ')
                    if n2 == "" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                        n2 = 0 + eval(n2)
                        n2 = 0 + integer(n2)
                    except:
                        print('Please enter an integer from 0 to 12 or return to exit')
                        continue
                elif op.lower() == "log" or op.lower() == "logarithm":
                    if n > 0:
                        n2 = input('Base: ')
                        if n2 == "" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                            n2 = 0 + eval(n2)
                        except:
                            print('Please enter a real number or expression greater than 0 and not equal to 1, or return to exit')
                            continue                                
                elif op.lower() == "choose" or op.lower() == "cho" or op.lower() == "comb":
                    if round(n, 12) == round(n) and n >= 0:
                        n2 = input(f'From {round(n)} choose: ')
                        if n2 == "" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                            n2 = 0 + eval(n2)
                        except:
                            print('Please enter a nonnegative integer or return to exit')
                            continue                                    
                elif op.lower() == "perm" or op.lower() == "permute" or op.lower() == "per":
                    if round(n, 12) == round(n) and n >= 0:
                        n2 = input(f'From {round(n)} permute: ')
                        if n2 == "" or n2 == "exit" or n2 == "exi":
                            continue
                        try:
                            n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                            n2 = 0 + eval(n2)
                        except:
                            print('Please enter a nonnegative integer or return to exit')
                            continue  
                else:
                    if op.lower() == "equal to" or op.lower() == "is":
                        op = "=="
                    elif op.lower() == "less than" or op.lower() == "less":
                        op = "<"
                    elif op.lower() == "greater than" or op.lower() == "greater":
                        op = ">"
                    elif op.lower() == "less than or equal to":
                        op = "<="
                    elif op.lower() == "greater than or equal to":
                        op = ">="
                    elif op.lower() == "not equal to" or op.lower() == "not":
                        op = "!="
                    n2 = input('Next term: ')
                    if n2 == "" or n2 == "exit" or n2 == "exi":
                        continue
                    try:
                        n2 = n2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                        n2 = 0 + eval(n2)
                    except:
                        print('Please enter a real number or expression, or return to exit')
                        continue
        try:
            if op.lower() == "equals" or op.lower() == "=" or op.lower() == "equ":
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "add" or op.lower() == "+":
                n += n2
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "subtract" or op.lower() == "-" or op.lower() == "sub":
                n -= n2
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "multiply" or op.lower() == "*" or op.lower() == "mul" or op.lower() == "x":
                n *= n2
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "divide" or op.lower() == "/" or op.lower() == "div":
                n /= n2
                if n == 0:
                    n = 0.0
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "remainder" or op.lower() == "r" or op.lower() == "%" or op.lower() == "modulo" or op.lower() == "rem" or op.lower() == "mod":
                n %= n2
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "exponent" or op.lower() == "^" or op.lower() == "exp" or op.lower() == "**":
                n **= n2
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "<" or op.lower() == ">" or op.lower() == ">=" or op.lower() == "<=" or op.lower() == "==" or op.lower() == "!=":
                print()
                print(eval(f"{n}" + op  + f"{n2}"))
                continue
            elif op.lower() == "store" or op.lower() == "sto":
                while True:
                    vname = input("Variable name (i): ")
                    if vname == "" or vname == "exit" or vname == "exi":
                        break
                    try:
                        if vname[0].isalpha() == False or vname[0].islower():
                            print("Please enter a variable name beginning with a capital letter")
                            print()
                        else:
                            break
                    except:
                        print("Please enter a variable name beginning with a capital letter")
                        print()
                if vname == "" or vname == "exit" or vname == "exi":
                    continue
                globals()[vname] = n
                print()
                print(vname + f" = {round(n, 12)}")
                keeps.append(vname)
            elif op.lower() == "round" or op.lower() == "~" or op.lower() == "rou":
                if n2 > 12:
                    n2 = 12
                if n2 == 0:
                    n = round(n)
                else:
                    n = round(n, n2)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "factorial" or op.lower() == "!" or op.lower() == "fac":
                n = factorial(round(n))
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "sqrt" or op.lower() == "square rt" or op.lower() == "squ":
                n = sqrt(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "cbrt" or op.lower() == "cube rt" or op.lower() == "cub":
                n = cbrt(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "log" or op.lower() == "logarithm":
                n = log(n, n2)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "integer divide" or op.lower() == "int div" or op.lower() == "floor divide" or op.lower() == "flo div" or op.lower() == "//":
                n //= n2
                print()
                if n == 0:
                    n = 0.0
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "integer" or op.lower() == "int":
                n = 0 + integer(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "choose" or op.lower() == "cho" or op.lower() == "comb":
                n = comb(round(n), round(n2))
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "perm" or op.lower() == "permute" or op.lower() == "per":
                n = perm(round(n), round(n2))
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "absolute value" or op.lower() == "||" or op.lower() == "abs" or op.lower() == "magnitude" or op.lower() == "mag":
                n = abs(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "radians" or op.lower() == "rad":
                n = radians(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "degrees" or op.lower() == "deg":
                n = degrees(n)
                print()
                print(f"ans (answer) = {round(n, 12)}")             
            elif op.lower() == "sin" or op.lower() == "sine" or op.lower() == "cos" or op.lower() == "cosine" or op.lower() == "tangent" or op.lower() == "tan":
                angle = input("Inputted in (r)adians or (d)egrees? ")
                if angle.lower() == "radians" or angle.lower() == "rad" or angle.lower() == "r":
                    n = n
                    go = True
                elif angle.lower() == "degrees" or angle.lower() == "deg" or angle.lower() == "d":
                    n = radians(n)
                    go = True
                else:
                    print('Please enter either "r" for radians or "d" for degrees')
                    go = False
                if go == True:
                    if op.lower() == "sin" or op.lower() == "sine":
                        n = sin(n)
                        print()
                        print(f"ans (answer) = {round(n, 12)}")
                    elif op.lower() == "cos" or op.lower() == "cosine":
                        n = cos(n)
                        print()
                        print(f"ans (answer) = {round(n, 12)}")
                    elif op.lower() == "tan" or op.lower() == "tangent":
                        n = tan()
                        print()
                        print(f"ans (answer) = {round(n, 12)}")
            elif op.lower() == "asin" or op.lower() == "arcsine" or op.lower() == "inverse sine" or op.lower() == "inv sin" or op.lower() == "acos" or op.lower() == "arccosine" or op.lower() == "inverse cosine" or op.lower() == "inv cos" or op.lower() == "atan" or op.lower() == "arctangent" or op.lower() == "inverse tangent" or op.lower() == "inv tan" or op.lower() == "asi" or op.lower() == "aco" or op.lower() == "ata":
                unit = input("Output in (r)adians or (d)egrees? ")
                quad = input("Output in default quadrant (yes/no)? ")
                go = True
                if op.lower() == "asin" or op.lower() == "asi" or op.lower() == "arcsine" or op.lower() == "inverse sine" or op.lower() == "inv sin":
                    if quad == "yes" or quad == "y":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = asin(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                            n = degrees(asin(n))                              
                    elif quad == "no" or quad == "n":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = pi - asin(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                            n = 180 - degrees(asin(n))                           
                elif op.lower() == "acos" or op.lower() == "arccosine" or op.lower() == "aco" or op.lower() == "inverse cosine" or op.lower() == "inv cos":
                    if quad == "yes" or quad == "y":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = acos(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                            n = degrees(acos(n))
                    elif quad == "no" or quad == "n":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = -acos(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                            n = -degrees(acos(n))
                elif op.lower() == "atan" or op.lower() == "arctangent" or op.lower() == "ata" or op.lower() == "inverse tangent" or op.lower() == "inv tan":
                    if quad == "yes" or quad == "y":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = atan(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                            n = degrees(atan(n))
                    elif quad == "no" or quad == "n":
                        if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                            n = pi - atan(n)
                        elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":                            
                            n = 180 - degrees(atan(n))
                angle = input("Output (p)ositive or (n)egative angle? ")
                if angle.lower() == "positive" or angle.lower() == "pos" or angle.lower() == "+" or angle.lower() == "p":
                    if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                        if round(n, 12) < 0:
                            n += 2 * pi
                    elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                        if round(n, 12) < 0:
                            n += 360
                    else:
                        go = False
                elif angle.lower() == "negative" or angle.lower() == "neg" or angle.lower() == "-" or angle.lower() == "n":
                    if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                        if round(n, 12) > 0:
                            n -= 2 * pi
                    elif unit.lower() == "degrees" or unit.lower() == "deg" or unit.lower() == "d":
                        if round(n, 12) > 0:
                            n -= 360
                    else:
                        go = False
                if unit != "radians" and unit != "rad" and unit != "r" and unit != "d" and unit != "degrees" and unit != "deg":
                    print()
                    print('Please enter either "r" for radians or "d" for degrees')
                    go = False
                if quad != "yes" and quad != "y" and quad != "no" and quad != "n":
                    print('Please enter either "yes" (y) or "no" (n)')
                    go = False       
                if angle != "p" and angle != "n" and angle != "positive" and angle != "negative" and angle != "pos" and angle != "+" and angle != "-" and angle != "neg":
                    print('Please enter either "p" for positive or "n" for negative')
                    print()
                    go = False
                if go == True:
                    print()
                    if unit.lower() == "radians" or unit.lower() == "rad" or unit.lower() == "r":
                        print(f"ans (answer) = {round(n, 12)} radians")
                    else:
                        print(f"ans (answer) = {round(n, 12)} degrees")
            else:
                print('Please enter a valid operation ("i" for info and return to exit)')
                print()
                continue
            ans = n
        except:
            print()
            print("OPERATION ERROR") 
            print("This error occurs when the inputs do not meet their restrictions, for example: ")
            print('Only real numbers, constants, and expressions can be entered as terms')
            print("Division, integer division, and remainder/modulo by 0 is undefined")
            print("Raising 0 to a negative power is undefined")
            print("Taking an even rt of a negative number is undefined over real numbers")
            print("The factorial, choose, and permute functions only accepts nonnegative integers")
            print("The logarithm function only accepts positive arguments and positive bases not equal to 1")
            print()

def binomial_expansion():
    global binsum
    print()
    print("Welcome to binomial expansion!")
    print("Please enter the binomial in the form (ax^b + cy^d) ^ n, where x and y are non-numeric variable names without spaces, a, b, and c are not equal to 0, and n is an integer")
    while True:
        clear_variables()
        binsum = ""
        print()
        a = input("a (i): ")
        if a == "" or a == "exit" or a == "exi":
            break
        elif a == "r" or a == "real" or a == "rea" or a == "real operations":
            real_operation()
            break
        elif a == "c" or a == "com" or a == "comp" or a == "complex operations":
            from_rectangular()
            break
        elif a  == "a" or a == "ari" or a == "arithmetic" or a == "arithmetic series":
            arithmetic()
            break
        elif a  == "g" or a == "geo" or a == "geometric" or a == "geometric series":
            geometric()
            break
        elif a == "m" or a == "mat" or a == "matrix" or a == "matrix operations":
            matrix_operation()
            break
        elif a == "f" or a == "fun" or a == "functions":
            polynomial()
            break
        elif a == "gam" or a == "ga" or a == "games":
            math24play()
            break
        elif a == "i" or a == "info" or a == "inf":
            print()
            print('Enter a nonzero real number or expression as the first coefficient')
            print('Enter "r" for real operations, "a" for arithmetic series, "g" for geometric series, "c" for complex operations (this will direct to rectangular form), "m" for matrix operations, "f" for functions (this will direct to polynomials), and "ga" for games (this will direct to play Math 24)')
            continue
        try:
            a = a.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            a = 0 + eval(a)
        except:
            print('Please enter a nonzero real number or expression, "i" for info, or return to exit')
            continue
        if a == 0:
            print('Please enter a nonzero real number or expression, "i" for info, or return to exit')
            continue
        while True:
            x = input("x (i): ")
            if x == "exit" or x == "exi" or x == "":
                break
            try:
                if x == "info" or x == "inf" or x == "i":
                    print()
                    print("Enter a non-numeric variable name without spaces")
                    print("The variable will not store any value, it is just the name that will be printed in the result")
                    print()
                elif x.find(" ") != -1 or x[0].isalpha() == False:
                    print('For clarity, please enter a non-numeric variable name without spaces, "i" for info, or return to exit')
                    print()
                else:
                    break
            except:
                print('Please enter a non-numeric variable name without spaces, "i" for info, or return to exit')
        if x == "exit" or x == "exi" or x == "":
            continue
        b = input("b: ")
        if b == "" or b == "exit" or b == "exi":
            continue
        try:
            b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            b = 0 + eval(b)
        except:
            print('Please enter a nonzero real number or expression, or return to exit')
            continue
        if b == 0:
            print('Please enter a nonzero real number or expression, or return to exit')
            continue
        if a == 1:
            aprint = ""
        elif a == -1:
            aprint = "-"
        else:
            aprint = f"{a}"
        if b == 1:
            bprint = ""
        else:
            bprint = f"^{b}"
        term1 = aprint + x + bprint
        print("Term 1: " + term1)
        print()
        c = input("c: ")
        if c == "" or c == "exit" or c == "exi":
            continue
        try:
            c = c.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            c = 0 + eval(c)
        except:
            print('Please enter a nonzero real number or expression, or return to exit')
            continue
        if c == 0:
            print('Please enter a nonzero real number or expression, or return to exit')
            continue
        while True:
            y = input("y (i, /): ")
            if y == "exit" or y == "exi" or y == "":
                break
            try:
                if y == "info" or y == "inf" or y == "i":
                    print()
                    print("Enter a non-numeric variable name without spaces")
                    print("The variable will not store any value, it is just the name that will be printed in the result")
                    print("Skipping will set the variable's exponent to 0")
                    print()
                elif y == "skip" or y == "/" or y == "ski":
                    break
                elif y.find(" ") != -1 or y[0].isalpha() == False:
                    print('For clarity, please enter a non-numeric variable name without spaces, "i" for info, or return to exit')
                    print()
                else:
                    break
            except:
                print('Please enter a non-numeric variable name without spaces, "i" for info, or return to exit')
                print()
        if y == "exit" or y == "exi" or y == "":
            continue
        if y != "skip" and y != "ski" and y != "/":
            d = input("d: ")
            if d == "" or d == "exit" or d == "exi":
                continue
            try:
                d = d.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                d = 0 + eval(d)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
        else:
            d = 0
        if c == 1:
            cprint = ""
        elif c == -1:
            cprint = "-"
        else:
            cprint = f"{c}"
        if d == 1 or d == 0:
            dprint = ""
        else:
            dprint = f"^{d}"
        if d == 0:
            yprint = ""
        else:
            yprint = f"{y}"
        term2 = cprint + yprint + dprint
        print("Term 2: " + term2)
        print()
        n = input("n: ")
        if n == "" or n == "exit" or n == "exi":
            continue
        try:
            n = n.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            n = 0 + eval(n)
            n = 0 + integer(n)
            if n < 0:
                binsum += "1 / ("
        except:
            print('Please enter an integer or return to exit')
            continue
        if term2[0] != "-":
            print("(" + term1 + " + " + term2 + ")" + " ^ " + f"{n}")
        else:
            term2 = term2[1:]
            print("(" + term1 + " - " + term2 + ")" + " ^ " + f"{n}")
        while True:
            print()
            un = input(f"Indexes of terms to find (1-{abs(n)+1}, i): ")
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Enter a list of indexes seperated by commas (,) and using colons (:) to indicate ranges")
                print('Eg. "1, 6:8, 10" will output the 1st, 6th, 7th, 8th, and 10th terms (if n >= 9)')
                if n >= 0:
                    print("If n is negative (it's not!), only the denominator of each term will be outputted (the sum will still be complete)")
                else:
                    print("If n is negative (it is!), only the denominator of each term will be outputted (the sum will still be complete)")
                print(f"All indexes must be positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive, and the second index of a range must be greater than the first index of the range")
                print(f'Enter "all" (1-{abs(n)+1}) to find/sum all terms')
                print()
            else:
                break
        if un == "" or un == "exit" or un  == "exi":
            continue
        if un == "all" or un == "a":
            un = f"1-{abs(n)+1}"
        un = un.replace(" ", "")
        un = un.split(",")
        print()
        for unterm in un:
            rangelist = unterm.split(":")
            if len(rangelist) == 1:
                try:
                    unterm = unterm.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                    unterm = 0 + eval(unterm)
                    unterm = 0 + integer(unterm)
                except:
                    print(f'"{unterm}" is not a positive integer between 1 and |n| + 1 ({abs(n) + 1}), inclusive')
                    continue
                if 0 < unterm <= abs(n) + 1:
                    k = unterm - 1
                    print_binomial(a, b, c, d, n, k, unterm, x, y)
                else:
                    print(f'"{unterm}" is not a positive integer between 1 and |n| + 1 ({abs(n) + 1}), inclusive')
            elif len(rangelist) == 2:
                try:
                    rangelist[0] = rangelist[0].replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                    rangelist[1] = rangelist[1].replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                    rangelist[0] = 0 + eval(rangelist[0])
                    rangelist[1] = 0 + eval(rangelist[1])
                    rangelist[0] = 0 + integer(rangelist[0])
                    rangelist[1] = 0 + integer(rangelist[1])
                except:
                    print(f'"{unterm}" is not a positive integer between 1 and |n| + 1 ({abs(n) + 1}), inclusive')
                    continue
                if rangelist[0] > 0 and rangelist[1] > rangelist[0] and rangelist[1] <= abs(n) + 1:
                    rangelist = list(range(rangelist[0], rangelist[1] + 1))
                    for unterm in rangelist:
                        k = unterm - 1
                        print_binomial(a, b, c, d, n, k, unterm, x, y)
                elif rangelist[1] <= rangelist[0]:
                    print(f'the second index of the range "{unterm}" must be greater than the first index')
                else:    
                    print(f'"{unterm}" is not a positive integer between 1 and |n| + 1 ({abs(n) + 1}), inclusive')
            else:
                print(f'"{unterm}" is not a range in the form x:y, where x and y are both positive integers between 1 and |n| + 1 ({abs(n) + 1}), inclusive, and y is greater than x')
        binsum = binsum[:len(binsum) - 3]
        if n < 0:
            binsum += ")"
        if binsum != "":
            print("Sum: " + binsum)

def arithmetic():
    global dif
    print()
    print("Welcome to arithmetic series!")
    while True:
        clear_variables()
        print()
        b = input("Term (i): ")
        if b == "" or b == "exit" or b == "exi":
            break
        elif b == "r" or b == "real" or b == "rea" or b == "real operations":
            real_operation()
            break
        elif b == "c" or b == "complex" or b == "com" or b == "complex operations":
            from_rectangular()
            break
        elif b == "g" or b == "geo" or b == "geometric" or b == "geometric series":
            geometric()
            break
        elif b == "b" or b == "bin" or b == "binomial" or b == "binomial expansion":
            binomial_expansion()
            break
        elif b == "m" or b == "mat" or b == "matrix" or b == "matrix operations":
            matrix_operation()
            break
        elif b == "f" or b == "fun" or b == "functions":
            polynomial()
            break
        elif b == "gam" or b == "ga" or b == "games":
            math24play()
            break
        elif b == "i" or b == "info" or b == "inf":
            print()
            print("Please enter a real number or expression as the value of one of the series terms")
            print('Enter "s" to enter a sum instead of terms')
            print('Enter "r" for real operations, "b" for binomial expansion, "g" for geometric series, "c" for complex operations (this will direct to rectangular form), "m" for matrix operations, "f" for functions (this will direct to polynomials), and "ga" for games (this will direct to play Math 24)')
            continue
        elif b == "s" or b == "sum":
            input_sum = input("Sum: ")
            if input_sum == "" or input_sum == "exi" or input_sum == "exit" or input_sum == "t" or input_sum == "ter" or input_sum == "terms":
                continue
            try:
                input_sum = input_sum.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                input_sum = 0 + eval(input_sum)
            except:
                print("Please enter a real number or expression, or return to exit")
                continue
            sum_number = input("Number of summed terms: ")
            if sum_number == "" or sum_number == "exi" or sum_number == "exit":
                continue
            try:
                sum_number = sum_number.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                sum_number = 0 + eval(sum_number)
                sum_number = 0 + integer(sum_number)
                if sum_number <= 0:
                    print("Please enter a positive integer or return to exit")
                    continue
            except:
                print("Please enter a positive integer or return to exit")
                continue
        else:
            try:
                b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                b = 0 + eval(b)
            except:
                print('Please enter a real number or expression, "i" for info, or return to exit')
                continue
            bn = input("Term index: ")
            if bn == "" or bn == "exit" or bn == "exi":
                continue     
            try:
                bn = bn.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                bn = 0 + eval(bn)
                bn = 0 + integer(bn)
            except:
                print('Please enter a positive integer or return to exit')
                continue
            if bn < 1:
                print('Please enter a positive integer or return to exit')
                continue
        if b != "s" and b != "sum":
            comdif = input("Common difference (t to enter term): ")
        else:
            comdif = input("Common difference: ")
        if comdif == "" or comdif == "exit" or comdif == "exi":
            continue
        elif (comdif == "t" or comdif == "ter" or comdif == "term") and b != "s" and b != "sum":
            c = input("Next term: ")
            if c == "" or c == "exit" or c == "exi":
                continue
            try:
                c = c.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                c = 0 + eval(c)  
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            cn = input("Term index: ")
            if cn == "" or cn == "exit" or cn == "exi":
                continue     
            try:
                cn = cn.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                cn = 0 + eval(cn)
                cn = 0 + integer(cn)
            except:
                print('Please enter a positive integer or return to exit')
                continue
            if bn < cn:
                comdif = (c - b) / (cn - bn)
            else:
                print("The index of term 2 must be greater than the index of term 1")
                continue
            a = b - comdif * (bn - 1)
        else:
            try:
                comdif = comdif.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                comdif = 0 + eval(comdif)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            if b != "s" and b != "sum":
                a = b - comdif * (bn - 1)
                cn = bn + 1
                c = b + comdif
            else:
                a = (2 * input_sum / sum_number - comdif * (sum_number - 1)) / 2
                b = a
                bn = 1
                c = b + comdif
                cn = bn + 1
        print()
        while True:
            n = input("Numbers of terms to sum (i, /): ")
            if n == "i" or n == "inf" or n == "info":
                print()
                print("Enter a list of positive integers separated by commas (,) and using colons (:) to indicate ranges")
                print('Eg. "1, 6:8, 10" will output the sum of the first 1, 6, 7, 8, and 10 terms')
                print('Enter "l" to enter last terms instead of numbers of terms (common difference cannot be 0)')
                print()
            else:
                break
        if n != "/" and n != "skip" and n != "ski":
            if n == "" or n == "exit" or n == "exi":
                continue
            elif n == "l" or n == "las" or n == "las ter" or n == "last terms" or n == "last":
                if round(comdif, 12) == 0:
                    print("If the common difference is 0, enter a number of terms to sum instead")
                    continue
                while True:
                    l = input("Last terms (i): ")
                    if l == "i" or l == "inf" or l == "info":
                        print()
                        print("Enter a list of terms separated by commas (,)")
                        print('Eg. "1, 3, 5" will output the sum through the terms 1, 3, 5 (if they exist)')
                        print('Enter "n" to enter numbers of terms instead of last terms')
                        print()
                    else:
                        break
                if l == "" or l == "exit" or l == "exi" or l == "n" or l == "num" or l == "number" or l == "number of terms":
                    continue
                l = l.replace(" ", "")
                l = l.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                l = l.split(",")
            else:
                n = n.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
        while True:
            un = input('Indexes of terms to find (i, /): ')
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Enter a list of indexes seperated by commas (,) and using colons (:) to indicate ranges")
                print('Enter "d" to find the common difference')
                print('Eg. "1, d, 6:8" will output the 1st, 6th, 7th, and 8th terms, and the common difference')
                print("All indexes must be positive integers, and the second index of a range must be greater than the first index of the range")
                print()
            else:
                break
        if un == "" or un == "exit" or un == "exi":
            continue
        if round(comdif, 12) != 0:
            while True:
                iun = input('Terms of indexes to find (i, /): ')
                if iun == "i" or iun == "info" or iun == "inf":
                    print()
                    print("Enter a list of terms seperated by commas (,)")
                    print('Enter "d" to find the common difference')
                    print('Eg. "1, d, 6" will output the indexes of the terms 1 and 6 (if they exist), and the common difference')
                    print()
                else:
                    break
            if iun == "" or iun == "exit" or iun == "exi":
                continue
        if (n != "/" and n != "skip" and n != "ski") or (un != "/" and un != "skip" and un != "ski") or (round(comdif, 12) != 0 and iun != "/" and iun != "skip" and iun != "ski"):
            print()
        if n == "l" or n == "las" or n == "las ter" or n == "last terms" or n == "last":
            for term in l:
                try:
                    term = 0 + eval(term)
                except:
                    print(f'Error: "{term}" is not a real number or expression')
                    continue
                ncalc = (term - a) / comdif + 1
                if round(ncalc) != round(ncalc, 12) or round(ncalc, 12) <= 0:
                    print(f'Error: "{term}" is not a term of the series')
                    continue
                ncalc = round(ncalc)
                sum = f"sum{ncalc}"
                sumcalc = (2 * a + (comdif * (ncalc - 1))) * ncalc / 2
                if round(sumcalc, 12) == 0:
                    sumcalc = 0.0
                globals()[sum] = sumcalc
                keeps.append(sum)
                print(sum + f" (sum through {round(term, 12)} (term {ncalc})) = {round(sumcalc, 12)}")
        elif n != "/" and n != "skip" and n != "ski":
            n = n.replace(" ", "")
            if n[0] == ",":
                n = n[1:]
            if n[len(n) - 1] == ",":
                n = n[:len(n) - 1]
            n = n.split(",")
            for number in n:
                srangelist = number.split(":")
                if len(srangelist) == 1:
                    try:
                        number = 0 + eval(number)
                        number = 0 + integer(number)
                    except:
                        print(f'"{number}" is not a positive integer')
                        continue
                    if number <= 0:
                        print(f'"{number}" is not a positive integer')
                        continue
                    sum = f"sum{number}"
                    sumcalc = (2 * a + comdif * (number - 1)) * number / 2
                    if round(sumcalc, 12) == 0:
                        sumcalc = 0.0
                    globals()[sum] = sumcalc
                    keeps.append(sum)
                    print(sum + f" (sum through term {number}) = {round(sumcalc, 12)}")
                elif len(srangelist) == 2:
                    try:
                        srangelist[0] = 0 + eval(srangelist[0])
                        srangelist[1] = 0 + eval(srangelist[1])
                        srangelist[0] = 0 + integer(srangelist[0])
                        srangelist[1] = 0 + integer(srangelist[1])
                    except:
                        print(f'"{number}" is not a positive integer')
                        continue
                    if srangelist[0] > 0 and srangelist[1] > srangelist[0]:
                        srangelist = list(range(srangelist[0], srangelist[1] + 1))
                        for item in srangelist:
                            sum = f"sum{item}"
                            sumcalc = (2 * a + comdif * (item - 1)) * item / 2
                            if round(sumcalc, 12) == 0:
                                sumcalc = 0.0
                            globals()[sum] = sumcalc
                            keeps.append(sum)
                            print(sum + f" (sum of through term {item}) = {round(sumcalc, 12)}")
                    elif srangelist[1] <= srangelist[0]:
                        print(f'"{number}" is not a range in the form x:y, where y > x')
                    else:    
                        print(f'"{number}" is not a positive integer')
                else:
                    print(f'"{number}" is not a range in the form x:y, where y > x')
        if un != "/" and un != "skip" and un != "ski":
            un = un.replace(" ", "")
            un = un.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            un = un.split(",")
            for unterm in un:
                rangelist = unterm.split(":")
                if len(rangelist) == 1:
                    try:
                        if unterm == "d" or unterm == "difference" or unterm == "com dif" or unterm == "common difference":
                            dif = comdif
                            print(f"dif (common difference) = {round(dif, 12)}")
                            continue
                        unterm = 0 + eval(unterm)
                        unterm = 0 + integer(unterm)
                    except:
                        print(f'"{unterm}" is not a positive integer')
                        continue
                    if unterm > 0:
                        sumterm = f"tm{unterm}"
                        globals()[sumterm] = a + comdif * (unterm - 1)
                        keeps.append(sumterm)
                        print(sumterm + f" (term {unterm}) = {round(a + comdif * (unterm - 1), 12)}")
                    else:
                        print(f'"{unterm}" is not a positive integer')
                elif len(rangelist) == 2:
                    try:
                        rangelist[0] = 0 + eval(rangelist[0])
                        rangelist[1] = 0 + eval(rangelist[1])
                        rangelist[0] = 0 + integer(rangelist[0])
                        rangelist[1] = 0 + integer(rangelist[1])
                    except:
                        print(f'"{unterm}" is not a positive integer')
                        continue
                    if rangelist[0] > 0 and rangelist[1] > rangelist[0]:
                        rangelist = list(range(rangelist[0], rangelist[1] + 1))
                        for unterm in rangelist:
                            sumterm = f"tm{unterm}"
                            globals()[sumterm] = a + comdif * (unterm - 1)
                            keeps.append(sumterm)
                            print(sumterm + f" (term {unterm}) = {round(a + comdif * (unterm - 1), 12)}")
                    elif rangelist[1] <= rangelist[0]:
                        print(f'"{unterm}" is not a range in the form x:y, where y > x')
                    else:    
                        print(f'"{unterm}" is not a positive integer')
                else:
                    print(f'"{unterm}" is not a range in the form x:y, where y > x')
        if round(comdif, 12) != 0 and iun != "/" and iun != "skip" and iun != "ski":
            iun = iun.replace(" ", "")
            iun = iun.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            iun = iun.split(",")
            for iunterm in iun:
                try:
                    if iunterm == "d" or iunterm == "difference" or iunterm == "comdif" or iunterm == "common difference":
                        dif = comdif
                        print(f"dif (common difference) = {round(dif, 12)}")
                        continue
                    iunterm = 0 + eval(iunterm)
                except:
                    print(f'"{iunterm}" is not a real number or expression')
                    continue
                indexcalc = (iunterm - a) / comdif + 1
                if round(indexcalc, 12) == round(indexcalc) and indexcalc > 0: 
                    series_find_constants(iunterm, indexcalc)
                else:
                    print(f'"{iunterm}" is not a term in the series')

def geometric():
    global rat
    print()
    print("Welcome to geometric series!")
    while True:
        clear_variables()
        print()
        b = input("Term (i): ")
        if b == "" or b == "exit" or b == "exi":
            break
        elif b == "r" or b == "real" or b == "rea" or b == "real operations":
            real_operation()
            break
        elif b == "c" or b == "complex" or b == "com" or b == "complex operations":
            from_rectangular()
            break
        elif b == "a" or b == "ari" or b == "arithmetic" or b == "arithmetic series":
            arithmetic()
            break
        elif b == "b" or b == "bin" or b == "binomial" or b == "binomial expansion":
            binomial_expansion()
            break
        elif b == "f" or b == "fun" or b == "functions":
            polynomial()
            break
        elif b == "m" or b == "mat" or b == "matrix" or b == "matrix operations":
            matrix_operation()
            break
        elif b == "g" or b == "gam" or b == "games":
            math24play()
            break
        elif b == "i" or b == "info" or b == "inf":
            print()
            print("Please enter a nonzero real number or expression as the value of one of the series terms")
            print('Enter "s" to enter a sum instead of terms')
            print('Enter "r" for real operations, "b" for binomial expansion, "a" for arithmetic series, "c" for complex operations (this will direct to rectangular form), "m" for matrix operations, "f" for functions (this will direct to polynomials), and "g" for games (this will direct to play Math 24)')
            continue
        elif b == "s" or b == "sum":
            input_sum = input("Sum: ")
            if input_sum == "" or input_sum == "exi" or input_sum == "exit" or input_sum == "t" or input_sum == "ter" or input_sum == "terms":
                continue
            try:
                input_sum = input_sum.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                input_sum = 0 + eval(input_sum)
                if round(input_sum, 12) == 0:
                    print("Please enter a nonzero real number or expression, or return to exit")
                    continue
            except:
                print("Please enter a nonzero real number or expression, or return to exit")
                continue
            sum_number = input("Number of summed terms (i for infinity): ")
            if sum_number == "" or sum_number == "exi" or sum_number == "exit":
                continue
            elif sum_number != "i" and sum_number != "inf" and sum_number != "infinity":
                try:
                    sum_number = sum_number.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                    sum_number = 0 + eval(sum_number)
                    sum_number = 0 + integer(sum_number)
                    if sum_number <= 0:
                        print("Please enter a positive integer or return to exit")
                        continue
                except:
                    print("Please enter an integer or return to exit")
                    continue
        else:
            try:
                b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                b = 0 + eval(b)
                if round(b, 12) == 0:
                    print('Please enter a nonzero real number or expression, "i" for info, or return to exit')
                    continue
            except:
                print('Please enter a nonzero real number or expression, "i" for info, or return to exit')
                continue
            bn = input("Term index: ")
            if bn == "" or bn == "exit" or bn == "exi":
                continue
            try:
                bn = bn.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                bn = 0 + eval(bn)
                bn = 0 + integer(bn)
            except:
                print('Please enter a positive integer or return to exit')
                continue
            if bn < 1:
                print('Please enter a positive integer or return to exit')
                continue
        if b == "s" or b == "sum":
            comrat = input("Common ratio: ")
        else:
            comrat = input("Common ratio (t to enter term): ")
        if comrat == "" or comrat == "exit" or comrat == "exi":
            continue
        elif (comrat == "t" or comrat == "term" or comrat == "ter") and b != "s" and b != "sum":
            c = input("Next term: ")
            if c == "" or c == "exit" or c == "exi":
                continue
            try:
                c = c.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                c = 0 + eval(c)  
            except:
                print('Please enter a nonzero real number or expression, or return to exit')
                continue      
            if round(c, 12) == 0:
                print('Please enter a nonzero real number or expression, or return to exit')
                continue
            cn = input("Term index: ")
            if cn == "" or cn == "exit" or cn == "exi":
                continue
            try:
                cn = cn.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                cn = 0 + eval(cn)
                cn = 0 + integer(cn)
            except:
                print('Please enter a positive integer or return to exit')
                continue
            if bn < cn:
                comrat = (c / b) ** (1/(cn - bn))
                if (cn - bn) % 2 == 0:
                    ratsign = input("Use (p)ositive or (n)egative common ratio? ")
                    if ratsign == "negative" or ratsign == "neg" or ratsign == "n" or ratsign == "-":
                        comrat *= -1
                    elif ratsign != "positive" and ratsign != "pos" and ratsign != "p" and ratsign != "+":
                        print('Please enter either "p" for positive or "n" for negative')
                a = b / comrat ** (bn - 1)
            else:
                print("The index of term 2 must be greater than the index of term 1")
                continue
        else:
            try:
                comrat = comrat.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                comrat = 0 + eval(comrat)
            except:
                print('Please enter a nonzero real number or expression, or return to exit')
                continue
            if round(comrat, 12) == 0:
                print('Please enter a nonzero real number or expression, or return to exit')
                continue
            if (b == "s" or b == "sum") and (sum_number == "i" or sum_number == "inf" or sum_number == "infinity"):
                if (comrat >= 1 or comrat <= -1):
                    print("Infinity is only accepted for nonzero common ratios between -1 and 1")
                    continue
                else:
                    a = input_sum * (1 - comrat)
                    b = a
                    bn = 1
                    c = b * comrat
                    cn = bn + 1
            elif (b == "s" or b == "sum") and round(comrat ** sum_number, 12) != 1:
                a = input_sum * (1 - comrat) / (1 - comrat ** sum_number)
                b = a
                bn = 1
                c = b * comrat
                cn = bn + 1
            elif (b == "s" or b == "sum") and round(comrat, 12) == 1:
                if round(input_sum, 12) > 0:
                    a = input_sum ** (1 / sum_number)
                else:
                    a = -1 * abs(input_sum) ** (1 / sum_number)
                b = a
                bn = 1
                c = b * comrat
                cn = bn + 1
            elif (b == "s" or b == "sum") and round(comrat, 12) == -1:
                print("The common ratio cannot be -1 if the number of summed terms is even, as this will always result in a sum of 0 regardless of the term values")
                continue
            else:
                c = b * comrat
                cn = bn + 1               
                a = b / comrat ** (bn - 1)
        print()
        while True:
            n = input("Numbers of terms to sum (i, /): ")
            if n == "i" or n == "info":
                print()
                print("Enter a list of positive integers separated by commas (,) and using colons (:) to indicate ranges")
                print('Enter "inf" for infinity (common ratio must be nonzero and between -1 and 1)')
                print('Eg. "1, inf, 6:8" will output the sum of the first 1, infinity, 6, 7, and 8 terms (if infinity is accepted)')
                print('Enter "l" to enter last terms instead of numbers of terms (common ratio cannot be 1 or -1)')
                print()
            else:
                break
        if n != "/" and n != "skip" and n != "ski":
            if n == "" or n == "exit" or n == "exi":
                continue
            elif n == "l" or n == "last terms" or n == "las" or n == "las ter" or n == "last":
                if abs(comrat) == 1:
                    print("If the common ratio is 1 or -1, enter a number of terms to sum instead")
                    continue
                while True:
                    l = input("Last terms (i): ")
                    if l == "i" or l == "inf" or l == "info":
                        print()
                        print("Enter a list of nonzero terms separated by commas (,)")
                        print('Enter "inf" for infinity (common ratio must be nonzero and between -1 and 1)')
                        print('Eg. "1, 3, inf" will output the sum through the terms 1, 3, and infinity (if they exist)')
                        print('Enter "n" to enter numbers of terms instead last terms')
                        print()
                    else:
                        break
                if l == "" or l == "exit" or l == "exi" or l == "n" or l == "num" or l == "number" or l == "number of terms":
                    continue
                l = l.replace(" ", "")
                l = l.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                l = l.split(",")
            else:
                n = n.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
        while True:
            un = input('Indexes of terms to find (i, /): ')
            if un == "i" or un == "info" or un == "inf":
                print()
                print("Enter a list of indexes seperated by commas (,) and using colons (:) to indicate ranges")
                print('Enter "r" to find the common ratio')
                print('Eg. "1, r, 6:8" will output the 1st, 6th, 7th, and 8th terms, and the common ratio')
                print("All indexes must be positive integers, and the second index of a range must be greater than the first index of the range")
                print()
            else:
                break
        if un == "" or un == "exit" or un == "exi":
            continue
        if round(abs(comrat), 12) != 1:
            while True:
                iun = input('Terms of indexes to find (i, /): ')
                if iun == "i" or iun == "info" or iun == "inf":
                    print()
                    print("Enter a list of terms seperated by commas (,)")
                    print('Enter "r" to find the common ratio')
                    print('Eg. "1, r, 6" will output the indexes of the terms 1 and 6 (if they exist), and the common ratio')
                    print()
                else:
                    break
            if iun == "" or iun == "exit" or iun == "exi":
                continue
        if (n != "/" and n != "skip" and n != "ski") or (un != "/" and un != "skip" and un != "ski") or (round(abs(comrat), 12) != 1 and iun != "/" and iun != "skip" and iun != "ski"):
            print()
        if n == "l" or n == "las" or n == "las ter" or n == "last terms" or n == "last":
            for term in l:
                if term != "infinity" and term != "inf":
                    try:
                        term = 0 + eval(term)
                    except:
                        print(f'Error: "{term}" is not a nonzero real number or expression')
                        continue
                    if term == 0:
                        print(f'Error: "{term}" is not a nonzero real nummber or expression')
                        continue
                    if round(term, 12) == round(a, 12) * -1:
                        print(f'Error: "{term}" causes the common ratio to be 1 or -1')
                        continue
                    if term == a:
                        ncalc = 1
                    else:
                        ncalc = log(abs(term / a), abs(comrat)) + 1
                    if round(ncalc) != round(ncalc, 12) or round(ncalc, 12) <= 0:
                        print(f'Error: "{term}" is not a term of the series')
                        continue
                    ncalc = round(ncalc)
                    sum = f"sum{ncalc}"
                    sumcalc = a * (1 - comrat ** ncalc) / (1 - comrat)
                    if round(sumcalc, 12) == 0:
                        sumcalc = 0.0
                    print(sum + f" (sum through {round(term, 12)} (term {ncalc})) = {round(sumcalc, 12)}")
                else:
                    sum = "suminf"
                    sumcalc = a / (1 - comrat)
                    print(sum + f" (sum through infinity) = {round(sumcalc, 12)}")
                globals()[sum] = sumcalc
                keeps.append(sum)
        elif n != "/" and n != "skip" and n != "ski":
            n = n.replace(" ", "")
            if n[0] == ",":
                n = n[1:]
            if n[len(n) - 1] == ",":
                n = n[:len(n) - 1]
            n = n.split(",")
            for number in n:
                srangelist = number.split(":")
                if len(srangelist) == 1:
                    if number != "infinity" and number != "inf":
                        try:
                            number = 0 + eval(number)
                            number = 0 + integer(number)
                        except:
                            print(f'"{number}" is not a positive integer')
                            continue
                        if number <= 0:
                            print(f'"{number}" is not a positive integer')
                            continue
                        sum = f"sum{number}"
                    else:
                        sum = "suminf"
                    if round(b, 12) != round(c, 12):
                        if number != "infinity" and number != "inf":
                            sumcalc = a * (1 - comrat ** number) / (1 - comrat)
                        elif round(comrat, 12) >= 1 or round(comrat, 12) <= -1:
                            print("Error: infinity is only accepted for nonzero common ratios between -1 and 1")
                            continue
                        else:
                            sumcalc = a / (1 - comrat)
                    else:
                        sumcalc = b * number
                    if round(sumcalc, 12) == 0:
                        sumcalc = 0.0
                    globals()[sum] = sumcalc
                    keeps.append(sum)
                    if number != "inf" and number != "infinity":
                        print(sum + f" (sum through term {number}) = {round(sumcalc, 12)}")
                    else:
                        print(sum + f" (sum through infinity) = {round(sumcalc, 12)}")
                elif len(srangelist) == 2:
                    try:
                        srangelist[0] = 0 + eval(srangelist[0])
                        srangelist[1] = 0 + eval(srangelist[1])
                        srangelist[0] = 0 + integer(srangelist[0])
                        srangelist[1] = 0 + integer(srangelist[1])
                    except:
                        print(f'"{number}" is not a positive integer')
                        continue
                    if srangelist[0] > 0 and srangelist[1] > srangelist[0]:
                        srangelist = list(range(srangelist[0], srangelist[1] + 1))
                        for item in srangelist:
                            sum = f"sum{item}"
                            if round(b, 12) != round(c, 12):
                                sumcalc = a * (1 - comrat ** item) / (1 - comrat)
                            else:
                                sumcalc = b * item
                            if round(sumcalc, 12) == 0:
                                sumcalc = 0.0
                            globals()[sum] = sumcalc
                            keeps.append(sum)
                            print(sum + f" (sum through term {item}) = {round(sumcalc, 12)}")
                    elif srangelist[1] <= srangelist[0]:
                        print(f'"{number}" is not a range in the form x:y, where y > x')
                    else:    
                        print(f'"{number}" is not a positive integer')
                else:
                    print(f'"{number}" is not a range in the form x:y, where y > x')
        if un != "/" and un != "skip" and un != "ski":
            un = un.replace(" ", "")
            un = un.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            un = un.split(",")
            for unterm in un:
                rangelist = unterm.split(":")
                if len(rangelist) == 1:
                    try:
                        if unterm == "r" or unterm == "ratio" or unterm == "comrat" or unterm == "common ratio":
                            rat = comrat
                            print(f"rat (common ratio) = {round(rat, 12)}")
                            continue
                        unterm = 0 + eval(unterm)
                        unterm = 0 + integer(unterm)
                    except:
                        print(f'"{unterm}" is not a positive integer')
                        continue
                    if unterm > 0:
                        sumterm = f"tm{unterm}"
                        globals()[sumterm] = a * comrat ** (unterm - 1)
                        keeps.append(sumterm)
                        print(sumterm + f" (term {unterm}) = {round(a * comrat ** (unterm - 1), 12)}")
                    else:
                        print(f'"{unterm}" is not a positive integer')
                elif len(rangelist) == 2:
                    try:
                        rangelist[0] = 0 + eval(rangelist[0])
                        rangelist[1] = 0 + eval(rangelist[1])
                        rangelist[0] = 0 + integer(rangelist[0])
                        rangelist[1] = 0 + integer(rangelist[1])
                    except:
                        print(f'"{unterm}" is not a positive integer')
                        continue
                    if rangelist[0] > 0 and rangelist[1] > rangelist[0]:
                        rangelist = list(range(rangelist[0], rangelist[1] + 1))
                        for unterm in rangelist:
                            sumterm = f"tm{unterm}"
                            globals()[sumterm] = a * comrat ** (unterm - 1)
                            keeps.append(sumterm)
                            print(sumterm + f" (term {unterm}) = {round(a * comrat ** (unterm - 1), 12)}")
                    elif rangelist[1] <= rangelist[0]:
                        print(f'"{unterm}" is not a range in the form x:y, where y > x')
                    else:    
                        print(f'"{unterm}" is not a positive integer')
                else:
                    print(f'"{unterm}" is not a range in the form x:y, where y > x')
        if round(abs(comrat), 12) != 1 and iun != "/" and iun != "skip" and iun != "ski":
            iun = iun.replace(" ", "")
            iun = iun.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            iun = iun.split(",")
            for iunterm in iun:
                try:
                    if iunterm == "r" or iunterm == "ratio" or iunterm == "comrat" or iunterm == "common ratio":
                        rat = comrat
                        print(f"rat (common ratio) = {round(rat, 12)}")
                        continue
                    iunterm = 0 + eval(iunterm)
                except:
                    print(f'"{iunterm}" is not a real number or expression')
                    continue
                if iunterm == a:
                    indexcalc = 1
                elif iunterm == a * -1:
                    print(f'"{iunterm}" is not a term in the series')
                    continue
                else:
                    indexcalc = log(abs(iunterm / a), abs(comrat)) + 1
                if round(indexcalc, 12) == round(indexcalc) and indexcalc > 0 and ((round(iunterm / a, 12) > 0 and comrat > 0) or (round(iunterm, 12) < 0 and comrat < 0 and a < 0 and indexcalc % 2 != 0) or (round(iunterm, 12) > 0 and comrat < 0 and a < 0 and indexcalc % 2 == 0) or (round(iunterm, 12) < 0 and comrat < 0 and a > 0 and indexcalc % 2 == 0) or (round(iunterm, 12) > 0 and comrat < 0 and a > 0 and indexcalc % 2 != 0)): 
                    series_find_constants(iunterm, indexcalc)
                else:
                    print(f'"{iunterm}" is not a term in the series')

def polynomial():
    global rt
    global rt2
    global im
    global im2
    global rl
    print()
    print("Welcome to polymial functions!")
    print("Please enter the equation in the form ax^2 + bx + c = 0, where x is a non-numeric variable name")
    while True:
        clear_variables()
        print()
        a = input('a (i): ')
        if a == "" or a == "exit" or a == "exi":
            break
        elif a == "o" or a == "ope" or a == "operations":
            real_operation()
            break
        elif a == "c" or a == "con" or a == "conic" or a == "conic sections":
            conic_section()
            break
        elif a == "sys" or a == "system" or a == "system of equations":
            system()
            break
        elif a == "s" or a == "sym" or a == "symmetry":
            symmetry()
            break
        elif a == "g" or a == "gam" or a == "games":
            math24play()
            break
        elif a == "info" or a == "inf" or a == "i":
            print()
            print("Please enter a real number or expression as the x^2 coefficient")
            print('Enter "sys" for system of equations, "c" for conic sections, "s" for symmetry, "o" for operations (this will direct to real operation), and "g" for games (this will direct to play Math 24)')
            continue
        try:
            a = a.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            a = 0 + eval(a)
        except:
            print('Please enter a real number or expression, "i" for info, or return to exit')
            continue
        b = input('b: ')
        if b == "" or b == "exit" or b == "exi":
            continue
        try:
            b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            b = 0 + eval(b)
        except:
            print('Please enter a real number or expression, or return to exit')
            continue            
        c = input('c: ')   
        if c == "" or c == "exit" or c == "exi":
            continue
        try:
            c = c.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            c = 0 + eval(c)
        except:
            print('Please enter a real number or expression, or return to exit')
            continue
        print()
        if round(a, 12) == 0 and round(b, 12) == 0 and round(c, 12) == 0:
            print("Roots: all numbers")
        elif round(a, 12) == 0 and round(b, 12) == 0:
            print("No rts")
        elif round(a, 12) == 0:
            rt = -c / b
            print(f"Root: x = {round(rt, 12)}")
            print(f"rt = {round(rt, 12)}")
        else:
            det = b ** 2 - 4 * a * c
            if round(det, 12) > 0:
                rt = (-b - sqrt(det)) / (2 * a)
                rt2 = (-b + sqrt(det)) / (2 * a)
                print(f"Roots: x = {round(rt, 12)} or x = {round(rt2, 12)}")
                print(f"rt = {round(rt, 12)}")
                print(f"rt2 = {round(rt2, 12)}")
            elif round(det, 12) == 0:
                rt = -b / (2 * a)
                print(f"Root: x = {round(rt, 12)}")
                print(f"rt = {round(rt, 12)}")
            else:
                rl = -b / (2 * a)
                im = sqrt(-det) / (2 * a)
                if round(rl, 12) != 0 and round(im, 12) > 0:
                    if round(im, 12) != 1:
                        print(f"Roots: x = {round(rl, 12)} - {round(im, 12)}i or x = {round(rl, 12)} + {round(im, 12)}i")
                    else:
                        print(f"Roots: x = {round(rl, 12)} - i or x = {round(rl, 12)} + i")
                elif round(rl, 12) == 0:
                    if round(im, 12) != 1 and round(im, 12) != -1:
                        print(f"Roots: x = {round(im * -1, 12)}i or x = {round(im, 12)}i")
                    elif round(im, 12) == 1:
                        print(f"Roots: x = -i or x = i")
                    else:
                        print(f"Roots: x = i or x = -i")
                elif round(im, 12) < 0:
                    if round(im, 12) != -1:
                        print(f"Roots: x = {round(rl, 12)} + {round(im * -1, 12)}i or x = {round(rl, 12)} - {round(im * -1, 12)}i")
                    else:
                        print(f"Roots: x = {round(rl, 12)} + i or x = {round(rl, 12)} - i")              
                print(f"rl (real part) = {round(rl, 12)}")
                im2 = im
                im *= -1
                print(f"im (imaginary part) = {round(im, 12)}")
                print(f"im2 (2nd imaginary part) = {round(im2, 12)}")

def symmetry():
    print()
    print("Welcome to fuction symmetry!")
    print("Please enter points in the form (x, y) and lines (if needed) in the form y = mx + b")
    while True:
        clear_variables()
        print()
        m = input("Slope (i): ")
        if m == "" or m == "exit" or m == "exi":
            break
        elif m == "info" or m == "inf" or m == "i":
            print()
            print("Please enter a real number or expression as the slope of the symmetry line")
            print('Enter "p" to enter points instead of slope and y-intercept')
            print('Enter "v" for a vertical and "h" for a horizontal symmetry line')
            print('Enter "pol" for polynomials, "s" for system of equations, "c" for conic sections, "o" for operations (this will direct to real operations), and "g" for games (this will direct to play Math 24)')
            continue
        elif m == "pol" or m == "polynomials":
            polynomial()
            break
        elif m == "s" or m == "sys" or m == "system" or m == "system of equations":
            system()
            break
        elif m == "o" or m == "ope" or m == "operations":
            real_operation()
            break
        elif m == "c" or m == "conic sections" or m == "con" or m == "conic":
            conic_section()
            break
        elif m == "g" or m == "gam" or m == "games":
            math24play()
            break
        elif m == "h" or m == "hor" or m == "horizontal":
            m = "0"
        if m != "v" and m != "ver" and m != "vertical" and m != "p" and m != "points" and m != "poi":
            try:
                m = m.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                m = 0 + eval(m)
            except:
                print('Please enter a real number or expression, "i" for info, or return to exit')
                continue
            b = input("Y-intercept: ")
            if b == "" or b == "exit" or b == "exi":
                continue
            try:
                b = b.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                b = 0 + eval(b)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            if round(m, 12) == 0:
                printm = ""
            elif round(m, 12) == 1:
                printm = f"x"
            else:
                printm = f"{round(m, 12)}x"
            if round(b, 12) == 0 and round(m, 12) != 0:
                printb = ""
            elif round(b, 12) == 0:
                printb = "0 (x-axis)"
            elif round(m, 12) == 0:
                printb = f"{round(b, 12)}"
            else:
                printb = f" + {round(b, 12)}"
            print("Symmetry line: y = " + printm + printb)
        elif m == "p" or m == "points" or m == "poi":
            p1 = input("Point 1 (s to enter slope): ")
            if p1 == "" or p1 == "exit" or p1 == "exi" or p1 == "s" or p1 == "slo" or p1 == "slope":
                continue
            p1 = p1.replace(" ", "")
            p1 = p1.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
            if p1[0] == "(":
                p1 = p1[1:]
            if p1[len(p1) - 1] == ")":
                p1 = p1[:len(p1) - 1]
            p1 = p1.split(",", 1)
            try:
                p1[0] = 0 + eval(p1[0])
                p1[1] = 0 + eval(p1[1])
            except:
                print("Please enter the points in the form (x, y), where x and y are real numbers or expressions")
                continue
            p2 = input("Point 2: ")
            if p2 == "" or p2 == "exit" or p2 == "exi":
                continue
            p2 = p2.replace(" ", "")
            p2 = p2.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")            
            if p2[0] == "(":
                p2 = p2[1:]
            if p2[len(p2) - 1] == ")":
                p2 = p2[:len(p2) - 1]
            p2 = p2.split(",", 1)
            try:
                p2[0] = 0 + eval(p2[0])
                p2[1] = 0 + eval(p2[1])
                if p2[0] == p1[0] and p2[1] == p1[1]:
                    print("Please enter two different points")
                    continue
            except:
                print("Please enter the points in the form (x, y), where x and y are real numbers or expressions")
                continue
            if p2[0] == p1[0]:
                m = "v"
                xint = p1[0]
                if xint != 0:
                    print(f"Symmetry line: x = {round(xint, 12)}")
                else:
                    print("Symmetry line: x = 0 (y-axis)")
            else:
                m = (p2[1] - p1[1]) / (p2[0] - p1[0])
                b = p1[1] - m * p1[0]
                if round(m, 12) == 0:
                    printm = ""
                elif round(m, 12) == 1:
                    printm = f"x"
                else:
                    printm = f"{round(m, 12)}x"
                if round(b, 12) == 0 and round(m, 12) != 0:
                    printb = ""
                elif round(b, 12) == 0:
                    printb = "0 (x-axis)"
                elif round(m, 12) == 0:
                    printb = f"{round(b, 12)}"
                else:
                    printb = f" + {round(b, 12)}"
                print("Symmetry line: y = " + printm + printb)
        else:
            xint = input("X-intercept: ")
            if xint == "" or xint == "exit" or xint == "exi":
                continue
            try:
                xint = xint.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
                xint = 0 + eval(xint)
            except:
                print('Please enter a real number or expression, or return to exit')
                continue
            if xint != 0:
                print(f"Symmetry line: x = {round(xint, 12)}")
            else:
                print("Symmetry line: x = 0 (y-axis)")
        print()
        reflect = input("Points to reflect (i): ")
        if reflect == "" or reflect == "exit" or reflect == "exi":
            continue
        elif reflect == "i" or reflect == "info" or reflect == "inf":
            print()
            print('Please enter a list of points to reflect in the form (x, y) separated by semicolons (;), eg. "(5, -3); (-1, 0); (4, 4)"')
            print()
            continue
        reflect = reflect.replace(" ", "")
        reflect = reflect.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
        reflect = reflect.split(";")
        for i in range(0, len(reflect)):
            print()
            pointlist = reflect[i].split(",")
            if len(pointlist) != 2:
                print(f'Error: "{reflect[i]}" is not a point in the form (x, y)')
                continue
            x_input = pointlist[0]
            y_input = pointlist[1]
            if "(" in x_input:
                x_input = x_input[x_input.find("(") + 1:]
            if ")" in y_input:
                y_input = y_input[:y_input.find(")")]
            try:
                x_input = 0 + eval(x_input)
            except:
                print(f'Error: "{reflect[i]}" is not a point in the form (x, y)')
                continue
            try:
                y_input = 0 + eval(y_input)
            except:
                print(f'Error: "{reflect[i]}" is not a point in the form (x, y)')
                continue
            if m != "v" and m != "ver" and m != "vertical":
                ang = atan(m)
                x = x_input * cos(2 * ang) + (y_input - b) * sin(2 * ang)
                y = x_input * sin(2 * ang) - (y_input - b) * cos(2* ang) + b
            else:
                x = -x_input + 2 * xint
                y = y_input
            if x == 0:
                x = 0.0
            if y == 0:
                y = 0.0
            xco = f"x{i + 1}"
            yco = f"y{i + 1}"
            globals()[xco] = x
            globals()[yco] = y
            keeps.append(xco)
            keeps.append(yco)
            print(f"Point {i + 1}: ({round(x, 12)}, {round(y, 12)})")
            print(xco + f" = {round(x, 12)}")
            print(yco + f" = {round(y, 12)}")

def conic_section():
    print()
    print("Welcome to conic sections!")

def matrix_operation():
    print()
    print("Welcome to matrix operations!")

def system():
    print()
    print("Welcome to system of equations!")

def math24play():
    global problems
    global print_problems
    global attempts
    print()
    print("Welcome to Play Math 24!")
    while True:
        clear_variables()
        random.seed(problems)
        numbers = pos[random.randrange(0, len(pos))]
        print_numbers = ""
        for number in numbers:
            print_numbers += str(number) + ", "
        print()
        if print_problems == len(pos):
            print(f"You've made it to Problem {len(pos)}!")
            print("This is the number of problems in the system, and also the number of possible Math 24 sets using the numbers 1-25, 36, 48, 72, 96, 120, and 144!")
            print("Congrats! You are now the God of Math!")
            print()
        elif print_problems % 10 == 0:
            print(f"You've made it to Problem {print_problems}!")
            print()
        print(f"Problem {print_problems}: " + print_numbers[:len(print_numbers) - 2])
        ops = [" + ", " - ", " * ", " / "]
        solved = False
        for i in range(0, 11):
            if solved == True:
                break
            for inumber1 in numbers:
                if solved == True:
                    break
                for op1 in ops:
                    if solved == True:
                        break
                    numbers2 = numbers[:]
                    numbers2.remove(inumber1)
                    for inumber2 in numbers2:
                        if solved == True:
                            break
                        for op2 in ops:
                            if solved == True:
                                break
                            numbers3 = numbers2[:]
                            numbers3.remove(inumber2)
                            for inumber3 in numbers3:
                                if solved == True:
                                    break
                                for op3 in ops:
                                    numbers4 = numbers3[:]
                                    numbers4.remove(inumber3)
                                    number4 = 0 + eval(str(numbers4[0]))
                                    number3 = 0 + eval(str(inumber3))
                                    number2 = 0 + eval(str(inumber2))
                                    number1 = 0 + eval(str(inumber1))
                                    if i <= 6:
                                        if i == 0:
                                            string = str(number1) + op1 + str(number2) + op2 + str(number3) + op3 + str(number4)
                                        elif i == 1:
                                            string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + op3 + str(number4)
                                        elif i == 2:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                        elif i == 3:
                                            string = str(number1) + op1 + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                        elif i == 4:
                                            string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                        elif i == 5:
                                            string = "(" + str(number1) + op1 + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                        elif i == 6:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + op3 + str(number4) + ")"
                                        string_print = string + " = 24"
                                    else:
                                        if i == 7:
                                            string = "((" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + ")" + op3 + str(number4)
                                            string_print = "[(" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + "]" + op3 + str(number4)
                                        elif i == 8:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + "))"
                                            string_print = str(number1) + op1 + "[" + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + ")]"
                                        elif i == 9:
                                            string = str(number1) + op1 + "((" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4) + ")"
                                            string_print = str(number1) + op1 + "[(" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4) + "]"
                                        else:
                                            string = "(" + str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + "))" + op3 + str(number4)
                                            string_print = "[" + str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + ")]" + op3 + str(number4)
                                        string_print += " = 24"
                                    try:
                                        if round(eval(string), 12) == 24:
                                            solutions = string_print
                                            solved = True
                                            break
                                    except:
                                        pass
        while True:
            attempts += 1
            input_sol = input(f"Attempt {attempts} (i, /): ")
            if input_sol == "" or input_sol == "exi" or input_sol == "exit" or input_sol == "l" or input_sol == "las" or input_sol == "last" or input_sol == "last problem" or input_sol == "/" or input_sol == "skip" or input_sol == "ski" or input_sol == "c" or input_sol == "cre" or input_sol == "create" or input_sol == "s" or input_sol == "sol" or input_sol == "solve" or input_sol == "o" or input_sol == "ope" or input_sol == "operations" or input_sol == "f" or input_sol == "fun" or input_sol == "functions":
                break
            elif input_sol == "i" or input_sol == "inf" or input_sol == "info":
                print()
                print("Math 24 is a game where players try to create the number 24 using 4 numbers and the 4 operations (+, -, *, /)")
                print("Enter a solution with each of the 4 numbers used once and any 3 operations, using parenthesis to change order")
                print('Eg. with the numbers 1, 5, 5, and 5, one solution is "5 * (5 - 1/5)"')
                print('Enter "l" to see the last problem')
                print('Enter "c" for create, "s" for solve, "o" for operations (this will direct to real operations) and "f" for functions (this will direct to polynomials)')
                print()
                continue
            sol = input_sol.replace(" ", "").replace("+", " + ").replace("-", " - ").replace("/", " / ").replace("*", " * ").replace("=24", "").replace(")(", ") (")
            evalsol = sol.replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(") (", ") * (")
            counter_list = evalsol.split(" ")
            counter = 0
            valid = True
            counter0 = 0
            counter1 = 0
            counter2 = 0
            counter3 = 0
            for a in counter_list:
                a = a.replace("(", "").replace(")", "")
                if a in ["+", "-", "/", "*"]:
                    counter += 1
                elif a in [str(numbers[0]), str(numbers[1]), str(numbers[2]), str(numbers[3])]:
                    if a == str(numbers[0]):
                        counter0 += 1
                    if a == str(numbers[1]):
                        counter1 += 1
                    if a == str(numbers[2]):
                        counter2 += 1
                    if a == str(numbers[3]):
                        counter3 += 1
                elif a != "":
                    valid = False
            if counter == 3 and counter0 == numbers.count(numbers[0]) and counter1 == numbers.count(numbers[1]) and counter2 == numbers.count(numbers[2]) and counter3 == numbers.count(numbers[3]) and valid == True:
                try:
                    if round(eval(evalsol), 12) == 24:
                        print()
                        print(f"Solved on Attempt {attempts}!")
                        attempts = 0
                        break
                    else:
                        print()
                        print(sol + f" = {round(eval(evalsol), 12)}, not 24")
                        print("Try again!")
                        print()
                        print(f"Problem {print_problems}: " + print_numbers[:len(print_numbers) - 2])
                        continue
                except:
                    print("The expression could not be evaluated")
                    print('Please enter a valid solution, "i" for info, or return to exit')
                    print()
                    print(f"Problem {print_problems}: " + print_numbers[:len(print_numbers) - 2])
                    continue
            else:
                print('Please enter a valid solution, "i" for info, or return to exit')
                print()
                print(f"Problem {print_problems}: " + print_numbers[:len(print_numbers) - 2])
                continue
        if input_sol == "" or input_sol == "exi" or input_sol == "exit":
            break
        elif input_sol == "l" or input_sol == "las" or input_sol == "last" or input_sol == "last problem":
            if problems != 1:
                print_problems -= 1
                problems -= 1
            continue
        elif input_sol == "/" or input_sol == "ski" or input_sol == "skip":
            print()
            print("Solution: " + solutions)
            problems += 1
            continue
        elif input_sol == "c" or input_sol == "cre" or input_sol == "create":
            math24create()
            break
        elif input_sol == "s" or input_sol == "sol" or input_sol == "solve":
            math24solve()
            break
        elif input_sol == "o" or input_sol == "ope" or input_sol == "operations":
            real_operation()
            break
        elif input_sol == "f" or input_sol == "fun" or input_sol == "functions":
            polynomial()
            break
        print_problems += 1
        problems += 1
            
def math24create():
    print()
    print("Welcome to Create Math 24!")
    while True:
        clear_variables()
        print()
        solutions = []
        input_use = input("Numbers to use (i): ")
        if input_use == "" or input_use == "exit" or input_use == "exi":
            break
        elif input_use == "i" or input_use == "inf" or input_use == "info":
            print()
            print('Enter a list of numbers separated by commas (,) and using colons (:) to indicate ranges and increments')
            print('Eg. "1, 2:6:2, 8:9" will output possible Math 24 sets using only the numbers 1, 2, 4, 6, 8, and/or 9')
            print("Note that the more numbers used (or the smaller the increments), the longer the calculation will take")
            print('Enter "p" for play, "s" for solver, "o" for operations (this will direct to real operations), and "f" for functions (this will direct to polynomials)')
            continue
        elif input_use == "p" or input_use == "pla" or input_use == "play":
            math24play()
            break
        elif input_use == "s" or input_use == "sol" or input_use == "solver":
            math24solve()
            break
        elif input_use == "o" or input_use == "ope" or input_use == "operations":
            real_operation()
            break
        elif input_use == "f" or input_use == "fun" or input_use == "functions":
            polynomial()
            break
        use = input_use.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(").replace(" ", "").split(",")
        fuse = []
        back = False
        for item in use:
            rangelist = item.split(":")
            if len(rangelist) == 1:
                try:
                    fuse.append(0 + eval(item))
                except:
                    print(f'Error: "{item}" is not a real number or expression')
                    back = True
                    break
            elif len(rangelist) == 2:
                try:
                    rangelist[0] = 0 + eval(rangelist[0])
                    rangelist[1] = 0 + eval(rangelist[1])
                except:
                    print(f'Error: "{item}" is not a real number or expression')
                    back = True
                    break
                if rangelist[1] <= rangelist[0]:
                    print(f'Error: "{item}" is not a range in the form x:y, where y > x')
                    back = True
                    break
                for addend in range(rangelist[0], rangelist[1] + 1):
                    fuse.append(addend)
            elif len(rangelist) == 3:
                try:
                    rangelist[0] = 0 + eval(rangelist[0])
                    rangelist[1] = 0 + eval(rangelist[1])
                    rangelist[2] = 0 + eval(rangelist[2])
                except:
                    print(f'Error: "{item}" is not a real number or expression')
                    back = True
                    break
                if rangelist[2] == 0:
                    print(f'Error: "{item}" is not a range in the form x:y:z, where z is nonzero')
                    back = True
                    break
                elif rangelist[2] > abs(rangelist[1] - rangelist[0]):
                    print(f'Error: "{item}" is not a range in the form x:y:z, where z <= |y-x|')
                    back = True
                    break
                if rangelist[1] >= rangelist[0]:
                    rangelist[2] = abs(rangelist[2])
                elif rangelist[1] < rangelist[0]:
                    rangelist[2] = -1 * abs(rangelist[2])
                for addend in range(rangelist[0], rangelist[1] + 1, rangelist[2]):
                    fuse.append(addend)
            else:
                print(f'Error: "{item}" is not a range in the form x:y or x:y:z')
                back = True
                break
        if back == True:
            continue
        for item in fuse:
            if fuse.count(item) > 1:
                fuse.remove(item)
        fuse.sort()
        input_ops = input("Operations to use (i): ")
        if input_ops in ["", "exit", "exi"]:
            continue
        elif input_ops in ["i", "inf", "info"]:
            print()
            print("Enter a list of operations (+, -, *, /) separated by commas")
            print("The order will also generally determine the order of the outputted sets")
            print('Eg. "+, *" will output possible Math 24 sets using only addition and/or multiplication, and will prioritize outputting sets with addition')
            print('Enter "a" to use all operations')
            continue
        elif input_ops == "a" or input_ops == "all":
            input_ops = "+, -, *, /"
        input_ops = input_ops.replace(" ", "").split(",")
        ops = []
        restart = False
        for operation in input_ops:
            if operation not in ["+", "-", "*", "/"]:
                restart = True
                break
            ops.append(" " + operation + " ")
        if restart == True:
            print('Please enter a valid input, "i" for info, or return to exit')
            continue
        sets_number = input("Number of sets to find (a for all): ")
        if sets_number not in ["a", "all"]:
            try:
                sets_number = 0 + integer(eval(sets_number))
                if sets_number <= 0:
                    print('Please enter a positive integer or return to exit')
                    continue
            except:
                print('Please enter a positive integer or return to exit')
                continue
        out = False
        for n1 in fuse:
            if out == True:
                break
            for n2 in fuse:
                if out == True:
                    break
                for n3 in fuse:
                    if out == True:
                        break
                    for n4 in fuse:
                        if sets_number not in ["a", "all"]:
                            if len(solutions) == sets_number:
                                out == True
                                break
                        numbers = [n1, n2, n3, n4]
                        solved = False
                        for op1 in ops:
                            if solved == True:
                                break
                            for op2 in ops:
                                if solved == True:
                                    break
                                for op3 in ops:
                                    if solved == True:
                                        break
                                    number4 = numbers[3]
                                    number3 = numbers[2]
                                    number2 = numbers[1]
                                    number1 = numbers[0]
                                    for i in range(0, 11):
                                        if i == 0:
                                            string = str(number1) + op1 + str(number2) + op2 + str(number3) + op3 + str(number4)
                                        elif i == 1:
                                            string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + op3 + str(number4)
                                        elif i == 2:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                        elif i == 3:
                                            string = str(number1) + op1 + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                        elif i == 4:
                                            string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                        elif i == 5:
                                            string = "(" + str(number1) + op1 + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                        elif i == 6:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + op3 + str(number4) + ")"
                                        elif i == 7:
                                            string = "((" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + ")" + op3 + str(number4)
                                        elif i == 8:
                                            string = str(number1) + op1 + "(" + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + "))"
                                        elif i == 9:
                                            string = str(number1) + op1 + "((" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4) + ")"
                                        else:
                                            string = "(" + str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + "))" + op3 + str(number4)
                                        try:
                                            if round(eval(string), 12) == 24:
                                                solutions.append(sorted([number1, number2, number3, number4]))
                                                solved = True
                                                break
                                        except:
                                            pass
        print()
        if len(solutions) != 0:
            print(f"Possible Math 24 sets:")
            for i in range(0, len(solutions)):
                if solutions.count(solutions[i]) > 1:
                    solutions[i] = "noprint"
                else:
                    '''res = ""
                    for b in solutions[i]:
                        res += str(b) + ", "
                    res = res[:len(res) - 2]
                    print(f"Set {i + 1}: " + res)'''
                    print(solutions[i], end = ", ")
                    print()
        else:
            print(f"There are no possible Math 24 sets using the entered numbers and operations")

def math24solve():
    print()
    print("Welcome to Solve Math 24!")
    while True:
        clear_variables()
        print()
        numbers = input("Numbers (i): ")
        if numbers == "" or numbers == "exit" or numbers == "exi":
            break
        elif numbers == "i" or numbers == "info" or numbers == "inf":
            print()
            print("Enter the 4 numbers to create 24 in a list separated by commas")
            print('Eg. with the numbers "1, 5, 5, 5", one solution is 5 * (5 - 1/5) = 24')    
            print('Enter "p" for play, "c" for create, "o" for operations (this will direct to real operations) and "f" for functions (this will direct to polynomials)')
            continue
        elif numbers == "o" or numbers == "ope" or numbers == "operations":
            real_operation()
            break
        elif numbers == "f" or numbers == "fun" or numbers == "functions":
            polynomial()
            break
        elif numbers == "p" or numbers == "pla" or numbers == "play":
            math24play()
            break
        elif numbers == "c" or numbers == "cre" or numbers == "create":
            math24create()
            break
        numbers = numbers.replace(" ", "")
        numbers = numbers.replace("^", "**").replace("[", "(").replace("]", ")").replace("{", "(").replace("}", ")").replace(")(", ")*(")
        numbers = numbers.split(",")
        if len(numbers) != 4:
            print('Please enter a list of 4 real numbers or expressions, "i" for info, or return to exit')
            continue
        input_ops = input("Operations to use (i): ")
        if input_ops in ["", "exit", "exi"]:
            continue
        elif input_ops in ["i", "inf", "info"]:
            print()
            print("Enter a list of operations (+, -, *, /) separated by commas")
            print("The order will also generally determine the order of the outputted solutions")
            print('Eg. "+, *" will output possible Math 24 sets using only addition and/or multiplication, and will prioritize outputting solutions with addition')
            print('Enter "a" to use all operations')
            continue
        elif input_ops == "a" or input_ops == "all":
            input_ops = "+, -, *, /"
        input_ops = input_ops.replace(" ", "").split(",")
        ops = []
        restart = False
        for operation in input_ops:
            if operation not in ["+", "-", "*", "/"]:
                restart = True
                break
            ops.append(" " + operation + " ")
        if restart == True:
            print('Please enter a valid input, "i" for info, or return to exit')
            continue
        sols = input("Number of solutions to find (a for all): ")
        if sols == "" or sols == "exit" or sols == "exi":
            continue
        elif sols == "all" or sols == "a":
            sols = "a"
        else:
            try:
                sols = 0 + integer(eval(sols))
                if sols <= 0:
                    print('Please enter a positive integer, "a" for all, or return to exit')
                    continue
            except:
                print('Please enter a positive integer, "a" for all, or return to exit')
                continue
        solutions = []
        previous = []
        solved = False
        for i in range(0, 11):
            if solved == True:
                break
            for inumber1 in numbers:
                if solved == True:
                    break
                for op1 in ops:
                    if solved == True:
                        break
                    numbers2 = numbers[:]
                    numbers2.remove(inumber1)
                    for inumber2 in numbers2:
                        if solved == True:
                            break
                        for op2 in ops:
                            if solved == True:
                                break
                            numbers3 = numbers2[:]
                            numbers3.remove(inumber2)
                            for inumber3 in numbers3:
                                if solved == True:
                                    break
                                for op3 in ops:
                                    numbers4 = numbers3[:]
                                    numbers4.remove(inumber3)
                                    try:
                                        number4 = 0 + eval(numbers4[0])
                                        number3 = 0 + eval(inumber3)
                                        number2 = 0 + eval(inumber2)
                                        number1 = 0 + eval(inumber1)
                                    except:
                                        print('Please enter a list of 4 real numbers or expressions, "i" for info, or return to exit')
                                        solved = True
                                        break
                                    tag = sorted(str(number1) + op1 + str(number2) + op2 + str(number3) + op3 + str(number4) + " = 24")
                                    if tag not in previous:
                                        if i <= 6:
                                            if i == 0:
                                                string = str(number1) + op1 + str(number2) + op2 + str(number3) + op3 + str(number4)
                                            elif i == 1:
                                                string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + op3 + str(number4)
                                            elif i == 2:
                                                string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                            elif i == 3:
                                                string = str(number1) + op1 + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                            elif i == 4:
                                                string = "(" + str(number1) + op1 + str(number2) + ")" + op2 + "(" + str(number3) + op3 + str(number4) + ")"
                                            elif i == 5:
                                                string = "(" + str(number1) + op1 + str(number2) + op2 + str(number3) + ")" + op3 + str(number4)
                                            elif i == 6:
                                                string = str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + op3 + str(number4) + ")"
                                            string_print = string + " = 24"
                                        else:
                                            if i == 7:
                                                string = "((" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + ")" + op3 + str(number4)
                                                string_print = "[(" + str(number1) + op1 + str(number2) + ")" + op2 + str(number3) + "]" + op3 + str(number4)
                                            elif i == 8:
                                                string = str(number1) + op1 + "(" + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + "))"
                                                string_print = str(number1) + op1 + "[" + str(number2) + op2 + "(" + str(number3) + op3 + str(number4) + ")]"
                                            elif i == 9:
                                                string = str(number1) + op1 + "((" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4) + ")"
                                                string_print = str(number1) + op1 + "[(" + str(number2) + op2 + str(number3) + ")" + op3 + str(number4) + "]"
                                            else:
                                                string = "(" + str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + "))" + op3 + str(number4)
                                                string_print = "[" + str(number1) + op1 + "(" + str(number2) + op2 + str(number3) + ")]" + op3 + str(number4)
                                            string_print += " = 24"
                                        try:
                                            if round(eval(string), 12) == 24:
                                                previous.append(tag)
                                                solutions.append(string_print)
                                                if sols != "a":
                                                    if len(solutions) == sols:
                                                        solved = True
                                                        break
                                        except:
                                            pass
        if solutions == []:
            print()
            print("There are no possible ways to create 24 with the entered numbers and operations")
        else:
            print()
            for i in range(0, len(solutions)):
                print(f"Solution {i + 1}: " + solutions[i])
            '''if solved == False:
                print()
                if len(solutions) == 1:
                    if sols == "a":
                        print(f"There is 1 way to create 24 with the entered numbers and operations")
                    else:
                        print(f"There is only 1 way to create 24 with the entered numbers and operations")
                else:
                    if sols == "a":
                        print(f"There are {len(solutions)} ways to create 24 with the entered numbers and operations")
                    else:
                        print(f"There are only {len(solutions)} ways to create 24 with the entered numbers and operations")'''

def main():
    global ans
    print("Welcome to The Ultimate Class Calculator!")
    while True:
        clear_variables()
        print()
        cat = input('Calculation category (i): ')
        cat = cat.replace(" ", "")
        if cat.lower() == "exit" or cat.lower() == "" or cat.lower() == "exi":
            break
        elif cat.lower() == "info" or cat.lower() == "inf" or cat.lower() == "i":
            print()
            print('Enter either "o" for operations, "f" for functions, "g" for games, or "s" for settings')
            print("Operations include: real operations, complex operations, matrix operations, and summations (binomial expansion, arithmetic series, and geometric series)")
            print("Functions include: polynomials, system of equations, conic sections, and symmetry")
            print("Games include: Math 24")
        elif cat.lower() == "s" or cat.lower() == "set" or cat.lower() == "settings":
            settings()
        elif cat.lower() == "f" or cat.lower() == "fun" or cat.lower() == "functions":
            while True:
                funtype = input("Function type (i): ")
                funtype = funtype.replace(" ", "")
                if funtype.lower() == "" or funtype.lower() == "exit" or funtype.lower() == "exi":
                    break
                elif funtype.lower() == "i" or funtype.lower() == "info" or funtype.lower() == "inf":
                    print()
                    print('Enter either "p" for polynomials, "se" for system of equations, "c" for conic sections, or "s" for symmetry')
                    print()
                elif funtype.lower() == "polynomials" or funtype.lower() == "p" or funtype.lower() == "pol":
                    polynomial()
                    print()
                elif funtype.lower() == "s" or funtype.lower() == "sym" or funtype.lower() == "symmetry":
                    symmetry()
                    print()
                elif funtype.lower() == "se" or funtype.lower() == "system of equations" or funtype.lower() == "sys" or funtype.lower() == "system":
                    system()
                    print()
                elif funtype.lower() == "con" or funtype.lower() == "conic" or funtype.lower() == "conic sections" or funtype.lower() == "c":
                    conic_section()
                    print()
                else:
                    print('Please enter a function type, "i" for info, or return to exit')
                    print()
        elif cat.lower() == "operations" or cat.lower() == "ope" or cat.lower() == "o":
            while True:
                opetype = input('Operation type (i): ')
                opetype = opetype.replace(" ", "")
                if opetype.lower() == "" or opetype.lower() == "exit" or opetype.lower() == "exi":
                    break
                elif opetype.lower() == "i" or opetype.lower() == "inf" or opetype.lower() == "info":
                    print()
                    print('Enter either "r" for real, "c" for complex, "m" for matrix, or "s" for summations (binomial expansion, arithmetic series, and geometric series)')
                    print()
                elif opetype.lower() == "real" or opetype.lower() == "rea" or opetype.lower() == "r" or opetype.lower() == "real operations":
                    real_operation()
                    print()
                elif opetype.lower() == "c" or opetype.lower() == "complex" or opetype.lower() == "com" or opetype.lower() == "complex operations":
                    while True:
                        ctype = input("From (r)ectangular or (p)olar form: ")
                        ctype = ctype.replace(" ", "")
                        if ctype.lower() == "rectangular" or ctype.lower() == "r" or ctype.lower() == "rect" or ctype.lower() == "rectangular form":
                            from_rectangular()
                            print()
                        elif ctype.lower() == "polar" or ctype.lower() == "p" or ctype.lower() == "pol" or ctype.lower() == "polar form":
                            from_polar()
                            print()
                        elif ctype.lower() == "" or ctype.lower() == "exit" or ctype.lower() == "exi":
                            print()
                            break
                        else:
                            print('Please enter either "r" for rectangular, "p" for polar, or return to exit')
                            print()
                elif opetype.lower() == "m" or opetype.lower() == "mat" or opetype.lower() == "matrix" or opetype.lower() == "matrix operations":
                    matrix_operation()
                    print()
                elif opetype.lower() == "summations" or opetype.lower() == "sum" or opetype.lower() == "s":
                    while True:
                        sumtype = input('Summation type (i): ')
                        sumtype = sumtype.replace(" ", "")
                        if sumtype.lower() == "" or sumtype.lower() == "exit" or sumtype.lower() == "exi":
                            print()
                            break
                        elif sumtype.lower() == "i" or sumtype.lower() == "inf" or sumtype.lower() == "info":
                            print()
                            print('Enter either "b" for binomial expansion, "a" for arithmetic series, or "g" for geometric series')
                            print()
                        elif sumtype.lower() == "b" or sumtype.lower() == "binomial" or sumtype.lower() == "bin" or sumtype.lower() == "binomial expansion":
                            binomial_expansion()
                            print()
                        elif sumtype.lower() == "a" or sumtype.lower() == "arithmetic" or sumtype.lower() == "ari" or sumtype.lower() == "arithmetic series":
                            arithmetic()
                            print()
                        elif sumtype.lower() == "geometric" or sumtype.lower() == "geo" or sumtype.lower() == "g" or sumtype.lower() == "geometric series":
                            geometric()
                            print()
                        else:
                            print('Please enter a summation type, "i" for info, or return to exit')
                            print()
                else:
                    print('Please enter either an operation type, "i" for info, or return to exit')
                    print()
        elif cat.lower() == "g" or cat.lower() == "gam" or cat.lower() == "games" or cat.lower() == "mat" or cat.lower() == "m" or cat.lower() == "24" or cat.lower() == "math 24":
            '''while True:
                game = input("Game (i): ")
                game = game.replace(" ", "")
                if game.lower() == "" or game.lower() == "exit" or game.lower() == "exi":
                    break
                elif game.lower() == "i" or game.lower() == "inf" or game.lower() == "info":
                    print()
                    print('Enter "m" for Math 24')
                    print()
                elif game.lower() == "m" or game.lower() == "mat" or game.lower() == "24" or game.lower() == "math 24" or game.lower() == "24":
                    while True:
                        mode = input("(P)lay, (c)reate, or (s)olve? ")
                        if mode.lower() == "" or mode.lower() == "exit" or mode.lower() == "exi":
                            print()
                            break
                        elif mode.lower() == "p" or mode.lower() == "play" or mode.lower() == "pla":
                            math24play()
                            print()
                        elif mode.lower() == "c" or mode.lower() == "cre" or mode.lower() == "create":
                            math24create()
                            print()
                        elif mode.lower() == "s" or mode.lower() == "sol" or mode.lower() == "solve":
                            math24solve()
                            print()
                        else:
                            print('Please enter either "p" for play, "c" for create, "s" for solve, or return to exit')
                            print()
                            continue
                else:
                    print('Please enter a game, "i" for info, or return to exit')
                    print()'''
            while True:
                mode = input("(P)lay, (c)reate, or (s)olve? ")
                if mode.lower() == "" or mode.lower() == "exit" or mode.lower() == "exi":
                    #print()
                    break
                elif mode.lower() == "p" or mode.lower() == "play" or mode.lower() == "pla":
                    math24play()
                    print()
                elif mode.lower() == "c" or mode.lower() == "cre" or mode.lower() == "create":
                    math24create()
                    print()
                elif mode.lower() == "s" or mode.lower() == "sol" or mode.lower() == "solve":
                    math24solve()
                    print()
                else:
                    print('Please enter either "p" for play, "c" for create, "s" for solve, or return to exit')
                    print()
                    continue
        else:
            print('Please enter a calculation category, "i" for info, or return to exit)')

main()
# %% [markdown]
# 

# %%



