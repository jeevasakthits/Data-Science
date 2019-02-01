# 'SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt'
# 'Total', 'Percent''Electrical'
# GrLivArea
# TotalBsmtSF
# HasBsmt
setwd("D:/ALL/data_science/dataset/home_rent_Regression")
train = read.csv("train.csv")

View(train)
library(dplyr)
library(MASS)


names(train)
#data = train %>% select(c())

str(train)

X_train = scale(train)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)