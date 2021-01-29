import random


class LotCard:
    def __init__(self, name_player: str, count_lines, count_bar_line):
        self.list_existing_bar = [i for i in range(1, 91)]
        self.game = []
        self.card = ''
        self.name_player = name_player
        self.count_lines = count_lines
        self.count_bar_line = count_bar_line
        self.count_bar = self.count_lines * self.count_bar_line

        self.check_count_bar()
        self.create_card()

    def check_count_bar(self):
        if self.count_bar > 90:
            print('Количество боченков не должно превышать 90!')
            exit()
    
    def create_card(self):
        header_half = (self.count_bar_line * 4 - int(len(self.name_player)) // 2) * "-"
        header = '\n' + header_half + ' ' + self.name_player + ' ' + header_half
        footer = (len(header) - 1) * "-"
        self.card = header + '\n'
        self.game.append(self.card)
        for _ in range(self.count_lines):
            temp_list = []
            for _ in range(self.count_bar_line):
                temp_list.extend([self.list_existing_bar[0], ' '])
                self.list_existing_bar.pop(0)
            random.shuffle(temp_list)
            self.game.append(temp_list)
            for el in temp_list:
                self.card += f'{el:4}'
            self.card += '\n'
        self.card += footer
        self.game.append(footer)
        print(self.card)


class LotGame:
    def __init__(self, *args):
        self.args = args
        self.bag_barrels = [i for i in range(1, 91)]

    def change_card(self):
        for el_arg in self.args:
            string_card = el_arg[0]
            for el_line in range(1, len(el_arg[1:])):
                for el_str in el_arg[el_line]:
                    string_card += f'{el_str:4}'
                string_card += '\n'
            string_card += el_arg[-1]
            print(string_card)

    def start(self):
        while True:
            random_bar = random.randint(0, len(self.bag_barrels) - 1)
            print(f'\n\nНовый бочонок: {self.bag_barrels[random_bar]} (осталось {len(self.bag_barrels) - 1})')
            self.change_card()
            if input('Зачеркнуть цифру? (y/n) ') == 'n':
                break
            else:
                for el_arg in self.args:
                    # print(el_arg)
                    for el in range(1, len(el_arg[1:])):
                        if self.bag_barrels[random_bar] in el_arg[el]:
                            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        print(el_arg[el])


# def start_game():
#     while True:
#         start = input('Want to start the game? y/n >>> ').lower()
#         if start == 'y':
#             break
#         elif start == 'n':
#             exit()

# name = input('Введите имя игрока >>> ')
# lines = int(input('Количество строк в карточке? >>> '))
# bar_inline = int(input('Количество боченков в строке? >>> '))


player = LotCard('Player', 3, 5)
computer = LotCard('Computer', 3, 5)
# start_game()

game = LotGame(player.game, computer.game)
game.start()
