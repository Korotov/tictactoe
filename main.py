from tkinter import Tk, Button, Frame

class GameState (object):
    ''' Класс хранящий состояние игры. Текущий ход, очки, имена игроков и т.п.'''
    def __update_current_label(self):
        self.current_label = self.CROSS_LABEL if self.isCross else self.NULL_LABEL

    def __init__(self):
        super().__init__()
        self.isCross = True # крестики ходять?
        self.CROSS_LABEL = '✗'
        self.NULL_LABEL = 'Ѻ'
        self.__update_current_label()

    def next_move(self):
        self.isCross = not self.isCross
        self.__update_current_label()

class GameFieldButton (Button) :

    def __make_move(self):
        if self.disable:
            return
        self['text'] = self.game.current_label # берем крестик или нолик
        self.disable = True # отключаем
        self.game.next_move() # следующий ход
        self.disable = False

    def __init__(self, parent, game_state: GameState):
        self.game = game_state
        self.disable = False
        super().__init__(parent, text=' ',
                         fg = '#fff',
                         bg = '#01a1a1',
                         font = ('Arial', 24, 'bold'),
                         width =2,
                         height = 1,
                         command = self.__make_move)


class GameField(Frame) :
    ''' Виджет генерирующий поле с кнопками, заданного размера'''
    def __init__(self, parent, game, width = 3, height = 3):
        super().__init__(parent)
        for row in range(height):
            for col in range(width):
                GameFieldButton(self, game).grid(row = row, column = col)


game_state = GameState()
root = Tk()
field = GameField(root, game_state)
field.pack()

root.mainloop()
