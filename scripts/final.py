from include.rcc_library import Raft
from util.drivecontrol import Controller

raft = Raft()
cont = Controller()

cont.start()

state = 0
turns_made = 0


while True:
    
    if state == 0:
        cont.drive_forwards()
        if cont.left_odom.get_count() >= 1000 and cont.right_odom.get_count() >= 1000 and turns_made == 0:
            state = 1
            cont.left_odom.reset_count()
            cont.right_odom.reset_count()
        elif cont.left_odom.get_count() >= 1000 and cont.right_odom.get_count() >= 1000 and turns_made == 1:
            state = 2
            cont.left_odom.reset_count()
            cont.right_odom.reset_count()

    if state == 1:
        cont.custom_left_turn(144)
        turns_made += 1
        state = 0

    
    if state == 2:
        cont.custom_right_turn(72)
        turns_made = 0
        state = 0
    
    if state == 3:
        cont.stop

