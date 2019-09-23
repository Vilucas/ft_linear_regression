# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/22 12:56:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/22 20:30:26 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

def     mileage():
    parser = argparse.ArgumentParser()
    parser = add.argument("mileage", type=str, help="Choose a mileage for your car\n")
    arg = parser.parse_arg()
    print(arg.mileage)
