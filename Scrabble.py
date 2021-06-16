letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters,points)}

#print(letter_to_points)
letter_to_points[" "] = 0

# This function calculates the number of points scored for a word
def score_word(word):
  point_total = 0
  for alphabet in word:
    point_total += letter_to_points[alphabet.upper()]
  return point_total

print(score_word('BROWNIE'))

player_to_words = {'player1':['BLUE','TENNIS','EXIT'],'wordNerd':['EARTH','EYES','MACHINE'],'Lexi':['ERASER','BELLY','HUSKY'],'Prof':['ZAP','COMA','PERIOD']}
player_to_points ={}

for player in player_to_words.keys():
  point = 0
  for word in player_to_words[player]:
    point += score_word(word)
    player_to_points[player] = point

print(player_to_points)

# This function would take in a player and a word, and add that word to the list of words they’ve played.
def play_word(player,word):
    player_to_words[player].append(word)

# This function would turn your nested loops into a function that you can call any time a word is played.
def update_point_totals(player,word):
  play_word(player,word)
  for player in player_to_words.keys():
    point = 0
    for word in player_to_words[player]:
      point += score_word(word)
      player_to_points[player] = point

#update_point_totals('player1','boba')
#print(player_to_points)