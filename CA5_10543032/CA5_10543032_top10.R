

# Student Name:       Karina Jonina 
# Student ID:         10521012
# Github:             https://github.com/KarinaPS11/B8IT105
# Module:             B8IT105 
# Module Name:        Programming for Big Data (DBS)

# Assignment 5        10% - R Data Interpretation

if (!require('MASS')) install.packages('MASS') #click Run
if (!require('aod')) install.packages('aod') #click Run
if (!require('car')) install.packages('car') #click Run
if (!require('dplyr')) install.packages('dplyr') #click Run
if (!require('ggplot2')) install.packages('ggplot2') #click Run
if (!require('rpart')) install.packages('rpart') #click Run
if (!require('rpart.plot')) install.packages('rpart.plot')

library(MASS) #click Run
library(dplyr)
library(ggplot2)
library(aod)
library(car)
library(rpart)
library(rpart.plot)

data_top10 <- read_csv('data_top10.csv')


# check the dataframe
class(data_top10)

# examining all the dataframe
head(data_top10)
summary(data_top10)

# unique values
unique_vals <- lapply(data_top10, unique)
print(unique_vals)

#Keep all the categorical variables as Factors
data_top10[sapply(data_top10, is.character)] <-
  lapply(data_top10[sapply(data_top10, is.character)], as.factor)

#convert the 0 and 1 in is_Cancelled to categorical variable
data_top10$is_canceled <-factor(data_top10$is_canceled)

# Organize the Month in proper order
data_top10$arrival_date_month <-
  factor(data_top10$arrival_date_month, levels = month.name)

str(data_top10)
summary(data_top10)


# =============================================================================
# number of reservations for each of the hotels
# =============================================================================

# Check the number of reservations for each of the hotels
table(data_top10$hotel)


# a graph for Booking Reservations for Both hotels
ggplot(data = data_top10, aes(x = hotel, fill = hotel)) +
  geom_bar(stat = 'count') +
  labs(title = 'Number of Reservations by Hotel type',
       x = 'Hotel type',
       y = 'Number of Reservation')+
  scale_fill_manual(values=c('#E69F00', '#56B4E9'))


# =============================================================================
# Reservation status for each of the hotels
# =============================================================================


table(data_top10$is_canceled, data_top10$hotel)


ggplot(data = data_top10, aes(x = country, fill = factor(is_canceled)), ) +
  geom_bar(stat='count', position='dodge') +
  labs(title = 'Booking Reservations by Country',
       x = 'Hotel Type') +
  scale_fill_discrete(
    name = 'Reservation Status',
    breaks = c('0', '1'),
    labels = c('Not Cancelled', 'Cancelled')) +
  theme_light()

#running Chi-square to examine the relationship between hotel and cancelations
tbl = table(data_top10$hotel, data_top10$is_canceled) 
chis.test(tbl)
summary(tbl)
# showing the tableq
tbl


# =============================================================================
# Examining Total number of guests for Both hotels
# =============================================================================

# a graph for Total number of guests for Both hotels
ggplot(data = data_top10, aes(x = total_guests, fill = total_guests)) +
  geom_bar(stat = 'count') +
  labs(title = 'Number of Guests per Reservation',
       x = 'Most Common Number of Guests',
       y = 'Count')+
  xlim(0,20)



# =============================================================================
# Total number of guests for Both hotels
# =============================================================================

# a graph for Total number of guests for Both hotels
ggplot(data = data_top10, aes(x = total_nights, fill = total_nights)) +
  geom_bar(stat = 'count') +
  labs(title = 'Number of Nights per Reservation',
       x = 'Number of Nights',
       y = 'Number of Reservation') +
  xlim(0,20)



# =============================================================================
#  reservation status for each year
# =============================================================================

# checking the data from the number of years.
unique(data_top10$arrival_date_year)
#2015, 2016, 2017

# table of the reservation status for each year
table(data_top10$arrival_date_year, data_top10$is_canceled)
#         0     1
#2015 11973  8086
#2016 29813 17838
#2017 19857 13233
#2016 had the most cancelations

ggplot(data = data_top10, aes(x = arrival_date_year, fill = factor(is_canceled))) +
  geom_bar(stat = 'count') +
  labs(title = 'Booking Reservations by Year',
       x = ' Year',
       y = 'Number of Reservation') +
  scale_fill_discrete(
    name = 'Reservation Status',
    breaks = c('0', '1'),
    labels = c('Not Cancelled', 'Cancelled'))


#running Chi-square to examine the relationship between hotel and cancelations
tbl = table(data_top10$arrival_date_year, data_top10$is_canceled) 
chis.test(tbl)
summary(tbl)
# showing the tableq
tbl



# =============================================================================
# reservation status for each month
# =============================================================================

# table of the reservation status for each month
table(data_top10$arrival_date_month, data_top10$is_canceled)

#graph of reservation status for each month
monthplot <- ggplot(data = data_top10, aes(x = arrival_date_month, fill = factor(is_canceled))) +
  geom_bar(stat = 'count') +
  labs(title = 'Booking Reservations by month',
       x = 'Month of the Year',
       y = 'Number of Reservation') +
  scale_fill_discrete(
    name = 'Reservation Status',
    breaks = c('0', '1'),
    labels = c('NotCancelled', 'Cancelled'))

#rotates the months on the x-axis to allow the months be more legible 
monthplot  + theme(axis.text.x = element_text(angle = 90))


# =============================================================================
# reservation status for each month and hotel
# =============================================================================

# table of the reservation status for each month and hotel
table(data_top10$arrival_date_month, data_top10$hotel)

monthplot1 <- ggplot(data = data_top10, aes(arrival_date_month, fill = hotel)) +
  geom_bar(position = position_dodge()) +
  labs(title = 'Booking Status by Month',
       x = 'Month',
       y = 'Count') + theme_bw() +
  scale_fill_manual(values=c('#E69F00', '#56B4E9'))

#rotates the months on the x-axis to allow the months be more legible 
monthplot1  + theme(axis.text.x = element_text(angle = 90))


# =============================================================================
# reservation status for each year and hotel
# =============================================================================

# table of the reservation status for each year and hotel
table(data_top10$arrival_date_year, data_top10$hotel)

yearplot1 <- ggplot(data = data_top10, aes(arrival_date_year, fill = hotel)) +
  geom_bar(position = position_dodge()) +
  labs(title = 'Booking Status by Month',
       x = 'Month',
       y = 'Count') + theme_bw()

#rotates the months on the x-axis to allow the months be more legible 
yearplot1  + theme(axis.text.x = element_text(angle = 90))


#splitting the data - all the check outs 
checkout_data_top10 <- data_top10[data_top10$reservation_status == 'Check-Out',]

#splitting the data - all the cancellations
cancel_data_top10 <- data_top10[data_top10$reservation_status == 'Canceled',]



# =============================================================================
# Daily Rate Per Person for each Hotel
# =============================================================================

#Average Daily Rate Per Person for each Hotel
ggplot(data = data_top10, aes(
  x = hotel,
  y = adr,
  fill = factor(is_canceled)
)) +
  geom_boxplot(position = position_dodge()) +
  labs(
    title = 'Cancellation By Hotel Type',
    subtitle = 'Based on Average Daily Rate',
    x = 'Hotel Type',
    y = 'Average Daily Rate Per Person'
  ) +
  ylim(0,400) +
  
  scale_fill_discrete(
    name = 'Booking Status',
    breaks = c('0', '1'),
    labels = c('Not Cancelled', 'Cancelled')
  ) + theme_light()

#Unbalanced data (And significantly - see above)
table(data_top10$hotel, data_top10$is_canceled)

#examining the relationship between hotel and cancelations on ADR
res.aov2 <- aov(adr ~ hotel * is_canceled, data = data_top10)
summary(res.aov2)

# Homogeneity of variances
plot(res.aov2, 1)
#violates ANOVA assumption of homogeneity

leveneTest(adr ~ hotel*is_canceled, data = data_top10)
#violates ANOVA assumption of homogeneity

plot(res.aov2, 2)

#shows the summary of Mean and Sd
group_by(data_top10, hotel, is_canceled) %>%
  summarise(
    count = n(),
    mean = mean(adr, na.rm = TRUE),
    sd = sd(adr, na.rm = TRUE))


# =============================================================================
#  Daily Rate Per Person for every Year
# =============================================================================

#Average Daily Rate Per Person for every Year
ggplot(data = data_top10, aes(
  x = hotel,
  y = adr,
  fill = factor(arrival_date_year)
)) +
  geom_boxplot(position = position_dodge()) +
  labs(
    title = 'Average Daily Rate By Hotel Type in Each year',
    subtitle = 'Based on Average Daily Rate',
    x = 'Hotel Type',
    y = 'Average Daily Rate Per Person'
  ) +
  ylim(0,400)+
  scale_fill_discrete(
    name = 'Year') + theme_light()



#Unbalanced data (And significantly - see above)
table(data_top10$hotel, data_top10$arrival_date_year)

#examining the relationship between hotel and cancelations on ADR
res.aov2 <- aov(adr ~ hotel * arrival_date_year, data = data_top10)
summary(res.aov2)

# Homogeneity of variances
plot(res.aov2, 1)
#violates ANOVA assumption of homogeneity

leveneTest(adr ~ hotel*arrival_date_year, data = data_top10)
#violates ANOVA assumption of homogeneity

plot(res.aov2, 2)

#shows the summary of Mean and Sd
group_by(data_top10, hotel, arrival_date_year) %>%
  summarise(
    count = n(),
    mean = mean(adr, na.rm = TRUE),
    sd = sd(adr, na.rm = TRUE))



# =============================================================================
# Daily Rate Per Person for every Month
# =============================================================================


#Average Daily Rate Per Person for every Month
ggplot(data = data_top10, aes(
  x = arrival_date_month,
  y = adr,
  fill = factor(arrival_date_month)
)) +
  geom_boxplot(position = position_dodge()) +
  labs(
    title = 'Average Daily Rate By  Each Monh',
    subtitle = 'Based on Average Daily Rate',
    x = 'Month of the Year',
    y = 'Average Daily Rate Per Person'
  ) +
  ylim(0,400)+
  scale_fill_discrete(
    name = 'Year') + theme_light()

#examining the relationship between hotel and cancelations on ADR
res.aov2 <- aov(adr ~ arrival_date_month, data = data_top10)
summary(res.aov2)

#Homogeneity of variances
plot(res.aov2, 1)
#violates ANOVA assumption of homogeneity

leveneTest(adr ~ arrival_date_month, data = data_top10)
#violates ANOVA assumption of homogeneity

plot(res.aov2, 2)
#violates ANOVA assumption of homogeneity

TukeyHSD(res.aov2, which = 'arrival_date_month')

#shows the summary of Mean and Sd
group_by(data_top10, arrival_date_month) %>%
  summarise(
    count = n(),
    mean = mean(adr, na.rm = TRUE),
    sd = sd(adr, na.rm = TRUE))



# =============================================================================
# Daily Rate Per Person for every Month
# =============================================================================

#Average Daily Rate Per Person for every Month
ggplot(data = data_top10, aes(
  x = hotel,
  y = adr_pp,
  fill = factor(arrival_date_month)
)) +
  geom_boxplot(position = position_dodge()) +
  labs(
    title = 'Average Daily Rate By  Each Monh',
    subtitle = 'Based on Average Daily Rate',
    x = 'Month of the Year',
    y = 'Average Daily Rate Per Person'
  ) +
  ylim(0,400)+
  scale_fill_discrete(
    name = 'Year') + theme_light()

#examining the relationship between hotel and cancelations on ADR
res.aov2 <- aov(adr ~ arrival_date_month * hotel, data = data_top10)
summary(res.aov2)

#Homogeneity of variances
plot(res.aov2, 1)
#violates ANOVA assumption of homogeneity

leveneTest(adr ~ arrival_date_month, data = data_top10)
#violates ANOVA assumption of homogeneity

plot(res.aov2, 2)
#violates ANOVA assumption of homogeneity

TukeyHSD(res.aov2, which = 'arrival_date_month')

#shows the summary of Mean and Sd
group_by(data_top10,hotel, arrival_date_month) %>%
  summarise(
    count = n(),
    mean = mean(adr, na.rm = TRUE),
    sd = sd(adr, na.rm = TRUE))#


# =============================================================================
# examine the relationship between hotel and country
# =============================================================================
ggplot(data = data_top10, aes(x = country, fill = factor(is_canceled))) +
  geom_bar(stat='count', position='dodge') +
  labs(title = 'Booking Reservations by Country',
       x = 'Hotel Type') +
  scale_fill_discrete(
    name = 'Reservation Status',
    breaks = c('0', '1'),
    labels = c('Not Cancelled', 'Cancelled')) +
  theme_light()


#running Chi-square to examine the relationship between hotel and country
tbl1 = table(data_top10$country, data_top10$is_canceled) 
chis.test(tbl1)
summary(tbl1)
# showing the tableq
tbl1


# =============================================================================
# Logistic Regression
# =============================================================================


# set a random seed 
set.seed(1)   

# random selection of indices. 
index <- sample(nrow(data_top10), nrow(data_top10)*0.3) 

# save 30% as a test dataset
test <- data_top10[index,]

# save the rest as a training set
training <-data_top10[-index,] 

#my
mytraining_varibles <- training[c('hotel','is_canceled','lead_time','total_guests','meal',
                                  'arrival_date_month','arrival_date_year','total_nights',
                                  'previous_cancellations','country', 'days_in_waiting_list',
                                  'adr','data_boolean')]
#creates a model
log_model <- glm(is_canceled ~., family = "binomial", data = mytraining_varibles)

#gives a summary of the regression model
summary(log_model)


## CIs using profiled log-likelihood
confint(log_model)


## CIs using standard errors
confint.default(log_model)


with(log_model, pchisq(null.deviance - deviance, df.null - df.residual, lower.tail = FALSE))

test$logit_pred_prob <- predict(log_model, test, type = "response")
test$logit_pred_class <- ifelse(test$logit_pred_prob > 0.5, "1", "0") 

table(test$is_canceled == test$logit_pred_class)
# FALSE  TRUE 
# 6995 23244 

table(test$logit_pred_class,test$is_canceled, dnn=c("predicted","actual"))
#           actual
# predicted     0     1
#         0 17667  5572
#         1   808  6192

(15877 + 7367)/nrow(test)
# 0.7686508  -  76% prediction accuracy






