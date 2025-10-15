from calculate import Calculate
import time
import logging


print('Привет! Я твой персональный тренер алгебры! Давай начнем качать левое полушарие!')
time.sleep(2)
while True:
     user_choose = input(
    'Выбери уровень сложности:\n'
    '   1 - Новичок в мате (формат 27 + 43)\n'
    '   2 - Студент-физтех (формат 236 + 528 или 432 - 123)\n'
    '   3 - Матемагистр (формат 14 * (23 - 5))\n'
    '   4 - Киборг алгебры (формат x + 234 / 12 - √49 = 25.5)\n'
    '   5 - Илон Маск математик (формат (log(1000, 10) + √144) * (x - 5) / 2^3 = 9.375)\n'
    '   6 - Я устал от чисел, для баланса Вселенной необходим перерыв\n'
)
     if int(user_choose) in range(1, 6):
         level = Calculate(int(user_choose))
         response = level.calc()
         if response == 1 and int(user_choose) < 5:
             logging.info('С первого раза решить пример! Давай повышать уровень!')
         elif response == 1 and int(user_choose) == 5:
             logging.info('С первого раза решить пример на максимальном уровне! Официально - ЗВАНИЕ КИБОРГ')
         elif response == 2:
             logging.info(f'Да, не с первого раза! Пару примеров уровня {user_choose} и алгебра будет бояться напора!')
         elif response == 0:
             logging.info(f'Не расстраивайся! Иногда числа могут играть в злые игры. Рекомендую несколько примеров уровня {int(user_choose) - 1} для закрепления и восстановления самооценки =)')
     elif int(user_choose) == 6:
         logging.info(f'Заходи ещё! Алгебры мало не бывает! =)')
         break
     else:
         logging.info(f'Неверно выбран раздел )')