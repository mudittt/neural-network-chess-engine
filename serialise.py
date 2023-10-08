import chess
import chess.pgn
import numpy as np
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

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
    # 14 instead of 12
    ser = np.zeros((14,8,8))
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            piece = str(piece).strip()
            pieceindex = connect.get(piece)
            # for individual pieces
            ser[pieceindex][i//8][i%8] = 1
            # for all whites
            if pieceindex>=0 and pieceindex <=5:
                ser[12][i//8][i%8] = 1
            # for all blacks
            elif pieceindex>=6 and pieceindex <=11:
                ser[13][i//8][i%8] = 1

    ser = tf.constant(ser) # converting numpy array to a tensor
    return ser