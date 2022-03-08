import colorama
import sys
import os
import math
import time
import copy
from time import perf_counter
from colorama import Fore, Back, Style

# custom modules
from constants import *
from input import input_to
from king import King
from gamecreate import *
from walls import Wall
from buildings import Building
from troops import Troop
colorama.init()

#initialise gaming constraints

game = Game()
# king = King(game)

while True:
    #keep it running smoothly
    # os.system('cls' if os.name == 'nt' else 'clear')
    #print board and take input key from input file
    board = game.print_board()

    
    print("\033[H\033[J", end="")
    #allow king to make move every 1 second
    key = input_to()
    #make game smoother

    #deploy troops based on spawn points
    start_time = time.time()
    game.start_time = start_time
    if (key == 'c'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[0][0],SPAWN_POINTS[0][1],Troop(game,np.array(SPAWN_POINTS[0]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'v'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[1][0],SPAWN_POINTS[1][1],Troop(game,np.array(SPAWN_POINTS[1]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])
    elif (key == 'b'):
        game.troops.append(Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time))
        # game.troop_list.append([SPAWN_POINTS[2][0],SPAWN_POINTS[2][1],Troop(game,np.array(SPAWN_POINTS[2]),BARB_HP,BARB_CHAR ,BARB_ATTACK,BARB_HP,start_time) ])

    #move king
    #if king exists, dp:
    if(game.king != ''):
        game.king.move(key)
        #allow king to attack wall multiple times
        game.king.attack_wall(key)
        game.king.attack_building(key)
        if(game.king.check_king() == True):
            game.board[game.king.x][game.king.y] = '|   |'
            game.king = ''

    #check if wall is hit
    for wa in game.walls:
        if(wa.check_wall() == True):
            game.walls.remove(wa)
            game.board[wa.x][wa.y] = '|   |'
            del game.wall_dict[(wa.x,wa.y)]
    #check if building is hit
    for bu in game.buildings:
        if(bu.check_bu() == True):
            game.buildings.remove(bu)
            #remove items in dictionaries whose keys are the tuple of coordinates
            for bu_co in bu.coords:
                game.board[bu_co[0]][bu_co[1]] = '|   |'
                del game.build_dict[tuple(bu_co)]
        if(time.time()-bu.building_time > 1):
            bu.bu_attack()
            bu.building_time = time.time()

    for tr in game.troops:
        if(time.time()-tr.troop_time > 1):
            tr.move()
            tr.troop_time = time.time()
        if tr.check_troop() == True:
            game.troops.remove(tr)
            #remove items in dictionaries whose keys are the tuple of coordinates
            tr_list = tr.coords.tolist()
            game.board[tr_list[0]][tr_list[1]] = '|   |'
                # del game.troops[tuple(tr_co)]
        #check if troop is hit
    
    #if king exists, print its health

    if (key != None):
        time.sleep(T)


    #if building list is empty, end game
    if(len(game.buildings) == 0):
        print(r''' 
            _        _       _               _             _         _      _        _         _    
 __/\\__  __/\\__  _/\\___ _____  __/\\___      __/\\___  _ /\\  __/\\___  _/\\___   _/\\_  
(_  ___))(_  ____)(_      v    ))(_  ____))    (_     _))/ \\ \\(_  ____))(_   _  ))(_  _)) 
 / || _   /  _ \\  /  :   <\   \\ /  ._))       /  _  \\ \:'/ // /  ._))   /  |))//  /  \\  
/:. \/ \\/:./_\ \\/:. |   //   ///:. ||___     /:.(_)) \\ \  // /:. ||___ /:.    \\ / \ :\\ 
\  ____//\  _   //\___|  //\  // \  _____))    \  _____//(_  _))\  _____))\___|  // \__/\// 
 \//      \// \//      \//  \//   \//           \//        \//   \//           \//     \//  
       _     _           _             _    _      _      _           ____     _            
  _   /\\ __/\\___  ___ /\\       ___ /\\  /\\   _/\\_  _/\\___      (:. _))__/\\           
 /\\ / //(_     _))/  //\ \\     /   |  \\/  \\ (____))(_      ))      \// /_   \\          
 \ \/ //  /  _  \\ \:.\\_\ \\    \:' |   \\   \\ /  \\  /  :   \\            /'://          
 _\:.//  /:.(_)) \\ \  :.  //     \  :   </   ///:.  \\/:. |   //       _   _\.:\\          
(_  _))  \  _____//(_   ___))    (_   ___^____))\__  //\___|  //      _/\\_\__  //          
  \//     \//        \//           \//             \//      \//      (:.__))  \//           
                                                                                            
                                                                                                                                                                               
        ''')
        break
    elif(len(game.troops) == 0 and game.king == ''):
        print(r''' 
                                                                                                    
                                                                                                             
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   @@@  
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@   
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   @!@  
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    !!!  
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!        
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  :!:  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::   ::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :  :::  
@@@ @@@   @@@@@@   @@@  @@@     @@@        @@@@@@    @@@@@@   @@@@@@@@             @@@      
@@@ @@@  @@@@@@@@  @@@  @@@     @@@       @@@@@@@@  @@@@@@@   @@@@@@@@            @@@       
@@! !@@  @@!  @@@  @@!  @@@     @@!       @@!  @@@  !@@       @@!                @@!        
!@! @!!  !@!  @!@  !@!  @!@     !@!       !@!  @!@  !@!       !@!          @!@  !@!         
 !@!@!   @!@  !@!  @!@  !@!     @!!       @!@  !@!  !!@@!!    @!!!:!       !@!  !!@         
  @!!!   !@!  !!!  !@!  !!!     !!!       !@!  !!!   !!@!!!   !!!!!:       !:!  !!!         
  !!:    !!:  !!!  !!:  !!!     !!:       !!:  !!!       !:!  !!:               !!:         
  :!:    :!:  !:!  :!:  !:!      :!:      :!:  !:!      !:!   :!:          :!:   :!:        
   ::    ::::: ::  ::::: ::      :: ::::  ::::: ::  :::: ::    :: ::::     :::     ::       
   :      : :  :    : :  :      : :: : :   : :  :   :: : :    : :: ::      :::       :      
                                                                                                                                                                                              
        ''')
        break

    #exit code by pressing button 'q'
    if(key == 'q'):
        sys.exit()
    # print("\033[0;0H")


