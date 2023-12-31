import random


def printCard(c):
    for i in c:  # 根據花色進行分別
        if i // 13 == 0:
            print(chr(9824), end='')  # 黑桃
        elif i // 13 == 1:
            print(chr(9829), end='')  # 愛心
        elif i // 13 == 2:
            print(chr(9830), end='')  # 鑽石
        else:
            print(chr(9827), end='')  # 梅花

        if i % 13 == 0:  # index = 0-12 代表黑桃 A ,2,3,4,5,6,7,8,9,10,11,12,13
            print('A', end=' ')
        elif i % 13 == 10:  # index = 13-25 代表愛心A ,2,3,4,5,6,7,8,9,10,11,12,13
            print('J', end=' ')
        elif i % 13 == 11:
            print('Q', end=' ')
        elif i % 13 == 12:
            print('K', end=' ')
        else:
            print(i % 13 + 1, end=' ')
    print()


def printMessage():
    print('玩家的牌：', end='')
    printCard(playerCard)
    print('玩家的牌面點數：', sum(playerPoint))
    print('莊家的牌：', end='')
    printCard(dealerCard)
    print('莊家的牌面點數：', sum(dealerPoint))
    print('----------------------------------')


def cardPoint(x):  # index = 0 ~ 51 , 代表黑桃、愛心、鑽石、梅花
    if x % 13 == 0:  # A -> 11點
        return 11
    elif x % 13 > 9:  # x = index =  J , Q , K -> 10點
        return 10
    else:
        return x % 13 + 1  # x = index = 0 ~ 9 , 代表牌數2~10
        # 所以 x = 9 % 13 是index =  9 , 9 + 1 = 10(牌數)


def deal(gamerCard, gamerPoint):
    temp = card.pop()  # 從一副撲克牌中抽取牌數 ,隨機抽撲克牌且不能重複 , 用pop
    gamerCard.append(temp)  # 玩家或電腦的牌
    gamerPoint.append(cardPoint(temp))  # 紀錄玩家或電腦現在一共有幾點


card = list(range(0, 52))  # 隨機選牌
random.shuffle(card)  # 隨機進行排列

playerCard = []
playerPoint = []
dealerCard = []
dealerPoint = []

# 發牌
for i in range(2):  # 預設玩家或莊家電腦都是2張牌
    deal(playerCard, playerPoint)

deal(dealerCard, dealerPoint)

printMessage()

while True:
    ans = input('玩家要加牌嗎(Y/N)?')
    if ans == 'N' or ans == 'n':
        break
    deal(playerCard, playerPoint)  # 回答不是N的話就會新增新的牌
    if sum(playerPoint) > 21:  # 檢查玩家的牌面總點數是否超過21點。
        if 11 in playerPoint:  # 檢查玩家的牌中是否有A（代表11點）。
            ans_1 = input('玩家要把A換成11嗎(Y/N)?')
            if ans_1 == 'N' or ans_1 == 'n':
                playerPoint[playerPoint.index(11)] = 1  # playerPoint.index(11) -> 回傳11這個數值在0~51的index, 所以回傳index = 11
                # 將第一張A的點數從11改為1，以防止總點數超過21點。此處假設第一張A即可避免爆牌。
                # 舉例:playerPoint 是一個包含玩家手牌點數的清單（例如 [2, 6, 11]，其中11代表黑桃A）
                # 檢查是否有11（代表黑桃A）在playerPoint中，
                # 如果是，進行下一步。
                # 使用
                # playerPoint.index(11)
                # 找到第一張黑桃A的索引位置，假設索引位置為2。
                # 將索引為2的黑桃A的點數從11更改為1，這樣列表會從[2, 6, 11]  變成  [2, 6, 1]。
                # printMessage() 印出更改後的玩家牌面及點數。
                printMessage()  # 更改後再印出
            else:
                playerPoint[playerPoint.index(11)] = 11
                if sum(playerPoint) > 21:
                    print('玩家爆牌，莊家獲勝'"玩家:", sum(playerPoint), "莊家電腦:", sum(dealerPoint), end='')
                    break
                # printMessage()  # 更改後再印出
        else:
            printMessage()  # 爆牌無需更改直接印出
            print('玩家爆牌，莊家獲勝')
            break
    else:
        printMessage()

if sum(playerPoint) < 22:
    while sum(dealerPoint) < 17:
        # 一旦莊家的手牌點數達到17或更高時，根據遊戲規則，通常莊家就不再需要繼續抽牌，因為17點已經被認為是一個相對安全的總和。
        # 這樣的設定也是基於統計學和機率學，給出了較為理想的莊家行動策略。
        deal(dealerCard, dealerPoint)
        if sum(dealerPoint) > 21:
            if 11 in dealerPoint:
                dealerPoint[dealerPoint.index(11)] = 1  # 將第一張A的點數從11改為1，以防止總點數超過21點。此處假設第一張A即可避免爆牌。
        printMessage()

    if sum(dealerPoint) > 21:
        print('莊家爆牌,玩家勝利', "玩家:", sum(playerPoint), "莊家電腦:", sum(dealerPoint), end='')
    elif sum(playerPoint) > sum(dealerPoint):
        print('玩家勝利', "玩家:", sum(playerPoint), "莊家電腦:", sum(dealerPoint), end='')
    elif sum(playerPoint) < sum(dealerPoint):
        print('莊家勝利', "玩家:", sum(playerPoint), "莊家電腦:", sum(dealerPoint), end='')
    elif sum(playerPoint) == sum(dealerPoint):
        print('和局', "玩家:", sum(playerPoint), "莊家電腦:", sum(dealerPoint), end='')
