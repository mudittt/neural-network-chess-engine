import chess.pgn
import chess.engine

def evaluate_position(board):
    if board is not None:
        with chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish") as engine:
            info = engine.analyse(board, chess.engine.Limit(depth=10))
            score = info["score"].relative.score()
            # 1 for white's turn
            turn = 0 if (board.turn == chess.BLACK) else 1
            
            # avoiding relative scores by stockfish
            if turn == 0:
                score = -score
            score = "{:.3f}".format(score/100)
            return turn, score