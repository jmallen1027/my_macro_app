import functions
import time
import json 
def bmr_calculater(weight,height,gender,age):

    if gender == 'M' or gender == 'm':
        bmr = 66.47 + (6.24 * weight) + (12.7 * height) - (6.75 * age)
    elif gender == 'F' or gender == 'f':
        bmr = 65.51 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return int(bmr)

def read_json(user_name):
    with open(f"{user_name}.json", 'r') as file:
        content = file.read()
    return json.loads(content)

def write_json(data, user_name):#filename='users.json'):
    with open(f"{user_name}.json", 'w') as outfile:
        json.dump(data, outfile, indent=4)

class User:

    def __init__(self, name, age, weight, height, gender, goal, activity_factor):
        self.name = name
        self.age = int(age)
        self.weight = int(weight)
        self.height = int(height)
        self.gender = gender
        self.goal = goal
        self.activity_factor = activity_factor
        self.bmr = functions.bmr_calc(self.weight, self.height, self.gender, self.age)
        self.calories = self.bmr * self.activity_factor
        if self.goal == 'cut' or goal == 'Cut':
            self.calories = self.calories - 500
        elif self.goal == 'bulk' or goal == 'Bulk':
            self.calories = self.calories + 500
        self.weight_list = [{str(time.strftime("%b %d, %Y %H:%M:%S")): weight}]

    def set_weight_list(self, new_weight):
        self.weight_list.append({str(time.strftime("%b %d, %Y %H:%M:%S")): new_weight})

    def weight_trend(self):
        test_list = []
        for i in self.weight_list:
            for t in i.values():
                test_list.append(t)
        return sum(test_list) / len(test_list)
    
    def get_calories(self):
        return self.calories
    
    def get_weight_list(self):
        return self.weight_list
    
    def get_goal(self):
        return self.goal
    
    def set_goal(self, new_goal):
        self.calories = self.calories * self.activity_factor
        self.goal = new_goal
        if self.goal == 'cut' or new_goal == 'Cut':
            self.calories = self.calories - 500
        elif self.goal == 'bulk' or new_goal == 'Bulk':
            self.calories = self.calories + 500
    
    def get_activity_factor(self):
        return self.activity_factor
    
    def set_activity_factor(self, af):
        self.activity_factor = af

    def get_user_object(self):
        return {
            self.name : 
            {
            'age' : self.age, 
            'weight' : self.weight, 
            'height' : self.height, 
            'gender' : self.gender,  
            'bmr' : self.bmr,
            'weight_list' : self.weight_list,
            'goal': self.goal,
            'activity': self.activity_factor,
            'calories': int(self.get_calories()),
            }
        }
    
    @classmethod
    def paresed(cls, user_str):
    
        data = user_str.split(" ")
        name = data[0]
        age = int(data[1])
        weight = int(data[2])
        height = int(data[3])
        sex = data[4]
        
        return cls(name,age,weight,height,sex)


