VALID_SYMBOLS="¬&S0=+.()>#"

def is_expression(x, VALID_SYMBOLS):
    return all(c in x for c in VALID_SYMBOLS)

def reduce_s(x):
    while "ss" in x:
        x = x.replace("ss", "s")

    if "s0" in x:
        x = x.replace("s0", "0")

    return x

def is_term(x):
    x = reduce_s(x)



    if x == "0":
        return True
    

    


#################################################

input_string = "hjkhjk"

if not is_expression(input_string, VALID_SYMBOLS):
    print("Expression")

else:
    print("Not an expression")


