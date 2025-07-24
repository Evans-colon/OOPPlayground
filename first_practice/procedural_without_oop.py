accountName = 'Joe'
accountBalance = 10000
accountPassword = 'wet'



print()
print('press b to get balance')
print('press d to make deposit')
print('press w to make a withdrawal')
print('press s to show account')
print('press q to quit')
print()


action = input('what do you want to do?')
action = action.lower()
action = action[0]
print()


if action == 'b':
    print('Get balance')
    userPassword = input('enter your password')
    if userPassword != accountPassword:
        print('incorrect password')
    else:
        print('Your balance is', accountBalance)

elif action == 'd':
    print('Make a deposit')
    userDepositAmount = input('Please, enter amount to deposit')
    userDepositAmount = int(userDepositAmount)
    userPassword = input('Please enter password')
    if userDepositAmount < 0 :
        print('Invalid Amount')
    elif userPassword != accountPassword:
        print('Invalid password')
    else:
        accountBalance = accountBalance + userDepositAmount
        print('Your balance is', accountBalance)

elif action == 'w':
    print('Make a withdrawal')
    userAmountWithdraw = input('Please, enter amount to withdraw')
    userAmountWithdraw = int(userAmountWithdraw)
    userPassword = input('Please enter password')

    if userPassword != accountPassword:
        print('invalid password')
    elif userAmountWithdraw < 0:
        print('Invalid Amount')
    elif userAmountWithdraw > accountBalance:
        print('insufficient fund')
    else:
        accountBalance = accountBalance - userAmountWithdraw
        print('Your account balance is:', accountBalance)