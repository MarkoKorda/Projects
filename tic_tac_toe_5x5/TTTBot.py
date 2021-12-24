import random 

list1 = [[0,0],[0,2],[2,0],[2,2],[1,1]]
list2 = [[0,0],[0,2],[2,0],[2,2]]
list3 = [[0,1],[1,0],[1,2],[2,1]]

class TTTBot:
    def __init__(self):
        self.first_or_second = 0
        self.field = []
        self.move_list = []
        self.me = ""
        self.enemy = ""

    def make_move(self,move_counter):
        if move_counter == 1:
            move = random.choice(list1)
            return move
        elif move_counter == 2:
            if self.move_list[0] == [1,1]:
                return random.choice(list2)
            elif self.move_list[0] in list2:
                return [1,1]
            elif self.move_list[0] == [0,1]:
                return [2,1]
            elif self.move_list[0] == [2,1]:
                return [0,1]
            elif self.move_list[0] == [1,0]:
                return [1,2]
            else:
                return [1,0]
        elif move_counter == 4:
            if (self.move_list[0] in list2) and (self.move_list[1] == [1,1]) and (self.move_list[2] in list2) and (self.move_list[0][0] + self.move_list[0][1] + self.move_list[2][0] + self.move_list[2][1] == 4):
                move = random.choice(list3)
                return move
        move = self.__attack1()
        if move == [-1,-1]:
            move = self.__defend()
            if move == [-1,-1]:
                move = self.__attack2()
        return move

    def __defend(self):
        move = [-1,-1]
        test_field = self.field.copy()
        for i in range(5):
            for j in range(5):
                if test_field[i][j] == " ":
                    test_field[i][j] = self.enemy
                    if self.__check_for_winner(test_field) == self.enemy:
                        test_field[i][j] = " "
                        return [i,j]
                    test_field[i][j] = " "
        return move

    def __attack1(self):
        move = [-1,-1]
        test_field = self.field.copy()
        for i in range(5):
            for j in range(5):
                if test_field[i][j] == " ":
                    test_field[i][j] = self.me
                    if self.__check_for_winner(test_field) == self.me:
                        test_field[i][j] = " "
                        return [i,j]
                    test_field[i][j] = " "
        return move

    def __attack2(self):
        possible_moves1 = []
        test_field = self.field.copy()
        k1max = 0
        for i1 in range(5):
            for j1 in range(5):
                if test_field[i1][j1] == " ":
                    test_field[i1][j1] = self.me
                    k1 = 0
                    for i2 in range(5):
                        for j2 in range(5):
                            if test_field[i2][j2] == " ":
                                test_field[i2][j2] = self.me
                                if self.__check_for_winner(test_field) == self.me:
                                    k1 += 1
                                test_field[i2][j2] = " "
                    test_field[i1][j1] = " "
                    if k1 > k1max:
                        possible_moves1 = []
                        move = [i1,j1]
                        possible_moves1.append(move)
                        k1max = k1
                    elif k1 == k1max:
                        move = [i1,j1]
                        possible_moves1.append(move)
        possible_moves2 = []
        k2max = 0
        for element in possible_moves1:
            i1 = element[0]
            j1 = element[1]
            test_field[i1][j1] = self.enemy
            k2 = 0
            for i2 in range(5):
                for j2 in range(5):
                    if test_field[i2][j2] == " ":
                        test_field[i2][j2] = self.enemy
                        if self.__check_for_winner(test_field) == self.enemy:
                            k2 += 1
                        test_field[i2][j2] = " "
            test_field[i1][j1] = " "
            if k2 > k2max:
                possible_moves2 = []
                move = [i1,j1]
                possible_moves2.append(move)
                k2max = k2
            elif k2 == k2max:
                move = [i1,j1]
                possible_moves2.append(move)
        move = random.choice(possible_moves2)
        return move

    def __check_for_winner(self,field):
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
