import random

# --- Настройки ---
DB_NAME_PLACEHOLDER = "s12345_db"  # Замените на имя вашей БД
NUM_ARTISTS = 30
NUM_TRACKS = 30
OUTPUT_SQL_FILENAME = "populate_music_db.sql"

# --- Списки для генерации данных ---

# Жанры музыки
genres = ["Рок", "Поп", "Хип-хоп", "Электроника", "Джаз", "Классика", "Кантри", "Рэп", "Фолк", "Метал"]

# Имена исполнителей (мужские и женские)
male_artists = ["Иван Иванов", "Алексей Петров", "Дмитрий Сидоров", "Сергей Козлов", "Михаил Орлов", 
                "Павел Волков", "Андрей Лебедев", "Владимир Соколов", "Глеб Морозов", "Петр Новиков",
                "Артем Жуков", "Кирилл Зверев", "Максим Громов", "Никита Белов", "Роман Титов"]

female_artists = ["Мария Иванова", "Елена Петрова", "Ольга Сидорова", "Анна Козлова", "Екатерина Орлова",
                  "Наталья Волкова", "Татьяна Лебедева", "Ксения Соколова", "Юлия Морозова", "Светлана Новикова",
                  "Алина Жукова", "Виктория Зверева", "Дарья Громова", "Ангелина Белова", "Евгения Титова"]

# Слова для генерации названий треков
track_words_1 = ["Темная", "Светлая", "Глубокая", "Высокая", "Далекая", "Близкая", "Тихая", "Громкая", 
                "Быстрая", "Медленная", "Вечная", "Мгновенная", "Таинственная", "Ясная", "Сложная"]

track_words_2 = ["ночь", "любовь", "мечта", "дорога", "песня", "история", "мелодия", "ритм", "эмоция", 
                "воспоминание", "надежда", "победа", "потеря", "радость", "грусть"]

track_words_3 = ["ветра", "огня", "воды", "земли", "времени", "пространства", "судьбы", "случая", 
                "жизни", "смерти", "свободы", "забвения", "памяти", "будущего", "прошлого"]

# --- Функции для генерации SQL-запросов ---

def generate_artists_insert_statements(num_records):
    """Генерирует INSERT запросы для таблицы artists."""
    inserts = []
    
    # Создаем список всех возможных исполнителей
    all_artists = male_artists + female_artists
    
    for i in range(num_records):
        name = all_artists[i] if i < len(all_artists) else f"Исполнитель {i+1}"
        genre = random.choice(genres)
        
        inserts.append(
            f"INSERT INTO `artists` (`name`, `genre`) VALUES "
            f"('{name}', '{genre}');"
        )
    return "\n".join(inserts)

def generate_tracks_insert_statements(num_records, num_artists):
    """Генерирует INSERT запросы для таблицы tracks."""
    inserts = []
    
    for i in range(num_records):
        artist_id = random.randint(1, num_artists)
        
        # Генерация названия трека
        title_parts = random.sample([track_words_1, track_words_2, track_words_3], random.randint(2, 3))
        title = " ".join(random.choice(part) for part in title_parts)
        
        # Генерация продолжительности трека (от 120 до 480 секунд)
        duration_seconds = random.randint(120, 480)
        
        inserts.append(
            f"INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES "
            f"({artist_id}, '{title}', {duration_seconds});"
        )
    return "\n".join(inserts)

# --- Основная логика скрипта ---
sql_script_content = []
sql_script_content.append(f"-- SQL-скрипт для заполнения БД '{DB_NAME_PLACEHOLDER}'")
sql_script_content.append(f"-- Генерация данных для музыкальной платформы\n")
sql_script_content.append(f"USE `{DB_NAME_PLACEHOLDER}`;\n")

sql_script_content.append("-- Очистка таблиц перед вставкой новых данных\n")
sql_script_content.append("SET FOREIGN_KEY_CHECKS = 0;")
sql_script_content.append("TRUNCATE TABLE `tracks`;")
sql_script_content.append("TRUNCATE TABLE `artists`;")
sql_script_content.append("SET FOREIGN_KEY_CHECKS = 1;\n")

sql_script_content.append("-- Заполнение таблицы 'artists' (30 исполнителей)\n")
sql_script_content.append(generate_artists_insert_statements(NUM_ARTISTS))
sql_script_content.append("\n-- Заполнение таблицы 'tracks' (30 треков)\n")
sql_script_content.append(generate_tracks_insert_statements(NUM_TRACKS, NUM_ARTISTS))

final_sql_string = "\n".join(sql_script_content)

# Создание файла
with open(OUTPUT_SQL_FILENAME, "w", encoding="utf-8") as f:
    f.write(final_sql_string)

print(f"SQL-скрипт '{OUTPUT_SQL_FILENAME}' успешно сгенерирован.")
print(f"Создано: {NUM_ARTISTS} исполнителей и {NUM_TRACKS} треков")
print("Сейчас начнется скачивание файла...")