import chess
import chess.pgn
import numpy as np
import pandas as pd


"""
If we just see the tensors in our terminal,
We will see the board position from the black's perspective

00th 8x8 -> white pawns
01th 8x8 -> white rooks
02th 8x8 -> white knights
03th 8x8 -> white bishops
04th 8x8 -> white queens
05th 8x8 -> white king
06th 8x8 -> black pawns
07th 8x8 -> black rooks
08th 8x8 -> black knights
09th 8x8 -> black bishops
10th 8x8 -> black queens
11th 8x8 -> black king
"""

# mapping for indexing purposes
connect = {
    'P':0,
    'R':1,
    'N':2,
    'B':3,
    'Q':4,
    'K':5,
    'p':6,
    'r':7,
    'n':8,
    'b':9,
    'q':10,
    'k':11
}

def serialise(board):
    ser = np.zeros((12,8,8))
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            piece = str(piece).strip()
            ser[connect.get(piece)][i//8][i%8] = 1

    ser=np.reshape(ser,(-1))
    return ser.tolist()
    

gm=0
pgn = open("./sampledata.pgn")
col_dic={}
for i,j in enumerate(connect):
    for k in range(1, 65):
        col_dic[j+str(k)]=[]

df=pd.DataFrame(data=col_dic)
while (True):
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    board = game.board()
    for i, move in enumerate(game.mainline_moves()):
        print("processing game %g move %i" % (gm, i))
        board.push(move)
        df.loc[len(df)]=(serialise(board))
    gm=gm+1

df.to_csv("temp.csv", index=False)