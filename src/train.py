import matplotlib.pyplot as plt
import os
from test import *
from data import *

def train(x, y, m):
	"""Train on the values to get theta0 and theta1"""

    #configure training
    learning_rate = 0.3
    epoch = 100
    tmp0 = 0
    tmp1 = 0
    
    for i in range(0, epoch):
        gradient0 = 0
        gradient1 = 0
        
		#Use temporary values to predict and adjust theta0 and theta1 
        for index in range(0, m):
            p = predict([x[index]], tmp0, tmp1)[0]
            gradient0 += p - y[index]
            gradient1 += (p - y[index]) * x[index]
        
        tmp0 -= learning_rate / m * gradient0
        tmp1 -= learning_rate /m * gradient1
        
    return tmp0, tmp1


def standard_deviation(df, mean_x, m):
    deviation = 0
    for x in df['km']:
        deviation += (x - mean_x) ** 2
    
    sd = (deviation / m) ** 0.5
    
    return sd

def main():
    
	#Verify if data.csv exists
    if not os.path.isfile("../data/data.csv"):
        print("../data/data.csv not found.")
        exit()

    df = get_dataset()
    
    #prepare values for the training
    m = len(df['km'])
    sum_x = sum(df['km'])
    mean_x = sum_x / m
    sd = standard_deviation(df, mean_x, m)
    df['x'] = [(x - mean_x) / sd for x in df['km']]
    
    #get temporary values for theta0 and theta1
    tmp0, tmp1 = train(df['x'], df['price'], m)
    
	#get theta0 and theta1
    theta0 = tmp0 - tmp1 * mean_x / sd
    theta1 = tmp1 / sd
    
	#plot values
    p = predict(df['km'], theta0, theta1)
    plot(p, df['km'], df['price'], theta0, theta1)
    
	#save theta0 and theta1 in theta.txt
    values = str(theta0) + '\n' + str(theta1)
    
    with open('../data/theta.txt', 'w') as fd:
        fd.write(values)
        
    print('../data/theta.txt was created.')
    
if __name__ == "__main__":
    main()
    
    
