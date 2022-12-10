import PySimpleGUI as sg
import functions as fun
def make_user_menu():
    user_menu= [

        [
            sg.Button("Returning User", font=('italic', 15), size=(20,1), key="--RETURNING_USER--"),
            sg.Button("New User", font=('italic', 15), size=(20,1), key="--NEW_USER--"),
        ],
        [
            sg.Push(),sg.Text("Name:   ", font=('italic', 20), visible=False, key="--NAME_TEXT--"),
            sg.In(size=(40,10), key="--NAME--", visible=False),sg.Push()
        ]
    ]
    return sg.Window("Test Calc", user_menu)

def current_mem_menu():

    return_name_menu = [    
        [
            sg.Push(),sg.Text("Name:", font=('italic', 20)),
            sg.In(size=(40,10), key="--NAME--"),sg.Push()
        ],
        [sg.Push(),sg.Button("Complete", font=('italic', 15), size=(20,1), key="--FIND_RETURNING_USER--"),sg.Push()],
    ]
    return sg.Window("Test Calc", return_name_menu)

def make_current_window(user_name):
    data = fun.read_json(user_name)
    user = data[0][user_name]
    
    return_user_menu= [

        [
            sg.Text(f"Welcome {user_name}", font=('italic', 30))
        ],
        [
            sg.Text(f"Goal: {user['goal']}   AF: {user['activity']}   BMR: {user['bmr']}   Weight: {user['weight']}", font=('italic', 20))
        ],
    ]
    
    calories_final = [        [
            sg.Push(),sg.Text(f"Calories {user['calories']}", font=('italic', 30)), sg.Push()
        ]
    ]
    calories_col = [

            [
            sg.Text('Protien: ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--PROTIENS--'), sg.Push()
        ],
        [
            sg.Text('Carbs:   ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--CARBS--'), sg.Push()
        ],
        [
            sg.Text('Fats:      ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--FATS--'), sg.Push()
        ],
        [
            sg.Button('Complete', key='--COMPLETED_MACROS--')
        ]
    ]

    user_col = [
        [
            sg.Text(f"Fats", key="--FAT_GRAMS--", font=('italic', 30))
        ],
                [
            sg.Text(f"Protien", key="--PROTIEN_GRAMS--", font=('italic', 30))
        ],
                [
            sg.Text(f"Carbs", key="--CARB_GRAMS--", font=('italic', 30))
        ]

    ]
    return_btn = [[sg.Button('Return to Meny', key='--RETURN_MENU--')]]
        
    return sg.Window("Current User Menu", layout=[
            [
                return_user_menu
                ], 
            [
                calories_final
                ],
            [
                sg.Col(calories_col), 
                sg.VSeparator(), 
                sg.Col(user_col)
            ], 
            [
                return_btn
            ]
        ], finalize=True, element_justification='c'
        )
def new_user_menu():

    top_name_menu = [    
        [

            sg.Push(),sg.Text("Name:   ", font=('italic', 20)),
            sg.In(size=(40,10), key="--NAME--"),sg.Push()
        ]
    ]
    create_user_menu = [

        [
            sg.Push(), sg.Text("Age:       ", font=('italic', 20)),
            sg.In(size=(10,2), key="--AGE--"), sg.Push()
        ],
        [
            sg.Push(), sg.Text("Weight: ", font=('italic', 20)),
            sg.In(size=(10,2), key="--WEIGHT--"), sg.Push()
        ],
        [
            sg.Push(), sg.Text("Height:  ", font=('italic', 20)),
            sg.In(size=(10,2), key="--HEIGHT--"), sg.Push()
        ]
    ]
    gender_col = [
        [sg.Text("Gender: ", font=('italic', 20))],
        [sg.Radio('Male', 1, key='--MALE--')],
        [sg.Radio('Female', 1, key='--FEMALE--')]
    ]

    goal_col =     [
        [
            sg.Listbox(['Cut', 'Bulk', 'Maintaine'], key='--GOAL--', size=(15, 1))
        ]
    ]
    bottom_part_menu = [
        [

            sg.Push(), sg.Text("Activity Factor:", font=('italic', 20)), sg.Push()
            
        ],
        [
            sg.Push(), sg.Slider((2,3), resolution=.1, orientation='h', s=(10,15), key='--AF--'), sg.Push()
        ],
        [
            sg.Push(), sg.Button("Complete",font=('italic', 20), size=(10,1), key="--COMPLETE--"), sg.Push()
        ]
    ]

    return sg.Window('New User Menu', layout = [
            top_name_menu,
            [sg.Col(create_user_menu), 
            sg.VSeparator(),
            sg.Col(gender_col),
            sg.VSeparator(),
            sg.Col(goal_col)],    
            bottom_part_menu
        ]
        )