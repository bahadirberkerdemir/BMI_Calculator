import tkinter as t
from asyncio.windows_events import NULL


window = t.Tk()
window.minsize(300,300)

kgLabel = t.Label(text="Enter your weight (kg)")
kgLabel.pack()

kgEntry = t.Entry(width=20)
kgEntry.pack()

lenLabel = t.Label(text="Enter your Height (cm)")
lenLabel.pack()

lenEntry = t.Entry(width=20)
lenEntry.pack()

answerLabel = t.Label()
def onButtonClick():
    answerLabel.config(text="")

    if not lenEntry.get() or not kgEntry.get():
        answerLabel.config(text="Please enter both weight and height!")
    else:
        try:
            controlInt = int(lenEntry.get()) + int(kgEntry.get())
            h=int(lenEntry.get())/100
            w=int(kgEntry.get())

            bmi=w/(h**2)


            if bmi<18.5 : answerLabel.config(text=f"Your bmi is {bmi:.2f}. You are weak.")
            elif bmi<25 : answerLabel.config(text=f"Your bmi is {bmi:.2f}. You are normal.")
            elif bmi<30 : answerLabel.config(text=f"Your bmi is {bmi:.2f}. You are a bit overweight.")
            elif bmi<35 : answerLabel.config(text=f"Your bmi is {bmi:.2f}. You are obese.")
            else : answerLabel.config(text=f"Your bmi is {bmi:.2f}. You are extremely obese")
        except ValueError:
            answerLabel.config(text="Please enter a valid value!")


    answerLabel.pack()

calcButton = t.Button(text="Calculate", height=1, command=onButtonClick)
calcButton.pack()

window.mainloop()