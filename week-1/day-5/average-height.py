# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height_summation = 0
total_students = 0
for student in student_heights:
  height_summation += student 
  total_students += 1
average_height = round(height_summation/total_students)
print(f"average height: {average_height}")