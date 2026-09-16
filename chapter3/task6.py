current_temperature = 100

if current_temperature <=50:
    print('No or moderate load on the machine.')
else:
    if current_temperature >50:
        if current_temperature >80:
            print('Machine is under extreme load, take action!')
        else:
            print('Machine is running under heavy load.')