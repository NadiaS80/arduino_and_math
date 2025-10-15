
import time
import requests
import logging
from arduinoUNO import green_light, red_light
from AI_HF import AI

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Calculate:

    def __init__(self, level):
        self.level = level

    def calc(self):
        while True:
            try:
                logging.info('Подбираю лучшие числовые комбинации...')
                self.ai = AI(level)
                neuro_response = self.ai._example()
                time.sleep(2)
                logging.info('Вычисляю ответ...')
                user_response = input(f'Пример: {neuro_response.split('|')[0]}\nОтвет: ')
                true_answer = float(neuro_response.split('|')[1].replace(' ', ''))
                if float(user_response) == true_answer:
                    logging.info(f'Верно!')
                    green_light()
                    return 1
                else:
                    logging.info(f'Ответ неверен!')
                    red_light()
                    while True:
                        user_choose = input('Что дальше?\n 1 - Я попробую решить заново\n 2 - Я хочу узнать ответ\n')
                        if user_choose == '1':
                            user_response = input(f'Пример: {neuro_response.split('|')[0]}\nОтвет: ')
                            if float(user_response) == true_answer:
                                green_light()
                                return 2
                            else:
                                logging.info(f'Ответ неверен!')
                                red_light()
                        elif user_choose == '2':
                            logging.info(f'Ответ на пример: {true_answer}. Удачи в следующих задачах!')
                            return 0
                        else:
                            logging.info(f'Неверная команда =(')
            except Exception as e:
                logging.error(f'Упс, ошибка: {e}')