CREATE TABLE `artists` (

  `artist_id` INT NOT NULL AUTO_INCREMENT,

  `name` VARCHAR(255) NOT NULL,

  `genre` VARCHAR(255) NOT NULL,

  PRIMARY KEY (`artist_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Создание таблицы для вакансий с указанием движка и кодировки

CREATE TABLE `tracks` (

  `track_id` INT NOT NULL AUTO_INCREMENT,
  
  `artist_id` INT NOT NULL ,

  `title` VARCHAR(255) NOT NULL,

  `duration_seconds` INT NOT NULL,

  PRIMARY KEY (`track_id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `artists` (`name`, `genre`) VALUES ('Иван Иванов', 'Классика');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Алексей Петров', 'Хип-хоп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Дмитрий Сидоров', 'Классика');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Сергей Козлов', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Михаил Орлов', 'Фолк');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Павел Волков', 'Кантри');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Андрей Лебедев', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Владимир Соколов', 'Фолк');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Глеб Морозов', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Петр Новиков', 'Хип-хоп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Артем Жуков', 'Хип-хоп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Кирилл Зверев', 'Классика');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Максим Громов', 'Хип-хоп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Никита Белов', 'Рэп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Роман Титов', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Мария Иванова', 'Фолк');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Елена Петрова', 'Электроника');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Ольга Сидорова', 'Хип-хоп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Анна Козлова', 'Фолк');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Екатерина Орлова', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Наталья Волкова', 'Рок');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Татьяна Лебедева', 'Метал');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Ксения Соколова', 'Фолк');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Юлия Морозова', 'Классика');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Светлана Новикова', 'Метал');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Алина Жукова', 'Электроника');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Виктория Зверева', 'Электроника');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Дарья Громова', 'Рок');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Ангелина Белова', 'Поп');
INSERT INTO `artists` (`name`, `genre`) VALUES ('Евгения Титова', 'Хип-хоп');

-- Заполнение таблицы 'tracks' (30 треков)

INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (7, 'мечта огня Мгновенная', 360);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (29, 'Тихая случая надежда', 305);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (3, 'Громкая мечта случая', 387);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (24, 'Громкая дорога', 234);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'Быстрая времени', 454);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'Сложная радость', 346);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (2, 'Светлая мечта', 407);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'огня эмоция', 277);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (9, 'судьбы Темная', 190);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (7, 'Вечная мелодия', 161);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (14, 'пространства ночь', 124);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'судьбы ритм Высокая', 368);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (13, 'прошлого эмоция', 281);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (23, 'песня будущего', 428);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (24, 'ночь Близкая', 474);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'смерти Ясная дорога', 370);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (9, 'ночь Медленная', 145);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (30, 'радость Темная ветра', 321);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (14, 'песня судьбы', 249);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (28, 'Ясная любовь забвения', 402);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'времени мечта Вечная', 143);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (12, 'мечта Медленная', 258);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (21, 'эмоция пространства Далекая', 321);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (29, 'грусть Мгновенная', 270);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (16, 'Близкая мелодия', 171);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (17, 'ритм земли', 344);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (11, 'воды история', 404);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (8, 'ночь огня Быстрая', 270);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (1, 'смерти радость', 380);
INSERT INTO `tracks` (`artist_id`, `title`, `duration_seconds`) VALUES (9, 'Медленная судьбы', 156);



SELECT * FROM artists WHERE genre = 'Рок';