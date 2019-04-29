# Getting & Cleaning Data Course Project

This repo contains the files required for the _Getting & Cleaning Data_ Course Project.

## Task

There are five tasks that must be completed for the projects. The tasks are as follow:

-  __Q1:__ Merges the training and the test sets to create one data set.
-  __Q2:__ Extracts only the measurements on the mean and standard deviation for each measurement.
-  __Q3:__ Uses descriptive activity names to name the activities in the data set
-  __Q4:__ Appropriately labels the data set with descriptive variable names.
-  __Q5:__ From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.

## R-Script Explanation

The R-script heavily relies on the __tidyverse__ library. Tidyverse is a beautiful library that allow readers to quickly grasp and understand how the code works.  

Here are step-by-step explanation of the R-script for those who needs help understanding:
1.  Load the `feature_names` and the `activity_labels` via the `read_delim()` function.
2.  Load the training and test dataset.
3.  To make it easier for __Q2__, the column name for both training and test dataset are renamed. The columns are renamed using the `feature_names` from step 1.
4.  Complete Q1 by merging the dataset using `bind_rows()` function. This function works exactly as the base `r_bind()` function, but is a much better function when handling with errors. 
5.  Complete Q2 by selecting columns with `-mean` and `-std` via two core functions which are `select()` and `contains()`.
6.  Complete Q3 by using `mutate()` and `factor()`
7.  Q4 was automatically completed in step 3
8.  Complete Q5 by using `group_by()` and `summarise_all()`

Many of the functions used are from tidyverser library as it is so easy to use and understand. 
