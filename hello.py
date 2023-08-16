print ("Welcome to the kingdom of meaye")
print ("Lets see how your life will be\n")
import random



attributes = {
  "friends": 0,
  "strength": 0,
  "intellect": 0,
  "magic": 0,
  "age": 0,
  }

def update_character(attr, value):
  if attr in attributes:
    attributes[attr] += value

random_number = random.randint(0,10)

if random_number <= 7:
  print("You were born a commoner")
  birth = 1
elif random_number<= 9:
  print("You were born to noble family")
  birth = 2
else:
  print("You were born a royal heir")
  birth = 3

if birth == 1:
  random_number = random.randint(1,3)
  power = random_number

if birth == 1 and power == 1:
  print("You were born in the land of soil. You have the power to manipulate earth.\n")
  update_character("age", 1)
if birth == 1 and power == 2:
  print("You were born in the land of sky. You have the power to manipulate air and clouds.\n")
  update_character("age", 1)
if birth == 1 and power == 3:
  print("You were born in the land of sea. You have the power to manipulate water and breathe in bodies of water.\n")
  update_character("age", 1)
if birth == 1 and attributes["age"] == 0:
  print("Your were born in the same year as the new royal heir. One day you will see him rise to power and learn to survive under any new laws that may be imposed. A simple life as a commoner isnt all bad. You are sure to be very sucessful in life.\n")
  update_character("age", 1)

if birth == 1 and attributes["age"] == 1:
  print("""
  1. Walk
  2. Talk
  3. Magic """)
  ans=input("You are now one year old. What will you do today?")
  if ans=="1":
    print("You took your first steps and your parents look at you in awe")
    update_character("strength", 1)
    update_character("age", 1)
  elif ans=="2":
    print("You began speaking in broken sentences. Your parents listen to every word")
    update_character("intellect", 1)
    update_character("age", 1)
  elif ans=='3' and power == 1:
    print("You used your magic and caused a large rock to bust a hole in the wall. Your parents can't help but laugh")
    update_character("magic", 1)
    update_character("age", 1)
  elif ans=='3' and power == 2:
    print("You used your magic and flew around the house causing your parents to chase u down for hours.")
    update_character("magic", 1)
    update_character("age", 1)
  elif ans=='3' and power == 3:
    print("You used your magic and whirlpool which sucked up all your blocks")
    update_character("magic", 1)
    update_character("age", 1)
  else:
    print("Not a valid answer")

if birth == 1 and attributes["age"] == 2:
  print(""" 
  1. Slide
  2. Swings
  3. Monkey bars""")
  ans=input("You are now 2 years old. Your parents took your to the playground. What will you play on.")
  if ans == '1':
   print("You fly off the slide and end up catching yourself using your powers. Luckily you are not hurt")
   update_character("magic", 1)
   update_character("age", 1)
  if ans == '2':
    print("You swing on the swings and start have a small chat with a little girl next to you. You seem to have made a new friend")
    update_character("friends", 1)
    update_character("intellect", 1)
    update_character("age", 1)
  if ans == '3':
    print("You play on the monkey bars for hours. Your parents are amazed at how much energy you have")
    update_character("strength", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] ==3:
  print("""
  1. Go and explore the shops
  2. Go into a resturant
  3. Go into the capitol gardens""")
  ans=input("You are now 3 years old you parents have taken your into the capitol. What will you do?")
  if ans == '1':
    print("Your parents take you around the shops and you are able to convince them to buy you the new popular toys")
    update_character("intellect", 1)
    update_character("age", 1)
  if ans == '2':
    print("You eat a delicious meal with your family at a fancy establishment. You leave feeling full and content")
    update_character("strength", 1)
    update_character("age", 1)
  if ans == '3':
    print("You drag your parents into the capitol gardens. They are full of strange magical plants. One of them sprays a strange miss on you causing you to giggle hysterically.")
    update_character("magic", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 4:
  print("""
  1. Pick out a library book
  2. Play in the play section
  3. Talk to a librarian """)
  ans=input("You are now 4 years old. Your parents take you to the library hoping to prepare you for school.")
  if ans == '1':
    print("You pick out a book and your parents try to teach you some of the letters and sounds. You are absolutely enthralled by the world of stories and your parents are very impressed at how fast you learn.")
    update_character("intellect", 1)
    update_character("age", 1)
  if ans == '2':
    print("You head over to the play section and spend the day playing with a little boy you ran into. It seems you have made a new friend.")
    update_character("strength", 1)
    update_character("friends", 1)
    update_character("age", 1)
  if ans == '3':
    print("You talked to the librarian where she told you about different types of magical crystals and how they can be used to do any type of magic you wished.")
    update_character("magic", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 5:
  print("""
  1. Fight back
  2. Try to find someone to help
  3. Insult them""")
  ans=input("You are now 5 years old and have been confronted on your first day by a group of bullies. They call you mean names and threaten to beat you up. What will your do?")
  if ans == '1' and attributes["strength"] >= 1:
    print("You beat up the bullies and made them run away crying!")
    update_character("age", 1)
  elif ans == '1' and attributes["magic"] >= 1: 
    print("You overwealmed them with your magical talents and made them run away crying!")
    update_character("age", 1)
  elif ans == '2' and attributes["friends"] >= 1:
    print("A child at school recognizes u and comes to your aid! They make the bullies go away and protect you throughout the school day")
    update_character("age", 1)
  elif ans == '3' and attributes["intellect"] >= 1:
    print("You insult each of them damaging their egos so severely they back off!")
    update_character("age", 1)
  else:
    print("Despite your best attempts the bully beat you up and laugh at you. You run away and leave the kindergarten and get kidnapped by a mysterious stranger... The end.")

if birth == 1 and attributes["age"] == 6:
  print("""
  1. Answer as many of the teachers questions that you can
  2. Use magic to play a prank on the teacher
  3. Go to use the bathroom and head outside to skip class """)
  ans=input("You are now six years old, and are sitting in the classroom what will you do.")
  if ans=="1":
    print("The teacher is very impressed with your knowledge and the class looks at you in admiration.")
    update_character("intellect", 1)
    update_character("age", 1)
  elif ans=="2":
    print("Your teacher look at you dissapointed and send you to the principal office, but all your classmates are quite impressed.")
    update_character("magic", 1)
    update_character("age", 1)
  elif ans=='3':
    print("You head to the bathroom before taking a sharp turn and sneaking out of the school building. You play on the playground until you are caught when recess time does come.")
    update_character("stregnth", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 7:
  print("""
  1. Go over and talk to them
  2. Proceed with the game
  3. Show them a magic trick to cheeer them up """)
  ans=input("You are now 7 years old. You are playing tag with the class and there is a child sitting alone in the corner. What will you do")
  if ans=="1":
    print("You go over and try to talk to them but the other children discourage you saying that the child is weird and creepy. You push them aside and go over to talk with them. They seem a bit cold and distant and dont open up much... but at least your tried.")
    update_character("intellect", 1)
    update_character("age", 1)
  elif ans=="2":
    print("You ignore the child and continue playing having a blast with the other children. You forget about the strange child after a while")
    update_character("strength", 1)
    update_character("age", 1)
  elif ans=='3':
    print("You used your magic to attempt to cheer them up and they smile at you. You begin to talk as you show them more of your magic and they open up to you. It seems the class has been shunning them for not being able to use magic yet themselves. You seem to hve made a new friend")
    update_character("magic", 1)
    update_character("friends", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 8:
  print("""
  1. Be polite with the neighboors and show off how well behaved you are.
  2. Help your neighboor in the kitchen and do some cooking.
  3. Play out in the neighboors garden. """)
  ans=input("Your are now 8 years old? You parents have taken you over to a neighboors house. What will you do?")
  if ans=="1":
    print("Your neighboors are impressed at how well behaved and how well spoken you are. Your parents are proud and take you to get ice-cream later!")
    update_character("intellect", 1)
    update_character("age", 1)
  elif ans=="2":
    print("You see you neighbor seeming stressed trying to get the midday meal together. You decide to help out and they praise you on what a strong and helpful little one you are.")
    update_character("strength", 1)
    update_character("age", 1)
  elif ans=='3':
    print("You decide to leave the grown ups alone and go and play in the garden. They have some singing plants that serenade you until its time to go.")
    update_character("magic", 1)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 9:
  print("""
  1. Sneak into the palace.
  2. Grab some glowing stones.
  3. Talk with the knights. """)
  ans=input("You are now 9 years old. Your parents take you into the capitol. You are right outside of the palace what will you do.")
  if ans=="1":
    print("You snuck into the palace and somehow managed to avoid notice of the guard by crawling through a small crack in the wall. You meet a young boy who introduces himself as the prince. You have a pleasant chat before hearing some grown up coming this way and are quicky rushed out before you get caught.")
    update_character("intellect", 5)
    update_character("friends", 1)
    update_character("age", 1)
  elif ans=="2":
    print("You grab some magical glowing stones. You feel a surge of energy course through your body and decide to keep them in your pocket for now")
    update_character("magic", 5)
    update_character("age", 1)
  elif ans=='3':
    print("The knights told you all about their careers and what it means to be a defender of the kingdom and the royal family. You feel yourself become inspired and start contemplating going to school to become a knight. You go home and train vigorously.")
    update_character("strength", 5)
    update_character("age", 1)

if birth == 1 and attributes["age"] == 10:
  print("""
  1. Take classes that value intellegence and critical thinking skills.
  2. Take classes that prioritize physical strength and power.
  3. Take classes that prioritize magical knwoledge and skill. """)
  ans=input("You are now 10 years old and in the Meaye school system this means the second stage of schooling has begun. You will be introduced to new career paths and explore new choices. What will you do today!")
  if ans=="1" and attributes["intellect"] >= 2:
    print("You dive head first into your studies loving the path you have choosen. These next few years will be a breeze.")
    update_character("age", 1)
  elif ans == '1' and attributes["friends"] >= 1:
    print("You struggled a bit at first but luckily your friends helped you study and you feel confident in your selection.")
  elif ans=="2" and attributes["strength"] >= 2 :
    print("You physical performance is incredible and you find yourself top of your class. You teachers encourage you down this path and suggest doing work for the royal family in your future.")
    update_character("age", 1)
  elif ans=='3' and attributes["magic"] >= 2: 
    print("You find you are immensly gifted when it comes to magic and your teachers suggest a career as part of the council. You are met with lots of encouragement. These next few years will be amazing.")
    update_character("age", 1)
  else: 
    print("You cant seem to get a handle of the path you have choosen. You end up dropping out in the first year and running away to work on a farm... The end.")






