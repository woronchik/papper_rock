from random import randint, shuffle, choice

players = []
marbles = []

print("""Добро пожаловать в игру “Русская рулетка”!
Правила игры: Из мешка с пятью зелеными шариками и одним
белым каждый игрок по очереди достает по одному шарику.
Если достался зеленый шарик - игра идет дальше, если кому-нибудь
из игроков достался белый, то игра заканчивается.
Удачи!""")

marbles_count = int(input("Введите количество шаров: "))

for i in range(marbles_count):
    marbles.append("green")

to_white = randint(0, (len(marbles)-1))
marbles[to_white] = "white"

while marbles_count > 1:
    to_red = randint(0, (len(marbles)-1))
    if to_red == to_white:
        continue
    else:
        marbles[to_red] = "red"
        break

shuffle(marbles)

while True:
    players_counter = int(input("Введите количество игроков: "))
    if players_counter > 3 or players_counter <= 0:
        continue
    else:
        break

for i in range(players_counter):
    players.append(input(f"Введите имя игрока №{i+1}: "))

taken = 0
current_player = 0

while taken < 6:
    if current_player == len(players):
        if len(players) == 0:
            print("Игроков больше нет! Конец игры.")
            break
        current_player = 0

    print(f"Очередь игрока №{current_player+1} с именем {players[current_player]}")
    input("Нажми Enter, чтобы достать шарик...")
    chosen_marble = choice(marbles)
    marbles.remove(chosen_marble)
    if chosen_marble == "white":
        print("Белый шарик!")
        print(f"Игрок под именем {players[current_player]} проиграл")
        print("Игра закончена")
        break
    elif chosen_marble == "red":
        print("Красный шарик!")
        print(f"Игрок под именем {players[current_player]} выбывает")
        players.pop(current_player) # [1, 2, 3]
        print("Ход переходит к следующему игроку")
        current_player -= 1
    else:
        print("Всё хорошо. Попался зелёный шарик")
        print("Ход переходит к следующему игроку")
    current_player += 1
    taken += 1






