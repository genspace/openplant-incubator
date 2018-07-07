library(readr)
library(dplyr)
library(stringr)
library(ggplot2)

labels <- c("time", "temp", "humidity", "lux", "input", "fan", "output")

raw_data1 <- read_csv('180703.LOG', col_names = labels)
raw_data2 <- read_csv('180704.LOG', col_names = labels)
raw_data3 <- read_csv('180705.LOG', col_names = labels)
raw_data4 <- read_csv('180706.LOG', col_names = labels)
raw_data5 <- read_csv('180707.LOG', col_names = labels)

working_data <- rbind(raw_data1, raw_data2, raw_data3, raw_data4, raw_data5) %>%
  transform(time = as.POSIXct(strptime(time, "%Y%m%d_%H:%M:%S")))

ggplot(data = working_data) +
  geom_line(aes(x = time, y = temp)) +
  geom_line(aes(x = time, y = output))
