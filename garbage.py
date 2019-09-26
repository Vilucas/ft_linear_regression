# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    garbage.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/25 16:19:11 by viclucas          #+#    #+#              #
#    Updated: 2019/09/25 16:25:16 by viclucas         ###   ########.fr        #
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

