<<<<<<< HEAD
print("Select a shape")
print("1. Triangular prism")
print("2. Cube")
print("3. Sphere")
print("4. Rectangle")
choice = input("Enter the name of the shape " )

Length = input("What is the length of the shape? " )
print(Length)
Width = input("what's the width of the shape? " )
print(Width)
Height = input("What's the height of the shape? " )
print(Height)
Radius = input("What's the radius of the shape? " )
print(Radius)


Triangular_Prism_Answer = (int(Length) * int(Width) * int(Height) * 1/2)
Rectangle_Answer = (int(Length) *int(Width) * int(Height))
Sphere_Answer =   (int(Radius)**3) * 4/3 * 3.14159
Cube_Answer = (int(Length) *int(Width) * int(Height))

if choice== "Cube" :
    print("your answer is" , Cube_Answer)

if choice== "Sphere" :
    print("your answer is" , Sphere_Answer)

if choice== "Triangular prism" :
    print("Your answer is" ,Triangular_Prism_Answer)

if choice== "Rectangle" :
    print("Your answer is", Rectangle_Answer)
=======
# rename directory 
# rename variables


print("What operation?\n")
print("Volume")
print("\n""Area")
choice = input("\nEnter the name of the operation? " )

print("Select a shape\n")
print("Triangular prism""\n")
print("Cube""\n")
print("Sphere""\n")
print("Rectangle""\n")
choice = input("\nEnter the name of the shape: " )

if choice == "Triangular prism" and "Volume" :
    Length = input("\n""What is the length of the shape? " )
    
    Width = input("\n""what's the width of the shape?: " )
    
    Height = input("\n""What's the height of the shape?: " )
    
    Triangular_Prism_Answer_Volume = (int(Length) * int(Width) * int(Height) * 1/2)

if choice == "Triangular prism" and "Volume" :
    print("\nYour answer is" ,Triangular_Prism_Answer_Volume)

if choice == "Cube" and "Volume" :
    Side = input("\n""What's the measuremant of a side?: " )
    Cube_Answer = (int(Side)**3)
    

if choice== "Cube" and "Volume" :
    print("\nyour answer is" , Cube_Answer)

if choice== "Sphere" and "Volume" :
    Radius = input("\n""What's the radius of the shape?: " )
    Sphere_Answer = (int(Radius)**3) * 4/3 * 3.14159

if choice== "Sphere" and "Volume" :
    print("\nyour answer is" , Sphere_Answer)

if choice== "Rectangle" and "Volume" :
    Length = input("\n""What is the length of the shape? : " )
    
    Width = input("\n""what's the width of the shape?: " )
    
    Height = input("\n""What's the height of the shape?: " )
    
    Rectangle_Answer = (int(Length) *int(Width) * int(Height))

if choice== "Rectangle" and "Volume" :
    print("\nyour answer is" , Rectangle_Answer)
 

 
>>>>>>> dd10cfc8a485c0664dcc34c986e6a58892ea2b35
