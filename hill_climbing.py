def steepest_hill(board):
  moves = {}
  for col in range(len(board)):
    best_move = board[col]
     
    for row in range(len(board)):
      if board[col] == row:
        continue
       
      board_copy = list(board)
      
      board_copy[col] = row
      moves[(col,row)] = get_h_cost(board_copy)
   
  best_moves = []
  h_to_beat = get_h_cost(board)
  for k,v in moves.iteritems():
    if v < h_to_beat:
      h_to_beat = v
       
  for k,v in moves.iteritems():
    if v == h_to_beat:
      best_moves.append(k)
   
  
  if len(best_moves) > 0:
    pick = random.randint(0,len(best_moves) - 1)
    col = best_moves[pick][0]
    row = best_moves[pick][1]
    board[col] = row
   
  return board