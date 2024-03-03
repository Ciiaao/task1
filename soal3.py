while 1 :
    print('enter the operation(sum,difference,multiple,divide\nenter EX to stop): ')

    operation=input()
    if operation=='EX':
        break
    print('enter numbers: ')
    a=input()
    b=input()
    try:
       a=int(a)
    except ValueError:
      a=float(a)

    try:
      b=int(b)
    except ValueError:
      b=float(b)

    if operation=='sum':
       print(float(a+b))
    if operation=='difference':
        print(float(a-b))
    if operation=='multiple':
        print(float(a*b))
    if operation=='divide':
        if b==0 :
            print('can not divide by zero')
        else:
            print(float(a/b))
    