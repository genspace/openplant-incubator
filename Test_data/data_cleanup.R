#' ---
#' title: "Analyzing the performance of the OpenPlant incubator at Genspace"
#'output:
#'  html_document:
#'    toc: true
#'    theme: united
#' ---

#/*making a note book with knitr.spin is preferable because of the dynamic possible code debugging*/
#/* YAML header, #' for drop into Rmarkdown (#, ## headers), #+ for chunks (try not to disrupt code chunks with comments, place before)*/

#/*set global knitr options*/
#+ knitr-options, message=FALSE, echo=FALSE
knitr::opts_chunk$set(warning = FALSE, tidy = FALSE)

#+ import-libraries, message=FALSE
require(readr)
require(dplyr)
require(tidyr)
require(stringr)
require(ggplot2)
require(zoo)

#+ session-info
sessionInfo() #for reproducibility

#' #Read in data and preprocess
#'
#+ import-process-data
#'declare the labels for the columns
labels <- c("time", "temp", "humidity", "lux", "input", "fan", "output")

#' list the files which will be read into the data table
files <- c("180703.LOG", "180704.LOG", "180705.LOG", "180706.LOG","180707.LOG")

#' prep the data table
working_data <- lapply(files, read_csv, col_names = labels) %>%
  bind_rows() %>%
  transform(time = as.POSIXct(strptime(time, "%Y%m%d_%H:%M:%S"))) %>%
  select(-input, -fan) %>%
  gather(measure, value, -time) %>%
  arrange(time, measure)

#+ display-data
#' plot the measures
ggplot(data = working_data, aes(x = time, y = value)) +
  scale_color_brewer(palette = "Set1") +
  geom_line(aes(alpha = 0.5)) +
  #geom_line(aes(y = rollmean(value, 30, fill = NA), colour = measure)) +
  facet_grid(measure ~ ., scales = "free_y")