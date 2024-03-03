account={'main_account':0}
while 1:
    print('what do you want to do with your account(show credit,add money or withdraw,EX to stop): ')
    account_operation=input()
    if account_operation=="EX":
        break
    if account_operation=='show credit':
        print(account['main_account'])
    elif account_operation=='add money':
        print('enter amount of money you want to add: ')
        added_amount=input()
        try:
            added_amount=int(added_amount)
        except ValueError:
            added_amount=float(added_amount)
        account["main_account"]=account['main_account']+added_amount
        print('done!')
    elif  account_operation=='withdraw':
        print('enter the amount you want to withdraw: ')
        withdrew_amount=input()
        try:
            withdrew_amount=int(withdrew_amount)
        except ValueError:
            withdrew_amount=float(withdrew_amount)
        if account['main_account']<withdrew_amount:
            print('you can not withdraw this amount of money!')
        else:
            account['main_account']=account['main_account']-withdrew_amount
            print('done!')
    else:
        print('invalid operation!')

