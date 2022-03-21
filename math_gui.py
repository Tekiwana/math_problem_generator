from tkinter import *
import random
import sys

complete = 0
window = Tk()
window.title("Math excercise")
window.geometry("350x450")

legnagyobb = StringVar(window)
feladat = StringVar(window)
tort = IntVar(window)
out = StringVar(window)


def exit():
    sys.exit()


def filter(feladat_a, operator, tort_num):
    if operator == "-":
        if eval(feladat_a) < 0:
            return False
        else:
            return True
    elif operator == "/":
        if float(feladat_a.split("/")[0]) % float(feladat_a.split("/")[1]) != 0:
            if tort_num == 1:
                return True
            else:
                return False
        else:
            return True
    else:
        return True


def main(operator):
    tort_num = tort.get()
    counter = 0
    max = int(legnagyobb.get())
    while counter != int(feladat.get()):
        feladat_a = str(generate(max, tort_num))+operator + \
                        str(generate(max, tort_num))
        if filter(feladat_a, operator, tort_num) is True:
            with open("excercise.txt", "a+") as f:
                f.write(feladat_a+"=________     ")
                counter += 1
    text_out = Text(window, height=4, width=18)
    text_out.grid(row=5, column=0)
    text_out.delete(0.0, END)
    text_out.insert(END, "DONE\nExcercise.txt")


def generate(max, tort_num):
    if tort_num == 1:
        return round(random.uniform(1, max), 2)
    else:
        return random.randint(1, max)


def osszeadas():
    operator = "+"
    main(operator)


def kivonas():
    operator = "-"
    main(operator)


def osztas():
    operator = "/"
    main(operator)


def szorzas():
    operator = "*"
    main(operator)


legnagyobb_label = Label(window, text="Biggest number")
legnagyobb_label.grid(row=0, column=0, sticky="W")
legnagyobb_label.config(font=("Arial", 15))
leg_entry = Entry(window, textvariable=legnagyobb)
leg_entry.grid(row=0, column=1)

feladat_label = Label(window, text="How many excercise?")
feladat_label.grid(row=1, column=0)
feladat_label.config(font=("Arial", 15))
feladat_entry = Entry(window, textvariable=feladat)
feladat_entry.grid(row=1, column=1)

tort_box = Checkbutton(window, text="Fractions?", variable=tort)
tort_box.grid(row=2, column=0, sticky="W")

osszeadas_button = Button(window, text="Aggregation ", command=osszeadas)
kivonas_button = Button(window, text="Subtraction", command=kivonas)
osztas_button = Button(window, text="Divison", command=osztas)
szorzas_button = Button(window, text="Multiplication", command=szorzas)
osszeadas_button.grid(row=3, column=0, ipadx=20, ipady=20)
kivonas_button.grid(row=4, column=0, ipadx=20, ipady=20)
osztas_button.grid(row=3, column=1, ipadx=20, ipady=20)
szorzas_button.grid(row=4, column=1, ipadx=20, ipady=20)


exit_button = Button(window, text="EXIT", command=exit)
exit_button.grid(row=5, column=1, ipadx=10, ipady=10)


window.mainloop()
