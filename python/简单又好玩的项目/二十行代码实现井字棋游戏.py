checkerboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(replace):
    print(checkerboard['top-L'] + '|' + checkerboard['top-M'] + '|' + checkerboard['top-R'])
    print('——' + '+' + '——')
    print(checkerboard['mid-L'] + '|' + checkerboard['mid-M'] + '|' + checkerboard['mid-R'])
    print('——' + '+' + '——')
    print(checkerboard['low-L'] + '|' + checkerboard['low-M'] + '|' + checkerboard['low-R'])
turn = 'X'
for i in range(9):
    printBoard(checkerboard)
    print('现在请'+ turn+ '出棋，请输入你的位置：')
    move = input()
    checkerboard[move] = turn
    if turn == 'X':
        turn = '0'
    else: turn = 'X'
    if i == 8:
        print('游戏结束，平棋')
