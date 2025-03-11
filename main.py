import sys
import os.path
# Example : 
# rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1

last_board = None

def FEN_parser(fen):

    if(fen.count("/") < 9): return None

    try:
        return ["".join([(" " * int(space) if space.isdigit() else space)
        for space in row]) for row in fen.split(" ")[0].split("/")]
    except:
        print("Invalid FEN string")
        return None

def diff(before , after):

    #print(before , after)
    x1, y1 , x2, y2 = 0, 0, 0, 0
    for i in range(10):
        for j in range(9):
            if(before[i][j] != after[i][j]):
                if(before[i][j] != " " and after[i][j] == " "):
                    x1, y1 = 9-i, j
                else:
                    x2, y2 = 9-i, j

    return (x1, y1, x2, y2)
def command_parser(str):
    global last_board

    board = FEN_parser(str)

    if(board == None): return None

    if(last_board == None):
        last_board = board
        return None
    
    x1 , y1 , x2 , y2 = diff(last_board, board)
    print(f"moveXiangqiRecord(board, {x1}, {y1}, {x2}, {y2});")
    last_board = board

if __name__ == "__main__":  
    
    for argv in sys.argv[1:]:
        if argv == __file__.rsplit("/", 1)[1].split('.')[0]:
            continue
        if(os.path.isfile(argv)):
            with open(argv, "r") as f:
                lines = f.readlines()
                for line in lines:
                    command_parser(line)

