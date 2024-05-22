# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# asking robot to create a square
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# hurdle challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for i in range(0,6):
#     jump()

# whileloop
# while at_goal() != True:
#     jump()

# hurdel 3 
# while at_goal() != True:
#     if front_is_clear():
#         move()
#     else:
#         jump()

# Hurdle 4
# def jump():
#     turn_left()
#     height = 0
#     while wall_on_right() and is_facing_north():
#         move()
#         height+=1
#     turn_right()
#     move()
#     turn_right()
#     for i in range(height):
#         move()
#     turn_left()
    
# while at_goal() != True:
#     if front_is_clear():
#         move()
#     else:
#         jump()

# # maze solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while at_goal() != True:
#     if right_is_clear():
#         turn_right()
#     if front_is_clear():
#         move()
#     elif not right_is_clear():
#         turn_left()