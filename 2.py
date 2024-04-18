# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:14:37 2024

@author: Administrator
"""
'''creat a list,use []to define
'''
empty_list = []
empty_list = list()
instruments = ['600010.SHA','000001.SZA','300010.SZA']
instruments

print(len(instruments))

print(instruments[0])

print(instruments[-1])

print(instruments[0:2])
print(instruments[::2])
#from the first to the last,and every two

#add a instrument
instruments.append('300102.SZA')

print(instruments)

#add some instruments
instruments = instruments + ['300010.SZA','600033.SHA']
print('nihao',instruments)



'''modify the first instrument
'''
instruments[0] = '600012.SHA'
instruments
print(instruments)

#delete the first instrument
instruments.remove('600033.SHA')
instruments





#sort
instruments.sort()
instruments
print('sort:',instruments)

#reverse sort and change the origin list
instruments.sort(reverse = True)
print(instruments)


#use the reversed to reverse sort and dont change the origin list
list(reversed(instruments))
print(instruments)


#find the instrument index
instruments.index('000001.SZA')
print(instruments.index('000001.SZA'))

#find the count about some instrument
instruments.count('000001.SZA')
    






#digits cannot mofify

digits = (0,1,'two')
print(digits)

#change the list to digits
digits = tuple([10,'a'])
print(digits)


print(digits[0])

#digits cannot modify!!!



#string
s = '000001.SZA'
print(len(s))
print(s[0])
print(s[0:6])


#使用{}定义的元素组合，组合中元素唯一，（字符串，数字，or元组）

#创建空集合
empty_set = set()

#创建非空集合
plates = {'shanghai','shenzhen','chuangye'}

#将列表转化为集合
concepts = set(['chuangye','cixin','guoqi'])

#集合求交集
print(plates&concepts)
#集合求并
print(plates|concepts)
#集合求差
print(plates - concepts)


#列表去重
a = ['000001.SZA','600001.SHA','000001.SZA']
set(a)


#字典，二维数组。列表元组一维数组
#使用{}定义的二元元组元素列表


#creat a empty dictionary
empty_dict = {}
empty_dict = dict()

positions = {'300010.SZA':'100','002100.SZA':'200','600010.SHA':'300'}

len(positions)
print(len(positions))


print(positions.get('002100.SZA',0))
print(positions['002100.SZA'])
print(positions.get('111111.SZA','0'))


'''modift the dictionary'''
positions['002100.SZA']='5'
print(positions)

'''delete'''
del positions['002100.SZA']
positions.pop('300010.SZA')
print(positions)

#add
positions['002102.SZA'] = '1000'
print(positions)

#键名查询
print(positions.keys())
#键值查询
print(positions.values())
#键对查询
print(positions.items())
