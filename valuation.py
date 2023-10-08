import chess.pgn
import chess.engine

def evaluate_position(board):
    if board is not None:
        with chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish") as engine:
            info = engine.analyse(board, chess.engine.Limit(depth=3))
            score = info["score"].relative.score()
            # avoiding relative scores by stockfish
            if board.turn == chess.BLACK:
                score = -score
            score = "{:.2f}".format(score/100)
            return score