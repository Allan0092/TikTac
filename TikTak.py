'''
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Front.RED + 'TEXT IN RED')

'''
class Game:
    def __init__(self):
        self.turn = 'O'
        self.limit = 0
        self.a = ' '
        self.b = ' '
        self.c = ' '
        self.d = ' '
        self.e = ' '
        self.f = ' '
        self.g = ' '
        self.h = ' '
        self.i = ' '
        self.end = False
        self.check = [0]
        l = True
        while l :# choosing X or O
            mark = input('\n \n For player one \n \n 1] O    2]X  \n Choose wisely.....  \n')
            print \
            ('-----------------------------------------------------------------------------------------------------------------------------------------------')
            if mark == '1' :
                self.SYM1 = 'O'
                self.SYM2 = 'X'
                l = False
            elif mark == '2' :
                self.SYM1 = 'X'
                self.SYM2 = 'O'
                l = False
            else :
                print('Enter a valid input [1 / 2]')

        print("\n")
        # SHOWS THE POSITIONS
        print("These are the positions")
        print(

            '     | ' + '   | ' + '\n'
            + '  ' + '1' +           ' | ' + '2' + ' | ' + '3' + '\n'
                                                                 '----+---+----' + '\n'
            + "  " + '4' +  ' | ' + '5' +' | ' + '6' + '\n'
                                                       '----+---+----' + '\n'
            + '  ' + '7' + ' | ' + '8' + ' | ' + '9' + '\n'
                                                       '     | ' + '   | ' + '\n'

        )
        self.loop()

    def loop(self):    #  Looping till the game ends
        while not self.end:
            if (self.a == 'O' and self.b == 'O' and self.c == 'O') or (
                    self.d == 'O' and self.e == 'O' and self.f == 'O') or (
                    self.g == 'O' and self.h == 'O' and self.i == 'O') or (
                    self.a == 'O' and self.d == 'O' and self.g == 'O') or (
                    self.b == 'O' and self.e == 'O' and self.h == 'O') or (
                    self.c == 'O' and self.f == 'O' and self.i == 'O') or (
                    self.a == 'O' and self.e == 'O' and self.i == 'O') or (
                    self.c == 'O' and self.e == 'O' and self.g == 'O'):
                self.winner = 'O'
                self.end = True
            elif (self.a == 'X' and self.b == 'X' and self.c == 'X') or (
                    self.d == 'X' and self.e == 'X' and self.f == 'X') or (
                    self.g == 'X' and self.h == 'X' and self.i == 'X') or (
                    self.a == 'X' and self.d == 'X' and self.g == 'X') or (
                    self.b == 'X' and self.e == 'X' and self.h == 'X') or (
                    self.c == 'X' and self.f == 'X' and self.i == 'X') or (
                    self.a == 'X' and self.e == 'X' and self.i == 'X') or (
                    self.c == 'X' and self.e == 'X' and self.g == 'X'):
                self.winner = 'X'
                self.end = True

            if self.limit >= 9:
                self.end = True
            if self.end :
                self.endOfGame()
            if self.end == False:
                self.multiplayer()
    def multiplayer(self):# asking players to make their move

        if self.limit in (0, 2, 4, 6, 8):
            self.turn = self.SYM1
        else:
            self.turn = self.SYM2
        try:
            self.move = int(input("\n Enter your move: "))
        except ValueError:
            print('enter an integer')
            self.multiplayer()
        try:
            if self.check.index(self.move) :
                print('Haha not so fast \n')
                self.multiplayer()
            self.check.append(self.move)
        except ValueError:
            self.check.append(self.move)

        try:
            if self.move == 1:
                self.a = self.turn
            elif self.move == 2:
                self.b = self.turn
            elif self.move == 3:
                self.c = self.turn
            elif self.move == 4:
                self.d = self.turn
            elif self.move == 5:
                self.e = self.turn
            elif self.move == 6:
                self.f = self.turn
            elif self.move == 7:
                self.g = self.turn
            elif self.move == 8:
                self.h = self.turn
            elif self.move == 9:
                self.i = self.turn
            else:
                print('Enter a existing move')
                self.multiplayer()
        except ValueError:
            print('Enter a existing move')
            self.multiplayer()
        self.limit += 1
        self.output()

    def output(self):# Displaying the output
        if self.end == False :
            print(

                '      | ' + '  | ' + '\n'
                + '  ' + self.a + ' | ' + self.b + ' | ' + self.c + '\n'
                                                                    '----+---+----' + '\n'
                + "  " + self.d + ' | ' + self.e + ' | ' + self.f + '\n'
                                                                    '----+---+----' + '\n'
                + '  ' + self.g + ' | ' + self.h + ' | ' + self.i + '\n'
                                                                    '    | ' + '  | ' + '\n'
            )

        self.loop()

    def get_names(self):
        self.name1 = input("Enter the name of player one: ")
        print('\n')
        self.name2 = input("Enter the name of player two: ")

    def endOfGame(self):
        try:
            if self.winner == 'O':
                print('O gets the VICTORY')
            else:
                print('X gets the VICTORY')
        except AttributeError:
            print('Its a DRAW')

        print("THE END")

a = game()
play_again = True
while play_again :
    ask = input('Do you wanna play again? [Y/N]')
    ask = ask.upper()
    if ask == 'Y':
        a = game()
    else :
        play_again = False
        print("Thank you for playing")
