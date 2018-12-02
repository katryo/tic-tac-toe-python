PLAYER_O = True
PLAYER_X = False


class Game:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.cur_player = PLAYER_O

    def is_end(self):
        for i in range(3):
            # horizontal
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != ' ':
                    return True
            # vertical
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] != ' ':
                    return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != ' ':
                return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] != ' ':
                return True
        return False

    def filled_all(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    # Return 0 if the move was invalid
    # Return 1 if the game continues
    # Return 2 if the game finishes
    def put(self, row, col):
        if row < 0 or col < 0 or row > 2 or col > 2:
            return 0
        if self.board[row][col] != ' ':
            return 0
        if self.cur_player == PLAYER_O:
            self.board[row][col] = 'O'
        else:
            self.board[row][col] = 'X'
        self.cur_player = self.cur_player == PLAYER_X
        if self.is_end():
            return 2
        return 1

    def show_board(self):
        print("-------")
        for row in self.board:
            print("|" + '|'.join(row) + '|')
            print("-------")


    def play(self):
        status = 1
        while status != 2:
            self.show_board()
            line = input()
            try:
                row, col = [int(s) for s in line.split(" ")]
            except:
                print("Your input was invalid. Play a move again.")
                continue

            status = self.put(row, col)
            if status == 0:
                print("Your move, ({}, {}) was invalid. Play a move again.".format(row, col))
            if self.filled_all():
                self.show_board()
                print("Tie.")
                return
        self.show_board()
        if self.cur_player == PLAYER_X:
            print("Player O won!")
        else:
            print("Player X won!")


if __name__ == '__main__':
    game = Game()
    game.play()