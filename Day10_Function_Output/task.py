def is_leap_year(year):
    """Function checks if the year is a leap year"""
    isDivisibleBy4 = year % 4 == 0
    isDivisibleBy100 = year % 100 == 0
    isDivisibleBy400 = year % 400 == 0

    if isDivisibleBy4:
        if isDivisibleBy100:
            if isDivisibleBy400:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

print(f"2020 is a leap year: {is_leap_year(2020)}")
print(f"1600 was a leap year: {is_leap_year(1600)}")

def format_name(f_name, l_name):
    """Take a first and last name and format it to 
    return the title case version of the name."""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

format_name("Joe", "Zoe")