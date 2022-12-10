import PySimpleGUI as sg
import user_class as uc

user_name = uc.User('jeff', 31, 180, 66, 'M', 'Cut', 2.1)
jeff = user_name.get_user_object()
print(jeff)

menu = ['Options', ['&Views', ['Percentages', 'Grams', 'Calories'], 'Goals', ['Cut', 'Bulk', 'Maintaine'], 'Docs', ['Macros', 'BMR', 'Goals'], 'Exit']]




def dec_conv(number):
    dec = number / 100
    return dec

def view_calculator(dic):
    pass
   # --MACRO_VIEW-- {'--MACRO_VIEW--': 'Grams', '--PROTIENS--': 30.0, '--CARBS--': 30.0, '--FATS--': 50.0}
   # print(dic)
   # print(dic['--MACRO_VIEW--'])
   # print(dic['--PROTIENS--'])
    #if dic['--MACRO_VIEW--'] == 'Grams':

      #  return window['--PROTIEN_GRAMS--'].update(f"Protien: {(dic['--PROTIENS--'] / 100) * })g"), window['--CARB_GRAMS--'].update(f"Carbs: {dic['--CARBS--'] / 100}g "), window['--FAT_GRAMS--'].update(f"Fats: {dic['--FATS--'] / 100}g")
pop_menu = [
        [
            sg.Text('Protien: ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--PROTIENS--')
        ],
        [
            sg.Text('Carbs:   ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--CARBS--')
        ],
        [
            sg.Text('Fats:      ', font=('italic', 20)),
            sg.Slider((1,100), resolution=1, orientation='h', s=(20,15), key='--FATS--')
        ]
]
window = sg.Window('Test', layout=[
        [sg.MenubarCustom([menu])],
        [
            sg.Push(), sg.Text(f"Welcome {'Jeff'}", font=('italic', 30)), sg.Push()
        ],
        [
            sg.Text(f"Goal: {jeff['jeff']['goal']}   AF: {jeff['jeff']['activity']}   BMR: {jeff['jeff']['bmr']}   Weight: {jeff['jeff']['weight']}", font=('italic', 20))
        ],
        [   
            
            sg.ButtonMenu(button_text='Menu',menu_def=menu, key='--MACRO_VIEW--'),
            sg.Push(), sg.Text(f"Calories: {jeff['jeff']['calories']}", font=('italic', 40)), sg.Push()
        ],
       
        [
            sg.Text(f"Fats: ", key="--FAT_GRAMS--", font=('italic', 20))
        ],
                [
            sg.Text(f"Protien: ", key="--PROTIEN_GRAMS--", font=('italic', 20))
        ],
                [
            sg.Text(f"Carbs:", key="--CARB_GRAMS--", font=('italic', 20))
        ],
        pop_menu
    ])

while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '--MACRO_VIEW--':
        if values['--MACRO_VIEW--'] == 'Calories':
            window['--PROTIEN_GRAMS--'].update(f"Protien: {int((values['--PROTIENS--'] / 100) * jeff['jeff']['calories'])}kj")
            window['--CARB_GRAMS--'].update(f"Carbs: {int((values['--CARBS--'] / 100) * jeff['jeff']['calories'])}kj ")
            window['--FAT_GRAMS--'].update(f"Fats: {int((values['--FATS--'] / 100) * jeff['jeff']['calories'])}kj")
        elif values['--MACRO_VIEW--'] == 'Grams':
            window['--PROTIEN_GRAMS--'].update(f"Protien: {int(((values['--PROTIENS--'] / 100) * jeff['jeff']['calories']) / 4)}g")
            window['--CARB_GRAMS--'].update(f"Carbs: {int(((values['--CARBS--'] / 100) * jeff['jeff']['calories']) / 4)}g ")
            window['--FAT_GRAMS--'].update(f"Fats: {int(((values['--FATS--'] / 100) * jeff['jeff']['calories']) / 9)}g")