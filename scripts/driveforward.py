from util.drivecontrol import Controller

my_controller = Controller()
my_controller.start()
my_controller.drive_forwards()

state = 0 
rightturns_made = 0
leftturns_made = 0

while True:
    if state == 0:
        my_controller.drive_forwards()
    
    if state == 1:
        my_controller.left_turn()
        leftturns_made += 1
        if leftturns_made >= 1:
            state = 3
        else:
            state = 0
    
    if state == 3:
        my_controller.right_turn()
        rightturns_made += 1
        if rightturns_made > 2:
            state = 2
        else:
            state = 0

    if state == 2:
        my_controller.stop()

    my_controller.drive_forwards()
    if my_controller.left_odom.get_count() >= 2000 and my_controller.right_odom.get_count() >= 2000:
        state = 3
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 1000 and my_controller.right_odom.get_count() >= 1000 and rightturns_made == 1:
        state = 3
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 1000 and my_controller.right_odom.get_count() >= 1000 and rightturns_made == 2:
        state = 1
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 1000 and my_controller.right_odom.get_count() >= 1000 and leftturns_made == 1:
        state = 3
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 1000 and my_controller.right_odom.get_count() >= 1000 and rightturns_made == 3:
        state = 3
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 1000 and my_controller.right_odom.get_count() >= 1000 and rightturns_made == 4:
        state = 3
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()
    elif my_controller.left_odom.get_count() >= 2000 and my_controller.right_odom.get_count() >= 2000 and rightturns_made == 5:
        state = 2
        my_controller.left_odom.reset_count()
        my_controller.right_odom.reset_count()

