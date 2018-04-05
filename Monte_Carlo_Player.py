import random

class MonteCarloPlayer:  

    def __init__(self,number=100):
        self.number_of_simulations=number
        self.o_indices= []
        self.free_indices=[]
        self.orig_board=[]
        self.temp_board=[]
        self.added_temp_board=[]
        self.removed_temp_board=[]
        self.score= {} #(index_from,index_to): score

    def get_optimal_next_move(self,board):
        self.clear()
        self.orig_board=board[:]
        self.load_indices()
        if self.get_number_of(1,self.orig_board)<3:
            for index2 in self.free_indices:
                self.added_temp_board=self.orig_board[:]
                self.added_temp_board[index2]=1
                won=0
                for j in range(self.number_of_simulations):
                    self.temp_board=self.added_temp_board[:]
                    if self.check_won(1):
                        won+=1
                        continue
                    if self.play_and_return_winnner()==1:
                        won+=1
                self.score.update({(-1,index2):won})
        else:
            for index1 in self.o_indices:
                self.removed_temp_board=self.orig_board[:]
                self.removed_temp_board[index1]=0
                for index2 in self.free_indices:
                    self.added_temp_board=self.removed_temp_board[:]
                    self.added_temp_board[index2]=1
                    won=0
                    for j in range(self.number_of_simulations):
                        self.temp_board=self.added_temp_board[:]
                        if self.check_won(1):
                            won+=1
                            continue
                        if self.play_and_return_winnner()==1:
                            won+=1
                    self.score.update({(index1,index2):won})
        return max(self.score,key=self.score.get)
        
    def play_and_return_winnner(self):
        x=0
        y=0
        while( x==0 and y==0):
            self.remove_and_set_random_new_pos(2)
            x=self.check_won(2)
            self.remove_and_set_random_new_pos(1)
            y=self.check_won(1)
        return 2 if x==2 else 1

    def load_indices(self):
        #get possible indices to remove o
        for index1 in range(9):
            if self.orig_board[index1]==1:
                self.o_indices.append(index1)
        
        # get possible indices to put o
        for index2 in range(9):
            if self.orig_board[index2]==0:
                self.free_indices.append(index2)
           
    def remove_and_set_random_new_pos(self,piece):
            prev_index=10 # so that it is never equal to index if there has been no removal
            if self.get_number_of(piece,self.temp_board)==3: #remove random if necessary
                pos=[]
                for index in range(9):
                    if self.temp_board[index]==piece:
                        pos.append(index)
                random.shuffle(pos)
                prev_index=pos[0]
                self.temp_board[pos[0]]=0
            
            empty=[]
            for index in range(9): #put random 
                if self.temp_board[index]==0 and index!= prev_index:
                    empty.append(index)
            random.shuffle(empty)
            self.temp_board[empty[0]]=piece

    def get_number_of(self,piece_int,board):
        count=0
        for numb in board:
            if numb==piece_int:
                count+=1
        return count
        
    def check_tripple(self,index1,index2,index3,piece_int):
        return (self.temp_board[index1]==self.temp_board[index2] and self.temp_board[index2]==self.temp_board[index3] and self.temp_board[index3]==piece_int)

    def check_won(self,piece_int):
        for i in range(3):
            if (self.check_tripple(3*i,3*i+1,3*i+2,piece_int) or self.check_tripple(i,i+3,i+6,piece_int)):
                return piece_int
        if (self.check_tripple(0,4,8,piece_int) or self.check_tripple(2,4,6,piece_int)):
            return piece_int
        return 0
    def clear(self):
        self.o_indices= []
        self.free_indices=[]
        self.orig_board=[]
        self.temp_board=[]
        self.added_temp_board=[]
        self.removed_temp_board=[]
        self.score= {} #(index_from,index_to): score

if (__name__=="__main__"):
    player=MonteCarloPlayer()
    print("test1")
    print(player.get_optimal_next_move([0,2,0,0,0,0,0,0,0]))
    print("test2")
    print(player.get_optimal_next_move([1,0,1,0,2,1,2,0,2]))