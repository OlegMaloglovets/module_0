import numpy as np


def game_core(number):
    range_low = 1
    range_hi = 100
    predict = (range_hi-range_low)//2
    count = 1
    while predict != number:
        count += 1
        if predict > number:
            range_hi = predict - 1
        elif predict < number:
            range_low = predict + 1
        predict = (range_hi-range_low)//2 + range_low
    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core)
