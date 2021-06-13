### BMI指數測量 ###

height = float(input("請輸入身高(公分): "))/100
weight = float(input("請輸入體重(公斤): "))

BMI = weight/(height**2)

if BMI < 18.5:
	print("體重過輕")
elif BMI >= 18.5 and BMI < 24:
	print("正常範圍")
elif 24 <= BMI < 27:
	print("過重")
elif 27 <= BMI < 30:
	print("輕度肥胖")
elif 30 <= BMI < 35:
	print("中度肥胖")
else:
	print("重度肥胖")