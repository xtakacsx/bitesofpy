WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    r1 = (WHITE + BLACK) * int((size / 2)) + "\n"
    r2 = (BLACK + WHITE) * int((size / 2)) + "\n"
    print((r1 + r2) * int((size / 2)))
