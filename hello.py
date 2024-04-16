# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:33:54 2024

@author: Administrator
"""

#py定义变量时不需要定义类型，系统会自动辨别变量的类型
"""
变量类型的查看可以通过
type（3）查看
type(30.32)
"""

float(3)
#将3转换到一个浮点数


print("Hello World!")
print("你好，世界！")

#一般以新的一行作为新的语句
#但是可以使用\将一行语句分行显示：
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three

        

# ' " ''' """
#单引号双引号三引号都可以表示字符串
#其中三引号可以由多行组成
word = 'word'
sentence = "this is a sentence"
paragraph = """this is a paragraph.
 about sth"""
 
 
 
#print输出默认换行，如果想要不换行则需要在变量末尾加上，

x = "a"
y = "b"
#换行输出
print (x)
print (y)

#不换行输出
print(x),
print(y),

print(x,y)

"""
if expression:
    suite
elif expression:
    suite
else:
    suite
  """
for letter in 'Python':
    if letter == 'h':
        continue
    print('当前字母：'),letter
    
    
var = 10
while var > 0:
    var = var - 1
if var == 5:
     continue
        print('值：'),var

print("Good bye!")    
    







