year_sample = 2024


def greet():
    print("Welcome to Python Programming")


def is_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


# greet()
result = is_leap_year(year_sample)
print(result)
