from tkinter import Tk, Button, Frame

class GameState (object):
    ''' Класс хранящий состояние игры. Текущий ход, очки, имена игроков и т.п.'''
    CROSS = 1
    NULL = 2

    def __update_current_label(self):
        self.current_label = self.CROSS_LABEL if self.isCross else self.NULL_LABEL

    def start(self):
        self.field = [[0]*self.field_width for i in range(self.field_height)]
        print(*self.field, sep = '\n') # отладка

    def __init__(self, **config):
        super().__init__()
        self.isCross = True # крестики ходять?
        self.CROSS_LABEL = '✗'
        self.NULL_LABEL = 'Ѻ'
        self.__update_current_label()
        self.field_width = 3
        self.field_height = 3
        if 'field_width' in config and 'field_height' in config:
            self.field_width = config['field_width']
            self.field_height = config['field_height']
        self.start()


    def __next_move(self):
        self.isCross = not self.isCross
        self.__update_current_label()
    def make_move (self, row:int, col:int):
        self.field[row][col] = self.CROSS if self.isCross else self.NULL
        print(*self.field, sep = '\n') # отладка
        self.__next_move()

class GameFieldButton (Button) :

    def __make_move(self):
        if self.disable:
            return
        self['text'] = self.game.current_label # берем крестик или нолик
        self.disable = True # отключаем
        self.game.make_move(*self.position) # сделать ход
        self.disable = False

    def __init__(self, parent, game_state: GameState, pos_x, pos_y):
        self.game = game_state
        self.disable = False
        self.position = pos_x, pos_y
        super().__init__(parent, text=' ',
                         fg = '#fff',
                         bg = '#01a1a1',
                         font = ('Arial', 24, 'bold'),
                         width =2,
                         height = 1,
                         command = self.__make_move)


class GameField(Frame) :
    ''' Виджет генерирующий поле с кнопками, заданного размера'''
    def __init__(self, parent, game: GameState):
        super().__init__(parent)
        for row in range(game.field_width):
            for col in range(game.field_height):
                GameFieldButton(self, game, row, col).grid(row = row, column = col)


game_state = GameState()
root = Tk()
field = GameField(root, game_state)
field.pack()

root.mainloop()
