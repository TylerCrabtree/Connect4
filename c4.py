# Tyler Crabtree
# Csci 121
# Assignment 9 

import random # for win choices 

class Board:
    def __init__( self, width, height ): 
        self.width = width 
        self.height = height 
        self.data = [] # this will be the board (b)
 
        for row in range( self.height ): 
            boardRow = [] 
            for col in range( self.width ): 
                boardRow += [' '] 
            self.data += [boardRow] 


    def __repr__(self):  # designs board
        s = '' 
        for row in range( self.height ):  #makes rows
            s += '|' 
            for col in range( self.width ): 
                s += self.data[row][col] + '|' # adds columns
            s += '\n' 
        s+= '__'*self.width + '\n' 
        
        for col in range(self.width):
            s+= ' ' + str(col%10) 
        return s # return it 
    
    
    def addMove(self, col, ox ):
        if self.allowsMove(col):
            for row in range( self.height ): 
                if self.data[row][col] != ' ': 
                    self.data[row-1][col] = ox # add the space character        
                    return 
            self.data[self.height-1][col] = ox 
        
    def allowsMove(self,col): #checks to see move is allowed.
        if 0 <= col < self.width:
            return self.data[0][col] == ' '
    
    
    def clear(self): # clears board
	for row in range(self.height):
	    for col in range(self.width):
		self.data[row][col] = ' '
	return 
	    
    def delMove(self, col): # deletes one move
	    for row in range( self.height ):
		if self.data[row][col] != ' ':
		    self.data[row][col] = ' '
		    return
	    #self.data[self.height][col] = ' '
	    
    def isFull(self): # basically checks to see if a draw	    
	for col in range( self.width ):
		if self.data[0][col] == ' ':
		    return False
	return True 
	    
    def setBoard( self, moveString ): # creates specific board
	nextCh = 'X'
	for colString in moveString:
	    col = int(colString)
	    if 0 <= col <= self.width:
		self.addMove(col, nextCh)
	    if nextCh == 'X':
		nextCh = 'O'
	    else:
		nextCh = 'X'    
    
    def winsFor(self, ox):
	
	
		
	for row in range(0,self.height-3): #vertical wins
	    for col in range(0,self.width):
		if self.data[row][col] == ox:
		    if self.data[row+1][col] == ox: 
			if self.data[row+2][col] == ox:
			    if self.data[row+3][col] == ox: 
				return True 
	
	for row in range(0,self.height): #hoizontal wins
	    for col in range(0,self.width-3):
		if self.data[row][col] == ox:
		    if self.data[row][col+1] == ox:
			if self.data[row][col+2] == ox:
			    if self.data[row][col+3] == ox:
				return True
	
	for row in range(0,self.height-3): #Downward slope / 
	    for col in range(3,self.width):
		if self.data[row][col] == ox:
		    if self.data[row+1][col-1] == ox:
			if self.data[row+2][col-2] == ox:
			    if self.data[row+3][col-3] == ox: 
				return True
			    
	for row in range(0,self.height-3): #Upward slope \
	    for col in range(0,self.width-3):
		if self.data[row][col] == ox:
		    if self.data[row+1][col+1] == ox:
			if self.data[row+2][col+2] == ox:  
			    if self.data[row+3][col+3] == ox: 
				return True	
	return False 
    
 
    
    def input(self,ox): # basic layout 
	while True:
	    game = input(ox + ", choose your destiny: ")
	    if self.allowsMove(game):
		return game    
    
    def hostGame(self): #actual game
	print self
	while True:
	    game = self.input('X')
	    self.addMove(game, 'X')
	    print self
	    if self.winsFor('X'):
		print random.choice([ "X is vitorious!", "X, take your pride!",\
		                      "X, you chose wisely", "Enjoy the taste of victoy X" ])
		b.clear()
		break
	    
	    game = self.input('O')
	    self.addMove(game,'O')
	    print self
	    if self.winsFor('O'):
		print random.choice([ "O, I do believe you won ", "O, you are unstoppable",\
		                      "O, glory awaits for you.", "O is the champion!"])
		b.clear()
		break
	    if self.isFull():
		print random.choice([ "It's a draw",  "Sometimes a tie is worse than a loss" , \
		                      "No one is the winner, that's life", "Maybe you should try again?"])
		                                            
		b.clear()
		break  
	    
	    
	    
	    
	    
	    
    def playGameWith(self,aiPlayer): #actual game
	print self
	while True:
	    checker = 'X'
	    game = self.input('X')
	    self.addMove(game, 'X')
	    print self
	    if self.winsFor('X'):
		print random.choice([ "X is vitorious!", "X, take your pride!",\
	                              "X, you chose wisely", "Enjoy the taste of victoy X" ])
		b.clear()
		break
	    
	    colNumber = aiPlayer.nextMove(self) #get move
	    self.addMove(colNumber,'O') #add move
	    print self
	    if self.winsFor('O'):
		print random.choice([ "O, is the taste of victory sweet?", "O, you are unstoppable",\
	                              "O, glory awaits for you.", "O is the champion!"])
		b.clear()
		break
	    if self.isFull():
		print random.choice([ "It's a draw",  "Sometimes a tie is worse than a loss" , \
	                              "No one is the winner, that's life", "Maybe you should try again?"])
							    
		b.clear()
		break 
	      
	    if checker == 'X':
		checker = 'O'
	    else: 
		checker = 'X'                
                
            
class Player:
    
    def __init__ (self,checker,ply):
        self.checker = checker
        self.ply = ply
	
    
        
    def nextMove(self, board):
        scores = self.scoresFor (board,self.checker,self.ply) 
	board.allowsMove(scores) 
        best = max(scores)
	#worst = random.choice(scores)
	#randomElement = random.choice[col]
	#randomScore = scores[col]
	
	for col in range(board.width):
	    """if randomScore == best:
		print "Player %s moves[%i]" % (self.checker,col) 
		return col"""			
	    
	    if best == scores[col]:
		#randomElement = random.choice[col]
		print "Player %s moves[%i]" % (self.checker,col) 
		return col		
		
	
# accumulated new list and randomly pick column 
# read chp 14 and check python.prg
	
        
        
    def scoresFor(self,board,ox,depth):
        scoresList = []
       
        for col in range(board.width): # -1?
	    if board.allowsMove(col): # checks if that wins
		board.addMove(col,ox)
		if board.winsFor(ox): # if you win
		    scoresList += [100.0]
		elif depth <1: #ply is 1, append 50
		    scoresList += [50.0]
		else:
		    if ox == 'X':
			opp = 'O'
		    else:
			opp = 'X'
		    oppList = self.scoresFor(board,opp,depth-1) #recursive ply
		    bestOpp = max(oppList)
		    #worstOpp = min(oppList)
		    #randomElement = random.choice(oppList)
		    invertedOppScore = 100.0 - bestOpp
		    scoresList += [invertedOppScore] 
		board.delMove(col) # gets rid of testing move
	    else:
		scoresList += [-1.0]
	return scoresList	    
	    

b = Board(7,6)
p = Player('O',4) 
b.playGameWith(p)

























	    
	    
"""class player:
    #ply = ?
    
    def __init__( self, ox, col ): 
	return
       # self.width = width 
        #self.height = height 
        #self.data = [] # this will be the board (b)
 
        #for row in range( self.height ): 
         #   boardRow = [] 
          #  for col in range( self.width ): 
           #     boardRow += [' '] 
            #self.data += [boardRow] 

    def nextMove(self,board): 
	scores = self.scores(board,self.ox,self.ply)
	moves = [[scores[i],i] for i in range(len(scores))]
	best = max(moves)
	return best[i]
    def scoreFor(self,board,ox,depth):
	scorelist =[]
	for col in range(board.width): 
	    if b.addMove(col) == True:
		if b.winsFor(col) == True:
		    scores = 100
	else:
	    scores = scores - 1
	    #append (100.0-max(l))
    
    
    
    
    
    #for col in range(board.width)
	#if Board.allowsMove('O') == True:
	    #return Board.addMove('O') 
	       
"""	
"""	       
class Player:
    
    def __init__ (self,checker,ply):
        self.checker = checker
        self.ply = ply
        
    def nextMove(self, board):
        scores = self.scoresFor(board,self.checker,self.ply) 
        best = max(scores)
        move = best[1] 
        row = move[0]
        col = move[1]
        board.addMove(row,col,self.checker)
        print "Player %s moves[%i.%i]" % (self.checker,row,col)
        
        
    def scoresFor(self,board,ox,depth):
        scoreList = []
        moves = board.possibleMoves()
        for move in moves:
            row = move[0]
            col = move[1]
            board.addMove(row,col,ox)
            if board.winsFor(ox):
                scoresList += [[100.0,move]]
            elif depth <1:
                scoresList += [[50.0, move]]
            else:
                if ox == 'X':
                    opp = 'O'
                else:
                    opp = 'X'
                oppList = self.scoresFor(board,opp,depth-1)
                bestOpp = max(oppList)
                invertedOppScore = 100.0 - bestOpp[0]
                scoresList += [invertedOppScore, move] 
                
        return scoresList
        
    """
            
#t = ticTacToe(3)
#p = Player('O', 3)
#t.hostGame(p)	       
	       












'''
b.addMove(0,'x')
b.addMove(1,'x')
b.addMove(2,'x')
b.addMove(3,'x')
b.addMove(4,'x')
b.addMove(5,'x')
'''

#b.setBoard('000000')

#b.setBoard('01010101010')
        
#b.setBoard('01122123333')        
#b.setBoard('21221103131213')
#b.setBoard('00020131234')        
# for testing
#b.addMove(1,'X')
#print b
#print b.winsFor('X')