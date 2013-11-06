#This function surveys the user then composes a list of suitable activities to
#cure the boredom.
print("")

print("Answer 'yes' or 'no' to the following questions:")

def boredom_solution(hunger, sociable, outside_permissible, athletic, tired, electronable, studious):
    activities = []
    if hunger == "yes":
        activities.append('eat, ')
    if sociable == "yes":
        activities.append(' hang-out with people, or call family and friends ')
    if outside_permissible == "yes":
        activities.append(', do something outside:')
        activities.append(' throw football')
        activities.append(', walk')
        activities.append(', lounge')
        activities.append(', go running.')
    if outside_permissible == "yes" and athletic == "no":
        activities.remove(', throw football')
        activities.remove(', walk')
        activities.remove(', go running')
    if tired == "yes":
        activities.append(', sleep')
    if electronable == "yes":
        activities.append(', watch a movie (on netflix or hulu), play LoL or counterstrike, program, listen to music, or learn stuff')
    if studious == "yes":
        activities.append(', do your job, or homework')
   
    print('')
    print('')
    sent_act = "".join(activities)
    print("Suitable activites for curing boredom may be as follows: ") + sent_act

#These variables are arguments for elements
bored = raw_input("Are you bored?: ")
if bored == "yes":
    pass
else:
    print("This is the wrong app for you!")
    exit()
hungry = raw_input("Are you hungry?: ")
if hungry == "yes":
    caf = raw_input("Is the Caf open?: ")
    if caf == "yes":
        pass
    else:
        food = raw_input("Do you have any food that you would like to eat, or any money to buy food?: ")
        if food != "yes":
            hungry = "no"
            
sociable = raw_input("Do you feel sociable?: ")
if sociable == "yes":
    confident = raw_input("Do you feel confident?: ")
    if confident == "yes":
        people = raw_input("Are there people to socialize with?: ")
        if people != "yes":
            sociable = "no"
    else:
        sociable = "no"

outside_ok = raw_input("Is it before curfew?: ")
if outside_ok == "yes":
    outside_desirable = raw_input("Is the weather / condition ok outside?: ")
    if outside_desirable != "yes":
        outside_ok = "no"
            
athletic = raw_input("Do you feel like doing physical activity?: ")

tired = raw_input("Are you tired?: ")

electronable = raw_input("Do you feel like entertaining yourself through electronics?: ")

studious = raw_input("Do you feel like working or doing homework? ")
procrast = raw_input("Do you have work or homework due tonight or tomorrow by class time?: ")
if procrast == "yes":
    studious = "yes"

boredom_solution(hungry, sociable, outside_ok, athletic, tired, electronable, studious)
