import random
import os
import time
import datetime

BOARD_SIZE = 3
EMPTY_CELL = "."

def print_board(board):
    os.system("cls")
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j] + "   ", end="")
        print("")

def record_winner(winner_name, is_two_players, is_draw):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if is_draw:
        new_entry = f"{timestamp} Произошла ничья\n"
    else:
        new_entry = f"{timestamp} Победу одержал {winner_name}\n"
    
    with open("Статистика.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if is_two_players :
        for i, line in enumerate(lines):
            if "------------------------------------" in line:
                lines.insert(i, new_entry)
                break
        with open("Статистика.txt", 'w', encoding='utf-8') as file:
            file.writelines(lines)
    else:
        with open("Статистика.txt", 'a', encoding='utf-8') as file:
            file.write(new_entry)

def meseg(board, name_vins):
    os.system("cls")
    print_board(board)
    if check_ful_board(board):
        print("Ничья (┬┬﹏┬┬)")
    else:
        print(f"Игрок {name_vins} победил  o(*￣︶￣*)o\n")
    time.sleep(5)
    os.system("cls")

def check_winner(board, symbol):
        for i in range(1, BOARD_SIZE + 1):
            if all(board[i][j] == symbol for j in range(1, BOARD_SIZE + 1)):
                return True
            if all(board[j][i] == symbol for j in range(1, BOARD_SIZE + 1)):
                return True
        
        if all(board[i][i] == symbol for i in range(1, BOARD_SIZE + 1)):
            return True
        if all(board[i][BOARD_SIZE + 1 - i] == symbol for i in range(1, BOARD_SIZE + 1)):
            return True
        
        return False

def check_ful_board(board):
    for i in range(1, BOARD_SIZE + 1):
        for j in range(1, BOARD_SIZE + 1):
            if board[i][j] == EMPTY_CELL:
                return False
    return True

def vins_game(board, player1_name , player_x , player_o, is_two_players ):
    
    symbols_players = [("X", player_x), ("O", player_o)]
    
    for symbol, player in symbols_players:
        if check_winner(board, symbol):
            is_human = is_two_players or player == player1_name
            winner_name = player if is_human else "Компутер"
            record_winner(winner_name, is_two_players, is_draw=False)
            meseg(board, winner_name)
            return True
    
    if check_ful_board(board):
        record_winner(None, is_two_players, is_draw = True)
        meseg(board, None)
        return True
    
    return False

def make_move(board, is_two_players, player, name, symbol):
    
    print_board(board)
    is_human = is_two_players  or player  == name
    if is_human:
        make_human_move(board, player , symbol)
    else:
        make_computer_move(board, symbol)

def make_human_move(board, name , symbol):
    
    while True:
        try:
            row = int(input(f"{name}, Введите номер строки (1 - {BOARD_SIZE}): "))
            col = int(input(f"{name}, Введите номер столбца (1 - {BOARD_SIZE}): "))
            if 0 < row < BOARD_SIZE + 1 and 0 < col < BOARD_SIZE + 1:
                if board[row][col] == ".":
                    board[row][col] = symbol
                    break
                else:
                    print_board(board)
                    print("Это место уже занято! ヾ(`ヘ´)ﾉﾞ")
            else:
                print_board(board)
                print("Вы вышли за границы! Значения должны быть от 1 до {BOARD_SIZE}! ヽ(`⌒´メ)ノ")
        except ValueError:
            print_board(board)
            print("Вводить нужно циферки! (ノ°益°)ノ")

def make_computer_move(board, symbol):
    print("Компутер думает (￣～￣;)")
    time.sleep(5)
    while True:
        row = random.randint(1,BOARD_SIZE)
        col = random.randint(1,BOARD_SIZE)
        if board[row][col] == EMPTY_CELL:
            board[row][col] = symbol
            print("")
            break

def creat_file():
    try:
        with open("Статистика.txt", 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        with open('Статистика.txt', 'w', encoding='utf-8') as file:
            file.write('=====Статистика побед в игре "Крестики Нолики"\n\n')
            file.write('Режим игры с другом\n')
            file.write('------------------------------------\n')
            file.write('Режим игры с Компьютером\n')

def main():
    
    creat_file()
    os.system("cls")
    exit = False
    while True:
        board = [[" ", "1", "2", "3"], 
                ["1", ".", ".", "."], 
                ["2", ".", ".", "."], 
                ["3", ".", ".", "."]]
        
        print("Выберите режим:\n1. С другом\n2. С компьтером\n0. Выход")
        while True:
            pleer = input("Ваш выбор: ")
            if pleer == "1":
                is_two_players  = True
                break
            elif pleer == "2":
                is_two_players  = False
                break
            elif pleer == "0":
                exit = True
                break
            else:
                print("Такого варианта нет!  (ノ°益°)ノ")
        
        if exit:
            print("До свидания ｡ﾟ･ (>﹏<) ･ﾟ｡")
            break
        
        os.system("cls")
        player1_name  = input("Игрок 1, введите своё имя: ")
        player1_name = player1_name.replace(" ", "").lower().capitalize()
        if is_two_players :
            player2_name  = input("Игрок 2, введите своё имя: ")
            player2_name = player2_name.replace(" ", "").lower().capitalize()
        else:
            player2_name  = "Компутер"
        
        player_x  = random.choice([player1_name , player2_name ])
        player_o = player2_name  if player_x  == player1_name  else player1_name 
        
        time.sleep(2)
        os.system("cls")
        print(f"Первым ходит - {player_x }")
        time.sleep(2)
        
        while True:
            make_move(board, is_two_players , player_x , player1_name , "X")
            if vins_game(board, player1_name, player_x , player_o, is_two_players ):
                break                      
            
            make_move(board, is_two_players , player_o , player1_name , "O")
            if vins_game(board, player1_name, player_x , player_o, is_two_players ):
                break

if __name__ == "__main__":
    main()
