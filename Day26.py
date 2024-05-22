# list comprehension
# numbers = [1,1,2,3,5,8,13,21,34,55]


# # write your 1 line code below
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# even_numbers = [num for num in numbers if num % 2 ==0]
# print(even_numbers)

# with open("file1.txt") as file1:
#     list1 = file1.readlines()
# print(list1)
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
# print(list2)
# result = [int(num) for num in list1 if num in list2]
# print(result)

# dictionary comprehension
# sentence = "What is the airspeed velocity of a unladen swallow?"

# result = {item:len(item) for item in sentence.split() }
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# result = {day: value +9/5 +32 for (day, value) in weather_c.items()}

# print(result)

student_dict = {
    "Student":["Angela","James","Lily"],
    "Score": [56,76,98]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.Student)