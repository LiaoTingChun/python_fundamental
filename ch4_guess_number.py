import random

print("請決定隨機數範圍: ")
start, end = input("請輸入兩個數字: ").split(',')
r = random.randint(int(start), int(end))

count = 0
while True:
	guess = int(input("猜一個數字: "))
	count += 1
	if guess == r:
		print("終於答對了!")
		print("一共猜了{}次".format(str(count)))
		break
	else:
		if guess > r:
			print("比答案大")
		else:
			print("比答案小")