from random import shuffle,randint


def game(args):
    marked_fields={}
    for k, v in args:
        field_no = int(k.split("_")[1])
        val = int(v)
        marked_fields[field_no] = val
    remaining_fields = list(set(range(9))-set(marked_fields.keys()))
    shuffle(remaining_fields)
    if remaining_fields:
        box_index = remaining_fields[0]
    else:
        box_index = -1
    game_won=0 #status of game-> to be completed
    ret=box_index
    return {'board_index':2,'test':5}