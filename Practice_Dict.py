# Dictionary Comprehension

# 寫法1:
# new_dict = { new_key: new_value for item in list }

# 寫法2:
# new_dict = { new_key: new_value for (key, value) in dict.item() if test }

student_scroe = {
    "Alex": 89,
    "Beth": 98,
    "Caroline": 62,
    "Dave": 81,
    "Eleanor": 38,
    "Freddie": 89,
}

"""
Dictionary Comprehension 2
You are going to use Dictionary Comprehension
to create a dictionary called weather_f that
takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
"""

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {
    key : value * 9 / 5 + 32 for (key, value) in weather_c.items()
}
print(weather_f)

