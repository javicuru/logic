# TODO: so far it breaks for input_string = "(v)". Is this an expression or not?
# obs: chose to reject "empty expressions" such as "()". Is it ok? 

VALID_SYMBOLS="S0+.=v|A¬&()"

VALID_CONSEC = (("S", "0"),
                ("0", "+.=)"),
                ("+.=", "0v("),
                ("v|", "+.=|)"),
                ("A", "v"),
                ("¬", "A("),
                ("&", "("),
                ("(", "S0vA¬"),
                (")", "+.=&"))

def check_valid_symbols(x, symbols):
    for c in x:
        if c not in symbols:
            return False, "symbol " + c
        
    return True, None

def check_first_symbol(x):
     return x[0] in "S0vA¬("

def check_last_symbol(x):
        return x[-1] in "0v|)"

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

def check_consecutive_symbols(x):
    for i, y in enumerate(x):
        for z in VALID_CONSEC:
            if y in z[0] and x[i+1] not in z[1]:
                return False, "consec: " + y + x[i+1]
            
        # elif y == "0" and x[i+1] not in ("+", ".", "=", ")"):
        #     return False

        # elif y in ("+", ".", "=") and x[i+1] not in "0v(":
        #     return False
        
        # elif y in "v|" and x[i+1] not in ("+", ".", "=", "|", ")"):
        #     return False

        # elif y == "A" and x[i+1] != "v":
        #     return False

        # elif y == "¬" and x[i+1] not in "A(":
        #     return False
            
        # elif y == "&" and x[i+1] != "(":
        #     return False
            
        # elif y == "(" and x[i+1] not in "S0vA¬":
        #     return False
        
        # elif y == ")" and x[i+1] not in "+.=&":
        #     return False
            
    return True

def check_has_equal(x):
    return "=" in x

def is_statement(x, symbols):
    valid, symbol = check_valid_symbols(x, symbols)

    if not valid:
        return False, symbol

    try:
        x = reduce_expression(x)  # this should not affect whether the original expression is a statement or not.
    
    except IndexError:
        return False, "empty"  #  expresión vacía, por ejemplo "()" las rechazo.

    print("After reducing expression: " + x)

    if not check_has_equal(x):
        return False, "equal"

    if not check_first_symbol(x):
        return False, "first"
    
    if not check_last_symbol(x):
        return False, "last"
    
    if not check_parenthesis(x):
        return False, "parenthesis"
    
    valid, consec = check_consecutive_symbols(x)

    if not valid:
        return False, consec

    # if not check_consecutive_symbols(x):
    #     return False, "consec"
    
    return True, None

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

def is_term(x):
    for y in x:
        if y not in "S0+.v|()":
            return False
    
    return True

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
if __name__ == "__main__":
    input_string = "(v=vv)"

    a, b = is_statement(input_string, VALID_SYMBOLS)

    print(a, b)



