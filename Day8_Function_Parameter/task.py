# Calculating number of weeks left for ones lifetime
def life_in_weeks(age):
    # assuming 90yeears is the total life span 
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)