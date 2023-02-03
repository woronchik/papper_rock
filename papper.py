import random

defeated_by = {
    "камень": ["ножницы", "ящерица"],
    "ножницы": ["ящерица", "бумага"],
    "бумага": ["камень", "спок"],
    "ящерица": ["спок", "бумага"],
    "спок": ["ножницы", "камень"]


}

all_elements = list(defeated_by.keys())

raunds_count = int(input("Введите количество раундов: "))
counter = 1

user_wins = 0
computer_wins = 0
nobody_wins = 0

while counter <= raunds_count:
    print(f"Раунд {counter}")
    while True:
        user_choice = input("Выберите элемент (камень, ножницы, бумага, ящерица или спок): ")
        if user_choice in all_elements:
            break

    computer_choice = random.choice(all_elements)
    print(f"Выбор компьтера: {computer_choice}")
    if computer_choice in defeated_by[user_choice]:
        print("В этом раунде победили вы!")
        user_wins += 1
    elif computer_choice == user_choice:
        print("Ничья!")
        nobody_wins += 1
    else:
        print("Победил компьютер!")
        computer_wins += 1
    counter += 1

print(f"Игрок победил {user_wins} раз, компьютер победил {computer_wins} раз, ничья {nobody_wins} раз")









