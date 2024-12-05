def BMI_Calculator(height, weight):
    '''This Function used to find BMI : The body mass index (BMI) is a measure used in
      medicine to see if someone is underweight or overweight.'''
    BMI = weight/(height**2)
    if BMI < 18.5:
        return f"Your BMI is : {round(BMI,2)} Category : Underweight"
    elif 18.5 <= BMI < 25:
        return f"Your BMI is : {round(BMI,2)} Category : Normal Weight"
    elif BMI >= 25:
        return f"Your BMI is : {round(BMI,2)} Category : Overweight"
    else:
        return f"Not Valid Input"
    
print(BMI_Calculator(1.85,85))