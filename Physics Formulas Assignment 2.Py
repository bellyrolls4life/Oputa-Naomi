print("PHYSICS FORMULA CALCULATOR")
print("1. Speed")
print("2. Force")
print("3. Kinetic Energy")
print("4. Ohm's Law (Voltage)")
print("5. Density")

choice = int(input("Choose a formula (1-5): "))

if choice == 1:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    speed = distance / time
    print("Speed =", speed, "m/s")

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    force = mass * acceleration
    print("Force =", force, "N")

elif choice == 3:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", ke, "J")

elif choice == 4:
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ω): "))
    voltage = current * resistance
    print("Voltage =", voltage, "V")

elif choice == 5:
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))
    density = mass / volume
    print("Density =", density, "kg/m³")

else:
    print("Invalid choice")
