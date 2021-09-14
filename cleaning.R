library(tidyverse)

df <- read_csv('data.csv')

df <- tibble(
  price = rnorm(100, 10),
  a = rnorm(100, -5, 5),
  b = sample(c('A', 'B'), 100, replace = TRUE)
)

n_levels <- df
m %>%
  map(unique) %>%
  map_dbl(length) %>%
  sort

m <- df %>%
  select(which(n_levels > 1)) %>%
  select(-`$/SQFT`) %>%
  select(1:10) %>%
  lm(formula = price ~ .)
