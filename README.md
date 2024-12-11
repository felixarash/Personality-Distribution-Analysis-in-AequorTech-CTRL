# Personality-Distribution-Analysis-in-AequorTech-CTRL
This project analyses the distribution of personality types among employees in AequorTech CTRL using Python. It utilizes a dataset of 350 employees, each assigned a random role and personality type. The primary goal is to provide an understanding of the overall distribution of personality types in the company and offer functions for retrieving personality information based on employee names or IDs
.
By: Fozan Ahmed
.
![personality_distribution](https://github.com/user-attachments/assets/602874f2-9f98-41f2-858f-2646777f5993)

Steps Involved:
1. Generating Sample Data:
The project begins by generating a synthetic dataset using random data to simulate the employee database. The following attributes are included in the dataset:
•	Employee ID: A unique ID for each employee (ranging from 1 to 350).
•	Name: The name of each employee, labelled as "Employee_1" through "Employee_350."
•	Role: The role of the employee, which is selected randomly from a predefined list of roles: Programmer, Engineer, Worker, Manager, Designer, Analyst, Technician, HR, Consultant.
•	Personality Type: The personality type of each employee, chosen randomly from a list of 16 personality types based on the Myers-Briggs Type Indicator (MBTI), such as INFP, ENFP, ISTP, etc.
The generated data is stored in a pandas DataFrame, making it easy to analyse and manipulate.
2. Analysing Personality Distribution:
The next step involves analyzing the distribution of personality types within the company. The value_counts() function is used to count the occurrences of each personality type. These counts are then converted to percentages to determine the relative proportion of each personality type in the dataset. This analysis is summarized in a DataFrame (summary_df), which includes the following columns:
•	Personality Type: The unique personality types found in the dataset.
•	Count: The number of employees assigned to each personality type.
•	Percentage: The percentage of employees with each personality type, calculated as (count / total number of employees) * 100.
3. Visualizing the Distribution:
To make the distribution analysis more accessible, a bar plot is generated using the Seaborn and Matplotlib libraries. The plot visualizes the percentage distribution of personality types in AequorTech CTRL. The following customizations are made:
•	A grid background for better readability.
•	The x-axis displays the different personality types.
•	The y-axis represents the percentage of employees in each personality type.
•	The chart is saved as a PNG file (personality_distribution.png) and also displayed on the screen.
4. Adding Lookup Functions:
To further enhance the functionality of the project, two lookup functions are added:
•	find_personality_by_name(name): This function allows the user to input an employee's name (e.g., "Employee_1") and retrieve their personality type.
•	find_personality_by_id(emp_id): This function takes an employee's ID (e.g., 1) and returns their personality type.
Both functions search the DataFrame for the corresponding employee and print their personality type. If the employee is not found, a message is displayed indicating that the employee does not exist in the dataset.
________________________________________
Example Usage:
1.	Looking up by Name:
o	To find the personality type of "Employee_1," the following code is used:
find_personality_by_("Employee_1")
Output:
Employee_1's Personality Type: INFP
2.	Looking up by ID:
o	To find the personality type of the employee with ID 1:
find_personality_by_id(1)
Output:
Employee ID 1's Personality Type: INFP

________________________________________
Conclusion:
This project provides a comprehensive analysis of the personality distribution within AequorTech CTRL. By utilizing random data generation, personality analysis, and visualization, it offers valuable insights into the company's employee dynamics. Additionally, the inclusion of lookup functions allows for easy access to individual employee personality information. This project can be expanded further to integrate real employee data and perform more advanced analyses.
________________________________________
Tools and Libraries Used:
•	pandas: For data manipulation and storage.
•	matplotlib: For creating visualizations.
•	seaborn: For creating aesthetically pleasing plots.
•	random: For generating random data.

________________________________________
Future Improvements:
•	Real Data Integration: Instead of using synthetic data, real employee data could be incorporated into the analysis for more accurate insights.
•	Interactive Dashboards: Implementing a web-based interactive dashboard using tools like Dash or Streamlit to allow users to query the dataset and visualize the results in real time.
•	Employee Role Analysis: Expanding the analysis to explore how personality types correlate with specific employee roles in the organization.
________________________________________
By:
Fozan Ahmed Memon
Data Analyst and Python Enthusiast
