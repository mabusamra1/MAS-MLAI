## Project Name: Analysis of Customer Acceptance of Coupon
### By Mohammad Abu-Samra
In this project we will follow the CRISP-DM process to try answer the question, will the customer accept the coupon?  The short term goal is to focus on the first 3 phases of the process: Business Understanding, Data Understanding and Data Preparation by utilizing the visualizing and probability distributions techniques to distinguish between customers who accepted a driving coupon versus those that did not.

### 1. Business Understanding

#### 1.1 Background
The firm has launched a marketing campaign in form of a coupon for different classes of restaurants and bars targeting drivers while in route to their destinations. The firm wanted to understand how effective this marketing campaign, so they conducted a survey on Amazon Mechanical Turk. They wanted to know what useful information can be extracted from the survey to help improving the business marketing strategies. For instance, they are looking for answers to the following questions: Would the deliver accept that coupon and take a short detour to the restaurant? Would the driver accept the coupon but use it on a subsequent trip? Would the driver ignore the coupon entirely? What if the coupon was for a bar instead of a restaurant? What about a coffee house? Would the driver accept a bar coupon with a minor passenger in the car? What about if it was just the driver and a partner in the car? Would weather impact the rate of acceptance? What about the time of day?

#### 1.2 Business Goals and KPIs
The business goal is a continuation of the background problem, which is to gain insight on what drives the drivers to accept the coupon.


### 2. Data Understanding
On the Data Understanding phase, we will gather, describe and explore the data to make sure it fits the business goal. The deliverable or result of this phase should include:

Data description
Early data exploration report
Data quality report

#### 2.1 Gathering and Describing Data
The data was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’. There are five different types of coupons -- less expensive restaurants (under $20$), coffee houses, carry out & take away, bar, and more expensive restaurants ($20$ - $50$).

The attributes of this data set include:
1. User attributes
    -  Gender: male, female
    -  Age: below 21, 21 to 25, 26 to 30, etc.
    -  Marital Status: single, married partner, unmarried partner, or widowed
    -  Number of children: 0, 1, or more than 1
    -  Education: high school, bachelors degree, associates degree, or graduate degree
    -  Occupation: architecture & engineering, business & financial, etc.
    -  Annual income: less than \\$12500, \\$12500 - \\$24999, \\$25000 - \\$37499, etc.
    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
    -  Number of times that he/she buys takeaway food: 0, less than 1, 1 to 3, 4 to 8 or greater
    than 8
    -  Number of times that he/she goes to a coffee house: 0, less than 1, 1 to 3, 4 to 8 or
    greater than 8
    -  Number of times that he/she eats at a restaurant with average expense less than \\$20 per
    person: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
    

2. Contextual attributes
    - Driving destination: home, work, or no urgent destination
    - Location of user, coupon and destination: we provide a map to show the geographical
    location of the user, destination, and the venue, and we mark the distance between each
    two places with time of driving. The user can see whether the venue is in the same
    direction as the destination.
    - Weather: sunny, rainy, or snowy
    - Temperature: 30F, 55F, or 80F
    - Time: 10AM, 2PM, or 6PM
    - Passenger: alone, partner, kid(s), or friend(s)


3. Coupon attributes
    - time before it expires: 2 hours or one day
   
Here is how the dataset looks like\
Total number of rows = 12684\

| No | Column.             |Non Null-Count    Type
|:---|:--------------------|:---------------------|
| 0   |destination          |12684 non-null  object|
| 1   |passanger            |12684 non-null  object|
| 2   |weather              |12684 non-null  object|
| 3   |temperature          |12684 non-null  int64 |
| 4   |time                 |12684 non-null  object|
| 5   |coupon               |12684 non-null  object|
| 6   |expiration           |12684 non-null  object|
| 7   |gender               |12684 non-null  object|
| 8   |age                  |12684 non-null  object|
| 9   |maritalStatus        |12684 non-null  object|
| 10  |has_children         |12684 non-null  int64 |
| 11  |education            |12684 non-null  object|
| 12  |occupation           |12684 non-null  object|
| 13  |income               |12684 non-null  object|
| 14  |car                  |108 non-null    object|
| 15  |Bar                  |12577 non-null  object|
| 16  |CoffeeHouse          |12467 non-null  object|
| 17  |CarryAway            |12533 non-null  object|
| 18  |RestaurantLessThan20 |12554 non-null  object|
| 19  |Restaurant20To50     |12495 non-null  object|
| 20  |toCoupon_GEQ5min     |12684 non-null  int64 |
| 21  |toCoupon_GEQ15min    |12684 non-null  int64 |
| 22  |toCoupon_GEQ25min    |12684 non-null  int64 |
| 23  |direction_same       |12684 non-null  int64 |
| 24  |direction_opp        |12684 non-null  int64 |
| 25  |Y                    |12684 non-null  int64 |

dtypes: float64(5), int64(11), object(9)



#### 2.2 Early Data Exporation and Data Quality Check
We need to check the quality of the data. For example, since many of the column/variable is categorical, we can check the summary of the data and see the number of customer of each categories. By doing this, we can also check whether there are any data that need to be cleansed or to be transformed. For example, we can check if there is a missing/empty values and duplicates. The below table lists the objects columns with their categorical data. 


| Column.             |Categorical Data
|:--------------------|:---------------------|
destination|                                 [No Urgent Place, Home, Work]
|passanger  |                           [Alone, Friend(s), Kid(s), Partner]
|weather    |                                         [Sunny, Rainy, Snowy]
|time       |                                   [2PM, 10AM, 6PM, 7AM, 10PM]
|coupon     |             [Restaurant(<20), Coffee House, Carry out & Ta...
|expiration |                                                      [1d, 2h]
|gender     |                                                [Female, Male]
|age        |                     [21, 46, 26, 31, 41, 50plus, 36, below21]
|maritalStatus|           [Unmarried partner, Single, Married partner, D...
|education    |           [Some college - no degree, Bachelors degree, A...
|occupation   |           [Unemployed, Architecture & Engineering, Stude...
|income       |           [$37500 - $49999, $62500 - $74999, $12500 - $2...
|car          |           [nan, Scooter and motorcycle, crossover, Mazda...
|Bar          |                          [never, less1, 1-3, gt8, nan, 4-8]
|CoffeeHouse  |                          [never, less1, 4-8, 1-3, gt8, nan]
|CarryAway    |                          [nan, 4-8, 1-3, gt8, less1, never]
|RestaurantLessThan20|                   [4-8, 1-3, less1, gt8, nan, never]
|Restaurant20To50    |                   [1-3, less1, never, gt8, 4~8, nan]

The first glance of the object columns and their categorical values, the following columns data will have to be trasformed and fixed:  Age, Occupation, Expiration, Income, Bar, CarryAway, RestaurantLessThan20 and Restaurant20To50.


### 3. Data Preparation
On the Data Understanding phase, we will prepare and cleanse the data so they are fit for analysis and making prediction. The data preparation take 80% of the data mining process.

The deliverable or result of this phase should include:

Data preparation steps\
Final data for analysis and modeling (if desired)

#### 3.1 Data Cleansing
On this process, we handle the data based on the problem we find during the data understanding phase. Based on our finding, the following process was executed:

a) Fixed the age values and converted it to numeric\
b) Shortened the occupation, education and coupon columns values\
c) converted the columns (Bar,CarryAway,CoffeeHouse,RestaurantLessThan20, Restaurant20To50) values and converting them to numeric'\
d) Converted the expiration column to numeric in hours\
e) Fixed the income column and converting the values to numeric (taking the average)\
f) Fixed the typo in passenger column name\
g) Treatment of the missing and duplicate data

All the missing values are from columns with type object/string.  the column cars is missing about 99% of the data, it was decided to drop it.  the other columns (Bar, CoffeeHouse, CarryAway, ResuarantLessThan20 and Restaurant20To50) are missing about 1% of their values, so dropping the missing rows should not impact the data analysis, hence were dropped.  The duplicates were dropped

Finally, after careful and rigorous data cleansing, we acquire our final data that will be used for analysis and modeling.



#### 3.2 Final Data



| No | Column.             |Non Null-Count    Type
|:---|:--------------------|:---------------------|
| 0   |destination          |12017 non-null  object|
| 1   |passanger            |12017 non-null  object|
| 2   |weather              |12017 non-null  object|
| 3   |temperature          |12017 non-null  int64 |
| 4   |time                 |12017 non-null  object|
| 5   |coupon               |12017 non-null  object|
| 6   |expiration           |12017 non-null  int64|
| 7   |gender               |12017 non-null  object|
| 8   |age                  |12017 non-null  int64|
| 9   |maritalStatus        |12017 non-null  object|
| 10  |has_children         |12017 non-null  int64 |
| 11  |education            |12017 non-null  object|
| 12  |occupation           |12017 non-null  object|
| 13  |income               |12017 non-null  int64|
| 15  |Bar                  |12017 non-null  object|
| 16  |CoffeeHouse          |12017 non-null  object|
| 17  |CarryAway            |12017 non-null  object|
| 18  |RestaurantLessThan20 |12017 non-null  object|
| 19  |Restaurant20To50     |12017 non-null  object|
| 20  |toCoupon_GEQ5min     |12017 non-null  int64 |
| 21  |toCoupon_GEQ15min    |12017 non-null  int64 |
| 22  |toCoupon_GEQ25min    |12017 non-null  int64 |
| 23  |direction_same       |12017 non-null  int64 |
| 24  |direction_opp        |12017 non-null  int64 |
| 25  |Y                    |12017 non-null  int64 |

### 4. Data Understanding through Analysis
The CRISP-DM process nature is an itterative one. We can go back and forth between process to make sure it fits the business and data mining goals. Here, we go back to data understanding phase to further explore and analyze the data before the modeling phase (out of scope for this project).

#### 4.1 Exploratory Data Analysis
The process of exploring and visualizing insight from the data is called Exploratory Data Analysis (EDA).



#### 4.1.1 Prior Observations
The first step in the data analysis is to understand the data distribution, i.e., if it is biased.  The distribution of the passenger type data indicates that most are under the "Alone" category by a wide margin.  This effect is propegated throguh the distribution of coupons for both accepted and rejected as shown in the below diagrams.

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/PassengerDistributionHistogram.png)

**Figure-1:** [Passenger Distribution Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/PassengerDistributionHistogram.png)

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponAcceptancePerPassengerType.png)

**Figure-2:** [Coupon Acceptance per Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponAcceptancePerPassengerType.png)

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponRejectionPerPassengerType.png)

**Figure-3:** [Coupon Rejection per Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponRejectionPerPassengerType.png)

The coupons bar diagram shows that the Coffee House coupon had the most observations/participants count and the Restaurant(20-50) coupon had the least number of observations/participants. 

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponTypesDistribution.png)

**Figure-4:** [Coupon Distribution](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponTypesDistribution.png)

Please note that this diagram does not show the percentage of acceptance/rejection of the coupon), instead it is shown in the below histogram which tells us the following about the coupon:

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAcceptanceRejectionHistogram.png)

**Figure-5:** [Coupon Acceptance Rejection Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAcceptanceRejectionHistogram.png)

1) Coffee house has the highest rejection rate of ( 16 %) and highest acceptance rate of ( 15.72 %).
2) Restaurant(<20)/Cheap coupon is 2nd with acceptance rate of ( 15.64 %) and rejection rate of ( 6.4 %)
3) Carry Out coupon was the 3rd with acceptance rate of ( 13.68 %) and has the least rejection rate of ( 4.92 %)
4) Bar coupon comes in number 4 of acceptance rate of ( 6.54 %) and rejection rate of ( 9.31 %)
5) Restaurant(20-50) is last with acceptance rate of ( 5.25 %) and rejection rate of ~( 6.50 %)

The temperature histogram shows that the coupon was best accepted when the temperature was around 80F and least accepted when the temperature around 30F


![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/temperatureHistogram.png)

**Figure-6:** [Temperature Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/temperatureHistogram.png)


#### 4.1.2 Observations

#### 4.1.2.1 Heatmap Anaylisis¶
Since this is a classification use case, there is no significant correlation between the coupon acceptance/rejection represented by the Y column and the other features. It was noticed that there is a 100% negative correlation between the same direction and opossite direction of the shop destination. However, this does not impact the driver decision on whether to accept or reject the coupon.

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponCorrHeatmap.png)

**Figure-7:** [Coupon Correlation HeatMap](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponCorrHeatmap.png)

#### 4.1.2.2 Drivers' Age Impact Analysis¶ 
From the catplot diagram, most of the drivers who accepted/rejected a coupon were between the age of 21 to 31, and it spikes again for the age greater than 50.  The Coffee House coupon was the most to be accepted/rejected.  The cheap restaurant < $20 was more likely to be selected after the Coffee house followed by the Carry out coupon. 

![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejAge.png)

**Figure-8:** [Temperature Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejAge.png)

<h4 style="color:black"> 4.1.2.3 Drivers' Marital Status Impact Analysis</h4>  
<p style="color:black"> The accepted diagram shows the single and married partner were the most to accept the Coffee House, cheap restaurant and Carry out coupons respectively.  The rejected diagram shows the same driver pattern as the accepted case to reject the Coffee House coupon with almost the same rate.  Also, it shows the married partner were rejecting the Bar coupon with a rate close to ($4.6$%)</p>
                           
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejMaritalStatus.png)

**Figure-9:** [Coupon Acceptance Rejection per Driver Marital Status](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejMaritalStatus.png)                        
                                                                                                                                                  

<h4 style="color:black"> 4.1.2.4 Drivers' with/out Chidren Impact Analysis</h4>  
<p style="color:black">The catplot diagram shows that close to ($10$%) of the drivers who don't have children were more likely to select the Coffee House and cheap restaurant coupons.  About ($8$%) of the same pattern were more likely to accept the Carry out coupon.  Also, about ($10$%) from the same pattern were more likely to reject the Coffee House coupon.
    
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejHasChildren.png)

**Figure-10:** [Coupon Acceptance Rejection per Driver's Family- Children](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejHasChildren.png)  

<h4 style="color:black"> 4.1.2.5 Drivers' income Impact Analysis</h4>  
<p style="color:black">From the diagram we can see that the drivers with average income between ($18K$)  and  ($56K$) and above ($100K$) were more likely to accept the cheap restaurant, Coffee House and Carry out coupons.  The drivers with the same pattern as the acceptance case were more likely to reject the Coffee House coupon. 
    
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejIncome.png)
**Figure-11:** [Coupon Acceptance Rejection per Driver's Income](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejIncome.png)

<h4 style="color:black"> 4.1.2.6 Drivers' Occupation Impact Analysis</h4>  
<p style="color:black">The catplot/count percentage shows that the unemployed, students and drivers who work in the Computer and Math fields have the highest acceptance rate of a coupon with an average about ($7.3$%) 
    
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejOccupation.png)
**Figure-12:** [Coupon Acceptance Rejection by Driver's Occupation](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejOccupation.png)


<h4 style="color:black"> 4.1.2.7 Drivers' Education Impact Analysis</h4>  
<p style="color:black"> The drivers with Bachelors and Some college degrees were more likely to accept the cheap restaurant, Coffee House and Carry out coupons respectively.  About the same percentage of the same drivers pattern were more likely to reject the Coffee House coupon.
    
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejEducation.png)
**Figure-13:** [Coupon Acceptance Rejection per Driver's Education](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejEducation.png)

<h4 style="color:black"> 4.1.2.8 Drivers' Gender Impact Analysis</h4>  
<p style="color:black">The catplot diagram shows that about ($7.5$%) of the male/female were more likely to accept the cheap restaurant, Coffee House and Carry out coupons.  About the same percent of both genders were more likely to reject the Coffee House coupon. 
    
 ![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGender.png)
**Figure-14:** [Coupon Acceptance Rejection per Driver's Gender](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGender.png)

<h4 style="color:black"> 4.1.2.9 Drivers' Gender and Passenger Impact Analysis</h4>  
<p style="color:black"> The male drivers without passengers (driving Alone) were more likely to accept a coupon with a rate = ($16$%).  The same pattern with a rate of about ($12.5$%) were more likely to reject a coupon.  The female drivers without passengers were almost equally likely to accept/reject a coupon with a rate about ($15$%)
    
 
![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGenderPassenger.png)
**Figure-15:** [Coupon Acceptance Rejection per Driver's Gender and Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGenderPassenger.png)

<h4 style="color:black"> 4.1.2.10 Further Analysis Conclusion</h4>  
<p style="color:black"> The above analysis showed that there is no single feature pattern can impact the driver decision with high percentage.  The drivers' decisions were driven by collection of features.  Because the data is biased as shown in section 4.1.1 above, I think the joint/conditional probability seems the best approach to properly predict the drivers' decisions. Interestingly, I noticed that the Coffee House coupon has the most acceptance rate among all the coupon types so I decided to explore it further with conditional probabilities.
The conditional probabilities plot shows that the drivers with Friend passenger has the highest probability to reject the Coffee House coupon. The driver traveling without passengers (Alone) has the highest probability to accept the Coffee House coupon.  
    
 ![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/pCoffeeHouseCouponAccptRejPassengerType.png)
**Figure-16:** [Conditional Probability of Accepting the Coffee House Coupon per PAssenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/pCoffeeHouseCouponAccptRejPassengerType.png)

### 5. Next Step and Future Work

Conducting more deeper analysis of the other driver characteristics combinations to predict the impacting features.  Also, preparing the data further to be ready for machine learning modeling, and to select the best model suites the case study.   

**Link to the Juypter Notebook** (https://github.com/mabusamra1/MAS-MLAI/blob/main/Coupon.ipynb)
