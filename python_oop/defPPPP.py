def printBoard(board):
    print(board['top-L' + board['top-M' + board['top-R']]])
    print('----------')
    print(board['mid-L'] + '|' + board['mid'])