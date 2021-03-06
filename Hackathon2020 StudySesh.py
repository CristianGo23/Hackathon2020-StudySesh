import pandas as pd

event_list = {'Host':  ['Alphonse', 'Jessica'],
        'Purpose': ['PSets', 'Studying'],
        'Time + Time Zone': ['1:00 PM PT', '9:00 AM EST'],
        'Day': ['Monday', 'Friday'],
        'Course?': ['ENGR79', 'PHYS51'],
        'Zoom Link': ['muddlink', 'muddylink'],
        '# Of People': ['3', '10']
}

schedule_list = {'Host':  [],
        'Purpose': [],
        'Time + Time Zone': [],
        'Day': [],
        'Course?': [],
        'Zoom Link': [],
        '# Of People': []
}

event_df = pd.DataFrame (event_list, columns = ['Host', 'Purpose', 'Time + Time Zone', 'Day', 'Course?', 'Zoom Link', '# Of People'])
schedule_df = pd.DataFrame (schedule_list, columns = ['Host', 'Purpose', 'Time + Time Zone', 'Day', 'Course?', 'Zoom Link', '# Of People'])

print("Hello New User! Welcome to the Study Sesh! \nHere you can post any study sessions you're willing to host \nalong with the time, course, purpose, and zoom link for said session \nDon't forget to put a zoom link!")

while True:
    print("What would you like to see?")
    firstChoice = input("-All Events \n-Events You're Attending\n-Back Out\n")
    if firstChoice == "All Events":
        print("These are all the events posted on our digital database!")
        print(event_df)
        while True:
            input1 = input("Add an Event? or Delete an Event? or Back Out?\n")
            if input1 == "Add an Event":
                host_input = input("Host: ")
                purpose_input = input("Purpose: ")
                time_input = input("Time + Time Zone: ")
                day_input = input("Day: ")
                course_input = input("Course: ")
                zoom_input = input("Zoom: ")
                people_input = input("# Of People: ")
                new_row = {'Host':host_input, 'Purpose':purpose_input, 'Time + Time Zone':time_input, 'Day':day_input, 'Course?':course_input, 'Zoom Link':zoom_input, '# Of People':people_input}
                event_df = event_df.append(new_row, ignore_index=True)
                print(event_df)
                
            elif input1 == "Delete an Event":
                event_df = event_df.drop(int(input("Which index? ")))
                print(event_df)
                
            else:
                print("Backing Out Now")
                break
        

    elif firstChoice == "Events You're Attending":
        print("These are all of the events that you have scheduled to visit!")
        print(schedule_df)
        while True:
            input2 = input("Add an Event? or Delete an Event? or Back Out?\n")
            if input2 == "Add an Event":
                print(event_df)
                input3 = int(input("Which event do you want to add to your schedule?\n"))
               
                temp_event_df = pd.DataFrame(event_df)
                event_to_add = temp_event_df.iloc[input3]

                schedule_df = schedule_df.append(event_to_add, ignore_index=True)

                print(schedule_df)
            elif input2 == "Delete an Event":
                schedule_df = schedule_df.drop(int(input("Which index? ")))
                print(schedule_df)
                
            else:
                print("Backing Out Now")
                break

    elif firstChoice == "Back Out":
        print('Okay, see you later!')
        break
    else:
        print("Sorry, I don't understand? Please type All Events or Events You're Attending in the box below...")


# Our mission: A lot of the time, it's a struggle to try and keep track of all of the grutoring/AE/office hours links, because
# they aren't all in one place. However, Study Sesh is the perfect tool to combine all of your study session needs.

 