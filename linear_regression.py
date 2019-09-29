# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/22 12:56:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/29 10:32:06 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from training import *

if __name__ == "__main__":
    result = []
    data_dico = {}
    line = ""

    try:
        print("Choose a mileage, we will give you a price approximation\n", "$> ", end="")
        s = int(input())
    except:
       print("Wrong input")
       exit()
    try:
        f = open(".result.cvs")
        line = f.readline()
    except:
        s = 0 
    if line:
        line = line.split(",")
    if s != 0:
        try:
            data_dico = average_compute(open("data.csv")) 
        except:
            print("give me my data file back :(")
            exit()
        s = s - min(data_dico['price_list'])
        s /= (max(data_dico['price_list']) - min(data_dico['price_list']))
        s = float(line[0]) + (float(line[1]) * float(s))
        s *= (max(data_dico['price_list']) - min(data_dico['price_list']))
        s = s + min(data_dico['price_list'])
    print("The estimated price for your mileage input is : ", end="")
    print(round(s))
