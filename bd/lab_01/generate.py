import random
from google.colab import files

# --- Настройки ---
DB_NAME_PLACEHOLDER = "s12345_db" #
NUM_CANDIDATES = random.randint(40, 50)
NUM_VACANCIES = random.randint(30, 40)
OUTPUT_SQL_FILENAME = "populate_db_v5_gender_correct.sql"

# --- Списки для генерации ГРАММАТИЧЕСКИ КОРРЕКТНЫХ данных ---

# 1. Разделяем имена по роду
male_first_names = ["Иван", "Алексей", "Дмитрий", "Сергей", "Михаил", "Павел", "Андрей", "Владимир", "Глеб", "Петр"]
female_first_names = ["Мария", "Елена", "Ольга", "Анна", "Екатерина", "Наталья", "Татьяна", "Ксения", "Юлия", "Светлана"]

# 2. Создаем пары фамилий (мужская, женская)
last_name_pairs = [
    ('Иванов', 'Иванова'), ('Петров', 'Петрова'), ('Смирнов', 'Смирнова'), ('Кузнецов', 'Кузнецова'),
    ('Васильев', 'Васильева'), ('Морозов', 'Морозова'), ('Волков', 'Волкова'), ('Лебедев', 'Лебедева'),
    ('Козлов', 'Козлова'), ('Новиков', 'Новикова'), ('Соколов', 'Соколова'), ('Михайлов', 'Михайлова'),
    ('Федоров', 'Федорова'), ('Яковлев', 'Яковлева'), ('Афанасьев', 'Афанасьева'), ('Филиппов', 'Филиппова'),
    ('Егоров', 'Егорова'), ('Виноградов', 'Виноградова'), ('Степанов', 'Степанова'), ('Журавлев', 'Журавлева')
]

# Списки для должностей и компаний остаются прежними
desired_positions = ["Frontend-разработчик", "Backend-разработчик", "QA-инженер", "Менеджер по продукту", "Аналитик данных", "UX/UI дизайнер", "Системный администратор"]
companies = ["ООО Ромашка", "ТехноСофт", "Стартап Инновации", "Веб-Студия Креатив", "IT-Решения", "ГлобалДейта", "Цифровые Технологии", "АльфаГрупп"]


# --- Функции для генерации SQL-запросов ---

def generate_candidates_insert_statements(num_records):
    """Генерирует INSERT запросы с корректным согласованием рода имени и фамилии."""
    inserts = []
    for _ in range(num_records):

        # 3. Новая логика генерации ФИО
        if random.random() < 0.5: # 50% шанс сгенерировать мужчину
            first_name = random.choice(male_first_names)
            last_name = random.choice(last_name_pairs)[0] # Берем мужскую форму (индекс 0)
        else: # 50% шанс сгенерировать женщину
            first_name = random.choice(female_first_names)
            last_name = random.choice(last_name_pairs)[1] # Берем женскую форму (индекс 1)

        full_name = f"{first_name} {last_name}"

        # Генерация остальных данных остается прежней
        desired_position = random.choice(desired_positions)
        if random.random() < 0.5:
            salary_expectation = round(random.uniform(101000.00, 350000.00))
        else:
            salary_expectation = round(random.uniform(45000.00, 99999.00))

        inserts.append(
            f"INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES "
            f"('{full_name}', '{desired_position}', {salary_expectation});"
        )
    return "\n".join(inserts)

def generate_vacancies_insert_statements(num_records):
    """Генерирует INSERT запросы для таблицы vacancies."""
    inserts = []
    for _ in range(num_records):
        company = random.choice(companies)
        position_title = random.choice(desired_positions)
        inserts.append(
            f"INSERT INTO `vacancies` (`company`, `position_title`) VALUES "
            f"('{company}', '{position_title}');"
        )
    return "\n".join(inserts)

# --- Основная логика скрипта ---
sql_script_content = []
sql_script_content.append(f"-- SQL-скрипт для заполнения БД '{DB_NAME_PLACEHOLDER}' (v5, с корректным родом ФИО)\n")
sql_script_content.append(f"USE `{DB_NAME_PLACEHOLDER}`;\n")

sql_script_content.append("-- Очистка таблиц перед вставкой новых данных\n")
sql_script_content.append("SET FOREIGN_KEY_CHECKS = 0;")
sql_script_content.append("TRUNCATE TABLE `candidates`;")
sql_script_content.append("TRUNCATE TABLE `vacancies`;")
sql_script_content.append("SET FOREIGN_KEY_CHECKS = 1;\n")

sql_script_content.append("-- Заполнение таблицы 'candidates'\n")
sql_script_content.append(generate_candidates_insert_statements(NUM_CANDIDATES))
sql_script_content.append("\n-- Заполнение таблицы 'vacancies'\n")
sql_script_content.append(generate_vacancies_insert_statements(NUM_VACANCIES))

final_sql_string = "\n".join(sql_script_content)

# Создание и скачивание файла
with open(OUTPUT_SQL_FILENAME, "w", encoding="utf-8") as f:
    f.write(final_sql_string)

print(f"SQL-скрипт '{OUTPUT_SQL_FILENAME}' успешно сгенерирован.")
print("Скрипт обновлен: имена и фамилии теперь согласованы по роду.")
print("Сейчас начнется скачивание файла...")

files.download(OUTPUT_SQL_FILENAME)