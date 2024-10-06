# Unit 1, Assignment 1: <br> Lab 1 - Dictionaries and DataFrames
Due: Tuesday, October 8th 2024

## Part 1 - Datacamp

**Complete the following on Datacamp:**<br><br>
Course 2 (Intermediate Python) > Chapter 2 (Dictionaries and Pandas) > 
* Dictionaries Part 1 + Exercises
* Dictionaries Part 2 + Exercises
* Pandas Part 1 + Exercises

## Part 2 - Lab

In this lab, you will practice manually generating a DataFrame from a Dictionary.  You will aslo learn how to re-label row indices using more intuitive labels.

1.  Create a new Jupyter Notebook file in your Physical Device > Data Science Portfolio > Labs folder titled `LastNameFirstInitial_Unit_1_Lab_1.ipynb`
2.  Select 4 rows and 4 columns from the dataset you selected from Bootstrap World.  You will be using these rows and columns to manually generate a small DataFrame containing a subset of the data in your dataset.
3.  Before you begin, respond to the following prompts in a markdown cell.

You will be creating a dictionary that takes the form:

```python
example_dictionary = {
  'key_1' : ['value_1', 'value_2', 'value_3'],
  'key_2' : ['value_1', 'value_2', 'value_3'],
  'key_2' : ['value_1', 'value_2', 'value_3'],
}
```

*  In general, what do each of the keys represent?
*  In relation to your specific data, what do each of the keys represent?
*  In general what do each of the values represent?<br>**Hint:** `'value_1'`, `'value_2'`, and `'value_3'` are not the values.  The lists containing `'value_1'`,`'value_2'`, and `'value_3'` are the values.
*  In relation to your specific data, what do each of the values represent?<br>**Remember:** `'value_1'`, `'value_2'`, and `'value_3'` are not the values.  The lists containing `'value_1'`,`'value_2'`, and `'value_3'` are the values.
   
4.  Import the numpy and pandas packages.
5.  Create a dictionary to represent the 4 rows and 4 columns you selected and assign it to an appropriately named variable.
6.  Create a DataFrame from the dictionary you just created and assign it to an appropriately named variable.
7.  Change the row indices of your DataFrame to labels consisting of two or three characters thar are more intuitive.  For example, if your rows represent states, the labels, `'NY'`, `'NJ'`, `'CT'`, etc. are more intuitive than the indices, `01`, `01`, `03`, etc.
8.  Display your DataFrame.

After you have completed this lab, upload your work to your GitHub > Data Science Portfolio > Labs folder.  **Remember to include an appropriate heading, appropriate comments, and commit message.**
