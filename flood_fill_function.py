from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "#######............#..",
    ".................###..",
    "##################....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    # Implement your code here.
    # Assert inputs are of right format
    assert type(input_board[0]) == str
    width = len(input_board[0])
    for s in input_board:
        assert len(s) == width
        assert type(s) == str
    assert type(old) == str
    assert type(new) == str
    assert type(x) == int
    assert type(y) == int

    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board
    elif input_board[x][y] != old:
        return input_board
    else:
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        flood_fill(input_board, old, new, x + 1, y)
        flood_fill(input_board, old, new, x - 1, y)
        flood_fill(input_board, old, new, x, y + 1)
        flood_fill(input_board, old, new, x, y - 1)
    return input_board

modified_board = flood_fill(board, ".", "~", 5, 12)

for a in modified_board:
    print(a)