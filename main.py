print("-" * 10, "Добро пожаловать в игру!", "-" * 10)
print("-" * 10, "В какую игру ты хочешь поиграть?", "-" * 10)
print("-" * 10, "Для игры в крестики-нолики нажми 1", "-" * 10)
print("-" * 10, "Для прохождения квеста нажми 2", "-" * 10)
print("-" * 10, "Для игры в города нажми 3", "-" * 10)
print("-" * 10, "Сделано Егором, Гришой и Колей", "-" * 10)
game_player = int(input())
if game_player == 1:
    print("-" * 10, "Игра Крестики-нолики для двух игроков", "-" * 10)
    print("-" * 10, "Сделано Егором, Гришой и Колей", "-" * 10)
    
    board = list(range(1,10))
    
    def draw_board(board):
        print("-" * 13)
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            print("-" * 13)
    def take_input(player_token):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token+"? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if(str(board[player_answer-1]) not in "XO"):
                    board[player_answer-1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
    
    def check_win(board):
        win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False
    
    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)
    main(board)
    
    input("Нажмите Enter для выхода!")
    
if game_player == 3:
    answer1=''
    answer2=''
    bukva=''
    next=True
    print("Чтобы закончить игру, напиши Все ")
    def end_game():
        print('Закончить игру?')
        a=input()
        if a=='Да' or a=='да':
            next=False
    def check(i):
        global bukva
        while i[-1]!=bukva and bukva!='':
            print('Не на ту букву!Введи заново')
            i=input()
    while next==True:
        print("Игрок 1, введи город на букву %s"% bukva)
        answer1=input()
        check(answer1)
        bukva=answer1[-1]
        print("Игрок 2, введи город на букву %s"% bukva)
        answer2=input()
        check(answer2)
        bukva=answer2[-1]
        end_game()    
if game_player == 2:
    print('Добро пожаловать в Квест.')
    print('Вы очнулись в незнакомом помещение')
    print('Перед вами 3 двери с номерами: 1, 2 или 3.')
    print('Дверь из которой можно выбраться - не крайняя, в какую пройдете?')
    otv1 = input()
    if otv1 == '3':
        print('Пройдя в эту дверь, она захлопнулась. Выхода нет. Game over.')
    elif otv1 == '1':
        print('Вы прошли в пропасть')
    if otv1 == '2':
        print('Вы в следующей комнате')
        print('Выход отсюда возможен через 2 двери.')
        print('Дверь справа под номером 1, дверь слева под номером 2,')
        print('над дверью слева написано: выход в двери под номером 2.')
        print('Выход справа или слева?')
        otv2 = input()
        if otv2 == 'справа':
            print('Вы смело открыли правую дверь. Но за ней вас подстерегала ')
            print('гигантская подземная жаба, которая проглотила вас целиком!')
        elif otv2 == 'слева':
            print('Вы на улице!')
    
