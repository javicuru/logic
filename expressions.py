VALID_SYMBOLS="S0+.=v|A¬&()"

def check_valid_symbols(x, symbols):
    return all(c in x for c in symbols)

def check_parenthesis(x):
    if "()" in x:
        return False

    cont = 0

    for y in x:
        if y == "(":
            cont += 1
        
        elif y == ")":
            cont += -1

        if cont < 0:
            return False
    
    return (cont == 0)

def check_arithm(x):
    for i, y in enumerate(x):
        if y in ("+", ".", "="):
            if x[i-1] not in "0v|)" or x[i+1] not in "0v|(":
                return False
    
    return True
            
def check_not(x):
    for i, y in enumerate(x):
        if y = "¬":
            if x[i+1] != "A(":
                return False
    
    return True

def check_s(x):
    for i, y in enumerate(x):
        if y = "S":
            if x[i+1] != "0":
                return False
    
    return True

def check_A(x):
    for i, y in enumerate(x):
        if y = "¬":
            if x[i+1] != "A(":
                return False
                

def is_valid_expression(x, symbols):
    #TODO: complete this function: not every string built with VALID_SYMBOLS is valid i.e. ")S0(" or "S&+".

    x = reduce_expression(x)  # this doesn't affect whether the original expression is valid or not.

    return all((check_valid_symbols(x, symbols),
                check_parenthesis(x),
                check_arithm(x),
                check_not,
                check_s))






    


def reduce_expression(x):
    while x[0] == "(" and x[-1] == ")":  # (((E))) -> E
        x = x[1:-1]

    while "ss" in x:
        x = x.replace("SS", "S")  # SSS0 -> S0

    if "s0" in x:
        x = x.replace("S0", "0")  # S0 -> 0

    while "||" in x:
        x = x.replace("||", "|")  # ||| -> |

    while "v|" in x:
        x = x.replace("v|", "v")  # v| -> v

    return x

def find_

def is_term(x):
    for y in x:
        if y not in "S0+.v|()":
            return False
    
    return True
>
    # x = reduce_s(x)

    # if x in ("0", "v", "v|"):
    #     return True
    
    # for i, y in enumerate(x):
    #     if y == "(":
    #         open_i = i
        
    #     elif y == ")":
    #         close_i = i

    #         return 
        
    
    
    

    


#################################################

input_string = "hjkhjk"

if not is_expression(input_string, VALID_SYMBOLS):
    print("Expression")

else:
    print("Not an expression")


