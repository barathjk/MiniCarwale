"""
EMI calculation
"""
def emi():
    """
    Getting input of Principal, rate and time and passing to other function to calculate
    """
    principal = int(input('Enter principal amount   : '))
    rate = float(input('Enter rate of interest   : '))
    time = int(input('Enter time in years      : '))
    emiinputs = emi_calculator(principal, rate, time)
    if emiinputs is None:
        print("Enter correct value of amount")
    else:
        return emiinputs

def emi_calculator(principal, rate, time):
    """
    EMI calculation
    """
    if principal > 0 and rate > 0 and time > 0:
        rate = rate / (12 * 100) # one month interest
        time = time * 12 # one month period
        emi_calc = (principal * rate * pow(1 + rate, time)) / (pow(1 + rate, time) - 1)
        emi_calc = round(emi_calc, 2)
        return emi_calc
    else:
        return None
