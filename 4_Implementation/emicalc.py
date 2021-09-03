"""
EMI calculation
"""
def emi():
    principal = int(input('Enter principal amount   : '))
    rate = float(input('Enter rate of interest   : '))
    time = int(input('Enter time in years      : '))
    emi = emi_calculator(principal, rate, time)
    if emi == None:
        print("Enter correct value of amount")
    else:
        return emi

def emi_calculator(principal, rate, time):
    if principal > 0 and rate > 0 and time > 0:
        rate = rate / (12 * 100) # one month interest
        time = time * 12 # one month period
        emi = (principal * rate * pow(1 + rate, time)) / (pow(1 + rate, time) - 1)
        emi = round(emi, 2)
        return emi
    else:
        return None
