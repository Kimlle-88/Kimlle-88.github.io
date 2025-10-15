import random
while True:
 choice = input('Roll a dice?')
 if choice.lower() == 'y' or choice.lower() =='yes':
   d1 = random.radiant(1, 6)
   d2 = random.radiant(1, 6)
   print('f'({d1},{d2}))
elif choice.lower() =='n' or choice.lower() =='no':
    print('Thanks for playing')
    break
else:
    print('NO VALID')
restart = input('Want to start again')
if restart.lower() != 'y' and restart.lower() != 'yes':
  print('END')
  break


