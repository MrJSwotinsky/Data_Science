# Documentation for `js_plot`
Designed by Mr. Swotinsky<br>
Monday, November 4th 2024

## Description
`js_plot` is a module containing functions for generating data visualizations that can be used to compare data.

## Functions
### Function 1 Name:

`double_bar_graph(bar1_label, bar1_values, bar2_label, bar2_values, categories, title, barWidth)`<br>

### Function 1 Description:

`double_bar_graph()` generates a double bar graph to represent two related sets of numerical data.<br>

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

`bar2_values` is accepted as a list and represents the list of values that correspond to the second set of bars.<br> 
In the example above, `bar2_values` = `[7000, 12000, 18000, 32000]`<br><br>

`categories` is accepted as a list of strings and represents the category labels for the double bar graph.<br>
In the example above, `categories` = `['Average Q1 Sales','Average Q2 Sales','Average Q3 Sales','Average Q4 Sales']`<br><br>

`title` is accepted as a string and represents the title for the double bar graph.<br>
In the example above, `title` = `'Quarterly Sales'`<br><br>

`barWidth` is accepted as a string and represents the width of each bar.<br>
In the example above, `barWdith` = 1<br><br>

### Function 2 Name:
`compare_to_mean_graphs(dataframe, index_column, records, columns)`

### Function 2 Description:

`compare_to_mean_graphs()` generates a set of double bar graphs to compare the values for one or more records in a dataframe to the mean values across all records in a dataframe.  For each record, a separate bar graph is generated.

For example, given the [Global Waste by Country 2019](https://docs.google.com/spreadsheets/d/1TOzs9GqIJIF9P6LVsGnt3Q6rueG43CYKQMoJrigJy-c/edit?gid=0#gid=0) data set available from [Bootstrap World](https://docs.google.com/spreadsheets/d/1TOzs9GqIJIF9P6LVsGnt3Q6rueG43CYKQMoJrigJy-c/edit?gid=0#gid=0), `compare_to_mean_graphs()` can be used to generate the double bar graphs below.<br><br>



The first bar graph highlights Canada's Municipal Solid Waste per Capita, Hazardous Waste per Capita, and Human Development Index compared to the mean values for Municipal Solid Waste per Capita, Hazardous Waste per Capita, and Human Development Index across all countries.

The second bar graph highlights the United State's Municipal Solid Waste per Capita, Hazardous Waste per Capita, and Human Development Index compared to the mean values for Municipal Solid Waste per Capita, Hazardous Waste per Capita, and Human Development Index across all countries.


[Sample Code In Action](https://github.com/MrJSwotinsky/Data_Science/blob/main/Unit_1_Data_Manipulation/Projects/Data_Module_Design_Project/Sample/Sample_Module_Design_Project_Functions_In_Action.ipynb)


