#Definition of a function - specifying what it is and what it does
#Parameter = data given in to the function
def calc_area(h = 8, b = 1):
    area = 0.5*h*b
    return area
#Return value  = data produced by function and given back to the caller

def run():
    #Call to the function - to make it run
    total_area = calc_area(2,10) + calc_area(9) + calc_area() + calc_area(b=10)
    
    print(f"The area is {total_area} cm^2")

