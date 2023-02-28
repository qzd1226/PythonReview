# 1.1 使用基本语法[]创建
# 创建空的列表 []
a = []
print(a) #结果，创建空的列表 []

# 创建列表[1, 2, ‘abc’]
b = [1,2,'abc']
print(b) #结果：[1, 2, ‘abc’]
print(b[2]) #结果：abc

#1.2 基于list()创建
c = list()
print(c) #结果：创建一个空的列表
c.append(1)
print(c)  #结果：[1]

c = list('abcdefg')
print(c)  #结果：[‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
print(c[1]) #结果：
d = list(range(10))
print(d) #结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

