import random
import os
# 2048游戏的规则如下：

# 1. **游戏目标**：通过合并相同的数字方块，尽可能地达到2048这个数字。

# 2. **游戏板**：游戏在一个4x4的方格板上进行。

# 3. **初始状态**：游戏开始时，板上会随机出现两个数字，通常是2或4。

# 4. **移动方块**：
#    - 玩家可以使用上下左右方向键（在这个实现中是W、A、S、D键）来移动所有的方块。
#    - 每次移动时，所有方块会尽可能地向指定方向滑动。
#    - 如果两个相邻的方块数字相同，它们会合并成一个方块，其数字为原来两个方块数字之和。

# 5. **新方块生成**：每次玩家移动后，会在一个随机的空白位置生成一个新的方块，数字为2或4。

# 6. **游戏结束**：
#    - 游戏在玩家无法进行任何有效移动时结束，即没有空格且没有相邻的相同数字可以合并。
#    - 游戏结束时，玩家的得分是所有方块上数字的总和。

# 7. **胜利条件**：当一个方块的数字达到2048时，玩家获胜。不过，玩家可以选择继续游戏以获得更高的分数。

# 希望这些规则能帮助你更好地理解和享受2048游戏！如果有其他问题或需要进一步的帮助，请告诉我。

def initialize_game():
    # 初始化游戏板，添加两个新的数字
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    # 在空白位置添加一个新的数字（2或4）
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = 2 if random.random() < 0.9 else 4

def print_board(board):
    # 清屏并打印当前的游戏板
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

def can_move(board):
    # 检查是否还有可以移动的步骤
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i < 3 and board[i][j] == board[i + 1][j]:
                return True
            if j < 3 and board[i][j] == board[i][j + 1]:
                return True
    return False

def compress(board):
    # 压缩非零数字到左侧
    new_board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][pos] = board[i][j]
                pos += 1
    return new_board

def merge(board):
    # 合并相邻且相同的数字
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    # 反转每一行
    new_board = []
    for i in range(4):
        new_board.append(list(reversed(board[i])))
    return new_board

def transpose(board):
    # 转置矩阵
    new_board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_board[i][j] = board[j][i]
    return new_board

def move_left(board):
    # 向左移动
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    # 向右移动
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    # 向上移动
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    # 向下移动
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def main():
    # 主函数，控制游戏流程
    board = initialize_game()
    print_board(board)
    while can_move(board):
        move = input("Use W/A/S/D to move: ").strip().lower()
        if move == 'w':
            board = move_up(board)
        elif move == 's':
            board = move_down(board)
        elif move == 'a':
            board = move_left(board)
        elif move == 'd':
            board = move_right(board)
        else:
            print("Invalid move! Use W/A/S/D keys.")
            continue
        add_new_tile(board)
        print_board(board)
    print("Game Over!")

if __name__ == "__main__":
    main()
