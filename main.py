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

class FieldBtn (Button) :
    def __init__(self, parent, game_state: GameState):
        self.game = game_state
        super().__init__(parent, text='', command = self.__make_move)
        self.disable = False
    def __make_move(self):
        if self.disable:
            return
        self['text'] = self.game.current_label # берем крестик или нолик
        self.disable = True # отключаем
        game.next_move() # следующий ход

class GameField(Frame) :
    ''' Виджет генерирующий поле с кнопками, заданного размера'''
    pass
game_state = GameState()
root = Tk()
root.mainloop()