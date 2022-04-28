
# Installation

Simply install all requirements using `pip install -r requirements.txt`

# Usage

To analyze a csv file run `python main.py --path /path/to/your/data.csv`

# Assumptions

## Structure
The goal was to create a reusable and extensible tool. If the user wants to use it 
as a command line tool he can run the command above. If he would like to integrate
it with another project he can simply import DataClass class.

## Report
The 4 aspects which we report on have the following underlying assumptions:
### Uniformity
In a production setting you would want some sort of schema to validate against. 
As this is not given and in order to keep the tool simple and multipurpose some 
workarounds were made to "automatically" detect incorrect data types.
For each column the most frequent data type is taken, and all other types are reported
as issues by giving the line numbers (starting at 0).
For simplicity only 2 data types are assumed: numeric and string.
This can easily be extended for more datatypes but as mentioned the better approach 
would be to introduce a schema.

### Duplicate
Reports show a tuple of all lines duplicated. This was chosen that the user could decide 
which row he would like to keep.

### Missing Values
Report shows the row number which contains at least one missing values. This could be
extended to also show which column is missing a value for that row.

### Outliers
There are many approaches to doing this each with its own pros and cons. To keep the
scope of this tool as simple as possible, we define an outlier to be any value which 
is more than 3 standard deviations away from the mean for a particular column. This is 
only done for numeric values. Determining the outliers of string values is beyond the 
scope of this project.