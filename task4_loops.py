video_game_sales = [
    [1, 'Wii Sports', 'Wii', 2006, 'Sports', 'Nintendo', 41.49, 29.02, 3.77, 82.74],
    [2, 'Super Mario Bros.', 'NES', 1985, 'Platform', 'Nintendo', 29.08, 3.58, 6.81, 40.24],
    [3, 'Mario Kart Wii', 'Wii', 2008, 'Racing', 'Nintendo', 15.85, 12.88, 3.79, 35.82],
    [4, 'Wii Sports Resort', 'Wii', 2009, 'Sports', 'Nintendo', 15.75, 11.01, 3.28, 33.0],
    [5, 'Pokemon Red/Blue', 'GB', 1996, 'Role-Playing', 'Nintendo', 11.27, 8.89, 10.22, 31.37],
    [6, 'Tetris', 'GB', 1989, 'Puzzle', 'Nintendo', 23.2, 2.26, 4.22, 30.26],
    [7, 'New Super Mario Bros.', 'DS', 2006, 'Platform', 'Nintendo', 11.38, 9.23, 6.5, 30.01],
    [8, 'Wii Play', 'Wii', 2006, 'Misc', 'Nintendo', 14.03, 9.2, 2.93, 29.02],
    [9, 'New Super Mario Bros. Wii', 'Wii', 2009, 'Platform', 'Nintendo', 14.59, 7.06, 4.7, 28.62],
    [10, 'Duck Hunt', 'NES', 1984, 'Shooter', 'Nintendo', 26.93, 0.63, 0.28, 28.31],
    [11, 'Nintendogs', 'DS', 2005, 'Simulation', 'Nintendo', 9.07, 11.0, 1.93, 24.76],
    [12, 'Mario Kart DS', 'DS', 2005, 'Racing', 'Nintendo', 9.81, 7.57, 4.13, 23.42],
    [13, 'Pokemon Gold/Silver', 'GB', 1999, 'Role-Playing', 'Nintendo', 9.0, 6.18, 7.2, 23.1],
    [14, 'Wii Fit', 'Wii', 2007, 'Sports', 'Nintendo', 8.94, 8.03, 3.6, 22.72],
    [15, 'Kinect Adventures!', 'X360', 2010, 'Misc', 'Microsoft', 14.97, 4.94, 0.24, 21.82],
    [16, 'Grand Theft Auto V', 'PS3', 2013, 'Action', 'Take-Two', 7.01, 9.27, 0.97, 21.4],
    [17, 'Grand Theft Auto: San Andreas', 'PS2', 2004, 'Action', 'Take-Two', 9.43, 0.4, 0.41, 20.81],
    [18, 'Super Mario World', 'SNES', 1990, 'Platform', 'Nintendo', 12.78, 3.75, 3.54, 20.61],
    [19, 'Brain Age', 'DS', 2005, 'Puzzle', 'Nintendo', 4.75, 9.26, 4.16, 20.22],
    [20, 'Pokemon Diamond/Pearl', 'DS', 2006, 'Role-Playing', 'Nintendo', 6.42, 4.52, 6.04, 18.36],
]

RANK = 0
NAME = 1
PLATFORM = 2
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA_SALES = 6
EU_SALES = 7
JP_SALES = 8
GLOBAL_SALES = 9

for i in range(len(video_game_sales)):
    if video_game_sales[i][9]>25:
        name = video_game_sales[i][1]
        Global_sales = video_game_sales[i][9]
        print(f"{name} {Global_sales}")

k=0
for i in range (len(video_game_sales)):
    if video_game_sales[i][3]<2000:
        k=k+1
        pre_2000_count = k
print(pre_2000_count)
total_NA_Sales = 0
total_JP_Sales = 0
for i in range (len(video_game_sales)):
    total_NA_Sales =  total_NA_Sales + video_game_sales[i][6]
    total_JP_Sales = total_JP_Sales + video_game_sales[i][8]
print(f"Total NA sales: {total_NA_Sales}")
print(f"Total JP sales: {total_JP_Sales}")
if  total_NA_Sales > total_JP_Sales:
    print('North America had higher sales')
else:
    print('Japan had higher sales')
nintendo_games =[]
k=0
for i in range(len(video_game_sales)):
    if video_game_sales[i][5]== 'Nintendo':
        k=k+1
        nintendo_games.append(video_game_sales[i][1])
print( nintendo_games)
print(k)
