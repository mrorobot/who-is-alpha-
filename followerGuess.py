import random
from game_data import data
from art import logo_higher_lower
from art import vs
print(logo_higher_lower)

i=0
play_agian=True
while play_agian:
  game_on=True
  while game_on:
    data1=random.choice(data)
    data2=random.choice(data)
    print(f"Compare A: {data1['name']} , a {data1['description']}, from{data1['country']} ")
    print(vs)
    print(f"Against B: {data2['name']} , a {data2['description']}, from{data2['country']} ")
    answer1=data1["follower_count"]
    answer2=data2["follower_count"]
    
    if answer1>answer2:
      real_ans=answer1
    else:
      real_ans=answer2
    guess=input("who has more followers,'A' or 'B'").lower
    if guess =="a":
      guess=answer1
    else:
      guess=answer2
    if guess==real_ans:
      print("you are right")
      i=i+1
      print(f"your score is {i}")
    else:
      print("Wrong answer, you lose all your progress")
      game_on=False
      continue
  play_on=input("do you want to play again,'y' or 'n'").lower()
  if play_on=="n":
    print("Thank you")
    play_agian=False
  elif not play_on=="y":
    print("enter valid input")
  else:
    play_agian=True
