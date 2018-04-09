def sim_annealing(board):
  temp = len(board)**2
  anneal_rate = 0.95
  new_h_cost = get_h_cost(board)
   
  while new_h_cost > 0:
    board = make_annealing_move(board,new_h_cost,temp)
    new_h_cost = get_h_cost(board)
    new_temp = max(temp * anneal_rate,0.01)
    temp = new_temp
    if steps >= 50000:
      break
 
def annealing_move(board,h_to_beat,temp):
  board_copy = list(board)
  found_move = False
 
  while not found_move:
    board_copy = list(board)
    new_row = random.randint(0,len(board)-1)
    new_col = random.randint(0,len(board)-1)
    board_copy[new_col] = new_row
    new_h_cost = get_h_cost(board_copy)
    if new_h_cost < h_to_beat:
      found_move = True
    else:
      delta_e = h_to_beat - new_h_cost
      accept_probability = min(1,math.exp(delta_e/temp))
      found_move = random.random() <= accept_probability
   
  return board_copy