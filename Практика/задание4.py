nums = (1,2,2,3,3,55,55,55,14,124)


stat_num = {
    'Одно':0,
    'Два':0,
    'Три':0
}

for num in nums:
    if len(str(num))==1:
        stat_num['Одно']+=1
    if len(str(num))==2:
        stat_num['Два']+=1
    if len(str(num))==3:
        stat_num['Три']+=1

for k,v in stat_num.items():
    print(f'{k} в колличестве {v} шт.')

