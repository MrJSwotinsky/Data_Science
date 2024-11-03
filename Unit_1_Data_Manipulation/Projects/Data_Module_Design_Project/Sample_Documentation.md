# Documentation for `js_plot`
Designed by Mr. Swotinsky<br>
Monday, November 4th 2024

## Description
`js_plot` is a module containing functions for generating data visualizations that can be used to compare data.

## Functions
### Function 1 Name:

`double_bar_graph(bar1_label, bar1_values, bar2_label, bar2_values, categories, title, barWidth)`<br>

### Function 1 Description:

`double_bar_graph()` accepts two sets of data of numerical data and generates a double bar graph.<br>

For example, `double_bar_graph()` can be used to convert Table 1 below to Bar Graph 1 below:<br>

**Table 1:**
||Average Q1 Sales|Average Q2 Sales|Average Q3 Sales|Average Q4 Sales|
|---|---|---|---|---|
|Company A|$25,000.00|$28,000.00|$19,000.00|$29,000.00|
|Company B|$7,000.00|$12,000.00|$18,000.00|$32,000.00|

**Bar Graph 1:**<br>
<img src="https://github.com/MrJSwotinsky/Data_Science/blob/main/Unit_1_Data_Manipulation/Projects/Data_Module_Design_Project/Quarterly_Sales.png">

### Function 1 Parameters:

`bar1_label` is accepted as a string and represents the label that applies to the first set of bars.<br>
In the example above, `bar1_label` = `'Company A'`<br><br>

`bar1_values` is accepted as a list and represents the list of values that correspond to the first set of bars.<br> 
In the example above, `bar1_values` = `[25000, 28000, 19000, 29000]`

`bar1_label` is accepted as a string and represents the label that applies to the second set of bars.<br>
In the example above, `bar2_label` = `'Company B'`<br><br>

`bar2_values` is accepted as a list and represents the list of values that correspond to the seco9nd set of bars.<br> 
In the example above, `bar2_values` = `[7000, 12000, 18000, 32000]`<br><br>

`categories` is accepted as a list of strings and represents the category labels for the double bar graph.<br>
In the example above, `categories` = `['Average Q1 Sales','Average Q2 Sales','Average Q3 Sales','Average Q4 Sales']`<br><br>

`title` is accepted as a string and represents the title for the double bar graph.<br>
In the example above, `title` = `'Quarterly Sales'`<br><br>

`barWidth` is accepted as a string and represents the width of each bar.<br>
In the example above, `barWdith` = 1<br><br>
