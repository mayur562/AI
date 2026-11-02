environment = {'A' : 'Clean' , 
               'B' : 'Dirty'}

location = 'A'

while True:
    print("Current Location : ",location)
    print("Environment : ",environment)

    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Goal Achieved Successfully !!! Both Rooms are cleaned...")
        break

    if environment[location] == 'Dirty':
        print("Action : [SUCK]")
        environment[location] = 'Clean'

    else:

        if location == 'A' :
            location = 'B'
        else:
            location = 'A'

    
