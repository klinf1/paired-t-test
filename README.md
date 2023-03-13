# Student's paired T-test
This code can be used to do the following: 
- Student's paired t-test in order to determine whether that two related or repeated samples have identical average (expected) values.
For additional info, please read [this.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html). 
- Student's t-test for independent samples to determine whether they have identical average (expected) values. Additional information can be found [here.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
- This code uses Shapiro-Wilk test to check normality of sample data.

## Modules used
- scipy.stats
- pandas

## Usage
- Clone the code to your system
- Install requirements
- Move desired .xlsx file(s) to the directory where main.py is
- Execute main.py 
- Select the test required: for related or independent samples
- When asked to submit the file name do so without extension

## Results interpretation
If p-value is less than your chosen p-level (usually 0,05), then the null hypothesis of equal averages should be ***rejected***.
