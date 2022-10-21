from numpy import row_stack


class Buscaminas():

    def __init__(self,rows,columns,bombs,caso1,caso2,show):

        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board = list()
        self.caso1 = None
        self.caso2 = None
        self.show = None
    

    def play(self,mov,col,row):

        if mov == 'undercover':
            self.show[row][col] = str(self.board[row][col])
        
        elif mov == 'flag':
            self.show[row][col] = 'F'

        for i in range(8):
            print(self.board[i]) 


        

    def win(self):
        



    

