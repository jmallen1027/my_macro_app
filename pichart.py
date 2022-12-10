import PySimpleGUI as sg
import matplotlib.pyplot as plotter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 

# The slice names of a population distribution pie chart
def macroImage(macro_list):
    macros = 'Protien', 'Carbs', 'Fats'

    figureObject, axesObject = plotter.subplots()

    axesObject.pie(macro_list,
            labels=macros,

            autopct='%1.2f',

            startangle=90)

    axesObject.axis('equal')
    return plotter.gcf()


def draw_fig_on_canvas(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [
    [sg.Text('Macros')],
    [sg.Canvas(size=(1000,1000), key='--CANVAS--')],
    [sg.Exit()]
]
window = sg.Window('Pie Graph', layout, finalize=True, element_justification='center')

draw_fig_on_canvas(window['--CANVAS--'].TKCanvas, macroImage([35,30,40]))

#while True:
    #event, values = window.read()

   # if event == sg.WIN_CLOSED or event == 'exit':
  #      break
#window.close()


