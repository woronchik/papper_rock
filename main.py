#Два ученика делают домашнее задание. Они договорились, что оба сделают по половине задач, а затем спишут друг у друга.
# Но они забыли договориться, какие номера задач они будут делать. Узнайте, сколько задач им ещё предстоит сделать.
# Даны количество всех задач, список задач, которые сделал первый ученик, и список задач, которые сделал второй ученик.

questions = 8
first_student = {2, 3, 6, 7}
second_student = {1, 6, 7, 8}
answer = first_student | second_student
left_to_decide = []
for i in range(1, questions):
    if i not in answer:
        left_to_decide.append(i)
print(list(left_to_decide))






















