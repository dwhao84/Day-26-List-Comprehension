
arg = []
for i in range(10):
    arg.append(i)

print(arg) # 應該會印出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 用 List Comprehension的方式撰寫。
arg1 = [i for i in range(10)]
print(arg1)

""" 
解釋如何使用List Comprehension
new_list對Developer來說，就是一個arg(也就是一個list)
而我們可以透過用new_item，for-loop list裡面的item之後，得到新的new_list。
new_list = [ new_item for item in list ]
"""
# 變化題:
# 既有的寫法
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# 用List Comprehension的寫法：
newest_list = [n + 1 for n in numbers]
print(newest_list)

# 用List Comprehension的變化題1:
name = "Angela"
letters_list = [letter for letter in name ]
print(letters_list) # 應該是顯示["A", "n", "g", "e", "l", "a"]

# Challenge range
# Create a new list from a range(1, 5), where the list items are double the values in the range.
number_list = [num * 2 for num in range(1, 5)]
print(number_list)

# Conditional List Comprehension 條件式 列表推導式
# 參考 新的list = [變化的值 for 值 in list if 你要的條件]
# 設定要找到名字，在四個字母以內，包含四個字母的
names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) <= 4]
print(short_name)

longer_name = [ name.upper() for name in names if len(name) > 4]
print(longer_name)