# Задание 15. Калькулятор времени

total_seconds = float(input('Bвeдитe количество секунд: '))

hours = (total_seconds // 3600) % 24  # Получить количество часов.
minutes = (total_seconds // 60) % 60  # Получить количество оставшихся минут.
seconds = total_seconds % 60  # Получить количество оставшихся секунд.
days = ((total_seconds // 3600) // 24) % 365
years = (((total_seconds // 3600) // 24) // 365)

if total_seconds <= 60:
    print("В введенном количестве секунд содержится:\nминут:", int(minutes), "\nсекунд:", int(seconds))
elif total_seconds > 60 and total_seconds <= 3600:
    print("В введенном количестве секунд содержится: \nчасов:", int(hours), "\nминут:", int(minutes), "\nсекунд:",
          int(seconds))
elif total_seconds > 3600 and total_seconds <= 86400:
    print("В введенном количестве секунд содержится: \n\
дней:", int(days), "\nчасов:", int(hours), "\nминут:", int(minutes), "\nсекунд:", int(seconds))
elif total_seconds > 86400:
    print("В введенном количестве секунд содержится: \n\
годы:", int(years), "\nдней:", int(days), "\nчасов:", int(hours), "\nминут:", int(minutes), "\nсекунд:", int(seconds))
