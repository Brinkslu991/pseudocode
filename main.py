# Lucas Brinks
# 9/24/24
# psuedocode

#Average quiz score
name = input('Enter your name: ')
print(f'Welcome {name}')

quiz1 = int(input('Enter your first quiz score: '))
quiz2 = int(input('Enter your second quiz score: '))
quiz3 = int(input('Enter your third quiz score: '))

sum = quiz1 + quiz2 + quiz3

average = (sum/3)

print('Your quiz scores and average:')
print(quiz1)
print(quiz2)
print(quiz3)
print(average)

fname = input('Enter your name: ')
print(f'welcome {fname}')
miles = float(input('How many miles did you drive today: '))
gallons = float(input('How many gallon of gas did your car use: '))

mpg = (miles / gallons)

print(f'You drove {miles} miles')
print(f'You used {gallons} gallons')
print(f'You get {mpg} miles per gallon')