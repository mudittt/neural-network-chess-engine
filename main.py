import chess
import chess.pgn
import serialise
import valuation

gm=0
pgn = open("./sampledata.pgn")
while (True):
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    board = game.board()
    
    for i, move in enumerate(game.mainline_moves()):
        print("processing game %g move %i" % (gm, i))
        board.push(move)
        ser = serialise.serialise(board)
        # very slow
        turn, val = valuation.evaluate_position(board) 
    gm=gm+1