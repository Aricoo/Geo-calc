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
 

 
