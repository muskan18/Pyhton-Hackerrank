def swap_case(s):
    str =''

    for f in s:
        if f.isupper():
            str=str+f.lower()
        else:
            str=str+f.upper()    
    return str

