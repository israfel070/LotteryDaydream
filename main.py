cashvalue = 0
taxpayment = 0


cashvalue = int(input('Welcome to Lottery Daydream! Enter the Cash Option value of the upcoming lottery:'))


def bracketone():
    global taxpayment
    taxpayment = (cashvalue) * .1

def brackettwo():
    global taxpayment
    taxpayment = (995 + ((cashvalue-9950)*.12))

def bracketthree():
    global taxpayment
    taxpayment = (4664 + ((cashvalue - 40525)*.22))

def bracketfour():
    global taxpayment
    taxpayment = (14751 + ((cashvalue - 86275) * .24))

def bracketfive():
    global taxpayment
    taxpayment = (33603 + ((cashvalue - 164925) * .32))

def bracketsix():
    global taxpayment
    taxpayment = (47843 + ((cashvalue - 209425) * .35))

def bracketseven():
    global taxpayment
    taxpayment = (157804 + ((cashvalue - 523600) * .37))


def bracketcrunch():
    if cashvalue <= 9950:
        bracketone()
    if cashvalue > 9950 and cashvalue <= 40525:
        brackettwo()
    if cashvalue > 40525 and cashvalue <= 86375:
        bracketthree()
    if cashvalue > 86375 and cashvalue <= 164925:
        bracketfour()
    if cashvalue > 164925 and cashvalue <= 209425:
        bracketfive()
    if cashvalue > 209425 and cashvalue <= 523600:
        bracketsix()
    if cashvalue > 523600:
        bracketseven()

bracketcrunch()
effectiverate = taxpayment / cashvalue

print('Your 2021 federal income taxes owed will be ' + '${:,.2f}'.format(taxpayment))
print('Your take-home amount will be ' + '${:,.2f}'.format(cashvalue-taxpayment))
print('Your effective tax rate will be ' + '{:.2%}'.format(effectiverate))