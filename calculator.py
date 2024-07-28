from tkinter import *
import time

first_number = second_number = operator = pretxt = None

def pre_label_display():
    global first_number, second_number, operator, pretxt
    if pretxt is not None:
        pre_label.config(text=str(pretxt))
    else:
        pre_label.config(text='')

def get_digit(digit):
    global first_number, second_number, operator
    if result_label['text'] == 'Error':
        result_label.config(text='')
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    global first_number, second_number, operator, pretxt
    result_label.config(text='')
    first_number = None
    second_number = None
    operator = None
    pretxt = None
    pre_label_display()

def get_operator(op):
    global first_number, second_number, operator, pretxt
    if result_label['text'] == 'Error':
        clear()
        return
    first_number_2 = None
    pre_number = first_number
    if first_number is not None and second_number is None:
        try:
            first_number_2 = int(result_label['text'])
        except:
            first_number_2 = float(result_label['text'])

        if operator == '+':
            first_number = first_number + first_number_2
            result_label.config(text=str(first_number))
        elif operator == '-':
            first_number = first_number - first_number_2
            result_label.config(text=str(first_number))
        elif operator == '*':
            first_number = first_number * first_number_2
            result_label.config(text=str(first_number))
        elif operator == '/':
            if first_number_2 != 0:
                result = round(first_number / first_number_2, 2)
                try:
                    result_label.config(text=str(result).rstrip('0').rstrip('.'))
                except:
                    result_label.config(text=str(round(first_number / first_number_2, 2)))

                try:
                    first_number = int(result_label['text'])
                except:
                    first_number = float(result_label['text'])

            else:
                clear()
                result_label.config(text="Error")

    if first_number is None:
        try:
            first_number = int(result_label['text'])
        except:
            first_number = float(result_label['text'])

    result_label.config(text='')
    if first_number_2 is None and pre_number is None:
        pretxt = f'{first_number} {op}'
    else:
        pretxt = f'{pre_number} {operator} {first_number_2} = {first_number} {op}'
    operator = op
    pre_label_display()


def get_result():
    global first_number, second_number, operator, pretxt
    try:
        second_number = int(result_label['text'])
    except:
        second_number = float(result_label['text'])

    if operator == '+':
        result_label.config(text=str(round(first_number + second_number, 2)))
        pretxt = f'{first_number} + {second_number} = {round(first_number + second_number, 2)}'
    elif operator == '-':
        result_label.config(text=str(round(first_number - second_number, 2)))
        pretxt = f'{first_number} - {second_number} = {round(first_number - second_number, 2)}'
    elif operator == '*':
        result_label.config(text=str(round(first_number * second_number, 2)))
        pretxt = f'{first_number} * {second_number} = {round(first_number * second_number, 2)}'
    elif operator == '/':
        if second_number != 0:
            result = round(first_number / second_number, 2)
            try:
                result_label.config(text=str(result).rstrip('0').rstrip('.'))
            except:
                result_label.config(text=str(round(first_number / second_number, 2)))
            res = result_label['text']
            pretxt = f'{first_number} / {second_number} = {res}'
        else:
            clear()
            result_label.config(text="Error")

    first_number = None
    second_number = None
    operator = None
    pre_label_display()

root = Tk()

root.title("Calculator")
root.geometry("280x350")
root.resizable(0,0) # window not resize x or y direction
root.config(background="black")

pre_label = Label(root, text='', bg="black", fg="white")
pre_label.grid(row=0, column=0, pady=(20,25), columnspan=5, sticky='ne')
pre_label.config(font=('verdana', 10))

result_label = Label(root, text='', bg="black", fg="white")
result_label.grid(row=0, column=0, pady=(50,25), columnspan=5, sticky='w')
result_label.config(font=('verdana', 30, "bold"))


btn7 = Button(root, text='7', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana', 13, "bold"))

btn8 = Button(root, text='8', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana', 13, "bold"))

btn9 = Button(root, text='9', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana', 13, "bold"))

btn_add = Button(root, text='+', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana', 13, "bold"))

btn4 = Button(root, text='4', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana', 13, "bold"))

btn5 = Button(root, text='5', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana', 13, "bold"))

btn6 = Button(root, text='6', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana', 13, "bold"))

btn_sub = Button(root, text='-', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('verdana', 13, "bold"))

btn1 = Button(root, text='1', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana', 13, "bold"))

btn2 = Button(root, text='2', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana', 13, "bold"))

btn3 = Button(root, text='3', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana', 13, "bold"))

btn_mul = Button(root, text='*', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_operator('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('verdana', 13, "bold"))

btn_clear = Button(root, text='C', bg="#00a65a", fg="white", width=5, height=2, command=lambda : clear())
btn_clear.grid(row=4, column=0)
btn_clear.config(font=('verdana', 13, "bold"))

btn0 = Button(root, text='0', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana', 13, "bold"))

btn_equals = Button(root, text='=', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_result())
btn_equals.grid(row=4, column=2)
btn_equals.config(font=('verdana', 13, "bold"))

btn_div = Button(root, text='/', bg="#00a65a", fg="white", width=5, height=2, command=lambda : get_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('verdana', 13, "bold"))


root.mainloop()