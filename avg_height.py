# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_height = sum_height + student_heights[n]
avg = sum_height / len(student_heights)
print(round(avg))
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
