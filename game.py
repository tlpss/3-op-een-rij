import random

class Game:
    def __init__(self):
        self._board=[0 for i in range(9)]
        self._pieces= {"empty":0,"o":1,"x":2}
        self._games_won=[0,0] #<x,o>
    
    def get_board_JSON_ready(self,succes=1):
        x_won=self.check_won(2)
        o_won=self.check_won(1)
        if x_won==2:
            self._games_won[0]+=1
            return {"board":self._board,"succes":succes,"won":x_won}
        elif o_won==1:
            self._games_won[1]+=1
            return {"board":self._board,"succes":succes,"won":o_won}
        else:
            return {"board":self._board,"succes":succes,"won":0}

    def get_position_from_JSON_args(self,args): 
        #return args  # test!!
        ret=int(args[0][0])
        return ret 

    def clear_board(self):
        self._board=[0 for i in range(9)]
        return self.get_board_JSON_ready()

    def get_number_of(self,piece_int):
        count=0
        for numb in self._board:
            if numb==piece_int:
                count+=1
        return count
    def check_tripple(self,index1,index2,index3,piece_int):
        return (self._board[index1]==self._board[index2] and self._board[index2]==self._board[index3] and self._board[index3]==piece_int)

    def check_won(self,piece_int):
        for i in range(3):
            if (self.check_tripple(3*i,3*i+1,3*i+2,piece_int) or self.check_tripple(i,i+3,i+6,piece_int)):
                return piece_int
        if (self.check_tripple(0,4,8,piece_int) or self.check_tripple(2,4,6,piece_int)):
            return piece_int
        return -1

    def remove_x(self,args):
        x_pos=self.get_position_from_JSON_args(args)
        if self._board[x_pos] != self._pieces["x"]:
            return self.get_board_JSON_ready(0)
        else: 
            self._board[x_pos]= self._pieces["empty"]
            return self.get_board_JSON_ready()

    def put_x(self,args):
        x_pos=self.get_position_from_JSON_args(args)
        if self._board[x_pos]==self._pieces["empty"]:
            self._board[x_pos]=self._pieces["x"]
            return self.get_board_JSON_ready(),1
        else:
            return self.get_board_JSON_ready(),0

    def put_and_remove_o(self):
        self._board[self.remove_and_set_random_new_pos_o()]=self._pieces["o"]
        return self.get_board_JSON_ready()
    
    def remove_and_set_random_new_pos_o(self):
        prev_index=10 # so that it is never equal to index if there has been no removal
        if self.get_number_of(1)==3:
            o_pos=[]
            for index in range(9):
                if self._board[index]==self._pieces["o"]:
                    o_pos.append(index)
            print(o_pos)
            random.shuffle(o_pos)
            prev_index=o_pos[0]
            self._board[o_pos[0]]=self._pieces["empty"]

        empty=[]
        for index in range(9): #put random "o"
            if self._board[index]==self._pieces["empty"] and index!= prev_index:
                empty.append(index)
        random.shuffle(empty)
        return empty[0] 



