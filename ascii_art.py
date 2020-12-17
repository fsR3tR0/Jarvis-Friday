#! /usr/bin/python3

from pyfiglet import Figlet

def render(text,style):
    f = Figlet(font = style)
    print("\n"*2)
    print(f.renderText(text))
    print("\n"*2)

# text_input = input()
# asd = 'doh'
# render(text_input,'slant')



# print("Heor")