library(tidyverse)

# Load the feature names and the activity labels
feature_names <- read_delim('UCI HAR Dataset/features.txt', delim = ' ', col_names = FALSE)
activity_labels <- read_delim('UCI HAR Dataset/activity_labels.txt', delim = ' ', col_names = FALSE)

# ---------------------------------------------------------------------------
# Data Preparations
# ---------------------------------------------------------------------------

# Read the train dataset
subject_train <- read_csv('UCI HAR Dataset/train/subject_train.txt', col_names = "subject")
y_train <- read_csv('UCI HAR Dataset/train/y_train.txt', col_names = 'activity')
x_train <- read.table('UCI HAR Dataset/train/X_train.txt') %>% 
  as_tibble()

# Rename the column name of the x_train dataset
names(x_train) <- feature_names$X2

# Insert the subject_train and y_train information into the x_train dataset
x_train['subject'] <- subject_train$subject
x_train['activity'] <- y_train$activity

# Read the test dataset
subject_test <- read_csv('UCI HAR Dataset/test/subject_test.txt', col_names = "subject")
y_test <- read_csv('UCI HAR Dataset/test/y_test.txt', col_names = 'activity')
x_test <- read.table('UCI HAR Dataset/test/X_test.txt') %>% 
  as_tibble()

# Rename the column name of the x_train dataset
names(x_test) <- feature_names$X2

# Insert the subject_train and y_train information into the x_train dataset
x_test['subject'] <- subject_test$subject
x_test['activity'] <- y_test$activity


# ---------------------------------------------------------------------------
# Q1: Merge the training & the test sets to create one data set
# ---------------------------------------------------------------------------

# Merge via bind_rows
df <- x_train %>% 
  bind_rows(x_test)


# ---------------------------------------------------------------------------
# Q2: Extracts only the mean and standard deviation for each measurement
# ---------------------------------------------------------------------------

# This can be achieved by using dplyr's select function
df <- df %>% 
  select(subject, activity, contains('mean'), contains('std'))


# ---------------------------------------------------------------------------
# Q3: Uses descriptive activity names to name the activities in the data set
# ---------------------------------------------------------------------------

# This can be achieved by converting the column 'activity' into factor and
# rename it using the label
df <- df %>% 
  mutate(activity = factor(activity, levels = 1:6,labels = activity_labels$X2))


# ---------------------------------------------------------------------------
# Q4: Appropriately labels the data set with descriptive variable names
# ---------------------------------------------------------------------------

# This step has already been completed in line number 18 and 31


# ---------------------------------------------------------------------------
# Q5: Create a second, independent tidy data set with the average of each 
#     variable for each activity and each subject
# ---------------------------------------------------------------------------

df_tidy <- df %>% 
  group_by(subject, activity) %>% 
  summarise_all(mean) %>% 
  ungroup()

# Write the tidy_dataset into a text file
write_csv(df_tidy, 'tidy.txt')
