#program-7: input card is lucky or not

lucky1 ='king of clubs'
lucky2 ='queen of diamonds' 
lucky3 = 'ace of spades'
lucky4 = '10 of hearts'


card = input("Enter your card:")

new_card=card.split()
# print(card)
# print(new_card)
# print(new_card[0])
# print(new_card[2])

if(new_card[0]=='king' and new_card[2]=='clubs' or new_card[0]=='queen' and new_card[2]=='diamonds' or new_card[0]=='ace' and new_card[2]=='spades' or new_card[0]=='10' and new_card[2]=='hearts'):
    print("*********************************************************************")
    print("You choose lucky card")
    print("*********************************************************************")
else:
    print("*********************************************************************")
    print('You choose not lucky card')
    print("*********************************************************************")