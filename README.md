# Expense Management System

This project is an expense management system that consists of a **Streamlit frontend application** and a **FastAPI backend server**.  
It allows users to add, update, view, and analyze daily expenses with category-wise analytics.

---

## Project Structure

---

## Features

- Add and update daily expenses
- Categorize expenses (Rent, Food, Shopping, etc.)
- View existing expenses by date
- Analyze expenses between date ranges
- Category-wise percentage breakdown
- Interactive UI using Streamlit

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** MySQL  
- **Visualization:** Pandas, Streamlit charts  
- **API Communication:** Requests  

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd expanse_tracking_system
```
2.**Install dependencies**
```bash
pip install -r requirements.txt
```
3.**Run the FastAPI server**
```bash
uvicorn server:app --reload
```
4.**Run the Streamlit app**
```bash
streamlit run frontend/app.py
```

