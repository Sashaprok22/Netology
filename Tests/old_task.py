def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    for visit in list(geo_logs):
        if "Россия" not in list(visit.values())[0]:
            geo_logs.remove(visit)

    return geo_logs


def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    result = []

    for ids_list in ids.values():
        result += ids_list

    result = list(set(result))
    return result


def task_3():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    words_counts = {}

    for query in queries:
        words = query.split()
        words_counts.setdefault(len(words), 0)
        words_counts[len(words)] += 1

    all_words_count = len(queries)
    result = {}
    for word_count, count in words_counts.items():
        result[word_count] = round(count / all_words_count * 100, 2)

    return result
