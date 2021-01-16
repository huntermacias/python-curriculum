
#key:value, key:value, key:value

#username:highscore
game_scores = {"python32":108, "java102":98, "C#":102, "C++":107}
username = []
highscores = []

for user in game_scores: 
	username.append(user)
	highscores.append(game_scores[user])

print(game_scores)
print("users: ", username)
print("high scores:", highscores)

#this gets every item in your dictionary
for x in game_scores.items():
	print(x)

#this only gets the keys in your dictionary
for x in game_scores.keys():
	print(x)

#this only gets the vals in your dictionary
for x in game_scores.values():
	print(x)