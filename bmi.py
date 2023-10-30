def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Weight Classification = Under Weight")
        value = -1
    elif bmi < 25.0:
        print("Weight Classification = Normal Weight")
        value = 0
    else:
        print("Weight Classification = Over Weight")
        value = 1
    return value


returnvalue = calculate_bmi(weight=57, height=1.73)