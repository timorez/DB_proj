import sqlite3

con = sqlite3.connect('dota2_heroes.sqlite')

cur = con.cursor()

n = int(input('Номер запроса: '))

# 1 Подсчет персов
if n == 1:
    res1 = list(cur.execute("""SELECT count(*) FROM heroes"""))[0]
    print(res1[0])
    print()
    # 124

# 2 Выборка персов по характеристике
elif n == 2:
    res2 = list(cur.execute("""SELECT name FROM heroes
                                  WHERE front = 1"""))
    print(list(str(i[0]) for i in res2))
    print()
    # ['Axe', 'Alchemist', 'Abbadon', 'Chaos Knight', 'Centaur Warrunner', 'Bristleback', 'Brewmaster',
    # 'Dawnbreaker', 'Dragon Knight', 'Medusa', 'Wraith King', 'Tiny', 'Timbersaw', 'Tidehunter', 'Pudge',
    # 'Primal Beast']

# 3 Выборка перса по минимальной/максимальной характеристике
elif n == 3:
    res3 = list(cur.execute("""SELECT name FROM heroes
                                  WHERE time = (SELECT min(time) FROM heroes)"""))[0]
    print(res3[0])
    print()
    # Primal Beast

# 4 Выборка персов по игроку
elif n == 4:
    res4 = list(cur.execute("""SELECT name FROM heroes
                                  WHERE PlayerID = (SELECT ID FROM Players 
                                          WHERE Nickname = 'Stray228')"""))
    print(list(str(i[0]) for i in res4))
    print()
    # ['Lion', 'Zeus', 'Sniper']

# 5 Выборка перса по минимальному/максимальному винрейту игрока
elif n == 5:
    res5 = list(cur.execute("""SELECT name FROM heroes
                                  WHERE PlayerID = (SELECT ID FROM Players 
                                          WHERE WR = (SELECT max(WR) FROM Players))"""))
    print(list(str(i[0]) for i in res5))
    print()
    # ['Lone Druid', 'Meepo', 'Tinker', 'Timbersaw']

# 6 Добавление перса
elif n == 6:
    print(list(cur.execute("""SELECT * FROM heroes WHERE name = 'ringmaster'""")))

    res6 = list(cur.execute("""INSERT INTO heroes (name, farm, time, meta, front, lane, active_sup, playerID)
                                 VALUES ('ringmaster', 0, 0, 0, 0, 0, 0, 0)"""))

    print(list(cur.execute("""SELECT * FROM heroes WHERE name = 'ringmaster'""")))
    print()
    # []
    # [('ringmaster', 0, 0, 0, 0, 0, 0, 0)]

# 7 Выбор случайного перса
elif n == 7:
    res7 = list(cur.execute("""SELECT * FROM heroes
                                  ORDER BY RANDOM() LIMIT 1"""))
    print(res7)
    print()
    # ('Axe', 2, 39, 0, 1, 1, 0, 3)

# 8 Выборка Уникальных характеристик перса по игроку
elif n == 8:
    res8 = list(cur.execute("""SELECT DISTINCT farm FROM heroes
                                  WHERE PlayerID = (SELECT ID FROM Players
                                                  WHERE Nickname = 'Yatoro')"""))
    print(list(int(_[0]) for _ in res8))
    print()
    # [2, 3]

# 9 Обновление существующего перса
elif n == 9:
    print(list(cur.execute("""SELECT meta FROM heroes WHERE name = 'Axe'"""))[0])

    res9 = list(cur.execute("""UPDATE heroes
                              SET meta = 1
                              WHERE name = 'Axe'"""))

    print(list(cur.execute("""SELECT meta FROM heroes WHERE name = 'Axe'"""))[0])
    print()
    # (0,)
    # (1,)

# 10 Выборка игроков отсортированная по винрейту
elif n == 10:
    res10 = list(cur.execute("""SELECT Nickname FROM Players
                                  ORDER BY WR DESC LIMIT 10"""))
    print(list(str(_[0]) for _ in res10))
    print()
    # ['Ace', 'Puppey', 'NothingToSay', 'Kaka', 'RAMZES666', 'Fng', 'Collapse',
    # 'zai', 'Miposhka', 'TORONTOTOKYO']

# 11 Выбор перса по аегисам его игрока
elif n == 11:
    res11 = list(cur.execute("""SELECT name FROM heroes
                                  WHERE PlayerID = (SELECT ID FROM Players
                                                        WHERE TeamID = (SELECT ID FROM Teams
                                                                            WHERE Aegis_count = 2))"""))
    print(list(str(_[0]) for _ in res11))
    print()

# con.commit()
