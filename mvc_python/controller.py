from model import Battle
class control:
 enemy1=Battle()
 enemy1.attack()
 print "you have "+str(enemy1.checklife())+" life left";
 inp = raw_input("Do you want a shield? y/n: ")
 while(enemy1.checklife() >= 0):
      if(inp != 'y'):
        enemy1.attack()
        print "you have "+str(enemy1.checklife())+" life left";
        inp = raw_input("Do you want a shield? y/n: ");
      else:
        print "You are under protection. Get prepared for battle";
        break
