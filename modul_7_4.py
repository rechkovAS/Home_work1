team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 40
team1_time = 2552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = ( team1_time + team2_time ) / tasks_total
challenge_result = 'Победа команды Волшебники данных!'
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
# Использование %:
print('В команде Мастера кода участников: %(team1_num)s ! ' % {'team1_num': team1_num})
print('В команде Волшебники данных участников: %(team2_num)s ! ' % {'team2_num': team2_num})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !"
      % {'team1_num': team1_num, 'team2_num': team2_num})
# Использование format():
print('Команда Мастера кода решила задач: {} !'.format(score_1))
print('Мастера кода решили задачи за {} с !'.format(round(team1_time, 2)))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(round(team2_time, 2)))
# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!.")