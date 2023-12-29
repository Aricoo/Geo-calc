def calculateSA():
    print()

def calculateVolume():
    print("\n\n\n\n======================")
    print("  SOLVE FOR VOLUME")
    print("======================")
    print("\n---  Pick a shape ---")
    print("1. Triangular prism")
    print("2. Cube")
    print("3. Sphere")
    print("4. Rectangle")
    print("----------------------\n")

    shapeName = input("Enter the name of the shape:  \n\n")

    print("\n\n\n\n\n\n\n\n")
    print("=========================")
    print(" ENTER YOUR MEASUREMENTS")
    print("=========================")
    print("\n\n\n\n\n\n")

    if shapeName == "Triangular Prism":
        length = int(input("what's the length of the shape? " ))
        width = int(input("what's the width of the shape? " ))
        height = int(input("What's the height of the shape? " ))
        answer = (length * width * height * 1/2)
    elif shapeName == "Cube":
        length = input("\n""What's the measuremant of a side?: " )
        answer = (int(length)**3)
    elif shapeName == "Sphere":
        radius = int(input("What's the radius of the shape? " ))
        answer =   ((radius ** 3) * 4/3 * 3.14159)
    elif shapeName == "Rectangle":
        length = int(input("What is the length of the shape? " ))
        width = int(input("what's the width of the shape? " ))
        height = int(input("What's the height of the shape? " ))
        answer = (length * width * height)
    else:
        answer = 0
    return answer




def intro():
    print("\n\n\n\n\n\n\n\n")
    print("============================================")
    print(" Hello! Welcome to the Geometry Assistant")
    print("============================================")
    print("\n\n\n\n")

    calculationChoice = input("What would you like to calculate? (Volume/SA) \n\n")

    while calculationChoice not in ["Volume", "Surface Area"]:

        calculationChoice = input("Incorrect input, would you like to calculate? (Volume/SA) \n\n")

    
    return calculationChoice


def finalAnswer(calculationChoice, answer):
    print("\n\n\n\n\n\n\n\n")
    print("============================================")
    print("     Your ", calculationChoice, " is", round(answer,2))
    print("============================================\n\n\n")



def main():
    # Run intro to ask for calculation volume or sa
    calculationChoice = intro()
    
    if calculationChoice == "Volume":
        answer = calculateVolume()
    elif calculationChoice == "Surface Area":
        answer = calculateSA()
    else:
        print("incorrect calculation choice")

    print(finalAnswer(calculationChoice, answer))


if __name__ == "__main__":
    main()