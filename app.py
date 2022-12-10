import PySimpleGUI as sg
import user_class as uc
import functions as fun
import views

window = views.make_user_menu()

while True: 
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    elif event == '--RETURNING_USER--':
        window.close()
        window = views.current_mem_menu()

    elif event == '--NEW_USER--':
        window.close()
        window = views.new_user_menu()
    
    elif event == '--FIND_RETURNING_USER--':
        try:
            
            window.close()
            user_name, window = values['--NAME--'], views.make_current_window(values['--NAME--'])
        
        except FileNotFoundError:
            sg.Popup("User Not Found.")
            window = views.make_user_menu()
            continue
        
    elif event == '--COMPLETE--':
        try:
            gender = "M"
            if values['--MALE--']:
                gender = "M"
            else:
                gender = "F"
            
            this_new_user = uc.User(            
                values['--NAME--'], 
                values['--AGE--'], 
                values['--WEIGHT--'], 
                values['--HEIGHT--'],
                gender,
                values['--GOAL--'],     
                values['--AF--']           
                )
            fun.write_json([this_new_user.get_user_object()], values['--NAME--'])

            window.close()
            window = views.make_current_window(values['--NAME--'])
        
        except ValueError:
            sg.Popup("Incorrect arguments.")
            window.close()
            window = views.new_user_menu()


    elif event == '--COMPLETED_MACROS--':
        data = fun.read_json(user_name)
        user = data[0][user_name]
        window['--PROTIEN_GRAMS--'].update(f"Protien: {int(fun.dec_conv(int(values['--PROTIENS--'])) * int(user['calories']))} ")
        window['--CARB_GRAMS--'].update(f"Fat: {int(fun.dec_conv(int(values['--CARBS--'])) * int(user['calories']))} ")
        window['--FAT_GRAMS--'].update(f"Carbs: {int(fun.dec_conv(int(values['--FATS--'])) * int(user['calories']))} ")
      
    
    elif event == '--RETURN_MENU--':
        window.close()
        window = views.make_user_menu()

window.close()