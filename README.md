# Student's paired T-test
This code can be used to do student's paired t-test in order to determine whether that two related or repeated samples have identical average (expected) values.
For additional info, please read [this.](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html). This code uses Shapiro-Wilk test to check normality of sample data and returns value error if the data distribution is not normal in either sample.

## Modules used
- scipy.stats
- pandas

## Usage
- Clone the code to your system
- Install requirements
- Move desired .xlsx file(s) to the directory where main.py is
- Execute main.py 
- When asked to submit the file name do so without extension

## Results interpretation
If p-value is less than your chosen p-level (usually 0,05), then the null hypothesis of equal averages should be ***rejected***.
