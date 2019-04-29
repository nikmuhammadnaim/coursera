# CodeBook

This code book describes the `tidy.txt` dataset

## Origin

This dataset was derived from the original UCI Human Activity Recognition using Smartphone Data Set. The derivation steps can be obtained from the `run_analysis.R` script

## Format

-  Delimiter: Comma-seperated
-  Number of rows: 180
-  Number of columns: 81

## Variables

### Identifiers & Labels

-  `subject`: 
    -  Identifies the person who performed the activity
    -  Range from 1 to 30. 
-  `activity`:
    -  Label name for each activity performed
    -  There are 6 unique activities: `WALKING`, `WALKING_UPSTAIRS`, `WALKING_DOWNSTAIRS`, `SITTING`, `STANDING` & `LAYING`
    
 ### Measurements
 
 These 79 variables contains the mean of each subject and each activity. All of them are normalized and bounded within [-1,1].    
 
 The acceleration signal from the smartphone accelerometer X axis in standard gravity units 'g'.  
 
 The angular velocity vector measured by the gyroscope for each window sample. The units are radians/second.  
 
 The full list of the 79 variables are:
 -  `tBodyAcc-mean()-X`
 -  `tBodyAcc-mean()-Y`
 -  `tBodyAcc-mean()-Z`
 -  `tGravityAcc-mean()-X`
 -  `tGravityAcc-mean()-Y`
 -  `tGravityAcc-mean()-Z`
 -  `tBodyAccJerk-mean()-X`
 -  `tBodyAccJerk-mean()-Y`
 -  `tBodyAccJerk-mean()-Z`
 -  `tBodyGyro-mean()-X`
 -  `tBodyGyro-mean()-Y`
 -  `tBodyGyro-mean()-Z`
 -  `tBodyGyroJerk-mean()-X`
 -  `tBodyGyroJerk-mean()-Y`
 -  `tBodyGyroJerk-mean()-Z`
 -  `tBodyAccMag-mean()`
 -  `tGravityAccMag-mean()`
 -  `tBodyAccJerkMag-mean()`
 -  `tBodyGyroMag-mean()`
 -  `tBodyGyroJerkMag-mean()`
 -  `fBodyAcc-mean()-X`
 -  `fBodyAcc-mean()-Y`
 -  `fBodyAcc-mean()-Z`
 -  `fBodyAcc-meanFreq()-X`
 -  `fBodyAcc-meanFreq()-Y`
 -  `fBodyAcc-meanFreq()-Z`
 -  `fBodyAccJerk-mean()-X`
 -  `fBodyAccJerk-mean()-Y`
 -  `fBodyAccJerk-mean()-Z`
 -  `fBodyAccJerk-meanFreq()-X`
 -  `fBodyAccJerk-meanFreq()-Y`
 -  `fBodyAccJerk-meanFreq()-Z`
 -  `fBodyGyro-mean()-X`
 -  `fBodyGyro-mean()-Y`
 -  `fBodyGyro-mean()-Z`
 -  `fBodyGyro-meanFreq()-X`
 -  `fBodyGyro-meanFreq()-Y`
 -  `fBodyGyro-meanFreq()-Z`
 -  `fBodyAccMag-mean()`
 -  `fBodyAccMag-meanFreq()`
 -  `fBodyBodyAccJerkMag-mean()`
 -  `fBodyBodyAccJerkMag-meanFreq()`
 -  `fBodyBodyGyroMag-mean()`
 -  `fBodyBodyGyroMag-meanFreq()`
 -  `fBodyBodyGyroJerkMag-mean()`
 -  `fBodyBodyGyroJerkMag-meanFreq()`
 -  `tBodyAcc-std()-X`
 -  `tBodyAcc-std()-Y`
 -  `tBodyAcc-std()-Z`
 -  `tGravityAcc-std()-X`
 -  `tGravityAcc-std()-Y`
 -  `tGravityAcc-std()-Z`
 -  `tBodyAccJerk-std()-X`
 -  `tBodyAccJerk-std()-Y`
 -  `tBodyAccJerk-std()-Z`
 -  `tBodyGyro-std()-X`
 -  `tBodyGyro-std()-Y`
 -  `tBodyGyro-std()-Z`
 -  `tBodyGyroJerk-std()-X`
 -  `tBodyGyroJerk-std()-Y`
 -  `tBodyGyroJerk-std()-Z`
 -  `tBodyAccMag-std()`
 -  `tGravityAccMag-std()`
 -  `tBodyAccJerkMag-std()`
 -  `tBodyGyroMag-std()`
 -  `tBodyGyroJerkMag-std()`
 -  `fBodyAcc-std()-X`
 -  `fBodyAcc-std()-Y`
 -  `fBodyAcc-std()-Z`
 -  `fBodyAccJerk-std()-X`
 -  `fBodyAccJerk-std()-Y`
 -  `fBodyAccJerk-std()-Z`
 -  `fBodyGyro-std()-X`
 -  `fBodyGyro-std()-Y`
 -  `fBodyGyro-std()-Z`
 -  `fBodyAccMag-std()`
 -  `fBodyBodyAccJerkMag-std()`
 -  `fBodyBodyGyroMag-std()`
 -  `fBodyBodyGyroJerkMag-std()` 
