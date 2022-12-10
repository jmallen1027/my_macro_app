import time
import functions 
def bmr_calc(weight,height,gender,age):

    if gender == 'M' or gender == 'm':
        bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.75 * age)
    elif gender == 'F' or gender == 'f':
        bmr = 65.51 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return int(bmr)

class User:

    def __init__(self, name, age, weight, height, gender):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.gender = gender
        self.bmr = bmr_calc(self.weight, self.height, self.gender, self.age)
        self.weight_list = [{str(time.strftime("%b %d, %Y %H:%M:%S")): weight}]
    
    def get_name(self): 
        return self.name    
    
    def get_bmr(self):
        return self.bmr
    
    def get_weight_list(self):
        return self.weight_list
    
    def get_goal(self):
        return self.goal

    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age

    def set_weight_list(self, new_weight):
        self.weight_list.append({str(time.strftime("%b %d, %Y %H:%M:%S")): new_weight})
    
    def set_weight(self, new_weight):
        self.weight = new_weight

    def set_height(self, new_height):
        self.weight = new_height

    def set_age(self, new_age):
        self.age = new_age
    
    def weight_trend(self):
        test_list = []
        for i in self.weight_list:
            for t in i.values():
                test_list.append(t)
        return sum(test_list) / len(test_list)

    def get_user_object(self):
        return {
            self.name : 
            {
            'age' : self.age, 
            'weight' : self.weight, 
            'height' : self.height, 
            'gender' : self.gender,  
            'bmr' : self.bmr,
            'weight_list' : self.weight_list
            }
        }

class Calorie_calculations(User):
    
    def __init__(self, bmr, activity_factor):
        self.activity_factor = activity_factor
        self.maintaince = bmr * activity_factor
        self.calories = bmr * activity_factor
        self.goal = 'maintaince'
    
    def cut(self):
        self.goal = 'cut'
        self.calories = self.calories - 500
    
    def bulk(self):
        self.goal = 'bulk'
        self.calories = self.calories + 500

    def maintaince(self):
        self.goal = 'maintaine'
        self.calories =self.maintaince

    def get_calories(self):
        return self.calories

    def get_calculations(self):
        return {
            'objectives':
                {
                'current_calories' : self.calories,
                'goal' : self.goal,
                'activity_factor' : self.activity_factor
                }
            }

class Macros(User):
    def __init__(self, calories, protien_perc, carb_perc, fat_perc):
        self.calories = calories
        self.protien_perc = protien_perc
        self.carb_perc = carb_perc
        self.fat_perc = fat_perc

    def cals(self):
        
        return {
            'cals' : {
                'protien': (self.protien_perc / 100) * self.calories,
                'carbs' : (self.carb_perc / 100) * self.calories,
                'fats' : (self.fat_perc / 100) * self.calories
            }
        }
    def grams(self):
        
        return {
            'grams' : {
                'Protiens': ((self.protien_perc / 100) * self.calories) / 4,
                'carbs' : ((self.carb_perc / 100) * self.calories) / 4,
                'fats' : ((self.fat_perc / 100) * self.calories) / 9
            }
        }

    def get_macros(self):
        return {
                'fats' : self.fat_perc,
                'protien' : self.protien_perc,
                'carbs' : self.carb_perc
                }
            
"""
new_person = User('jeff',31, 180, 66, 'M')




print(new_person.get_user_object())

my_cuurent_cals = Calorie_calculations(new_person.get_bmr(), 2.1)
my_cuurent_cals.cut()
print(my_cuurent_cals.get_calculations())

my_macs = Macros(my_cuurent_cals.get_calories(),30,30,40)

my_macs.grams()
print(my_macs.get_macros())


make_new_json = [
        new_person.get_user_object()
    ]



make_new_json[0]['objectives'] = my_cuurent_cals.get_calculations()
make_new_json[0]['macros'] = my_macs.get_macros()
print(make_new_json[0])

functions.write_json(make_new_json, new_person.get_name())
"""