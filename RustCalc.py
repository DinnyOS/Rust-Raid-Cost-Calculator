# foundation data

sulfur_costs = {
    "wooden_wall": {
        "cost": 1400,  # 1 Rocket + 10 Rifle Ammunition
        "additional_info": {
            "rockets": 1,
            "rifle_ammunition": 10
        }
    },
    "stone_wall": {
        "cost": 5600,  # 4 Rockets
        "additional_info": {
            "rockets": 4
        }
    },
    "sheet_metal_wall": {
        "cost": 8400,  # 3 C4's + 75 Explosive Rifle Ammunition
        "additional_info": {
            "c4": 3,
            "explosive_rifle_ammunition": 75
        }
    },
    "armored_wall": {
        "cost": 16150,  # 7 C4's + 30 Explosive Rifle Ammunition
        "additional_info": {
            "c4": 7,
            "explosive_rifle_ammunition": 30
        }
    },
    "wooden_door": {
        "cost": 450,  # 18 Explosive Rifle Ammunition
        "additional_info": {
            "explosive_rifle_ammunition": 18
        }
    },
    "sheet_metal_door": {
        "cost": 1600,  # 63 Explosive Rifle Ammunition
        "additional_info": {
            "explosive_rifle_ammunition": 63
        }
    },
    "garage_door": {
        "cost": 3600,  # 1 C4 + 1 Rocket
        "additional_info": {
            "c4": 1,
            "rockets": 1
        }
    },
    "armored_door": {
        "cost": 4400,  # 2 C4's
        "additional_info": {
            "c4": 2
        }
    },
    "armored_double_door": {
        "cost": 5200,  # 2 C4's + 31 Explosive Rifle Ammunition
        "additional_info": {
            "c4": 2,
            "explosive_rifle_ammunition": 31
        }
    },
    "auto_turret": {
        "cost": 600,  # 3 High Velocity Rockets
        "additional_info": {
            "high_velocity_rockets": 3
        }
    },
    "workbench_3": {
        "cost": 4400,  # 2 C4's
        "additional_info": {
            "c4": 2
        }
    },
    "external_stone_wall": {
        "cost": 4400,  # 2 C4's
        "additional_info": {
            "c4": 2
        }
    },
    "external_wooden_wall": {
        "cost": 2800,  # 2 Rockets + 10 Explosive Rifle Ammunition
        "additional_info": {
            "rockets": 2,
            "explosive_rifle_ammunition": 10
        }
    },
    "embrasure": {
        "cost": 5600,  # 4 Rockets
        "additional_info": {
            "rockets": 4
        }
    },
    "ladder_hatch": {
        "cost": 1600,  # 63 Explosive Rifle Ammunition
        "additional_info": {
            "explosive_rifle_ammunition": 63
        }
    }
}

rocket_costs = {
    "wooden_wall": {
        "cost": 1400,  # 1 Rocket + 10 Rifle Ammunition
        "additional_info": {
            "rockets": 1,
            "rifle_ammunition": 10
        }
    },
    "stone_wall": {
        "cost": 5600,  # 4 Rockets
        "additional_info": {
            "rockets": 4
        }
    },
    "sheet_metal_wall": {
        "cost": 11200,  # 8 Rockets
        "additional_info": {
            "rockets": 8
        }
    },
    "armored_wall": {
        "cost": 21000,  # 15 Rockets
        "additional_info": {
            "rockets": 15
        }
    },
    "wooden_door": {
        "cost": 1400,  # 1 Rocket
        "additional_info": {
            "rockets": 1
        }
    },
    "sheet_metal_door": {
        "cost": 2800,  # 2 Rocket
        "additional_info": {
            "rockets": 2
        }
    },
    "garage_door": {
        "cost": 4200,  # 3 Rockets
        "additional_info": {
            "rockets": 3
        }
    },
    "armored_door": {
        "cost": 7000,  # 5 Rockets
        "additional_info": {
            "rockets": 5
        }
    },
    "armored_double_door": {
        "cost": 7000,  # 5 Rockets
        "additional_info": {
            "rockets": 5

        }
    },
    "auto_turret": {
        "cost": 600,  # 3 High Velocity Rockets
        "additional_info": {
            "high_velocity_rockets": 3
        }
    },
    "workbench_3": {
        "cost": 8400,  # 6 Rockets
        "additional_info": {
            "rockets": 6

        }
    },
    "external_stone_wall": {
        "cost": 5600,  # 4 Rockets
        "additional_info": {
            "rockets": 4
        }
    },
    "external_wooden_wall": {
        "cost": 4200,  # 3 Rockets
        "additional_info": {
            "rockets": 3
        }
    },
    "embrasure": {
        "cost": 5600,  # 4 Rockets
        "additional_info": {
            "rockets": 4
        }
    },
    "ladder_hatch": {
        "cost": 2800,  # 2 Rockets
        "additional_info": {
            "rockets": 2
        }
    }
}





# calculator mechanics

def options():
    print("\nWooden Wall: WW\n"
          "Stone Wall: SW\n"
          "Sheet Metal Wall: SMW\n"
          "Armored Wall: AW\n"
          "Wooden Door: WD\n"
          "Sheet Metal Door: SMD\n"
          "Garage Door: GD \n"
          "Armored Door: AD\n"
          "Armored Double Door: ADD\n"
          "Auto Turret: AT\n"
          "Workbench 3: WB3\n"
          "External Stone Wall: ESW\n"
          "External Wooden Wall: EWW\n"
          "Embrasure: EMB\n"
          "Ladder Hatch: LH\n")


def mode_selector():
    print("Welcome to the Rust Raid Cost Calculator! \n\n")
    print("1: ROCKET RAID COST CALCULATOR\n2: CHEAPEST RAID COST CALCULATOR\n")

    mode_select = input("Select the mode that you would like to run: ")
    mode = None

    valid_mode_input = ["1", "2"]
    while mode_select not in valid_mode_input:
        mode_select = input("Incorrect input. Select the mode using the CORRECT number from above: ")

    if mode_select == "1":
        mode = rocket_costs
    else:
        mode = sulfur_costs

    return mode
def input_gather(mode):

    user_input = input("\n\nSelect the obstacle that you want to break using the abbreviation from above: ").upper()

    #validate input
    valid_input = ["WW", "SW", "SMW", "AW", "WD", "SMD", "GD", "AD", "ADD", "AT", "WB3", "ESW", "EMB", "LH", "EWW"]
    while user_input not in valid_input:
        user_input = input("Incorrect input. Select the obstacle using the CORRECT abbreviation from above: ").upper()


    selected_obstacle = None

    match user_input:
        case "WW":
            selected_obstacle = mode.get("wooden_wall")

        case "SW":
            selected_obstacle = mode.get("stone_wall")

        case "SMW":
            selected_obstacle = mode.get("sheet_metal_wall")

        case "AW":
            selected_obstacle = mode.get("armored_wall")

        case "WD":
            selected_obstacle = mode.get("wooden_door")

        case "SMD":
            selected_obstacle = mode.get("sheet_metal_door")

        case "GD":
            selected_obstacle = mode.get("garage_door")

        case "AD":
            selected_obstacle = mode.get("armored_door")

        case "ADD":
            selected_obstacle = mode.get("armored_double_door")

        case "AT":
            selected_obstacle = mode.get("auto_turret")

        case "WB3":
            selected_obstacle = mode.get("workbench_3")

        case "ESW":
            selected_obstacle = mode.get("external_stone_wall")

        case "EWW":
            selected_obstacle = mode.get("external_wooden_wall")

        case "EMB":
            selected_obstacle = mode.get("embrasure")

        case "LH":
            selected_obstacle = mode.get("ladder_hatch")

        case _:
            selected_obstacle = None  # In case of an invalid input, set to None

    if selected_obstacle:
        while True:
            try:
                quantity = int(input(f"For how many {user_input}'s do you want to calculate the raid cost for: "))
                break  # Exit the loop if conversion to int succeeds
            except ValueError:
                print(f"\nIncorrect input. Please enter a CORRECT amount of {user_input}'s.")

        calculate_cost(selected_obstacle, quantity, user_input)


def calculate_cost(selected_obstacle, quantity, user_input):
    if selected_obstacle:
        base_cost = selected_obstacle["cost"] * quantity
        additional_info = selected_obstacle.get("additional_info", {})

        # Calculate the total amount of needed items to break the obstacle
        additional_cost = sum(additional_info[item] * quantity for item in additional_info)


        # Print the result
        print(f"\nRaid cost for {quantity} {user_input}'s is:\n{base_cost} sulfur.")
        print("\nBreakdown of required items:")
        for item, amount in additional_info.items():
            print(f"{amount * quantity} {item}")



def calculate():
    while True:
        mode = mode_selector()
        options()
        input_gather(mode)

        another_calculation = input("\n\nWould you like to calculate the raid cost for another obstacle? (Y to continue)").upper()
        if another_calculation != "Y":
            break

calculate()