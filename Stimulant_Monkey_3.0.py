from tkinter import *
from math import * 

root = Tk()
root.title("Stimulant Monkey v3")
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

def simple_calculator():

    def run_calculator(event):
        
        x = eval(input.get())
        output.delete('1.0',END)
        output.insert("end", str(x))

    simple_calculator = Tk()
    simple_calculator.title("Simple Calculator")
    intro = Label(simple_calculator, text = 'Input:')
    output_intro = Label(simple_calculator, text = 'Output:')
    input = Entry(simple_calculator, width = 35, borderwidth = 5)
    output  = Text(simple_calculator, width = 26, borderwidth = 5, height = 1)
    outro = Label(simple_calculator, text = 'Enter/return to run.')

    simple_calculator.bind('<Return>', run_calculator)
    intro.grid(row = 0, column = 0)
    input.grid(row=0,column=1)
    output_intro.grid(row = 3, column = 0)
    output.grid(row = 3, column = 1)
    outro.grid(row = 4, column = 1)
    simple_calculator.mainloop()
   

def equation_calculator():

    def run_calculator(event):
        x = eval(x_input.get())
        y = eval(y_input.get())
        output.delete('1.0',END)
        output.insert("end", str(y))

    equation_calculator = Tk()
    equation_calculator.title("equation Calculator")
    x_intro = Label(equation_calculator, text = 'X Input:')
    y_intro = Label(equation_calculator, text = 'String Input:')
    output_intro = Label(equation_calculator, text = 'Output:')
    x_input = Entry(equation_calculator, width = 5, borderwidth = 5)
    y_input = Entry(equation_calculator, width = 35, borderwidth = 5)
    output  = Text(equation_calculator, width = 26, borderwidth = 5, height = 1)
    outro = Label(equation_calculator, text = 'Enter/return to run.')
    equation_calculator.bind('<Return>', run_calculator)
    x_intro.grid(row = 0, column = 0)
    x_input.grid(row=0,column=1)
    y_intro.grid(row = 1, column = 0)
    y_input.grid(row=1,column=1)
    outro.grid(row=4,column=1)
    output_intro.grid(row = 3, column = 0)
    output.grid(row = 3, column = 1)
    equation_calculator.mainloop()

def patch_notes():
    patch_notes = Tk()
    patch_notes.title("Patch Notes")
    L1=Label(patch_notes, text = '1.0 : taught myself how to code python', anchor = "w")
    L2=Label(patch_notes, text = '1.1 : function to determine instant velocity')
    L3=Label(patch_notes, text = '1.2 : added function to determin slope of a line through a single point')
    L4=Label(patch_notes, text = '2.0 : changed the way inputs were added from variable by variable to string equations')
    L5=Label(patch_notes, text = '2.0.1 : made the program mobile compatible through pythonista')
    L6=Label(patch_notes, text = '2.2 : redesigned the layout of the selection menu')
    L7=Label(patch_notes, text = '2.2.1 : went live, patched to be downloaded by colleagues as a .py executable')
    L8=Label(patch_notes, text = '2.2.2 : patched an issue with the way selections were made which crashed the program')
    L9=Label(patch_notes, text = '	 (changed selection = eval(input()) to selection = int(input())')
    L10=Label(patch_notes, text = '2.3 : began rewriting my c++ trig calculator as a single function')
    L11=Label(patch_notes, text = '2.3.1 : minor bug fixes')
    L12=Label(patch_notes, text = '2.3.2 : Finally got the meth monkey to calculate SAS triangles correctly, after many many hours of frustration')
    L13=Label(patch_notes, text = '2.4 : added ASA and SSS triangles. Also added some dependant functions')
    L14=Label(patch_notes, text = '2.4.1 : added some example problems to entry_guide, as well as some notes on trig calculator')
    L15=Label(patch_notes, text = '2.4.2 : fixed issue preventing trig calculator from working')
    L16=Label(patch_notes, text = '3.0 : Began the process of building a GUI, completed \'simple calculator\' \'equation calculator\' and \'patch notes\'')
    L1.pack(side= TOP, anchor="w")
    L2.pack(side= TOP, anchor="w")
    L3.pack(side= TOP, anchor="w")
    L4.pack(side= TOP, anchor="w")
    L5.pack(side= TOP, anchor="w")
    L6.pack(side= TOP, anchor="w")
    L7.pack(side= TOP, anchor="w")
    L8.pack(side= TOP, anchor="w")
    L9.pack(side= TOP, anchor="w")
    L10.pack(side= TOP, anchor="w")
    L11.pack(side= TOP, anchor="w")
    L12.pack(side= TOP, anchor="w")
    L13.pack(side= TOP, anchor="w")
    L14.pack(side= TOP, anchor="w")
    L15.pack(side= TOP, anchor="w")
    L16.pack(side= TOP, anchor="w")
   
def instant_velocity():

    def run_instant_velocity(event):
        print('under construction')

    instant_velocity = Tk()
    instant_velocity.title("Instant Velocity")
    x_intro = Label(instant_velocity, text = 'X Input:')
    y_intro = Label(instant_velocity, text = 'String Input:')
    output_intro = Label(instant_velocity, text = 'Output:')
    x_input = Entry(instant_velocity, width = 5, borderwidth = 5)
    y_input = Entry(instant_velocity, width = 35, borderwidth = 5)
    output  = Text(instant_velocity, width = 26, borderwidth = 5, height = 1)
    outro = Label(instant_velocity, text = 'Enter/return to run.')
    instant_velocity.bind('<Return>', run_instant_velocity)
    x_intro.grid(row = 0, column = 0)
    x_input.grid(row=0,column=1)
    y_intro.grid(row = 1, column = 0)
    y_input.grid(row=1,column=1)
    outro.grid(row=4,column=1)
    output_intro.grid(row = 3, column = 0)
    output.grid(row = 3, column = 1)
    instant_velocity.mainloop()


button_0 = Button(root, text='Patch Notes', padx = 10, pady = 5,borderwidth=5,command=patch_notes)
button_1 = Button(root, text='Simple Calculator', padx = 10, pady = 5,borderwidth=5,command=simple_calculator)
button_2 = Button(root, text='Equation Calculator', padx = 10, pady = 5,borderwidth=5,command=equation_calculator)
button_3 = Button(root, text='Instant Velocity', padx = 10, pady = 5,borderwidth=5,command=instant_velocity)

button_0.grid(row = 0, column = 0, sticky = 'W')
button_1.grid(row=1,column=0, sticky = 'W')
button_2.grid(row=2,column=0, sticky = 'W')
button_3.grid(row=3,column=0, sticky = 'W')

root.mainloop()
