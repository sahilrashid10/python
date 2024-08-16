import random
#### BASICS OF RANDOM FILE
# print(random.randint(1,2)) 
# rand_no_0_to_1 = random.random() *10 ## 10 exclusive
# print(rand_no_0_to_1)
# print(random.uniform(1,10)) #includes 10

#### COIN FLIP
# rint = random.randint(0,1)
# if rint == 0:
#    print("HEADS")
# else:
#    print("TAILS")

#### LISTS
# states_in_india = ["delhi","mumbai","kolkata"]
# states_in_india[0]="J&k"
# states_in_india.append("yoyoland")
# print(states_in_india[3])

#### Who will pay the bill
# friends = ["leo","ronny","luca","zeezu","sergio"]
# x = random.randint(0,4)
# print(f"{friends[x]} will pay the bill")
# print(random.choice(friends))

#### ROCK PAPER SCISSORS
rock = '''   
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

paper = '''     
---'    ____)_________
           ______)____)
          ______________)
         __________)
---.______________)'''

scissor = '''
   (_)  / )
     | (_/ 
    _+/  
   //|\
  // | )
 (/  |/      
'''
game=[rock,paper,scissor]
x= random.randint(0,2)
y = input("Enter R=Rock,P=Paper,3=Scissor")
temp = 'play'
while temp == 'play':
    if y=='R':
        y=rock
    if y=='P':
        y=paper
    if y=='S':
       y=scissor 
       print(f"BOT :{x}")
       print(f"YOU{y}")
    temp=input("press exit or play")



    
