# Unit 0, Assignment 05: <br> Lab 1 - Element Wise Operations
Due: Friday, September 13th 2024

In this lab, you will practice leveraging some of the basic features of NumPy with the data set you selected from Bootstrap World.  As you work, be sure to include appropriate comments in your code.

1.  Identify two columns in your dataset that would make sense to operate with each other.  For example, in the Global Waste dataset, it could make sense to operate columns F (Population), and L (Percent Urban) which would result in the number of people living in an urban setting.  However, it would make less sense to operate columns columns F (Population) and O (Obesity Rate by BMI) because there it might not result in a meaningful datapoint.  This does not mean that there is no meaningful relationship between columns F and O.  It just might not be the most appropriate pair of columns to operate for the purposes of this lab.<br>**Note:** In some datasets it is easier to find a pair of colums to operate with each other than in others.  For this lab, feel free to use any data set.
2.  Download the dataset you will be using for this lab.
3.  Create a new Jupyter Notebook file titled, `LastNameFirstInitial_Unit_0_Lab_1.ipynb` (Remember to use markdown to include an appropriate heading.)
4.  In markdown, identify...
     * What data set you have selected.
     * Which columns you have selected.
     * What each column represents.
     * How you will operate the columns (e.g. multiplying them together, dividing one by the other, something else, or possibly something a bit more complex.)
     * What the resulting values will represent.
5.  Import the pandas and numpy packages.
6.  Generate a dataframe from your dataset and assign it to an appropriately named variable.
7.  Generate two or more NumPy arrays (one for each column), and assign each to an appropriately named variable.
8.  Generate a new NumPy array by operating your columns together **(element-wise)** using the operation you described above and assign it to an appropriately named variable.
9.  In a new cell, in markdown, identify a condition you will test for (e.g. in the Global Waste data set example above, you could test for whether or not a country has 500,000 or more individuals living in an urban setting.
10.  Generate a boolean NumPy array to identify which  rows meet the condition you are testing for and assign it to an appropriately named variable.
11.  Generate a Numpy array containing only the specific values that meet the condition you tested for.
12.  Upload your work to a new folder titled `Labs` in your GitHub portfolio.

