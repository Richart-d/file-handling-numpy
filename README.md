# 📊 Loan Data Analysis Using File Handling and NumPy

A beginner-friendly project demonstrating how to perform file input/output operations using Python and analyze real-world data using NumPy.

This was created as part of a Data Science assignment to develop practical skills in reading CSV files, managing resources with the `open()` function, and calculating descriptive statistics.

---

## 📌 Project Overview

The project works with a CSV file that contains **loan records**, including:

- Loan ID
- Customer Gender
- Location
- Region
- Total Loan Amount

The goal is to:

- Use Python's built-in `open()` function to access raw data from the file
- Use `numpy.genfromtxt()` to load the CSV into an array
- Perform basic statistical analysis using NumPy:
  - **Mean**
  - **Median**
  - **Standard Deviation**

---

## 🧠 Learning Objectives

- Master Python’s `open()` and `close()` for file operations
- Learn to load CSV data using NumPy
- Apply `mean()`, `median()`, and `std()` functions on numerical data
- Understand the importance of resource management in data workflows

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- CSV file format

---


## ⚙️ How to Run the Project

1. **Clone the repo**

```bash
git clone https://github.com/Richart-d/file-handling-numpy.git
cd loan-data-numpy-file-handling
```


## ✅ Key Features
- Cleanly opens and closes the CSV file using with open()

- Reads only relevant numeric columns (loan amounts)

- Handles comma-separated values with proper delimiter

- Prints descriptive stats directly to the terminal


## 📌 Future Improvements
- Add data cleaning logic for missing or non-numeric entries

- Visualize distribution with Matplotlib or Seaborn

- Support analysis by region or gender using grouped operations


## 👨‍💻 Author
Richard – Data Scientist 

Created as part of hands-on coursework during a Data Science Bootcamp.

