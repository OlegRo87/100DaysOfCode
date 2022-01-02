# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visisted, cities_visited):
    new_country = {"country": country_visited, "visits": times_visisted, "cities": cities_visited}
    print(new_country)
    travel_log.append(new_country)







#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


