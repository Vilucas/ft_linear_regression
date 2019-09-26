# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/23 09:52:36 by viclucas          #+#    #+#              #
#    Updated: 2019/09/25 16:52:33 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  argparse
import  numpy as np

def     average_compute(averagef):
    price_list = []
    mileage_list = []
    line = averagef.readline()
    try:
        while (True):
            line = averagef.readline()
            if not line:
                break
            tmp_list = line.split(",")
            tmp_list[1].rstrip("\n")
            price_list.append(int(tmp_list[0]))
            mileage_list.append(int(tmp_list[1].rstrip("\n")))
    except:
        print("Good data file hum ?")
        exit();
    return price_list, mileage_list

def     loss_computing(price_list, mileage_list, slope, c, lr):
     for i in range(len(price_list)):
            y = slope * price_list[i] + c
            residual += (mileage_list[i] - y) ** 2
        print(residual)
        loss = (residual * lr) / float(len(price_list))
    return loss

def     gradient_descent(price_list, mileage_list):
    slope = 0
    c = 0
    lr = 0.0001
    iteration = 100
    residual = 0

    for j in range(inter):
        residual = loss_computing(price_list, mileage_list, slope, c, lr)
        
if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data file needed')
    parser.add_argument('file', type=str, help='a file with some data')
    args = parser.parse_args()
    try:
        averagef = open(args.file)
        f = open(args.file)
    except:
        print("open failled for '", args.file, "'")
    #instantion instantiation
    average_price, average_mileage, price_list, mileage_list = average_compute(averagef)
    gradient_descent(price_list, mileage_list)
#   linear(average_price, average_mileage, price_list, mileage_list)
#   print(average_price, averace_mileage)
#   linear_regression(average_price, average_mileage)
    training(f)
