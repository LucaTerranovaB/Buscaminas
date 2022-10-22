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


        

    def win(self,row,col,mov,cant):
        
        for i in range(8):
            for j in range(8):

                if self.board[i][j] == 'B' and self.board[i][j] == 'F':
                    cant += 1
                
        print(cant)

        if cant == self.bombs:
            return True

        else:
            return False

    def lose(self):

        for i in range(8):
            for j in range(8):

                if self.board[i][j] == 'B' and self.board[i][j] != 'F':

                    return True

                else: 

                    return False   
        

        

    def proximity_bomb(self):

        cant = 0

        for i in range(7):
            for j in range(7):

                if self.board[i][j]=="" and self.board[i-1][j] == 'B':
                    cant += 1
                
                elif self.board[i][j] == "" and self.board[i+1][j] == 'B':
                    cant +=1

                elif self.board[i][j] == "" and self.board[i][j-1] == 'B':
                    cant +=1

                elif  self.board[i][j] == "" and self.board[i][j+1] == 'B':
                    cant += 1
                
                elif self.board[i][j]=="" and self.board[i-1][j-1] == 'B':
                    cant += 1
                
                elif self.board[i][j]=="" and self.board[i-1][j+1] == 'B':
                    cant += 1

                elif self.board[i][j]=="" and self.board[i+1][j-1] == 'B':
                    cant += 1
                
                elif self.board[i][j]=="" and self.board[i+1][j+1] == 'B':
                    cant += 1

                if cant != 0:
                    self.board[i][j] = cant
                cant = 0    


    def set(self):
        self.board[4][3] = "B"
        self.board[3][4] = "B"