import os
import matplotlib.pyplot as plt
from test import mse, mae, score


def predict(x_list, theta0, theta1):
	"""predict a list of values"""
    p = [theta0 + theta1 * value for value in x_list]
    return p

def get_dataset():
    """convert data.csv file into a dictionnary"""
    if not os.path.isfile("../data/data.csv"):
        print('"../data/data.csv" has not been found.')
        exit()
        
    try:    
        with open("../data/data.csv", "r") as fd:
            file = fd.read().splitlines()
    except:
        print('"../data/data.csv" is not a valid dataset.')
        exit()
        
    if len(file) < 3:
        print('Not enough data to predict value in "../data/data.csv".')
        exit()

    try:
        x = [float(item.split(',')[0]) for item in file[1:]]
        y = [float(item.split(',')[1]) for item in file[1:]]
        print(len(x))
    except:
        print('Error: "Data.csv" must only contain numbers.')
        exit()

    data = {'km' : x, 'price' : y}

    return data

def plot(p, x, y, theta0, theta1):
    """Create graphs including price, mileage et the prediction"""
    x_min = min(x)
    x_max = max(x)
    p_min = predict([x_min], theta0, theta1)
    p_max = predict([x_max], theta0, theta1)
    
    print("\ntheta0: " + str(theta0))
    print("theta1: " + str(theta1) + '\n')
    
    print("Mean square error: %.2f" % mse(y, p))
    print("Mean absolute error: %.2f" % mae(y, p))
    print("Determination coefficient score: %2.f" % score(y, p) + '\n')
    
    #plot the price and the prediction
    plt.title("Price and prediction")
    plt.plot()
    pred = plt.plot(p, label = 'prediction')
    price =plt.plot(y, label = 'price')
    plt.xlabel('\nmileage')
    plt.ylabel('price\n')
    plt.legend()
    plt.show()
    
    #plot the line that goes through the middle of each point (x = mileage, y = price)
    plt.title("Linear regression")
    plt.scatter(x, y)
    plt.xlabel('\nmileage')
    plt.ylabel('price\n')
    plt.plot([x_min, x_max], [p_min, p_max], color = 'red')
    plt.text(145000, 8000, r'$\theta^0=$' + str(round(theta0, 4)) + r'    $\theta^1=$' + str(round(theta1, 4)))
    plt.grid()
    plt.show()
