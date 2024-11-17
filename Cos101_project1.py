def area_of_triangle():
    base=float(input('Enter base '))
    height=float(input('Enter height '))
    area=base*height/2
    print('the area of triangle is', area, 'cm^2')

def calculate_density():
    mass=float(input('Enter mass '))
    volume=float(input('Enter volume '))
    density=(mass/volume)
    print('the density is', density, 'kg/m^3')

def calculate_frequency():
    wave_speed=float(input('Enter wave_speed'))
    wavelength=float(input('Enter wavelength'))
    frequency=wave_speed/wavelength
    print('the frequency is', frequency, 'Hertz')

def calculate_impulse():
    force=float(input('Enter force'))
    time=float(input('Enter time'))
    impulse=force/time
    print('the impulse is', impulse, 'N/S')

def area_of_rectangle():
    length=float(input('Enter length'))
    breadth=float(input('Enter breadth'))
    area=length*breadth
    print('The area of rectangle is', area, 'cm^2')


start = int(input("Type 1 for area of triangle\nType 2 for density\nType 3 for frequency\nType 4 for impulse\nType 5 for area of rectangle"))

if start == 1:
    area_of_triangle()
elif start == 2:
    calculate_density()
elif start == 3:
    calculate_frequency()
elif start == 4:
    calculate_impulse()
elif start == 5:
    area_of_rectangle()
else:
    print("Invalid entry, Try again.")


