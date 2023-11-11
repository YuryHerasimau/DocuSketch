import psutil
import requests


# Задаем пороговое значение потребления памяти (в %), при котором будет срабатывать тревога
memory_threshold = 80


def check_memory_usage():
    """Скрипт контролирует потребление памяти и генерирует alarm путем отправки http запроса на API"""

    # Получаем информацию о текущем использовании памяти
    memory_usage = psutil.virtual_memory().percent

    # Проверяем, превышает ли использование памяти пороговое значение
    if memory_usage > memory_threshold:
        # Отправляем HTTP-запрос на API для генерации тревоги
        api_url = "http://127.0.0.1:8080/api/key/name"
        response = requests.get(api_url)

        if response.status_code == 200:
            print(
                f"Тревога успешно сгенерирована!\nТекущее использование памяти: {memory_usage} > {memory_threshold} %"
            )

        else:
            print(
                f"Произошла ошибка при отправке запроса на API {api_url}. Статус-код: {response.status_code}"
            )

    else:
        print(
            f"Использование памяти находится в пределах допустимых значений: {memory_usage} < {memory_threshold} %"
        )


# Вызываем функцию для проверки использования памяти
check_memory_usage()
