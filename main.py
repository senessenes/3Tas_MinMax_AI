import pygame
import os
import math
pygame.init()
sayi=0

BG=pygame.image.load(os.path.join("Assets", "background.jpg"))
BEYAZ_PUL_IMAGE=pygame.image.load(os.path.join("Assets", "png.png"))
SIYAH_PUL_IMAGE=pygame.image.load(os.path.join("Assets", "siyahpul.png"))

text = ''
font = pygame.font.SysFont("calibri.ttf", 48)
img = font.render(text, True, (255,0,0))

rect = img.get_rect()
WIDTH,HEIGHT=700,700
board=[["_","_","_"],
       ["_","_","_"],
        ["_","_","_"]]


sira="b"
kazanan=""
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("3 Tas")

pul_pozisyonlari=[
    [[50,50],[315,50],[550,50]],
    [[50,315],[315,315],[550,315]],
    [[50,580],[315,580],[550,580]]
]
siyah_pullar=[]
beyaz_pullar=[]


START_BEYAZ_X,START_BEYAZ_Y=450,200

START_SIYAH_X,START_SIYAH_Y=450,200
def pul():

    if(sira=="b"):
        return BEYAZ_PUL_IMAGE
    if(sira=="s"):
        return SIYAH_PUL_IMAGE
def possible_moves_once(board):
    moves=[]


    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(move_possible([i+1,j+1],0)==True):
                moves.append([i+1,j+1])
    return moves

def possible_moves_sonra(board,renk):
        moves = []


        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if (board[i][j]==renk):

                    for k in range(0, len(board)):
                        for l in range(0, len(board[k])):
                            if (move_possible([k+1,l+1], [i+1,j+1]) == True):
                                moves.append([[i+1, j + 1],[k+1,l+1]])


        return moves





beyaz_pul_pozisyonlari=[]
siyah_pul_pozisyonlari=[]
def drawScreen():




    WIN.blit(BG,(0,0))
    for i in range(0, len(beyaz_pullar)):
        WIN.blit(beyaz_pullar[i], tuple(beyaz_pul_pozisyonlari[i]))
    for i in range(0, len(siyah_pullar)):
        WIN.blit(siyah_pullar[i], tuple(siyah_pul_pozisyonlari[i]))
    if (kazanan == "b"):
        text = "Beyaz Kazandı"
        img = font.render(text, True, (255, 0, 0))
        WIN.blit(img, (250, 20))

    elif (kazanan == "s"):

        text = "Siyah Kazandı"
        img = font.render(text, True, (255, 0, 0))
        WIN.blit(img, (250, 20))




    pygame.display.update()


def is_finished(board):
    global kazanan
    columns=[[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]]]
    for i in columns:
        if i==["b","b","b"]:
            kazanan="b"
            return True
        elif i==["s","s","s"]:
            kazanan="s"
            return True
    for i in board:
        if i==["b","b","b"]:
            kazanan="b"
            return True
        elif i==["s","s","s"]:
            kazanan="s"
            return True
    return False

def comp_is_finished(board):
    global kazanan
    columns=[[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]]]
    for i in columns:
        if i==["b","b","b"]:

            return "b"
        elif i==["s","s","s"]:

            return "s"
    for i in board:
        if i==["b","b","b"]:

            return "b"
        elif i==["s","s","s"]:

            return "s"
    return False
def isDraw(board):
    for i in board:
        for j in i:
            if j=="_":
                return False
    if comp_is_finished(board)==False:
        return True
    return False







def move_possible(yer,tas):
    if(tas==0):
        if (not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], beyaz_pul_pozisyonlari)) and not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], siyah_pul_pozisyonlari))):
            return True
        return False
    else:
        if(abs(int(yer[0])-int(tas[0]))>1 or abs(int(yer[1])-int(tas[1]))>1):
            return False
        elif (abs(int(yer[0]) - int(tas[0])) > 0 and abs(int(yer[1]) - int(tas[1])) > 0):
            return False
        else:
            if (not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], beyaz_pul_pozisyonlari)) and not (icindemi(pul_pozisyonlari[int(yer[0]) - 1][int(yer[1]) - 1], siyah_pul_pozisyonlari))):

                return True

            return False




def compMove():
    bestScore=-1000
    bestMove=[]
    if(len(siyah_pullar)<3):

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if(board[i][j])=="_":
                    board[i][j]="s"
                    siyah_pullar.append(pul())
                    score=miniMax(board,0,False,len(siyah_pullar))
                    siyah_pullar.pop(len(siyah_pullar)-1)

                    board[i][j]="_"
                    if(score>bestScore):
                        bestScore=score


                        bestMove=[i,j]


        board[int(bestMove[0])][int(bestMove[1])] = "s"
        return bestMove
    else:
        best_score=-1000

        best_move = [[], []]
        possible_moves = possible_moves_sonra(board, "s")
        for i in possible_moves:
            tas = i[0]
            tas[0] -= 1
            tas[1] -= 1
            yer = i[1]
            yer[0] -= 1
            yer[1] -= 1

            board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
            score = miniMax(board, 4, False,len(siyah_pullar))
            board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
            if (score > best_score):
                best_score = score
                best_move = i

        return best_move







def miniMax(board,depth,isMaximizing,length):



    if(length>=3):
        if comp_is_finished(board) == "s":
            return 100
        elif comp_is_finished(board) == "b":
            return -100
        elif depth <= 0:

            return 0
        else:
            if(isMaximizing):
                best_score = -1000
                best_move = [[], []]
                possible_moves = possible_moves_sonra(board, "s")
                for i in possible_moves:
                    tas = i[0]
                    tas[0] -= 1
                    tas[1] -= 1
                    yer = i[1]
                    yer[0] -= 1
                    yer[1] -= 1
                    board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
                    siyah_pullar.append(pul())
                    score = miniMax(board, depth-1, False,len(siyah_pullar))
                    siyah_pullar.pop(len(siyah_pullar)-1)
                    board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
                    if (score > best_score):
                        best_score = score
                        best_move = i
                return best_score
            else:
                best_score = 800

                possible_moves = possible_moves_sonra(board, "b")
                for i in possible_moves:
                    tas = i[0]
                    tas[0] -= 1
                    tas[1] -= 1
                    yer = i[1]
                    yer[0] -= 1
                    yer[1] -= 1
                    board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
                    score = miniMax(board, depth-1, True,len(siyah_pullar))
                    board[tas[0]][tas[1]], board[yer[0]][yer[1]] = board[yer[0]][yer[1]], board[tas[0]][tas[1]]
                    if (score < best_score):
                        best_score = score

                return best_score
    else:
        if comp_is_finished(board) == "s":
            return 100
        elif comp_is_finished(board) == "b":
            return -100
        elif isDraw(board):
            return 0
        else:
           if isMaximizing:
               bestScore = -1000

               for i in range(0, len(board)):
                   for j in range(0, len(board[i])):
                       if (board[i][j]) == "_":
                           board[i][j] = "s"
                           siyah_pullar.append(pul())
                           score = miniMax(board, 0, False,len(siyah_pullar))
                           siyah_pullar.pop(len(siyah_pullar)-1)
                           board[i][j] = "_"
                           if (score > bestScore):
                               bestScore = score

               return bestScore




           else:
               bestScore = 800

               for i in range(0, len(board)):
                   for j in range(0, len(board[i])):
                       if (board[i][j]) == "_":

                           board[i][j] = "b"

                           score = miniMax(board, 0, True,len(siyah_pullar))
                           board[i][j] = "_"
                           if (score < bestScore):
                               bestScore = score

               return bestScore







def icindemi(array1,array2):
    for i in array2:
        for j in i:
            if j==array1:
                return True
    return False
def main():
    secili=False
    yer=[]
    tas=[]
    pygame.init()
    run = True
    global sira
    clock=pygame.time.Clock()
    clock.tick(60)



    while run:




        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                run = False
            if event.type== pygame.MOUSEBUTTONUP:
                enyakin=[0,0]
                for i in range(0,len(pul_pozisyonlari)):
                    for j in range(0,len(pul_pozisyonlari[i])):
                        if math.dist(pul_pozisyonlari[i][j],list(pygame.mouse.get_pos()))<math.dist(pul_pozisyonlari[enyakin[0]][enyakin[1]],list(pygame.mouse.get_pos())):
                            enyakin=[i,j]
                if(len(beyaz_pullar)<3):
                    yer=enyakin

                    if(move_possible([yer[0]+1,yer[1]+1],0)):
                        beyaz_pul_pozisyonlari.append([pul_pozisyonlari[int(yer[0])][int(yer[1])]])

                        beyaz_pullar.append(pul())
                        board[int(yer[0])][int(yer[1])] = "b"
                        print(board[0])
                        print(board[1])
                        print(board[2])

                        sira = "s"
                        print(enyakin)
                else:
                    if(secili)==False:
                        tas=enyakin
                        secili=True
                    else:
                        yer=enyakin
                        print("Yer:"+str(yer[0])+str(yer[1]))
                        print("Taş:"+str(tas[0])+str(tas[1]))

                        print("girdi")
                        if (move_possible([yer[0] + 1, yer[1] + 1], [tas[0]+1,tas[1]+1])):
                            for i in range(0, len(beyaz_pul_pozisyonlari)):
                                for j in beyaz_pul_pozisyonlari[i]:
                                    if j == pul_pozisyonlari[int(tas[0])][int(tas[1])]:
                                        beyaz_pul_pozisyonlari[i][0] = pul_pozisyonlari[int(yer[0])][
                                        int(yer[1])]
                                        board[int(yer[0])][int(yer[1])], board[int(tas[0])][
                                            int(tas[1])] = board[int(tas[0])][int(tas[1])], \
                                                                   board[int(yer[0])][int(yer[1])]

                                        sira = "s"
                            secili=False

        if sira == "s":
            if (len(siyah_pullar) >= 3):

                hamle = compMove()
                tas = hamle[0]

                yer = hamle[1]

                for i in range(0, len(siyah_pul_pozisyonlari)):

                    for j in siyah_pul_pozisyonlari[i]:

                        if j == pul_pozisyonlari[int(tas[0])][int(tas[1])]:
                            siyah_pul_pozisyonlari[i][0] = pul_pozisyonlari[int(yer[0])][int(yer[1])]
                            board[int(yer[0])][int(yer[1])], board[int(tas[0])][int(tas[1])] = board[int(tas[0])][
                                                                                                   int(tas[1])], \
                                                                                               board[int(yer[0])][
                                                                                                   int(yer[1])]
                            print(board[0])
                            print(board[1])
                            print(board[2])

                            sira = "b"


            else:

                yer = compMove()
                print(yer)

                if (move_possible([int(yer[0]) + 1, int(yer[1]) + 1], 0)):
                    siyah_pul_pozisyonlari.append([pul_pozisyonlari[yer[0]][yer[1]]])

                    siyah_pullar.append(pul())
                    board[int(yer[0])][int(yer[1])] = "s"
                    print(board[0])
                    print(board[1])
                    print(board[2])

                    sira = "b"

        drawScreen()













    pygame.quit()














if __name__=="__main__":
    main()

