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
