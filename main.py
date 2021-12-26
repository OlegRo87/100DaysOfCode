height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_2 = float(height) ** 2


bmi = (float(weight) / height_2)
bmi_int = round(bmi)


if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif 18.5 < bmi_int < 25:
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif 25 < bmi_int < 30:
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif 30 < bmi_int < 35:
    print(f"Your BMI is {bmi_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_int}, you are clinically obese.")














