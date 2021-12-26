
age = input("What is your current age?")
age_int = int(age)
limit_years = 90
days = (limit_years - age_int)*365
weeks = (limit_years - age_int) * 52
months = (limit_years - age_int) * 12


print(f"You have {days} days, {weeks} weeks, and {months} months left.")