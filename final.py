note = [ ]

username = input('Пожалуйста, введите имя пользователя: ')
title_1 = input('Заголовок заметки №1: ')
title_2 = input('Заголовок заметки №2: ')
title_3= input('Заголовок заметки №3: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате "день-месяц-год", например "10-11-2024": ')
issue_date = input('Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": ')
titles = [ title_1, title_2, title_3 ]

note.append(username)
note.append(titles)
note.append(content)
note.append(status)
note.append(created_date)
note.append(issue_date)

print(f"Имя пользователя: {note[0]}")
print(f"Содержание заметки: {note[1]}")
print(f"Статус: {note[2]}")
print(f"Дата создания: {note[3]}")
print(f"Дата изменения: {note[4]}")
print(f"Заголовки: {note[5]}")