import pandas as pd

student_dict = {
    "student":["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# 把dict的內容用pandas轉成data frame.
student_df = pd.DataFrame(student_dict)
print(student_df)

# Loop through rows of a data frame.
# 用pandas裡面的data frame的 iterrows 去找到對應key的資料
for (index, row) in student_df.iterrows():
    print(index)
    print(row.score)   # 印出所有的分數
    print(row.student) # 印出所有的學生名字

# 另一個寫法就是:
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score) # 這時候應該會顯示56
