import numpy as np

def game_core_v3(number: int=1) -> int:
    """Сначала выбираем случайное число, а потом, в зависимости от того 
    больше оно загаданного или меньше, меняем границу поиска нового
    случайного числа
        Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    a, b = 1, 101 # Определяем стратовые границы поиска от 1 до 100
    predict = np.random.randint(a, b) # Выбираем число

    while number != predict: # Выполняем цикл пока числа загаданное и случайное не совпадут
        count += 1
        if number > predict:
            a = predict + 1
        elif number < predict:
            b = predict
        predict = np.random.randint(a, b) # Выбираем случайное число в новых границах поиска
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(game_core_v3)