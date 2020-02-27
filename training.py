# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/23 09:52:36 by viclucas          #+#    #+#              #
#    Updated: 2019/09/29 10:32:06 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  argparse

def     data_normalization(data):
    for i in range(len(data['price_list'])):
        data['price_list'][i] = data['price_list'][i] - min(data['price_list'])
        data['price_list'][i] /= max(data['price_list']) - min(data['price_list']) 
    for i in range(len(data['mileage_list'])):
        data['mileage_list'][i] = data['mileage_list'][i] - min(data['mileage_list'])
        data['mileage_list'][i] /= max(data['mileage_list']) - min(data['mileage_list']) 
    return data

def     gradient_descent(data_b):
    m = 0
    b = 0
    lr = 0.1
    iteration = 215
    error = 0
    derror_db = 0
    derror_dm = 0

    for j in range(iteration):
        for i in range(len(data_b['price_list'])):
            y_p = b + m * data_b['mileage_list'][i]
            derror = 2 * (y_p - data_b['price_list'][i])
            derror_db += derror * 1
            derror_dm += derror * data_b['mileage_list'][i]
        b = b - (derror_db / len(data_b['price_list'])) * lr
        m = m - (derror_dm / len(data_b['mileage_list'])) * lr
        derror = 0
        derror_db = 0
        derror_dm = 0
    data_b['b'] = b
    data_b['m'] = m
    return data_b

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

def     training():
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
    data_dico['o_price_list'] = list(data_dico['price_list'])
    data_dico['o_mileage_list'] = list(data_dico['mileage_list'])
    data_dico = data_normalization(data_dico)
    data_dico = gradient_descent(data_dico)
    f.close()
    f = open(".result.cvs", "w")
    s = str(data_dico['b']) + "," + str(data_dico['m'])
    f.write(s)
    return (data_dico)

if  __name__ == "__main__":
    training()
