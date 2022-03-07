print()


def main():
    start_num = float(input('Please type your first odometer reading in miles: '))
    end = float(input('Please type your final odometer reading in miles: '))
    gallons = float(input('Please type the amount of fuel in reading in gallons: '))
    mpg = float(miles_per_gallon(end, start_num, gallons))
    lp100k = float(lp100k_from_mpg(mpg))
    print(f'{mpg:.1f} miles per gallon')
    print(f'{lp100k:.2f} liters per 100 kilometers')
    pass
def miles_per_gallon(x, y,z):
    mpg = abs((x - y)/ z)
    return mpg
def lp100k_from_mpg(mpg):
    lp100k= float(235.215/mpg)
    return lp100k

main()
