while 1 :
    print('enter the current temp type:(F or C and EX to stop) ')
    a=input()
    if a=='EX':
        break
    if a=='C':
        print('enter the temp number: ')
        b=input()
        try:
            b=int(b)
        except ValueError:
            b=float(b)
        result=b*1.8+32
        print('the temp in fahrenheit is ',result)
    elif a=='F':
        print('enter the temp number: ')
        b=input()
        try:
           b=int(b)
        except ValueError:
            b=float(b)
        result=(b-32)/1.8
        print('the temp in celsius is ',result)
    else:
        print('invalid character!')