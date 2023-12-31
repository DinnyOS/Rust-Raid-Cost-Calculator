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


# calculator mechanics

def options():
    print("Welcome to the Rust Raid Cost Calculator! \n\n")
    print("Wooden Wall: WW\n"
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
          "Embrasure: EMB\n"
          "Ladder Hatch: LH\n")




def input_gather():

    user_input = input("\n\nSelect the obstacle that you want to break using the abbreviation from above: ").upper()

    #validate input
    valid_input = ["WW", "SW", "SMW", "AW", "WD", "SMD", "GD", "AD", "ADD", "AT", "WB3", "ESW", "EMB", "LH"]
    while user_input not in valid_input:
        user_input = input("Incorrect input. Select the obstacle using the CORRECT abbreviation from above: ").upper()


    selected_obstacle = None

    match user_input:
        case "WW":
            selected_obstacle = sulfur_costs.get("wooden_wall")

        case "SW":
            selected_obstacle = sulfur_costs.get("stone_wall")

        case "SMW":
            selected_obstacle = sulfur_costs.get("sheet_metal_wall")

        case "AW":
            selected_obstacle = sulfur_costs.get("armored_wall")

        case "WD":
            selected_obstacle = sulfur_costs.get("wooden_door")

        case "SMD":
            selected_obstacle = sulfur_costs.get("sheet_metal_door")

        case "GD":
            selected_obstacle = sulfur_costs.get("garage_door")

        case "AD":
            selected_obstacle = sulfur_costs.get("armored_door")

        case "ADD":
            selected_obstacle = sulfur_costs.get("armored_double_door")

        case "AT":
            selected_obstacle = sulfur_costs.get("auto_turret")

        case "WB3":
            selected_obstacle = sulfur_costs.get("workbench_3")

        case "ESW":
            selected_obstacle = sulfur_costs.get("external_stone_wall")

        case "EMB":
            selected_obstacle = sulfur_costs.get("embrasure")

        case "LH":
            selected_obstacle = sulfur_costs.get("ladder_hatch")

        case _:
            selected_obstacle = None  # In case of an invalid input, set to None

    if selected_obstacle:
        quantity = int(input(f"For how many {user_input}'s do you want to calculate the raid cost for: "))

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
        options()
        input_gather()

        another_calculation = input("\n\nWould you like to calculate the raid cost for another obstacle? (Y to continue)").upper()
        if another_calculation != "Y":
            break

calculate()
