import sqlite3

con = sqlite3.connect('dota2_heroes.sqlite')

cur = con.cursor()

# 1 Подсчет персов
res1 = list(cur.execute("""SELECT count(*) FROM heroes"""))[0]
print(res1[0])
print()

# 2 Выборка персов по характеристике
res2 = list(cur.execute("""SELECT name FROM heroes
                                WHERE front = 1"""))
print(list(str(i[0]) for i in res2))
print()

# 3 Выборка перса по минимальной/максимальной характеристике
res3 = list(cur.execute("""SELECT name FROM heroes
                                WHERE time = (SELECT min(time) FROM heroes)"""))[0]
print(res3[0])
print()

# 4 Выборка персов по игроку
res4 = list(cur.execute("""SELECT name FROM heroes
                                WHERE PlayerID = (SELECT ID FROM Players 
                                        WHERE Nickname = 'Stray228')"""))
print(list(str(i[0]) for i in res4))
print()

# 5 Выборка перса по минимальному/максимальному винрейту игрока
res5 = list(cur.execute("""SELECT name FROM heroes
                                WHERE PlayerID = (SELECT ID FROM Players 
                                        WHERE WR = (SELECT max(WR) FROM Players))"""))
print(list(str(i[0]) for i in res5))
print()

# 6 Добавление перса
print(list(cur.execute("""SELECT * FROM heroes WHERE name = 'ringmaster'""")))
res6 = list(cur.execute("""INSERT INTO heroes (name, farm, time, meta, front, lane, active_sup, playerID)
                               VALUES ('ringmaster', 0, 0, 0, 0, 0, 0, 0)"""))
print(list(cur.execute("""SELECT * FROM heroes WHERE name = 'ringmaster'""")))
print()
# con.commit()

# 7 Выбор случайного перса
res7 = list(cur.execute("""SELECT * FROM heroes
                                ORDER BY RANDOM() LIMIT 1"""))
print(res7)
print()

# 8 Выборка Уникальных характеристик перса по игроку
res8 = list(cur.execute("""SELECT DISTINCT farm FROM heroes
                                WHERE PlayerID = (SELECT ID FROM Players
                                                WHERE Nickname = 'Yatoro')"""))
print(res8)
print()

# 9 Обновление существующего перса
print(list(cur.execute("""SELECT meta FROM heroes WHERE name = 'Axe'"""))[0])
res9 = list(cur.execute("""UPDATE heroes
                            SET meta = 1
                            WHERE name = 'Axe'"""))
print(list(cur.execute("""SELECT meta FROM heroes WHERE name = 'Axe'"""))[0])
print()
# con.commit()

# 10 Выборка игроков отсортированная по винрейту
res10 = list(cur.execute("""SELECT Nickname FROM Players
                                ORDER BY WR DESC LIMIT 10"""))
print(res10)
print()
