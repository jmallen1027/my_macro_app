import json

def bmr_calc(weight,height,gender,age):
    if gender == 'M' or gender == 'm':
        bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.75 * age)
    elif gender == 'F' or gender == 'f':
        bmr = 65.51 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return int(bmr)

def read_json(user_name):
    with open(f"./users/{user_name}.json", 'r') as file:
        content = file.read()
    return json.loads(content)

def write_json(data, user_name):#filename='users.json'):
    with open(f"./users/{user_name}.json", 'w') as outfile:
        json.dump(data, outfile, indent=4)

def dec_conv(number):
    dec = number / 100
    return dec