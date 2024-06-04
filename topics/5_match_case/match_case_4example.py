#list
# item_1 = ["evening", 879]
# item_2 = ["day", "play games"]
# item_3 = ["evening", 456, "action"]

# match item_3:
#     case ['evening', action]:
#         print(f'You almost finished the day! Now {action}!')
#     case [time, action]:
#         print(f'Good {time}! It is time to {action}!')
#     case _:
#         print('The time is invalid.')


# dict
item_1 = {"time": 'evening', "action": "go to a bed"}
item_2 = {"time": 'day', "action": "go a walk"}
item_3 = {"time": 'morning', "move": "other", "action": "go to work"}
item_4 = {}

match item_4:
    case {"time": 'evening', "action": action}:
        print(f"You almost finished the day! Now you must {action}!")
    case {"time": time, "action": action}:
        print(f"Good {time}! It is time to {action}!")
    case _:
        print("The time is invalid.")
