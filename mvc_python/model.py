class Battle:
 ask=raw_input("Do you want to give challenge? y/n: ")
 if(ask == 'y'):
    life = int(raw_input("Take a life betn 2 to 5: "))
 else:
    print("Take your time");
    exit()
 def attack(self):
    print('you are being attacked')
    self.life -= 1

 def checklife(self):
   if self.life <= 0:
       print('Now you are dead and out of game. Come back later')
   else:
       return self.life
