

# 💰 Expense Tracker with Data Visualization

## **Project Overview**

The **Expense Tracker** is a Python application that helps users record, manage, and visualize their daily expenses.
It stores expense data in a CSV file and provides **interactive charts** to track spending trends by category and over time.
This project demonstrates **Python data handling, Pandas, Matplotlib/Streamlit, and GUI/web app development skills** — making it ideal for a portfolio.

---

## **Features**

* ✅ Add expenses with **amount, category, date, and description**
* ✅ View all expenses in a **table or dashboard**
* ✅ Visualize spending with **bar charts (by category)** and **line charts (monthly trends)**
* ✅ Filter expenses by **category** and **date range** *(Streamlit version)*
* ✅ Optional GUI using **Tkinter** or interactive web app via **Streamlit**

---

## **Tech Stack**

* **Python 3.10+**
* **Pandas** – data handling & aggregation
* **Matplotlib / Plotly** – data visualization
* **Tkinter** – desktop GUI *(optional)*
* **Streamlit** – web dashboard *(optional)*
* **CSV** – simple persistent storage

---

## **Installation**

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Navigate to the project folder:

```bash
cd expense_tracker
```

3. Install required packages:

```bash
pip install pandas matplotlib streamlit
```

---

## **Usage**

### **Command-line / Script**

```bash
python expense_tracker.py
```

* Add expenses directly in the code or via CLI prompts.
* Visualize charts in separate windows.

### **Streamlit Web App**

```bash
streamlit run expense_tracker.py
```

* Open your browser at **[http://localhost:8501](http://localhost:8501)**
* Add expenses, view tables, and interact with charts.



## **Future Enhancements**

* OCR receipt scanning to automatically add expenses
* Budget alerts and notifications
* Export filtered reports to **PDF or Excel**
* Multi-user support with login authentication
