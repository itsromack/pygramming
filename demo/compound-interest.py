def compound_interest(principal_amount, annual_interest_rate, number_of_times_interest, number_of_years):
    interest = principal_amount * ((1 + (annual_interest_rate / number_of_times_interest)) * (number_of_times_interest * number_of_years))
    return interest


print(compound_interest(1000000, 5, 10, 15))
