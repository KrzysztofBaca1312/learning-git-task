print('lista zakupów')
shoping_list = {
  'piekarnia':['chleb','bułki','pączek'],
  'warzywniak':['marchew','seler','rukola']
}

for key in shoping_list:
  print('ide do', key.title(), 'i kupuje tam',str(shoping_list[key]).title())

sum_list=sum(len(value) for value in shoping_list.values())

print('w sumie kupuję',sum_list,'produktów')
