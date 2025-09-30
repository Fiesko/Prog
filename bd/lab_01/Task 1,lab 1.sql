-- Создание таблицы для кандидатов с указанием движка и кодировки

CREATE TABLE `candidates` (

  `candidate_id` INT NOT NULL AUTO_INCREMENT,

  `full_name` VARCHAR(255) NOT NULL,

  `desired_position` VARCHAR(255) NOT NULL,

  `salary_expectation` DECIMAL(10, 2) NOT NULL COMMENT 'Зарплатные ожидания (10 знаков, 2 после запятой)',

  PRIMARY KEY (`candidate_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Создание таблицы для вакансий с указанием движка и кодировки

CREATE TABLE `vacancies` (

  `vacancy_id` INT NOT NULL AUTO_INCREMENT,

  `company` VARCHAR(255) NOT NULL,

  `position_title` VARCHAR(255) NOT NULL,

  PRIMARY KEY (`vacancy_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Владимир Степанов', 'Менеджер по продукту', 75801);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Алексей Федоров', 'Frontend-разработчик', 78878);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Андрей Морозов', 'Backend-разработчик', 91339);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Татьяна Филиппова', 'Frontend-разработчик', 346275);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Ольга Морозова', 'Frontend-разработчик', 47632);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Ксения Лебедева', 'Backend-разработчик', 77483);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Светлана Виноградова', 'QA-инженер', 49943);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Наталья Филиппова', 'Менеджер по продукту', 66200);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Мария Волкова', 'Аналитик данных', 69004);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Екатерина Егорова', 'Менеджер по продукту', 98009);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Иван Яковлев', 'UX/UI дизайнер', 51380);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Васильев', 'Backend-разработчик', 71160);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Алексей Петров', 'Аналитик данных', 327690);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Глеб Морозов', 'Менеджер по продукту', 62310);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Анна Филиппова', 'Backend-разработчик', 308146);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Журавлев', 'Менеджер по продукту', 331858);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Иван Егоров', 'Аналитик данных', 106868);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Анна Михайлова', 'UX/UI дизайнер', 232570);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Елена Филиппова', 'Frontend-разработчик', 135530);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Михаил Виноградов', 'QA-инженер', 331982);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Елена Волкова', 'Системный администратор', 68535);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Владимир Егоров', 'Менеджер по продукту', 234739);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Владимир Виноградов', 'Frontend-разработчик', 64252);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Мария Афанасьева', 'UX/UI дизайнер', 92450);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Ольга Афанасьева', 'QA-инженер', 140016);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Павел Смирнов', 'Frontend-разработчик', 213306);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Дмитрий Егоров', 'Аналитик данных', 315810);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Васильев', 'UX/UI дизайнер', 276924);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Светлана Журавлева', 'QA-инженер', 84757);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Васильев', 'QA-инженер', 269543);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Елена Кузнецова', 'Frontend-разработчик', 59809);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Яковлев', 'Менеджер по продукту', 338871);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Петр Федоров', 'QA-инженер', 97257);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Ксения Новикова', 'Менеджер по продукту', 262353);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Владимир Степанов', 'Аналитик данных', 72829);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Михаил Козлов', 'Backend-разработчик', 61281);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Екатерина Афанасьева', 'QA-инженер', 99543);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Мария Федорова', 'Аналитик данных', 54870);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Мария Петрова', 'Backend-разработчик', 84539);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Петр Новиков', 'Менеджер по продукту', 77185);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Андрей Новиков', 'Системный администратор', 83127);
INSERT INTO `candidates` (`full_name`, `desired_position`, `salary_expectation`) VALUES ('Сергей Новиков', 'UX/UI дизайнер', 165857);

-- Заполнение таблицы 'vacancies'

INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ООО Ромашка', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('АльфаГрупп', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'Аналитик данных');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Менеджер по продукту');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'Менеджер по продукту');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Цифровые Технологии', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Цифровые Технологии', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('АльфаГрупп', 'Аналитик данных');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Backend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Аналитик данных');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'Backend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'QA-инженер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Аналитик данных');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'Frontend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ООО Ромашка', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Backend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Frontend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ГлобалДейта', 'QA-инженер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Менеджер по продукту');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Цифровые Технологии', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Менеджер по продукту');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'Backend-разработчик');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('IT-Решения', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('IT-Решения', 'Системный администратор');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('Стартап Инновации', 'UX/UI дизайнер');
INSERT INTO `vacancies` (`company`, `position_title`) VALUES ('ТехноСофт', 'Backend-разработчик');

select * from vacancies;
select * from candidates where salary_expectation >100000;