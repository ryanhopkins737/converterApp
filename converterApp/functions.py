import pytemperature as pt
from main import categorySelect, catInput, catOutput, userInput


def convert():
    if categorySelect.get() == "Temperature":
        user_input = float(userInput.get())
        if catInput.get() == "Celsius":
            if catOutput.get() == "Kelvin":
                return pt.c2k(user_input)
            if catOutput.get() == "Fahrenheit":
                return pt.c2f(user_input)
        elif catInput.get() == "Kelvin":
            if catOutput.get() == "Celsius":
                return pt.k2c(user_input)
            if catOutput.get() == "Fahrenheit":
                return pt.k2f(user_input)
        elif catInput.get() == "Fahrenheit":
            if catOutput.get() == "Celsius":
                return pt.f2c(user_input)
            if catOutput.get() == "Kelvin":
                return pt.f2k(user_input)
    elif categorySelect.get() == "Length":
        pass
