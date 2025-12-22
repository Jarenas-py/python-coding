import numpy as np

class TempCalc:
    def __init__(self):
        self.arr = np.zeros((2, 3, 2), dtype= float)
        self.Ave = None

    def data_Struct(self, floor, room, hr1, hr2 ):
        self.arr[floor, room]= [hr1, hr2]

    def temp_Ave(self):
        self.Ave = np.mean(self.arr, axis= 2)
        ave_Array= self.Ave
        return ave_Array

    def __str__(self):
        return """\nInstructions: Select floors and rooms and input their temperatures in Celcius.
        Input the temperature of the rooms by their hour.
        The Average Temperature in Celcius of each room in their respective floor will be calculated.
        A 2-Dimensional Array would also be provided."""

TempLogger = TempCalc()
print(TempLogger)

while True:
    floor= input("\nSelect Floor (1 or 2): ")
    match floor:
        case "1":
            while True:
                floor1= input("Enter Floor 1 Room (1-3): ")
                match floor1:
                    case "1":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(0,0, hr1, hr2)
                        room1_decision= input("\nDo you want to continue setting temperatures for floor 1 rooms? (Y/N): ")
                        room1_dec= room1_decision.upper()
                        if room1_dec == 'N':
                            break

                    case "2":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(0, 1, hr1, hr2)
                        room2_decision= input("\nDo you want to continue setting temperatures for floor 1 rooms? (Y/N): ")
                        room2_dec= room2_decision.upper()
                        if room2_dec == 'N':
                            break

                    case "3":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(0, 2, hr1, hr2)
                        room3_decision= input("\nDo you want to continue setting temperatures for floor 1 rooms? (Y/N): ")
                        room3_dec= room3_decision.upper()
                        if room3_dec == 'N':
                            break

                    case _:
                        print("Error: Enter a valid input.")

        case "2":
             while True:
                floor2= input("Enter Floor 2 Room (1-3): ")
                match floor2:
                    case "1":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(1, 0, hr1, hr2)
                        room1_decision= input("\nDo you want to continue setting temperatures for floor 2 rooms? (Y/N): ")
                        room1_dec= room1_decision.upper()
                        if room1_dec == 'N':
                            break

                    case "2":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(1, 1, hr1, hr2)
                        room2_decision= input("\nDo you want to continue setting temperatures for floor 2 rooms? (Y/N): ")
                        room2_dec= room2_decision.upper()
                        if room2_dec == 'N':
                            break

                    case "3":
                        hr1= float(input("Input Temperature for Hour 1: "))
                        hr2= float(input("Input Temperature for Hour 2: "))
                        TempLogger.data_Struct(1, 2, hr1, hr2)
                        room3_decision= input("\nDo you want to continue setting temperatures for floor 2 rooms? (Y/N): ")
                        room3_dec= room3_decision.upper()
                        if room3_dec == 'N':
                            break

                    case _:
                        print("\nError: Enter a valid input.")

        case _:
            print("\nError: Enter a valid input.")

    floor_Decision= input("\nDo you want to stop setting values and acquire average temperatures for each room? (Y/N): ")
    floor_dec= floor_Decision.upper()
    match floor_dec:
        case "Y":
            break

while True:
    print(f"""\nALL ROOM TEMPERATURE AVERAGES\n
          Floor 1:
          Room 1= {TempLogger.temp_Ave()[0, 0]} Celcius
          Room 2= {TempLogger.temp_Ave()[0, 1]} Celcius
          Room 3= {TempLogger.temp_Ave()[0, 2]} Celcius
          
          Floor 2:
          Room 1= {TempLogger.temp_Ave()[1, 0]} Celcius
          Room 2= {TempLogger.temp_Ave()[1, 1]} Celcius
          Room 3= {TempLogger.temp_Ave()[1, 2]} Celcius""")
    
    print (f"Generated 2D Numpy Array after Calculation: {TempLogger.temp_Ave()}")
    decision= input("Do you want to exit the probram? (Y/N): ")
    dec= decision.upper()
    match dec:
        case 'Y':
            print("Thank you for using our program!")
            break
        
        case 'N':
            pass

        case _:
            print("Error: Enter a valid input.")