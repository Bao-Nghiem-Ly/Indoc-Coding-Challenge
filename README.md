#Indoc-Coding-Challenge
My solution to the Indoc Research coding Challenge.

#Techinical Specifications
##Assumptions
* Program only has to deal with one specific input: csv file containing 50 sets of data for three different 
classes of iris plant
* All users using this program are running it on Linux 

##Design
I decided to go with a serial approach to parsing and processing the csv file given as input. Since I can 
assume the input file is very specific and only contains 150 lines, splitting up the file and then parsing 
the file using multiple processes is unnecessary and would actually take longer compared to the current method.

I decided to plot the average sepal and petal lengths of the three iris classes in a double bar graph to best
represent the differences between each class of iris plants. Plotting the data as a bar graph allows the data
to be represented in an easy to compare visual representation without correlating data sets that might not
be directly connected. Alternatively, the opposite approach can be taken with a scatter plot with x = average 
petal length and y = average sepal length would also work to show the relationship between increasing petal
length and the correlating sepal length.

#How to Run the Script
Setup:
* must have python3 installed
* place csv file in input folder

To run the script using the Linux terminal:
* Use the terminal and navigate to folder containing the script and the input file
    * Use the following command to navigate through the terminal: cd name 
* type into the terminal: python3 main.py

To run the script using an IDE:
* Press file in the top right and select open
* navigate to the folder containing the script and the input file
* select folder and press open
* Open main.py by double clicking it on the project menu to the left
* right click anywhere in the code and select run main.py