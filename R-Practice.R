v <- c(9,6,4)
class(v)
b <- factor(v)
class(b)
color_vector <- c('blue', 'red', 'green', 'white', 'black', 'yellow')
factor_color <- factor(color_vector)
color_vector
factor_color
day_vector <- c('evening', 'morning', 'afternoon', 'midday', 'midnight', 'evening')
factor_day <- factor(day_vector, order = TRUE, levels =c('morning', 'midday', 'afternoon', 'evening', 'midnight'))
factor_day
summary(factor_day)
dataset <- mtcars
dataset
class(mpg)
class(dataset)
dataset <- mtcars
class(dataset)
a <-mtcars
class(a)
a
b <- c('book', 'pen', 'textbook', 'pencil_case')
c <- c(TRUE,FALSE,TRUE,FALSE)
d <- c(2.5, 8, 10,90)
df <- data.frame(a,b,c,d)
df
str(df)
