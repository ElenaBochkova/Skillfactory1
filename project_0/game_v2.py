"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def more_predict(number: int = 1) -> int:
    """Угадываем число при помощи подсказок, больше оно или меньше названного

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    less_boundary = 0  #нижняя граница для угадывания
    more_boundary = 101  #верхняя граница для угадывания
        
    while True:
        count += 1
        predict_number = np.random.randint(less_boundary, more_boundary)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            less_boundary = predict_number # нижняя граница, если число больше
        else:
            more_boundary = predict_number #верхняя граница, если число меньше
    return count


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    print("Случайный алгоритм:")
    score_game(random_predict)
    print("Алгоритм со сдвижением границ")
    score_game(more_predict)
