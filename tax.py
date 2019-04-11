# !/usr/bin/env python

def calc_mpf(income):
    if income < 85200:
        mpf = 0
    elif 85200 <= income < 360000:
        mpf = (income * 0.05) * 12
    else:
        mpf = 1500 * 12
    return mpf


def inputs(strs):
    while True:
        s = str(input(strs))
        if s.isdigit():
            break
        else:
            print('Please enter NUMBER format !')
    return s


def get_learn_input():
    learn = int(inputs('Please enter your Self Education Expenses: '))
    if learn < 0 or learn > 100000:
        print("The maximum tax-free of Self Education Expenses is $100,000.")
        return get_learn_input()
    return learn


def get_donation_input():
    donation = int(inputs('Please enter your Approved Charitable Donations: '))
    if donation < 0:
        print("The value must be equal or bigger than 0.")
        return get_donation_input()
    return donation


def get_loan_input():
    loan = int(inputs('Please enter your Home Loan Interest: '))
    if loan < 0 or loan > 100000:
        print("The maximum tax-free of Home Loan Interest is $100,000.")
        return get_loan_input()
    return loan


def get_support_input():
    support = int(inputs('Number of elderly resided in residential care home: '))
    if support < 0 or support > 4:
        print("The maximum number of elderly resided in residential care home is 4.")
        return get_support_input()
    return support


def get_children_input():
    children = int(inputs('Number of dependent children: '))
    if children < 0:
        print("The number of dependent children must be equal or bigger than 0.")
        return get_children_input()
    return children


while True:
    str_input = inputs("What is your marital status? 1 = Single / 2 = Married");
    if str_input == '1':
        income = int(inputs("What is your annual income: "))


        learn = get_learn_input()
        donation = get_donation_input()
        loan = get_loan_input()
        support = get_support_input()
        children = get_children_input()
        mpf = calc_mpf(income)
        tax = (income - mpf) * 0.15
        print("MPF paid this year: ${}".format(mpf))
        if income < 132000:
            print('You do not need to pay tax')
        else:
            print('You have to pay: $', tax, 'for the tax')

    elif str_input == '2':
        income1 = int(inputs("What is your annual income: "))
        income2 = int(inputs("What is your partner's annual income: "))
        learn = get_learn_input()
        donation = get_donation_input()
        loan = get_loan_input()
        support = get_support_input()
        children = get_children_input()

        # Cal mpf
        mpf1 = calc_mpf(income1)
        mpf2 = calc_mpf(income2)

        # Com tax
        comincome = ((income1 - mpf1) + (income2 - mpf2))
        comtax = comincome * 0.15

        # Sp tax
        selftax = (income1 - mpf1) * 0.15
        if income1 < 132000:
            selftax = 0
        else:
            selftax = selftax
        othertax = (income2 - mpf2) * 0.15
        if income2 < 132000:
            othertax = 0
        else:
            othertax = othertax
        sptax = selftax + othertax

        # Output
        print("MPF paid this year by you: {}".format(mpf1))
        print("MPF paid this year by your partner: {}".format(mpf2))

        print('In sperate tax:')
        if income1 < 132000:
            print('You do not have to pay the tax')
        else:
            print('You have to pay: $', selftax, 'for the tax')
        if income2 < 132000:
            print('Your partner do not have to pay the tax')
        else:
            print('You partner have to pay: $', othertax, 'for the tax')
        if sptax < 1:
            print('You and your partner do not have to pay the tax')
        else:
            print('You and your partner have to pay: $', sptax, 'for the tax')

        print('In combine tax:')
        if comincome < 264000:
            print('You and your partner do not have to pay the tax')
        else:
            print('You and your partner have to pay: $', comtax, ' for the tax')

        if comtax >= sptax:
            print("It is RECOMMEND paying tax by using seperate tax method.".format(sptax))
        else:
            print("It is RECOMMEND paying tax by using combine tax method".format(comtax))

    else:
        print('Input error, please input again!')
