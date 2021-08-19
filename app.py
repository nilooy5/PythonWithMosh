from EmojiConverter import emoji_converter
from GreetUser import greet_user
from Classes import Point, Person
from TryExcept import age_risk
from CarGame import car_game

#car_game()
# age_risk()

def find_max(*argv):
  return max(*argv)

max = find_max(2, 4, 8, 3, 1, 33, 25, 65)

print('Maximum value is ' + str(max))

greet_user("Fazal Mahmud", "Niloy")
greet_user("Munira", "Tabassum")
emoji_converter("hello bros :) how are you :( sad? :D")

point1 = Point(15, 10)
niloy = Person("Niloy")
niloy.talk("haga ashche")