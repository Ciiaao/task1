while 1:
    print('enter your input: ')
    input_str=input()
    try:
        input_str=int(input_str)
    except ValueError :
        try:
            input_str=float(input_str)
        except ValueError:
            if input_str[0]=='['and x[-1]==']':
                input_str=list(input_str)
    print(type(input_str))