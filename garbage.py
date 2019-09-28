# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    garbage.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/25 16:19:11 by viclucas          #+#    #+#              #
#    Updated: 2019/09/27 21:49:09 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    return round(sum(price_list) / len(price_list), 2), round(sum(mileage_list) / len(mileage_list), 2), price_list, mileage_list


def     other_average(price_list, mileage_list, average_price, average_mileage):
    average_pm = 0
    average_pp = 0

    for i in range(len(price_list)):
        average_pm += price_list[i] * mileage_list[i]
    average_pm /= len(price_list)
    for i in range(len(price_list)):
        average_pp += price_list[i] * price_list[i]
    print(average_price, average_mileage, int(average_pm), average_pp)
    m = ((average_price * average_mileage) - int(average_pm))
    m /= (average_price * average_price) - average_pp
    return m

def     data_destandardization(d):

    for i in range(len(d['price_list'])):
        d['price_list'][i] = round((d['price_list'][i] * d['sd_price']) + d['average_price'])
    for i in range(len(d['mileage_list'])):
        d['mileage_list'][i] = round((d['mileage_list'][i] * d['sd_mileage']) + d['average_mileage'])
    return d

def     data_standardization(d):
    sd_price = 0

    for i in range(len(d['price_list'])):
        sd_price += (d['price_list'][i] - d['average_price']) ** 2
    sd_price = sd_price / len(d['price_list'])
    sd_price = math.sqrt(sd_price)
    for i in range(len(d['price_list'])):
        d['price_list'][i] = (d['price_list'][i] - d['average_price']) / sd_price
    ##
    #mileage
    ##
    sd_mileage = 0
    for i in range(len(d['mileage_list'])):
        sd_mileage += abs(d['mileage_list'][i] - d['average_mileage']) ** 2
    sd_mileage = sd_mileage / len(d['mileage_list'])
    sd_mileage = math.sqrt(sd_mileage)
    for i in range(len(d['mileage_list'])):
        d['mileage_list'][i] = (d['mileage_list'][i] - d['average_mileage']) / sd_mileage
    d['sd_mileage'] = sd_mileage
    d['sd_price'] = sd_price
    return d
