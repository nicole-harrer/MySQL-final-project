USE ijk8;

#**********************User Tables************************

#user_profile - removed latitude and longitude and place them in new table

CREATE TABLE user_profile (
    userID VARCHAR(10) PRIMARY KEY NOT NULL,
    smoker VARCHAR(10) NOT NULL,
    drink_level CHAR(15) NOT NULL,
    dress_preference VARCHAR(15) NOT NULL,
    ambience_preference VARCHAR(15) NOT NULL,
    transport VARCHAR(10) NOT NULL,
    marital_status VARCHAR(10) NOT NULL,
    children VARCHAR(15) NOT NULL,
    birth_year DATETIME NOT NULL,
    interest CHAR(15) NOT NULL,
    personality VARCHAR(25) NOT NULL,
    religion CHAR(15) NOT NULL,
    activity VARCHAR(20) NOT NULL,
    color CHAR(10) NOT NULL,
    weight INT(3) NOT NULL,
    budget VARCHAR(10) NOT NULL,
    height DECIMAL NOT NULL
)  ENGINE=INNODB;

/*USER PAYMENT - References the user_profile. We did not link "user_payment" with 
the "restaurant_accepts", because there is no transaction being recorded, these
are simply attributes of each catergory */

CREATE TABLE user_payment (
    userID VARCHAR(10) NOT NULL,
    payment_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (userID)
        REFERENCES user_profile (userID)
)  ENGINE=INNODB;

/* user_geo_location*/

CREATE TABLE user_geo_location(
	userID VARCHAR(10) NOT NULL,
    latitude DECIMAL (15) NOT NULL, 
	longitude DECIMAL (15) NOT NULL,
    FOREIGN KEY (userID)
		REFERENCES user_profile (userID)

)  ENGINE=INNODB;

/*user_cuisine_preference - We created a seperate table because the users have multiple 
cuisine preferences listed. We did not put user-cuisine preference in the same table as
the one listing the the cuisines offered by restaurants, because the restaurants also had 
several cuisine types. This would also mess up the results for one of the queries.

Auto-incremented to seperate the users different preferences */

CREATE TABLE user_cuisine_pref(
	ucuisine_id int(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    userID VARCHAR(10) NOT NULL,
    cuisine_pref VARCHAR(25) NOT NULL,
    FOREIGN KEY (userID)
		REFERENCES user_profile (userID)
) ENGINE=INNODB;






#*******************RESTAURANT TABLES****************************

/*Restaurant General Information - We removed fax, because there was not any
data listed for any of the restaurants excepts a "?". Other attributes were moved to
different tables
*/
CREATE TABLE restaurant (
    placeID INT(10) PRIMARY KEY NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    the_geom_meter VARCHAR(150) NOT NULL,
    alcohol VARCHAR(15) NOT NULL,
    price CHAR(10) NOT NULL,
    url VARCHAR(20) NOT NULL,
    franchise CHAR(10) NOT NULL
)  ENGINE=INNODB;


/*RESTAURANT HOURS/DAYS*/

CREATE TABLE time_open(
placeID INT(10) NOT NULL,
hours VARCHAR(20) NOT NULL,
days CHAR (25),
FOREIGN KEY (placeID) 
	REFERENCES restaurant(placeID)
) ENGINE = INNODB;

/* restaurant cuisine */

CREATE TABLE restaurant_cuisine(
	cuisine_id int(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    placeID INT(10) NOT NULL,
    r_cuisine VARCHAR(25) NOT NULL,
    FOREIGN KEY (placeID)
		REFERENCES restaurant (placeID)
) ENGINE=INNODB;

/*RESTAURANT PAYMENT*/

CREATE TABLE restaurant_payment (
    PRIMARY KEY (placeID , rpayment_type),
    placeID INT(10) NOT NULL,
    rpayment_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID)
)  ENGINE=INNODB;

/*Restaurant Coordinates*/

CREATE TABLE res_geo_location (
    placeID INT(10) NOT NULL,
    latitude DECIMAL(15) NOT NULL,
    longitude DECIMAL(15) NOT NULL,
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID)
)  ENGINE=INNODB;

/* Restaurant Address  */

CREATE TABLE address (
    placeID INT(10) NOT NULL,
    street VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(50) NOT NULL,
    country VARCHAR(100) NOT NULL,
    zip VARCHAR(10) NOT NULL,
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID)
)  ENGINE=INNODB;

/* Restaurant Ambience */

CREATE TABLE ambience (
    placeID INT(10) NOT NULL,
    smoking_area CHAR(15) NOT NULL,
    dress_code CHAR(15) NOT NULL,
    accessibility VARCHAR(20) NOT NULL,
    ambience_type CHAR(10) NOT NULL,
    area CHAR(10) NOT NULL,
    other_services CHAR(10) NOT NULL,
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID)
)  ENGINE=INNODB;


/* Restaurant Parking  */

CREATE TABLE parking (
    placeID INT NOT NULL,
    parking_lot VARCHAR(50) NOT NULL,
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID)
)  ENGINE=INNODB;

/***************RATINGS FINAL*************/

CREATE TABLE ratings_final (
    PRIMARY KEY (userID , placeID),
    FOREIGN KEY (userID)
        REFERENCES user_profile (userID),
    FOREIGN KEY (placeID)
        REFERENCES restaurant (placeID),
    userID VARCHAR(20) NOT NULL,
    placeID INT(10) NOT NULL,
    rating INT(2) NOT NULL,
    food_rating INT(2) NOT NULL,
    service_rating INT(2) NOT NULL
)  ENGINE=INNODB;


