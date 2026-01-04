#run this to generate the report for the analysis

require(knitr)
require(rmarkdown)

render(spin("data_cleanup.R", knit = FALSE))