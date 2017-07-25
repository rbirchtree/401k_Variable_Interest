contribution = int(raw_input("How much do you want to contribute to your 401k per a year?"))
# money contributed to 401k
waxBall = int(raw_input("What is your 401k worth now?"))
# sum of all contribution plus interest of every year
time= int(raw_input("How many years from now do you want to withdraw on it?"))
# time in years
print "How much do you think you can earn on your investments in 3 different years? Please type in decimal format...i.e .3" 
x = float(raw_input())
y = float(raw_input())
z = float(raw_input())
interest_rate = [x,y,z]
#average return rate randomized
#fix variable names
from random import choice
import locale
locale.setlocale( locale.LC_ALL, '')
'English_United States.1252'
choice(interest_rate)
for x in range (0,time):
    wax_ball= contribution+(waxBall*(1+choice(interest_rate)))
print locale.currency(waxBall)

if waxBall > 2000000:
	print "Great saving"
elif waxBall < 2000000:
	print "Save more, spend less and/or earn more."
