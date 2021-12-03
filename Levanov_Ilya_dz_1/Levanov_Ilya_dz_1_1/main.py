duration = 3600

t_day = duration // 86400
t_hour = (duration - t_day * 86400) // 3600
sec = duration - t_day * 86400 - t_hour * 3600
t_min = sec // 60
t_sec = sec - t_min * 60

print(f'{t_day} дн {t_hour} ч {t_min} мин {t_sec} сек')

#Упрощение кода на основании увиденного в выполненных дз