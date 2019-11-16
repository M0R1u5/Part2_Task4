hours1 = int(input('Enter the first hours: '))
minutes1 = int(input('Enter 1st minutes: '))
seconds1 = int(input('Enter 1st seconds: '))
hours2 = int(input('Enter the second hours: '))
minutes2 = int(input('Enter 2nd minutes: '))
seconds2 = int(input('Enter 2nd seconds: '))

print(((hours2-hours1)*3600)+((minutes2-minutes1)*60)+(seconds2-seconds1))