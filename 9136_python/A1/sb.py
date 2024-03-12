from random import choice, choices

#snakes
snake_h = 0
min_sh = 2 #inclusive
max_sh = 100 #exclusive
min_st = 0
num_s = 5

#ladders
min_la = 2 #inclusive
max_la = 100 #inclusive


snake_heads = choices(range(min_sh, max_sh), k=num_s)

snake_tails = []
for snake_head in snake_heads:
    snake_tails.append(choice(list(set(list(range(min_st, snake_h))) - set(snake_heads + snake_tails))))







print(snake_heads)

