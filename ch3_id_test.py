### 密碼重試程式 ###

print("最多輸入3次密碼")

correct_ID = 'a123456'
chance = 3

while chance > 0:
	chance -= 1 
	user_ID = input("請輸入密碼: ")
	if user_ID == correct_ID:
		print("登入成功!")
		break
	else:
		if chance > 0:
			print("密碼錯誤!還有{}次機會".format(str(chance)))
		else:
			print("Your account has been locked!")