current_speed = 80
speed_limit = 80

if current_speed > speed_limit:
    if current_speed - speed_limit <5:
        print('Stop accelerating.')
    else:
        print('Break!')
else:
    print('No need to break.')

