# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/23 09:52:36 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 12:28:11 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  argparse

def     training(f):
    while (1):
        s = f.readline()
        if not s:
            return
        print(s)
            
    

if  __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data file needed')
    parser.add_argument('file', type=str, help='a file with some data :v')
    args = parser.parse_args()
    try:
        f = open(args.file)
    except:
        print("open failled for '", args.file, "'")
    training(f)
