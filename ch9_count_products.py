def count_products(data):
    if len(data) == 0:
        return None
    else:
        dic = {}
        for d in data:
            stuff, count = d.split(' ')[0], int(d.split(' ')[1])
            if stuff not in dic:
                dic[stuff] = count
            else:
                dic[stuff] += count
    return dic

data = {'麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1', '御飯糰 5'}
print(count_products(data))