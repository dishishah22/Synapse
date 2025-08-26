from itertools import combinations

Pokedox = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
 "Lugia": ("Psychic", "Flying", "Water"),
 "Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}

def strongest_team(pokedox,k):
    max_type=0
    best_team=None

    for team in combinations(pokedox.keys(),k):
        unique_data=set()
        for names in team:
            unique_data.update(pokedox[names])

        if len(unique_data)>max_type:
            max_type=len(unique_data)
            best_team=(team,unique_data)

    return best_team,max_type


best_team, max_type = strongest_team(Pokedox,3)
print("Name of Strongest Team : ",best_team[0])
print("Their Types : ",best_team[1])
print("Number of counts ",max_type)
