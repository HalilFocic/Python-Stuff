

import time
def validMove(x,y):
    if x<0 or x>7:
        return False
    if y<0 or y>7:
        return False
    return True
def solution(src,dest):
    rowMoves=[-2,-2,2,2,1,1,-1,-1]
    colMoves=[-1,1,-1,1,2,-2,2,-2]
    moves=0
    src_x= src//8
    src_y=src%8
    
    dest_x=dest//8
    dest_y=dest%8
    destination=(dest_x,dest_y)
    if src_x==dest_x and src_y ==dest_y:
        return 0
    search=True
    queue=[]
    new_queue=[(src_x,src_y)]
    visited = [(src_x,src_y)]
    while search:
        queue=new_queue
        new_queue=[]
        for item in queue:
            for move in range(0,len(rowMoves)):
                currentMove = (item[0]+rowMoves[move],item[1]+colMoves[move])
                if currentMove==destination:
                    return moves+1
                if validMove(currentMove[0],currentMove[1]) and currentMove not in visited:
                    new_queue.append(currentMove)
        moves+=1





# dobijamo odredjene kordinate
# Svaka destinacija je povezana sa odredjenim brojevima
# trazimo najkracu putanju
# Ubacimo pocetnu vrijednost u Queue i sirimo se na susjede dok ne nadjemo vrijednost
