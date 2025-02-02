def create_board():
    board = ["       ",
             "       ",
             "       ",
             "       ",
             "       ",
             "       "]
    return board

def print_board(board):
    for row in board:
        i = 0
        print("|", end="")
        for x in row:
            print(row[i] + "|", end="")
            i += 1
        print()
        
def drop_piece(board, col, piece):
    for row in reversed(board):
        if row [col] == " ":
            row[col] = piece
            return True
    return False
        
 
def is_valid_column(board, col):
    if col<0:
        return False
    elif col >6: 
        return False
    elif board[0][col] != " ":
        return False
    else: 
        return True
    
def check_winner(board, piece):
    
    for row in (board):
        for h in range(4):
            if(row[h] == row[h+1] == row[h+2] == row[h+3]==piece):
                return True
                
    for i in range (7):
        for j in range(6):
            if(board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i]==piece):
                return True   
            
    for k in range(3,6):
        for l in range(4):
            if(board[k][l] == board[k-1][l+1] == board[k-2][l+2] == board[k-3][l+3]==piece):
                return True
    
    for m in range(3):
        for n in range(4):
            if(board[m][n] == board[m+n][l+n] == board[m+n][l+n] == board[m+n][l+n]==piece):
                return True
    
    return False
            
def main():
    turn = 0
    if(turn % 2 ==0):
        piece = "X"
    else: 
        piece = "O"
    board = create_board()
    print("Welcome to Connect 4")
    print_board(board)
    if check_winner(board, piece):
        print("Player " + piece + " wins")
    
            
    
     
            
main()
