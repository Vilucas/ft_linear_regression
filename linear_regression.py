# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/22 12:56:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/27 23:36:19 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from training import *


global_m = 0
global_b = 0

if __name__ == "__main__":
    result[]
    try:
        print("Choose a mileage, we will give you a price approximation\n", "$> ", end="")
        s = int(input())
    except:
       print("Wrong input :v")
       exit()
    f = open(".result.cvs")
    line = f.readline()
    line.split(",")
    print("The estimated price for ur mileage input is :", end="")
    print(int(line[0]) + (int(line[i]) * s))
