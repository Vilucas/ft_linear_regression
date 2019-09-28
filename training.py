# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/23 09:52:36 by viclucas          #+#    #+#              #
#    Updated: 2019/09/27 22:01:38 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  argparse
import  numpy as np
import  math
import statistics

def     data_denormalization(data):
    for i in range(len(data['price_list'])):
        data['price_list'][i] = data['price_list'][i] + min(data['price_list'])
        data['price_list'][i] *= max(data['price_list']) + min(data['price_list']) 
    for i in range(len(data['mileage_list'])):
        data['mileage_list'][i] = data['mileage_list'][i] + min(data['mileage_list'])
        data['mileage_list'][i] *= max(data['mileage_list']) + min(data['mileage_list']) 
    return (data)

def     data_normalization(data):
    for i in range(len(data['price_list'])):
        data['price_list'][i] = data['price_list'][i] - min(data['price_list'])
        data['price_list'][i] /= max(data['price_list']) - min(data['price_list']) 
    for i in range(len(data['mileage_list'])):
        data['mileage_list'][i] = data['mileage_list'][i] - min(data['mileage_list'])
        data['mileage_list'][i] /= max(data['mileage_list']) - min(data['mileage_list']) 
    return data

def     loss_computing(price_list, mileage_list, slope, c, lr):
    for i in range(len(price_list)):
        y = slope * price_list[i] + c
        residual += (mileage_list[i] - y) ** 2
        loss = (residual * lr) / float(len(price_list))
    return loss

def     gradient_descent(data_b):
    m = 0
    b = 0
    lr = 0.1
    iteration = 1000
    error = 0
    new_b = 0
    new_m = 0
    derror_db = 0
    derror_dm = 0

    for j in range(iteration):
        for i in range(len(data_b['price_list'])):
            y_p = b + m * data_b['mileage_list'][i]
            error = (y_p - data_b['price_list'][i]) ** 2 # MSE
            derror = 2 * (y_p - data_b['price_list'][i])
            derror_db += derror * 1
            derror_dm += derror * data_b['mileage_list'][i]
        b = b - derror_db / len(data_b['price_list']) * lr
        m = m - derror_dm / len(data_b['mileage_list']) * lr
        derror_db = 0
        derror_dm = 0
    print(b)
    return data_b
#        residual = loss_computing(price_list, mileage_list, slope, b, lr)

 

def     average_compute(averagef):
    price_list = []
    mileage_list = []
    data_b = {}
    line = averagef.readline()
    try:
        while (True):
            line = averagef.readline()
            if not line:
                break
            tmp_list = line.split(",")
            tmp_list[1].rstrip("\n")
            price_list.append(int(tmp_list[1]))
            mileage_list.append(int(tmp_list[0].rstrip("\n")))
    except:
        print("Good data file is ./data.csv")
        exit();
    data_b['price_list'] = price_list
    data_b['mileage_list'] = mileage_list
    data_b['average_price'] = sum(price_list) / len(price_list)
    data_b['average_mileage'] = sum(mileage_list) / len(mileage_list)
    return data_b


if  __name__ == "__main__":
    b = 0
    m = 0
    data_dico = {} #dico is a lingo word for dictionary in french
    parser = argparse.ArgumentParser(description='Example: python3 training data.csv')
    parser.add_argument('file', type=str, help=': the data file in the current directory')
    args = parser.parse_args()
    try:
        averagef = open(args.file)
        f = open(args.file)
    except:
        print("open failled for '", args.file, "'")
        exit()
    data_dico = average_compute(averagef)
    print(data_dico['price_list'])
    #price_list, mileage_list, sd_price, sd_mileage
    data_dico = data_normalization(data_dico)
    b, m = gradient_descent(data_dico)
    print(data_dico['price_list'])
  #  data_dico = data_denormalization(data_dico)
