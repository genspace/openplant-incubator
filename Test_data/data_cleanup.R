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
  select(time, temp, humidity, lux, fan, output) %>%
  gather(measure, value, -time, rm.na = TRUE) %>%
  arrange(time, measure)

#+ display-data
#' plot something
ggplot(data = working_data) +
  geom_line(aes(x = time, y = temp)) +
  geom_line(aes(x = time, y = output))
