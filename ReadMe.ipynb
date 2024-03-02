{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6336a824",
   "metadata": {},
   "source": [
    "## Project Name: Analysis of Customer Acceptance of Coupon"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91eb775a",
   "metadata": {},
   "source": [
    "In this project we will follow the CRISP-DM process to try answer the question, will the customer accept the coupon?  The short term goal is to focus on the first 3 phases of the process: Business Understanding, Data Understanding and Data Preparation by utilizing the visualizing and probability distributions techniques to distinguish between customers who accepted a driving coupon versus those that did not."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60d28271",
   "metadata": {},
   "source": [
    "### 1. Business Understanding"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d6585f3",
   "metadata": {},
   "source": [
    "#### 1.1 Background\n",
    "The firm has launched a marketing campaign in form of a coupon for different classes of restaurants and bars targeting drivers while in route to their destinations. The firm wanted to understand how effective this marketing campaign, so they conducted a survey on Amazon Mechanical Turk. They wanted to know what useful information can be extracted from the survey to help improving the business marketing strategies. For instance, they are looking for answers to the following questions: Would the deliver accept that coupon and take a short detour to the restaurant? Would the driver accept the coupon but use it on a subsequent trip? Would the driver ignore the coupon entirely? What if the coupon was for a bar instead of a restaurant? What about a coffee house? Would the driver accept a bar coupon with a minor passenger in the car? What about if it was just the driver and a partner in the car? Would weather impact the rate of acceptance? What about the time of day?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b41f1af4",
   "metadata": {},
   "source": [
    "#### 1.2 Business Goals and KPIs\n",
    "The business goal is a continuation of the background problem, which is to gain insight on what drives the drivers to accept the coupon.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f44433c1",
   "metadata": {},
   "source": [
    "### 2. Data Understanding\n",
    "On the Data Understanding phase, we will gather, describe and explore the data to make sure it fits the business goal. The deliverable or result of this phase should include:\n",
    "\n",
    "Data description\n",
    "Early data exploration report\n",
    "Data quality report\n",
    "\n",
    "#### 2.1 Gathering and Describing Data\n",
    "The data was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’. There are five different types of coupons -- less expensive restaurants (under $20$), coffee houses, carry out & take away, bar, and more expensive restaurants ($20$ - $50$).\n",
    "\n",
    "The attributes of this data set include:\n",
    "1. User attributes\n",
    "    -  Gender: male, female\n",
    "    -  Age: below 21, 21 to 25, 26 to 30, etc.\n",
    "    -  Marital Status: single, married partner, unmarried partner, or widowed\n",
    "    -  Number of children: 0, 1, or more than 1\n",
    "    -  Education: high school, bachelors degree, associates degree, or graduate degree\n",
    "    -  Occupation: architecture & engineering, business & financial, etc.\n",
    "    -  Annual income: less than \\\\$12500, \\\\$12500 - \\\\$24999, \\\\$25000 - \\\\$37499, etc.\n",
    "    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    -  Number of times that he/she buys takeaway food: 0, less than 1, 1 to 3, 4 to 8 or greater\n",
    "    than 8\n",
    "    -  Number of times that he/she goes to a coffee house: 0, less than 1, 1 to 3, 4 to 8 or\n",
    "    greater than 8\n",
    "    -  Number of times that he/she eats at a restaurant with average expense less than \\\\$20 per\n",
    "    person: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8\n",
    "    \n",
    "\n",
    "2. Contextual attributes\n",
    "    - Driving destination: home, work, or no urgent destination\n",
    "    - Location of user, coupon and destination: we provide a map to show the geographical\n",
    "    location of the user, destination, and the venue, and we mark the distance between each\n",
    "    two places with time of driving. The user can see whether the venue is in the same\n",
    "    direction as the destination.\n",
    "    - Weather: sunny, rainy, or snowy\n",
    "    - Temperature: 30F, 55F, or 80F\n",
    "    - Time: 10AM, 2PM, or 6PM\n",
    "    - Passenger: alone, partner, kid(s), or friend(s)\n",
    "\n",
    "\n",
    "3. Coupon attributes\n",
    "    - time before it expires: 2 hours or one day\n",
    "   \n",
    "Here is how the dataset looks like\\\n",
    "Total number of rows = 12684\\\n",
    "\n",
    "| No | Column.             |Non Null-Count    Type\n",
    "|:---|:--------------------|:---------------------|\n",
    "| 0   |destination          |12684 non-null  object|\n",
    "| 1   |passanger            |12684 non-null  object|\n",
    "| 2   |weather              |12684 non-null  object|\n",
    "| 3   |temperature          |12684 non-null  int64 |\n",
    "| 4   |time                 |12684 non-null  object|\n",
    "| 5   |coupon               |12684 non-null  object|\n",
    "| 6   |expiration           |12684 non-null  object|\n",
    "| 7   |gender               |12684 non-null  object|\n",
    "| 8   |age                  |12684 non-null  object|\n",
    "| 9   |maritalStatus        |12684 non-null  object|\n",
    "| 10  |has_children         |12684 non-null  int64 |\n",
    "| 11  |education            |12684 non-null  object|\n",
    "| 12  |occupation           |12684 non-null  object|\n",
    "| 13  |income               |12684 non-null  object|\n",
    "| 14  |car                  |108 non-null    object|\n",
    "| 15  |Bar                  |12577 non-null  object|\n",
    "| 16  |CoffeeHouse          |12467 non-null  object|\n",
    "| 17  |CarryAway            |12533 non-null  object|\n",
    "| 18  |RestaurantLessThan20 |12554 non-null  object|\n",
    "| 19  |Restaurant20To50     |12495 non-null  object|\n",
    "| 20  |toCoupon_GEQ5min     |12684 non-null  int64 |\n",
    "| 21  |toCoupon_GEQ15min    |12684 non-null  int64 |\n",
    "| 22  |toCoupon_GEQ25min    |12684 non-null  int64 |\n",
    "| 23  |direction_same       |12684 non-null  int64 |\n",
    "| 24  |direction_opp        |12684 non-null  int64 |\n",
    "| 25  |Y                    |12684 non-null  int64 |\n",
    "\n",
    "dtypes: float64(5), int64(11), object(9)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6b45cc9",
   "metadata": {},
   "source": [
    "#### 2.2 Early Data Exporation and Data Quality Check\n",
    "We need to check the quality of the data. For example, since many of the column/variable is categorical, we can check the summary of the data and see the number of customer of each categories. By doing this, we can also check whether there are any data that need to be cleansed or to be transformed. For example, we can check if there is a missing/empty values and duplicates. The below table lists the objects columns with their categorical data. \n",
    "\n",
    "\n",
    "| Column.             |Categorical Data\n",
    "|:--------------------|:---------------------|\n",
    "destination|                                 [No Urgent Place, Home, Work]\n",
    "|passanger  |                           [Alone, Friend(s), Kid(s), Partner]\n",
    "|weather    |                                         [Sunny, Rainy, Snowy]\n",
    "|time       |                                   [2PM, 10AM, 6PM, 7AM, 10PM]\n",
    "|coupon     |             [Restaurant(<20), Coffee House, Carry out & Ta...\n",
    "|expiration |                                                      [1d, 2h]\n",
    "|gender     |                                                [Female, Male]\n",
    "|age        |                     [21, 46, 26, 31, 41, 50plus, 36, below21]\n",
    "|maritalStatus|           [Unmarried partner, Single, Married partner, D...\n",
    "|education    |           [Some college - no degree, Bachelors degree, A...\n",
    "|occupation   |           [Unemployed, Architecture & Engineering, Stude...\n",
    "|income       |           [$37500 - $49999, $62500 - $74999, $12500 - $2...\n",
    "|car          |           [nan, Scooter and motorcycle, crossover, Mazda...\n",
    "|Bar          |                          [never, less1, 1-3, gt8, nan, 4-8]\n",
    "|CoffeeHouse  |                          [never, less1, 4-8, 1-3, gt8, nan]\n",
    "|CarryAway    |                          [nan, 4-8, 1-3, gt8, less1, never]\n",
    "|RestaurantLessThan20|                   [4-8, 1-3, less1, gt8, nan, never]\n",
    "|Restaurant20To50    |                   [1-3, less1, never, gt8, 4~8, nan]\n",
    "\n",
    "The first glance of the object columns and their categorical values, the following columns data will have to be trasformed and fixed:  Age, Occupation, Expiration, Income, Bar, CarryAway, RestaurantLessThan20 and Restaurant20To50.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84e186a4",
   "metadata": {},
   "source": [
    "### 3. Data Preparation\n",
    "On the Data Understanding phase, we will prepare and cleanse the data so they are fit for analysis and making prediction. The data preparation take 80% of the data mining process.\n",
    "\n",
    "The deliverable or result of this phase should include:\n",
    "\n",
    "Data preparation steps\\\n",
    "Final data for analysis and modeling (if desired)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "980aa451",
   "metadata": {},
   "source": [
    "#### 3.1 Data Cleansing\n",
    "On this process, we handle the data based on the problem we find during the data understanding phase. Based on our finding, the following process was executed:\n",
    "\n",
    "a) Fixed the age values and converted it to numeric\\\n",
    "b) Shortened the occupation column values\\\n",
    "c) converted the columns (Bar,CarryAway,CoffeeHouse,RestaurantLessThan20, Restaurant20To50) values and converting them to numeric'\\\n",
    "d) Converted the expiration column to numeric in hours\\\n",
    "e) Fixed the income column and converting the values to numeric (taking the average)\\\n",
    "f) Fixed the typo in passenger column name\\\n",
    "g) Treatment of the missing and duplicate data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "007e367c",
   "metadata": {},
   "source": [
    "All the missing values are from columns with type object/string.  the column cars is missing about 99% of the data, it was decided to drop it.  the other columns (Bar, CoffeeHouse, CarryAway, ResuarantLessThan20 and Restaurant20To50) are missing about 1% of their values, so dropping the missing rows should not impact the data analysis, hence were dropped.  The duplicates were dropped\n",
    "\n",
    "Finally, after careful and rigorous data cleansing, we acquire our final data that will be used for analysis and modeling.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4d8b445",
   "metadata": {},
   "source": [
    "#### 3.2 Final Data\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6f2ca5b",
   "metadata": {},
   "source": [
    "| No | Column.             |Non Null-Count    Type\n",
    "|:---|:--------------------|:---------------------|\n",
    "| 0   |destination          |12017 non-null  object|\n",
    "| 1   |passanger            |12017 non-null  object|\n",
    "| 2   |weather              |12017 non-null  object|\n",
    "| 3   |temperature          |12017 non-null  int64 |\n",
    "| 4   |time                 |12017 non-null  object|\n",
    "| 5   |coupon               |12017 non-null  object|\n",
    "| 6   |expiration           |12017 non-null  int64|\n",
    "| 7   |gender               |12017 non-null  object|\n",
    "| 8   |age                  |12017 non-null  int64|\n",
    "| 9   |maritalStatus        |12017 non-null  object|\n",
    "| 10  |has_children         |12017 non-null  int64 |\n",
    "| 11  |education            |12017 non-null  object|\n",
    "| 12  |occupation           |12017 non-null  object|\n",
    "| 13  |income               |12017 non-null  int64|\n",
    "| 15  |Bar                  |12017 non-null  object|\n",
    "| 16  |CoffeeHouse          |12017 non-null  object|\n",
    "| 17  |CarryAway            |12017 non-null  object|\n",
    "| 18  |RestaurantLessThan20 |12017 non-null  object|\n",
    "| 19  |Restaurant20To50     |12017 non-null  object|\n",
    "| 20  |toCoupon_GEQ5min     |12017 non-null  int64 |\n",
    "| 21  |toCoupon_GEQ15min    |12017 non-null  int64 |\n",
    "| 22  |toCoupon_GEQ25min    |12017 non-null  int64 |\n",
    "| 23  |direction_same       |12017 non-null  int64 |\n",
    "| 24  |direction_opp        |12017 non-null  int64 |\n",
    "| 25  |Y                    |12017 non-null  int64 |"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35d28cc2",
   "metadata": {},
   "source": [
    "### 4. Data Understanding through Analysis\n",
    "The CRISP-DM process nature is an itterative one. We can go back and forth between process to make sure it fits the business and data mining goals. Here, we go back to data understanding phase to further explore and analyze the data before the modeling phase (out of scope for this project).\n",
    "\n",
    "#### 4.1 Exploratory Data Analysis\n",
    "The process of exploring and visualizing insight from the data is called Exploratory Data Analysis (EDA).\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7f0d7a2",
   "metadata": {},
   "source": [
    "#### 4.1.1 Prior Observations\n",
    "The first step in the data analysis is to understand the data distribution, i.e., if it is biased.  The distribution of the passenger type data indicates that most are under the \"Alone\" category by a wide margin.  This effect is propegated throguh the distribution of coupons for both accepted and rejected as shown in the below diagrams.\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/PassengerDistributionHistogram.png)\n",
    "\n",
    "**Figure-1:** [Passenger Distribution Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/PassengerDistributionHistogram.png)\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponAcceptancePerPassengerType.png)\n",
    "\n",
    "**Figure-2:** [Coupon Acceptance per Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponAcceptancePerPassengerType.png)\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponRejectionPerPassengerType.png)\n",
    "\n",
    "**Figure-3:** [Coupon Rejection per Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/CouponRejectionPerPassengerType.png)\n",
    "\n",
    "The coupons bar diagram shows that the Coffee House coupon had the most observations/participants count and the Restaurant(20-50) coupon had the least number of observations/participants. \n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponTypesDistribution.png)\n",
    "\n",
    "**Figure-4:** [Coupon Distribution](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponTypesDistribution.png)\n",
    "\n",
    "Please note that this diagram does not show the percentage of acceptance/rejection of the coupon), instead it is shown in the below histogram which tells us the following about the coupon:\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAcceptanceRejectionHistogram.png)\n",
    "\n",
    "**Figure-5:** [Coupon Acceptance Rejection Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAcceptanceRejectionHistogram.png)\n",
    "\n",
    "1) Coffee house has the highest rejection rate of ( 16 %) and highest acceptance rate of ( 15.72 %).\n",
    "2) Restaurant(<20)/Cheap coupon is 2nd with acceptance rate of ( 15.64 %) and rejection rate of ( 6.4 %)\n",
    "3) Carry Out coupon was the 3rd with acceptance rate of ( 13.68 %) and has the least rejection rate of ( 4.92 %)\n",
    "4) Bar coupon comes in number 4 of acceptance rate of ( 6.54 %) and rejection rate of ( 9.31 %)\n",
    "5) Restaurant(20-50) is last with acceptance rate of ( 5.25 %) and rejection rate of ~( 6.50 %)\n",
    "\n",
    "The temperature histogram shows that the coupon was best accepted when the temperature was around 80F and least accepted when the temperature around 30F\n",
    "\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/temperatureHistogram.png)\n",
    "\n",
    "**Figure-6:** [Temperature Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/temperatureHistogram.png)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5be52e51",
   "metadata": {},
   "source": [
    "#### 4.1.2 Observations\n",
    "\n",
    "#### 4.1.2.1 Heatmap Anaylisis¶\n",
    "Since this is a classification use case, there is no significant correlation between the coupon acceptance/rejection represented by the Y column and the other features. It was noticed that there is a 100% negative correlation between the same direction and opossite direction of the shop destination. However, this does not impact the driver decision om whether to accept or reject the coupon.\n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponCorrHeatmap.png)\n",
    "\n",
    "**Figure-7:** [Coupon Correlation HeatMap](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponCorrHeatmap.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04e22fc3",
   "metadata": {},
   "source": [
    "#### 4.1.2.2 Drivers' Age Impact Analysis¶ \n",
    "From the catplot diagram, most of the drivers who accepted/rejected a coupon were between the age of 21 to 31, and it spikes again for the age greater than 50.  The Coffee House coupon was the most to be accepted/rejected.  The cheap restaurant < $20 was more likely to be selected after the Coffee house followed by the Carry out coupon. \n",
    "\n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejAge.png)\n",
    "\n",
    "**Figure-8:** [Temperature Histogram](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejAge.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1588978",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.3 Drivers' Marital Status Impact Analysis</h4>  \n",
    "<p style=\"color:black\"> The accepted diagram shows the single and married partner were the most to accept the Coffee House, cheap restaurant and Carry out coupons respectively.  The rejected diagram shows the same driver pattern as the accepted case to reject the Coffee House coupon with almost the same rate.  Also, it shows the married partner were rejecting the Bar coupon with a rate close to ($4.6$%)</p>\n",
    "                           \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejMaritalStatus.png)\n",
    "\n",
    "**Figure-9:** [Coupon Acceptance Rejection per Driver Marital Status](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejMaritalStatus.png)                        \n",
    "                                                                                                                                                  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9065a44",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.4 Drivers' with/out Chidren Impact Analysis</h4>  \n",
    "<p style=\"color:black\">The catplot diagram shows that close to ($10$%) of the drivers who don't have children were more likely to select the Coffee House and cheap restaurant coupons.  About ($8$%) of the same pattern were more likely to accept the Carry out coupon.  Also, about ($10$%) from the same pattern were more likely to reject the Coffee House coupon.\n",
    "    \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejHasChildren.png)\n",
    "\n",
    "**Figure-10:** [Coupon Acceptance Rejection per Driver's Family- Children](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejHasChildren.png)  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea770ab1",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.5 Drivers' income Impact Analysis</h4>  \n",
    "<p style=\"color:black\">From the diagram we can see that the drivers with average income between ($18K$)  and  ($56K$) and above ($100K$) were more likely to accept the cheap restaurant, Coffee House and Carry out coupons.  The drivers with the same pattern as the acceptance case were more likely to reject the Coffee House coupon. \n",
    "    \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejIncome.png)\n",
    "**Figure-11:** [Coupon Acceptance Rejection per Driver's Income](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejIncome.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52b2543f",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.6 Drivers' Occupation Impact Analysis</h4>  \n",
    "<p style=\"color:black\">The catplot/count percentage shows that the unemployed, students and drivers who work in the Computer and Math fields have the highest acceptance rate of a coupon with an average about ($7.3$%) \n",
    "    \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejOccupation.png)\n",
    "**Figure-12:** [Coupon Acceptance Rejection per Driver's Income](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejOccupation.png)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79331ef8",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.7 Drivers' Education Impact Analysis</h4>  \n",
    "<p style=\"color:black\"> The drivers with Bachelors and Some college degrees were more likely to accept the cheap restaurant, Coffee House and Carry out coupons respectively.  About the same percentage of the same drivers pattern were more likely to reject the Coffee House coupon.\n",
    "    \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejEducation.png)\n",
    "**Figure-13:** [Coupon Acceptance Rejection per Driver's Education](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejEducation.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7ef588b",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.8 Drivers' Gender Impact Analysis</h4>  \n",
    "<p style=\"color:black\">The catplot diagram shows that about ($7.5$%) of the male/female were more likely to accept the cheap restaurant, Coffee House and Carry out coupons.  About the same percent of both genders were more likely to reject the Coffee House coupon. \n",
    "    \n",
    " ![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGender.png)\n",
    "**Figure-14:** [Coupon Acceptance Rejection per Driver's Gender](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGender.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c229b91",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.9 Drivers' Gender and Passenger Impact Analysis</h4>  \n",
    "<p style=\"color:black\"> The male drivers without passengers (driving Alone) were more likely to accept a coupon with a rate = ($16$%).  The same pattern with a rate of about ($12.5$%) were more likely to reject a coupon.  The female drivers without passengers were almost equally likely to accept/reject a coupon with a rate about ($15$%)\n",
    "    \n",
    " \n",
    "![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGenderPassenger.png)\n",
    "**Figure-15:** [Coupon Acceptance Rejection per Driver's Gender and Passenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/couponAccptRejGenderPassenger.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3135bbc4",
   "metadata": {},
   "source": [
    "<h4 style=\"color:black\"> 4.1.2.10 Further Analysis Conclusion</h4>  \n",
    "<p style=\"color:black\"> The above analysis showed that there is no single feature pattern can impact the driver decision with high percentage.  The drivers' decisions were driven by collection of features.  Because the data is biased as shown in section 4.1.1 above, I think the joint/conditional probability seems the best approach to properly predict the drivers' decisions. Interestingly, I noticed that the Coffee House coupon has the most acceptance rate among all the coupon types so I decided to explore it further with conditional probabilities.\n",
    "The conditional probabilities plot shows that the drivers with Friend passenger has the highest probability to reject the Coffee House coupon. The driver traveling without passengers (Alone) has the highest probability to accept the Coffee House coupon.  \n",
    "    \n",
    " ![Thumbnail](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/pCoffeeHouseCouponAccptRejPassengerType.png)\n",
    "**Figure-16:** [Conditional Probability of Accepting the Coffee House Coupon per PAssenger Type](https://github.com/mabusamra1/MAS-MLAI/blob/main/images/pCoffeeHouseCouponAccptRejPassengerType.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d24ca314",
   "metadata": {},
   "source": [
    "### 5. Next Step and Future Work"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "522f980d",
   "metadata": {},
   "source": [
    "Conducting more deeper analysis of the other driver characteristics combinations to predict the impacting features.  Also, preparing the data further to be ready for machine learning modeling, and to select the best model suites the case study.   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
