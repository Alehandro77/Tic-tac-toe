import random
import os
import time
import datetime

BOARD_SIZE = 3
EMPTY_CELL = "."
NAME_FILE = "Статистика.txt"

def print_board(board):
    os.system("cls")
    print("   ", end="")
    for i in range(BOARD_SIZE):
        print(i + 1, end = "  ")
    print()

    for i in range(len(board)):
        print(i + 1, end = "  ")
        for j in range(len(board[i])):
            print(f"{board[i][j]}  ", end="")
        print()

def record_winner(winner_name, is_two_players, is_draw):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if is_draw:
        new_entry = f"{timestamp} Произошла ничья\n"
    else:
        new_entry = f"{timestamp} Победу одержал {winner_name}\n"
    
    with open(NAME_FILE, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if is_two_players :
        for i, line in enumerate(lines):
            if "------------------------------------" in line:
                lines.insert(i, new_entry)
                break
        with open(NAME_FILE, 'w', encoding='utf-8') as file:
            file.writelines(lines)
    else:
        with open(NAME_FILE, 'a', encoding='utf-8') as file:
            file.write(new_entry)

def show_end_game_message(board, name_vins):
    os.system("cls")
    print_board(board)
    if check_full_board(board):
        print("Ничья (┬┬﹏┬┬)")
    else:
        print(f"Игрок {name_vins} победил  o(*￣︶￣*)o\n")
    time.sleep(5)
    os.system("cls")

def check_winner(board, symbol):
        for i in range(0, BOARD_SIZE):
            if all(board[i][j] == symbol for j in range(0, BOARD_SIZE)):
                return True
            if all(board[j][i] == symbol for j in range(0, BOARD_SIZE)):
                return True
        
        if all(board[i][i] == symbol for i in range(0, BOARD_SIZE)):
            return True
        if all(board[i][BOARD_SIZE - 1 - i] == symbol for i in range(0, BOARD_SIZE)):
            return True
        
        return False

def check_full_board(board):
    return all(cell != EMPTY_CELL for row in board for cell in row)

def make_human_move(board, name , symbol):
    
    while True:
        try:
            row = int(input(f"{name}, Введите номер строки (1 - {BOARD_SIZE}): ")) - 1
            col = int(input(f"{name}, Введите номер столбца (1 - {BOARD_SIZE}): ")) - 1 
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if board[row][col] == EMPTY_CELL:
                    board[row][col] = symbol
                    break
                else:
                    print_board(board)
                    print("Это место уже занято! ヾ(`ヘ´)ﾉﾞ")
            else:
                print_board(board)
                print(f"Вы вышли за границы! Значения должны быть от 1 до {BOARD_SIZE}! ヽ(`⌒´メ)ノ")
        except ValueError:
            print_board(board)
            print("Вводить нужно циферки! (ノ°益°)ノ")

def make_computer_move(board, symbol):
    print("Компутер думает (￣～￣;)")
    time.sleep(3)
    while True:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] == EMPTY_CELL:
            board[row][col] = symbol
            break

def create_file():
    try:
        with open(NAME_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        with open('Статистика.txt', 'w', encoding='utf-8') as file:
            file.write('=====Статистика побед в игре "Крестики Нолики"\n\n')
            file.write('Режим игры с другом\n')
            file.write('------------------------------------\n')
            file.write('Режим игры с Компьютером\n')

def main():
    
    create_file()
    os.system("cls")
    while True:
        board = [[EMPTY_CELL for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        print("===== ИГРА КРЕСТИКИ И НОЛИКИ =====\n")
        print("Выберите режим:\n1. С другом\n2. С компьтером\n0. Выход")
        while True:
            choice = input("Ваш выбор: ")
            if choice == "0":
                print("До свидания ｡ﾟ･ (>﹏<) ･ﾟ｡")
                return True
            elif choice == "1" or choice == '2':
                is_two_players = True if choice == "1" else False
                break
            else:
                print("Такого варианта нет!  (ノ°益°)ノ")
        
        os.system("cls")
        player1_name  = input("Игрок 1, введите своё имя: ").replace(" ", "").lower().capitalize()
        if is_two_players :
            player2_name  = input("Игрок 2, введите своё имя: ").replace(" ", "").lower().capitalize()
        else:
            player2_name  = "Компутер"
        
        player1 = {
            "name": player1_name,
            "symbol": None,
            "is_human": True
        }
        
        player2 = {
            "name": player2_name,
            "symbol": None,
            "is_human": is_two_players
        }
        
        if random.choice([True, False]):
            player1["symbol"] = "X"
            player2["symbol"] = "O"
            current_player = player1
        else:
            player1["symbol"] = "O"
            player2["symbol"] = "X"
            current_player = player2
        
        time.sleep(2)
        os.system("cls")
        print(f"Первым ходит - {current_player['name']}")
        time.sleep(2)
        
        while True:
            print_board(board)
            if current_player["is_human"]:
                make_human_move(board, current_player["name"], current_player["symbol"])
            else:
                make_computer_move(board, current_player["symbol"])
            
            if check_winner(board, current_player["symbol"]):
                show_end_game_message(board, current_player['name'])
                record_winner(current_player['name'], is_two_players, is_draw=False)
                break
            
            if check_full_board(board):
                show_end_game_message(board, None)
                record_winner(None, is_two_players, is_draw=True)
                break
            
            current_player = player1 if current_player is player2 else player2

if __name__ == "__main__":
    main()
