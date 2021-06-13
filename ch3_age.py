### 年齡判斷程式 ###

driving = input("Have you driven cars before? ")
age = int(input("Hoe old are you? "))

if driving !=  "yes" and driving != "no":
	print("Please answer my question.")
	raise SystemExit

if driving == "yes":
	if age >= 18:
		print("OK, you passed the exam.")
	else:
		print("You cannot drive before 18!")
else:
	if age >= 18:
		print("You should start learning to drive!")
	else:
		print("Great, just go home and study.")