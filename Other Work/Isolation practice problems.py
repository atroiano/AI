import copy
xlim= 3
ylim= 2
class GameState:

    def __init__(self):
        self._board = [[0]*ylim for _ in range(xlim)]
        self._board[xlim-1][ylim-1] = 1
        self._players = 1
        self._moves = [None, None]
        self._player_flg = [None, None]     
            
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
       if move not in get_legal_moves():
            assert 'Yo, your move is not valid'
        if self._players not in (1,2):
            assert 'Yo, your player is not valid'
        self._moves[self._players-1] = move
        if self._players == 1:
            self._player_flg[0] = 1
            self._players = 2
        else:
            self._player_flg[1] = 1
            self._players = 1
            
        game_copy = copy.deepcopy(self)
        game_copy._board[move[0]][move[1]] = 1 
        return game_copy
    
    def get_all_moves(self):
        self.valid_move=[]
        self._indices = [i for i, _ in enumerate(self._board)]
        for i in self._indices:
            for x in range(len(self._board[i])):
                if self._board[i][x] == 0:
                    self.valid_move.append((i,x))
        return(self.valid_move)
    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
            def get_legal_moves(self):
        """
        #get blank spaces
        #get the other players locations
        #if there is only one move. 
        self._avail_moves = []
        if (self._player_flg[self._players-1]==None):
            return self.get_all_moves()
    
        if (self._players == 1 and self._player_1_flg==None):
            for x in test2.get_all_moves():
                if x[1] == test2._moves[0][1] and test2._moves[0][0] in (x[0]):
                    self._avail_moves.append(x)
        #get all the moves in the row or column that are free
        #remoev anthing that is blocked
            return 'no good'
            #remove the moves that are block
        #return (self.valid_move)
        #get blank spaces
        #get the other players locations
        #if there is only one move. 
        
test = GameState()
test2=test.forecast_move((2,0))
test2._board 
test2._moves
test2._players
test2.get_legal_moves()
for i in test2.get_legal_moves():
    print (i)
test3=test2.forecast_move((0,0))
test3._board 
test3._moves
test3._players


valid_move = []
indices = [i for i, _ in enumerate(test2._board)]
for i in indices:
    for x in range(len(test2._board[i])):
        if test2._board[i][x] == 0:
            valid_move.append((i,x))
            
            
i,_ in enumerate(test2._board[1])

[[(i,x) for i, x in enumerate(row) if i == 0] for row in board] 

avail_moves =[x for x in test3.get_all_moves() if x[1]==test3._moves[test3._players-1][1]]
if test3._players == 1:
    avail_moves_up = [x for x in avail_moves if x[1]]
for x in test3.get_all_moves():
    if x[1] == test2._moves[test2._players-1][1]:
        avail_moves.append(x)
        if test2._moves[test2._players-1][0] < test2._moves[test2._players][0]:
            avail_moves_up = [x for x in avail_moves if test2._moves[test2._players][0]>x[0]]
        if test2._moves[test2._players-1][0] > test2._moves[test2._players][0]:
            avail_moves_up = [x for x in avail_moves if test2._moves[test2._players][0]<x[0]]
        

#        if test2._moves[test2._players-1][0] < test2._moves[test2._players][0]:
#            avail_moves_up = [x for x in avail_moves if x[0]<test2._moves[test2._players][0][0]]
#        if test2._moves[test2._players-1][0] > test2._moves[test2._players][0]:
#            avail_moves_up = [x for x in avail_moves if x[0]>test2._moves[test2._players][0][0]]
def cond(i):
    if i % 4 == 0: return 'four'
    elif i % 6 == 0: return 'six'


[(x[0],x[1]) for x in test3.get_all_moves() ]
    print(x)
    print(y)

avail_moves_up = [x for x in avail_moves if test2._moves[test2._players-1][0] < test2._moves[test2._players][0]]
avail_moves_up = [x for x in avail_moves if x[0] > test2._moves[test2._players][0]]

for x in test3.get_all_moves():
    print(x[0])