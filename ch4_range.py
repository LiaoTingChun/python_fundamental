### range ###
import random

for i in range(100):
	print("This is the", i+1, "time you generate a number: ", end ='')
	print(random.randint(0,1000)) 