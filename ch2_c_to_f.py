### 攝氏溫度轉華氏溫度 ###

temprature_c = float(input("請輸入攝氏溫度: "))
temprature_f = temprature_c*9/5 + 32

temprature_c = round(temprature_c, 2)
temprature_f = round(temprature_f, 2)
print("攝氏{0}度等於華氏{1}度".format(str(temprature_c), str(temprature_f)))