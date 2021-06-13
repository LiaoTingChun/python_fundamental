import time
import progressbar

### 讀取留言 ###
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		bar.update(count)
print("一共讀取", count, '筆資料')


### 篩選留言長度 ###
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有",len(new),"筆留言長度小於100")

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print("一共有",len(good),"筆留言有good字串")

### 速寫法 ###
good = [d for d in data if 'good' in d]
print("一共有",len(good),"筆留言有good字串")


### 留言分析(文字計數) ###
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, '秒')
print(len(wc))

while True:
	word = input("你想查什麼字: ")
	if word == 'q':
		print('感謝使用')
		break
	if word in wc:
		print(word, "出現過的次數為:", wc[word])
	else:
		print('This word is NOT in dictionary!')