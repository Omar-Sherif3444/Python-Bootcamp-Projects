import random
numbers=[1,2,3]
new_numbers=[n+1 for n in numbers]
# print(new_numbers)
name="Smoozie"
nn=[letter for letter in name]
# print(nn)

rr=range(1,5)
nr=[n*2 for n in rr]
# print(nr)

names=["omar","fady","mostafa","mohamed","malek","abdullah"]
short_names=[name.upper() for name in names if len(name)<5]
# print(short_names)

names3=["omar","fady","mostafa","mohamed","malek","abdullah"]
student_score={
        "omar":89,
        "fady":75,
        "mostafa":42,
        "mohamed":64,
        "malek":91,
        "abdullah":81,

}
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)
passed_students={student:score for (student,score) in student_scores.items() if score>=60}
print(passed_students)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)
