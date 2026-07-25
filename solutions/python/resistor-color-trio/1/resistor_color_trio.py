def label(colors):

    color_label = {
        "black":"0",
        "brown":"1",
        "red":"2",
        "orange":"3",
        "yellow": "4",
        "green":"5",
        "blue":"6",
        "violet":"7",
        "grey":"8",
        "white":"9"
    }
    multiplier_label = {
        "black":"",
        "brown":"0",
        "red":"00",
        "orange":"000",
        "yellow": "0000",
        "green":"00000",
        "blue":"000000",
        "violet":"0000000",
        "grey":"00000000",
        "white":"000000000"
    }
    resistor = ""

# first two labels
    resistor += color_label[colors[0]]
    resistor += color_label[colors[1]]
   
# Multiplier
    resistor += multiplier_label[colors[2]]
   

    x = 0
    y = 0
    empty_list = []
    for index in reversed(resistor):
        empty_list.append(index)
        if index == "0":
            x = x + 1
        if x == 3:
            for i in range(0,x):
                    empty_list.pop()
            x = 0
            y += 1
        
    empty_list.reverse()    
    scientific_notation = {0:"", 1:"kilo",2:"mega",3:"giga"}
    if empty_list[0] == "0":
        empty_list.pop(0)
    final_result = ""

    for a in empty_list:
         final_result += a

    final_result += " " + scientific_notation[y] + "ohms"
    return(final_result)