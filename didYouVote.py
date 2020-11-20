age = input('type your age')

if int(age) >= 18:
    print("cool! did you vote? Yes or No (case sensative) ")

if int(age) < 18:
    print("nevermind")
    

answer = input()
if answer == ('Yes'):
    print('nice, who did you vote for? Biden or Trump (case sensative)')

if answer == ('No'):
    print('ok')
    
president = input()


if president == ('Biden'):
    print("nice, you get a pat on the back")

if president == ("Trump"):
    print("nice, you get also get a pat on the back")

input('press enter to close')
