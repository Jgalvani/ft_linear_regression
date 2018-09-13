import os
from train import plot
from data import *

def no_values(msg):
	"""initialize theta0 and theta1 to 0"""
    print(msg)
    return 0, 0


def get_theta():
	"""Calculate the slope and the intercept then plot the values"""
    df = get_dataset()
    
    length = len(df['km'])
    print(length)
    
    df['xy'] = [item[0] * item[1] for item in zip(df['km'], df['price'])]
    df['x2'] = [x * x for x in df['km']]
        
    sum_x = sum(x for x in df['km'])
    sum_y = sum(y for y in df['price'])
    sum_xy = sum(xy for xy in df['xy'])
    sum_x2 = sum(x2 for x2 in df['x2'])
        
    intercept = ((sum_y * sum_x2) - (sum_x * sum_xy)) /((length * sum_x2) - (sum_x * sum_x)) 
        
    slope = ((length * sum_xy) - (sum_x * sum_y)) / ((length * sum_x2) - (sum_x * sum_x))
    
    #Plot values
    p = predict(df['km'], intercept, slope)
    plot(p, df['km'], df['price'], intercept, slope)
    
    return intercept, slope


def main():
    
	#Ask for another way to predict the price
    choice = raw_input("Do you want to calculate theta0 and theta1 ?: (y/n)\n") 
	
    while choice != 'y' and choice != 'n':
        choice = raw_input("Write 'y' or 'n': ")
    
    #Calculate slope and intercept
    if choice == 'y':
        theta0, theta1 = get_theta()
        
    else:
        #Seek for trained values
        if os.path.isfile("../data/theta.txt"):
            with open("../data/theta.txt", 'r') as fd:
                values = fd.read()
            
			#if theta.txt is not valid, initialize theta0 and theta1 to 0
            if len(values.splitlines()) < 2 or not values.splitlines()[0].replace('.', '').isdigit() or not values.splitlines()[1].replace('.', '').isdigit():
                theta0, theta1 = no_values("../data/theta.txt is not a valid file. Theta0 and theta1 will be initialized to 0.")
                
            else:
                theta0 = float(values.splitlines()[0])
                theta1 = float(values.splitlines()[1])
                
        else:
            #If no value was found, initialize theta0 and theta1 to 0
            theta0, theta1 = no_values("No trained values has been found.")
    
    #Ask the user for prediction
    value = raw_input('Enter mileage to predict price: ')
    while not value.isdigit() or (predict([int(value)], theta0, theta1) <= 0 and theta0 != 0 and theta1 != 0):
        if not value.isdigit():
            value = raw_input('Enter a number: ')
        else:
            value = raw_input('Mileage is too high, enter a smaller number: ')
        
    pred = predict([int(value)], theta0, theta1)     
    print("The price for a car with a mileage of " + value + " km should be around %.2f" % pred[0] + '$.')
    
    
if __name__ == '__main__':
    main()
        
