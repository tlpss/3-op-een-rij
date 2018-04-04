from game import Game

game= Game()

game.clear_board()
game.put_x(1)
game.put_and_remove_o()
game.put_x(4)
game.put_x(7)
print game.check_tripple(1,4,7,2)
print game.check_won(2)
