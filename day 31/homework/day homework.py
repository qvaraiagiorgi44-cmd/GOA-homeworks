favorite_games = ["fc 25", "minecraft", "ufc 5"]
print("ჩემს სიაშია", len(favorite_games), "ელემენტი")


games = ["Minecraft", "GTA V", "Fortnite"]
games.append("Valorant")
print(games)


games1 = ["ufc 5", "fc 26"]
games1.insert(0, "minecraft")
print (games1)


favorite_games1 = ["minecraft", "ufc 5", "fc 25"]
removed_game = favorite_games.pop()
print("deleted game:", removed_game)
print("last list:", favorite_games)



fruits = ["apple", 93, "bannana", 23, "mango", True, 15, False, 3.1, "Hello World!"]
res = []
for item in fruits:
    if type(item) == int:
        res.append(item)
print(res)



words = ["cat", "elephant", "dog", "hippopotamus", "ox", "python", "a"]
res = []
for word in words:
    if len(word) > 4:
        res.append(word)
print(res)                                                                                                                                                                                                  