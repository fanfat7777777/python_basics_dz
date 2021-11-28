duration = 400153

if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    t_min = duration // 60
    t_sec = duration - 60 * t_min
    print(f'{t_min} мин {t_sec} сек')
elif duration < 86400:
    t_hour = duration // 3600
    sec = duration - 3600 * t_hour
    t_min = sec // 60
    t_sec = sec - t_min * 60
    print(f'{t_hour} ч {t_min} мин {t_sec} сек')
else:
    t_day = duration // 86400
    t_hour = (duration - t_day * 86400) // 3600
    sec = duration - t_day * 86400 - t_hour * 3600
    t_min = sec // 60
    t_sec = sec - t_min * 60
    print(f'{t_day} дн {t_hour} ч {t_min} мин {t_sec} сек')