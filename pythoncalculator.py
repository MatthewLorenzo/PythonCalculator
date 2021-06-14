#Followed a python tutorial to create a simple python calculator with gui using tkinter
from tkinter import *

#created the window
window = Tk()
window.title('Calculator')
window.geometry('355x475')
window.configure(bg = 'grey')
window.resizable(width = False, height = False)

#methods
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set('0')

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set('ERROR')
        expression = ""

#frame for all the buttons to go on
button_frame = Frame(window, bg = 'grey')
button_frame.pack()

#entry box where the equation and answer will be displayed
equation = StringVar()
equation.set('0')
entry_box = Entry(button_frame, textvariable = equation, justify = 'right', font = ('arial', 20,'bold'))

#created all the buttons including numbers and operators
button1 = Button(button_frame, text = '1', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(1))
button2 = Button(button_frame, text = '2', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(2))
button3 = Button(button_frame, text = '3', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(3))
button_add = Button(button_frame, text = '+', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press('+'))
button4 = Button(button_frame, text = '4', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(4))
button5 = Button(button_frame, text = '5', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(5))
button6 = Button(button_frame, text = '6', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(6))
button_sub = Button(button_frame, text = '-', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press('-'))
button7 = Button(button_frame, text = '7', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(7))
button8 = Button(button_frame, text = '8', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(8))
button9 = Button(button_frame, text = '9', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(9))
button_mult = Button(button_frame, text = '*', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press('*'))
button0 = Button(button_frame, text = '0', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press(0))
button_dec = Button(button_frame, text = '.', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press('.'))
button_clear = Button(button_frame, text = 'C', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = clear)
button_div = Button(button_frame, text = '/', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white', width = 8, height = 3, command = lambda:press('/'))
button_equal = Button(button_frame, text = '=', font = ('arial', 12), 
    relief = 'ridge', borderwidth = 1, bg = 'white',width = 8, height = 3, command = equal)

#placed the buttons in specific places on the frame
entry_box.grid(row = 0,column = 0, columnspan = 4, ipadx = 8, ipady = 25, pady = 15)
button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button_add.grid(row = 1, column = 3)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button_sub.grid(row = 2, column = 3)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
button_mult.grid(row = 3, column = 3)
button0.grid(row = 4, column = 0)
button_dec.grid(row = 4, column = 1)
button_clear.grid(row = 4, column = 2)
button_div.grid(row = 4, column = 3)
button_equal.grid(row = 5, column  = 0, columnspan = 4, sticky = 'NSEW')

window.mainloop()
