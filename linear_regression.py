# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/22 12:56:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/27 21:56:24 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from training import updater

def     ft_linear_regression():
    parser = argparse.ArgumentParser()
    parser = add.argument("mileage", type=str, help="Choose a mileage for your car\n")
    arg = parser.parse_arg()
    print(arg.mileage)
