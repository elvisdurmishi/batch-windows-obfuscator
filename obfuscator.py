#!/usr/bin/env python

import random
import string

# qellimi i skriptit: Te ekzekutojme nje program.
# psh: Calculator qe ndodhet C:/Windows/System32/calc.exe

goal = "start C:/Windows/System32/calc.exe"

variables = []

# gjenerojme nje emer te rastesishem per variablen
def generate_random_variable_name(min_length=5, max_length =10):
    global variables

    while True:
        variable = "".join([ random.choice(string.ascii_lowercase) for _ in range(random.randrange(min_length, max_length)) ])
        if variable not in variables:
            variables.append(variable)
            return variable

# krijojme emrat e variablave per operatoret baze qe na nevojiten
set_operator = generate_random_variable_name()
space_character = generate_random_variable_name()
equals_character = generate_random_variable_name()

# krijojme nje set instruksionesh per te krijuar komanden baze
instructions = [
    f"set {set_operator}=set",
    f"%{set_operator}% {space_character}= ",
    f"%{set_operator}%%{space_character}%{equals_character}==",
]

# krijojme funksionin qe na gjeneron variablat per cdo karakter te kodit qe duam te ekzekutojme
def create_variable(varname, value):
    return f"%{set_operator}%%{space_character}%{varname}%{equals_character}%{value}"

command = {}
var_settings = []
for char in goal:
    varname = generate_random_variable_name()
    value = char
    var_settings.append(create_variable(varname, value))
    command[value] = varname

# krijojme komanden qe duam te ekzekutojme
execute = ["".join([f"%{command[char]}%" for char in goal])]

# bashkojme bashke te gjitha instruksionet per te krijuar payload final
code = [] + instructions + var_settings + execute

final_code = ("\n".join(code))
with open("payload.bat", "w") as handle:
    handle.write(final_code)