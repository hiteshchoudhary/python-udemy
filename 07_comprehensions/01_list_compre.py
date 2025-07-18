menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)