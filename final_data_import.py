import csv
import os
from utilities import sqlutils



# restaurant payment final
counter = 0
input_data = "data/chefmozaccepts.csv"

with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO restaurant_payment(placeID, rpayment_type) "
            sql = sql + "VALUES(%s, %s); SET FOREIGN_KEY_CHECKS=1" #NEED TO HAVE AS MANY OF THESE WEIRD PLACEHOLDERS AS THERE ARE VALUES
            sqlutils.execMysqlQuery(sql, (row[0], row[1]))
            # print(sql)

        counter = counter + 1





#user_profile

counter = 0
input_data = "data/userprofile.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO user_profile(userID,smoker,drink_level, dress_preference," \
                  " ambience_preference, transport, marital_status, children, birth_year, interest, personality, religion, activity, color, weight, budget, height) "
            sql = sql + "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" #NEED TO HAVE AS MANY OF THESE WEIRD PLACEHOLDERS AS THERE ARE VALUES
            sqlutils.execMysqlQuery(sql, (row[0], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))
            # print(sql)

        counter = counter + 1


#user_payment

counter = 0
input_data = "data/userpayment.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO user_payment(userID, payment_type) "
            sql = sql + "VALUES(%s, %s);" #NEED TO HAVE AS MANY OF THESE WEIRD PLACEHOLDERS AS THERE ARE VALUES
            sqlutils.execMysqlQuery(sql, (row[0], row[1]))
            # print(sql)

        counter = counter + 1




#restaurant - cuisine
counter = 0
input_data = "data/chefmozcuisine.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO restaurant_cuisine(placeID, r_cuisine) "
            sql = sql + "VALUES(%s, %s); SET FOREIGN_KEY_CHECKS=1;"
            sqlutils.execMysqlQuery(sql, (row[0], row[1]))
            # print(sql)

        counter = counter + 1



#address 

counter = 0
input_data = "data/geoplaces2.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO address(placeID,street,city,state,country,zip) "
            sql = sql + "VALUES(%s, %s, %s, %s, %s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[5], row[6], row[7], row[8], row[10]))
            # print(sql)

        counter = counter + 1


#user_geo_location

counter = 0
input_data = "data/userprofile.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO user_geo_location(userID, latitude, longitude) "
            sql = sql + "VALUES(%s, %s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[1], row[2]))
            # print(sql)

        counter = counter + 1



#user_cuisine_preference

counter = 0
input_data = "data/usercuisine.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO user_cuisine_pref(userID, cuisine_pref) "
            sql = sql + "VALUES(%s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[1]))
            # print(sql)

        counter = counter + 1
        


#time open

counter = 0
input_data = "data/chefmozhours4.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO time_open(placeID, hours, days) "
            sql = sql + "VALUES(%s, %s, %s); SET FOREIGN_KEY_CHECKS=1"
            sqlutils.execMysqlQuery(sql, (row[0], row[1], row[2]))
            # print(sql)

        counter = counter + 1

#restaurant - main

counter = 0
input_data = "data/geoplaces2.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO restaurant(placeID,the_geom_meter, name, alcohol, price, url, franchise) "
            sql = sql + "VALUES(%s, %s, %s, %s, %s, %s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[3], row[4], row[10], row[14], row[15], row[18]))
            # print(sql)

        counter = counter + 1


#user_geo_location

counter = 0
input_data = "data/geoplaces2.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO res_geo_location(placeID, latitude, longitude) "
            sql = sql + "VALUES(%s, %s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[1], row[2]))
            # print(sql)

        counter = counter + 1


#AMBIENCE

counter = 0
input_data = "data/geoplaces2.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "INSERT INTO ambience(placeID,smoking_area, dress_code, accessibility, ambience_type, area, other_services) "
            sql = sql + "VALUES(%s, %s, %s, %s, %s, %s, %s);"
            sqlutils.execMysqlQuery(sql, (row[0], row[12], row[13], row[14], row[17], row[19], row[20]))
            # print(sql)

        counter = counter + 1


#PARKING

counter = 0
input_data = "data/chefmozparking.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO parking(placeID, parking_lot) "
            sql = sql + "VALUES(%s, %s); SET FOREIGN_KEY_CHECKS=1;"
            sqlutils.execMysqlQuery(sql, (row[0], row[1]))
            # print(sql)

        counter = counter + 1

#Ratings Final

counter = 0
input_data = "data/rating_final.csv"


with open(input_data, 'rU') as f:
    for row in csv.reader(f):
        if any(row) and counter > 0:
            print(row[0] + ': ' + row[1])
            sql = "SET FOREIGN_KEY_CHECKS=0; INSERT INTO ratings_final(userID, placeID,rating,food_rating, service_rating) "
            sql = sql + "VALUES(%s, %s, %s, %s, %s); SET FOREIGN_KEY_CHECKS=1;"
            sqlutils.execMysqlQuery(sql, (row[0], row[1], row[2], row[3], row[4]))
            # print(sql)

        counter = counter + 1

