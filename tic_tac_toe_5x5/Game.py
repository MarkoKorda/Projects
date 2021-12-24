import time
import TTTBot 

letter_list = ["A","B","C","D","E"]

class Game:
    def __init__(self):
        self.field = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
        self.move_list = []
        self.player1 = ""
        self.player2 = ""
        self.move_counter = 0
        self.bot = 0
        self.bot_first_or_second = 0

    def __reset(self):
        self.field = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
        self.move_list = []
        self.player1 = ""
        self.player2 = ""
        self.move_counter = 0
        self.bot = 0
        self.bot_first_or_second = 0

    def __who_starts_first_pvp(self):
        while True:
            wsf = input("Who starts first? (Answers: o,O,x,X) :")
            wsf = wsf.strip()
            wsf = wsf.lower()
            if wsf == "o":
                self.player1 = "O"
                self.player2 = "X"
                break
            elif wsf == "x":
                self.player1 = "X"
                self.player2 = "O"
                break
            else:
                print("Wrong input! Possible answers: o,O,x,X!")

    def __show(self):
        print("    1   2   3   4   5")
        for i in range(5):
            print("-----------------------")
            print(letter_list[i] + " " + "|" + " " + self.field[i][0] + " " + "|" + " " + self.field[i][1] + " " + "|" + " " + self.field[i][2] + " " + "|" + " " + self.field[i][3] + " " + "|" + " " + self.field[i][4] + " " + "|")
        print("-----------------------")
        

    def __update_pvp(self):
        if self.move_counter % 2 == 1:
            player = self.player1
        else:
            player = self.player2
        print()
        print("Player " + player + " is playing!")
        print()
        while True:
            move = input("Make move! Enter letter and number(example: B2):")
            move = move.strip()
            move = move.lower()
            index1, index2 = self.__input_validation(move)
            if (index1 == -1) or (index2 == -1):
                print("Invalid input!")
            elif not(self.field[index1][index2] == " "):
                print("Field is taken! Choose another!")
            else:
                self.field[index1][index2] = player
                self.move_list.append([index1,index2])
                break

    def __input_validation(self,inp):
        if len(inp) != 2:
            return -1, -1
        letter = inp[0]
        number = int(inp[1])
        if letter == "a":
            index1 = 0
        elif letter == "b":
            index1 = 1
        elif letter == "c":
            index1 = 2
        elif letter == "d":
            index1 = 3
        elif letter == "e":
            index1 = 4
        else:
            index1 = -1
        if (number > 0) and (number < 6):
            index2 = number - 1
        else:
            index2 = -1
        return index1, index2

    def __check_for_winner(self):
        for i in range(5):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] == self.field[i][3] != " ":
                return self.field[i][0]
            elif self.field[i][1] == self.field[i][2] == self.field[i][3] == self.field[i][4] != " ":
                return self.field[i][1]
        for i in range(5):
            if self.field[0][i] == self.field[1][i] == self.field[2][i] == self.field[3][i] != " ":
                return self.field[0][i]
            elif self.field[1][i] == self.field[2][i] == self.field[3][i] == self.field[4][i] != " ":
                return self.field[1][i]
        for i in range(2):
            for j in range(2):
                if self.field[i][j] == self.field[i+1][j+1] == self.field[i+2][j+2] == self.field[i+3][j+3] != " ":
                    return self.field[i][j]   
        for i in range(2):
            for j in range(2):
                if self.field[i+3][j] == self.field[i+2][j+1] == self.field[i+1][j+2] == self.field[i][j+3] != " ":
                    return self.field[i+3][j] 
        return "_"

    def start_game_pvp(self):
        self.__reset()
        self.__who_starts_first_pvp()
        while True:
            if self.move_counter == 25:
                self.__show()
                print()
                print("It's a tie!")
                print()
                break
            self.move_counter += 1
            self.__show()
            self.__update_pvp()
            winner = self.__check_for_winner()
            if not(winner == "_"):
                self.__show()
                print()
                print(winner + " is winner!!!")
                print()
                break

    def __who_starts_first_pve(self):
        while True:
            wsf = input("Are you O or X? (Answers: o,O,x,X) :")
            wsf = wsf.strip()
            wsf = wsf.lower()
            if wsf == "o":
                self.player1 = "O"
                self.player2 = "X"
                self.bot.me = "X"
                self.bot.enemy = "O"
                break
            elif wsf == "x":
                self.player1 = "X"
                self.player2 = "O"
                self.bot.me = "O"
                self.bot.enemy = "X"
                break
            else:
                print("Wrong input! Possible answers: o,O,x,X!")
        while True:
            wsf = input("Who starts first? Bot or you? (Answers: bot/me) :")
            wsf = wsf.lower()
            wsf = wsf.strip()
            if wsf == "me":
                self.bot_first_or_second = 2
                break
            elif wsf == "bot":
                self.bot_first_or_second = 1
                x = self.player1
                self.player1 = self.player2
                self.player2 = x
                break
            else:
                print("Wrong input! Possible answers: bot/me!")
    
    def __update_pve(self):
        if self.move_counter % 2 == self.bot_first_or_second:
            bot_move = self.bot.make_move(self.move_counter)
            self.__update_bot(bot_move)
            self.move_list.append(bot_move)
        else:
            self.__update_human()
    
    def __update_bot(self,move):
        print()
        print("Bot is playing!")
        print()
        time.sleep(1.5)
        index1 = move[0]
        index2 = move[1]
        self.field[index1][index2] = self.bot.me

    def __update_human(self):
        print()
        print("You are playing!")
        print()
        while True:
            move = input("Make move! Enter letter and number(example: B2):")
            move = move.strip()
            move = move.lower()
            index1, index2 = self.__input_validation(move)
            if (index1 == -1) or (index2 == -1):
                print("Invalid input!")
            elif not(self.field[index1][index2] == " "):
                print("Field is taken! Choose another!")
            else:
                self.field[index1][index2] = self.bot.enemy
                self.move_list.append([index1,index2])
                break

    def start_game_pve(self):
        self.__reset()
        self.bot = TTTBot.TTTBot()
        self.__who_starts_first_pve()
        self.bot.first_or_second = self.bot_first_or_second
        self.bot.field = self.field
        self.bot.move_list = self.move_list
        if self.bot_first_or_second == 2:
            self.bot_first_or_second = 0
        while True:
            if self.move_counter == 25:
                self.__show()
                print()
                print("It's a tie!")
                print()
                break
            self.move_counter += 1
            self.__show()
            self.__update_pve()
            winner = self.__check_for_winner()
            if not(winner == "_"):
                if winner == self.bot.me:
                    winner = "Bot is"
                elif winner == self.bot.enemy:
                    winner = "You are"
                self.__show()
                print()
                print(winner + " winner!!!")
                print()
                break
