def bmi_calc(weight, height):
    bmi = weight/height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return bmi, result


if __name__ == '__main__':
    user_weight = float(input('your weight [kg]:'))
    user_height = float(input('your height [m]:'))
    user_bmi, user_result = bmi_calc(user_weight, user_height)
    print(f' your bmi is {user_bmi}. and you are {user_result}')