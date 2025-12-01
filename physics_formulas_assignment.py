#print('a', 'b', 'c', 'd', 'e' formulas)
name = str(input('Enter your name: '))
print('Hey ' + name)

print("Welcome to Emelie's Calculator :)")
print("Here are my available physics formulas")
print('a. force = mass * acceleration')
print('b. kinetic_energy = 0.5 * mass * velocity^2')
print('c. velocity = displacement / time')
print('d. voltage = current * resistance')
print('e. binding_energy = mass_defect * speed_of_light^2')


chosen_formula = input('Which of the above physics formulas would you like to use? ')
if chosen_formula == 'a':
    mass = float(input('Enter the mass: '))
    print('mass, m = ' + str(mass) + 'kg')
    acceleration = float(input('Enter the acceleration: '))
    print('acceleration, a = ' + str(acceleration) + 'm/s^2')
    print('F = m x a')
    print('the calculated force = ' + str(mass * acceleration) + 'N')

elif chosen_formula == 'b':
    mass = float(input('Enter the mass: '))
    print('mass, m = ' + str(mass) + 'kg')
    velocity = float(input('Enter the velocity: '))
    print('velocity, v = ' + str(velocity) + 'm/s')
    print('K.E = 0.5 x m x v^2')
    print('the calculated kinetic energy = ' + str(0.5 * mass * velocity**2) + 'J')

elif chosen_formula == 'c':
    displacement = float(input('Enter the displacement: '))
    print('displacement, d = ' + str(displacement) + 'm')
    time = float(input('Enter the time: '))
    print('time, t = ' + str(time) + 's')
    print('v = d / t')
    print('the calculated velocity = ' + str(displacement / time) + 'm/s')

elif chosen_formula == 'd':
    current = float(input('Enter the current: '))
    print('current, I = ' + str(current) + 'A')
    resistance = float(input('Enter the resistance: '))
    print('resistance, R = ' + str(resistance) + 'ohms')
    print('V = I x R')
    print('the calculated voltage = ' + str(current * resistance) + 'v')

elif chosen_formula == 'e':
    mass_defect = float(input('Enter the mass defect: '))
    print('mass defect, m = ' + str(mass_defect) + 'kg')
    speed_of_light = int(3 * 10**8)
    print('speed of light, c = 3 x 10^8 m/s')
    print('E = mc^2')
    print('the calculated binding energy = ' + str(mass_defect * (speed_of_light**2)) + 'J')

else:
    print("Oops! Seems like I don't have this physics formula")


print("Thanks for using Emelie's Calculator")