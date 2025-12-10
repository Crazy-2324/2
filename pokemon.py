import random
c_attacks = ["Flamethrower", "Dragon Claw", "Ember", "Fire Spin"]
c_attacks_dmg = [90, 80, 40, 35]
c_health = 100
p_attack = ["Thunder Shock", "Quick Attack", "Electro Ball", "Thunderbolt","Run"] 
p_attacks_dmg = [40, 50, 60, 90]
p_health = 100
print("A wild charizard appeared!")
game_over = False
while not game_over:
    print("\nChoose your attack:")
    for i, attack in enumerate(p_attack):
        print(f"{i + 1}. {attack}")
    choice = input("Enter the number of your attack: ")
    if choice.isdigit() and 1 <= int(choice) <= len(p_attack):
        choice = int(choice) - 1
        if p_attack[choice] == "Run":
            print("You ran away safely!")
            game_over = True
            continue
        damage = p_attacks_dmg[choice]
        c_health -= damage
        print(f"You used {p_attack[choice]} and dealt {damage} damage!")
        if c_health <= 0:
            print("Charizard fainted! You win!")
            game_over = True
            continue
        c_choice = random.randint(0, len(c_attacks) - 1)
        c_damage = c_attacks_dmg[c_choice]
        p_health -= c_damage
        print(f"Charizard used {c_attacks[c_choice]} and dealt {c_damage} damage!")
        print(f"Your health: {p_health}, Charizard's health: {c_health}")
        if p_health <= 0:
            print("You fainted! Game over!")
            game_over = True
    else:
        print("Invalid choice. Please try again.")
