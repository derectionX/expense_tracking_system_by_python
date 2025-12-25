import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_by_month_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_month = st.date_input(
            "Start Month",
            datetime(2024, 8, 1)
        )

    with col2:
        end_month = st.date_input(
            "End Month",
            datetime(2024, 9, 1)
        )

    if st.button("Get Monthly Analytics"):
        # Convert month selection to full date range
        start_date = start_month.replace(day=1)

        end_date = end_month.replace(day=1)
        if end_date.month == 12:
            end_date = end_date.replace(day=31)
        else:
            end_date = (
                end_date.replace(month=end_date.month + 1, day=1)
                - pd.Timedelta(days=1)
            )

        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("Failed to fetch monthly analytics")
            st.write(response.text)
            return

        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[c]["total"] for c in response],
            "Percentage": [response[c]["percentage"] for c in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Total", ascending=False)

        st.subheader("Monthly Expense Breakdown")

        st.bar_chart(
            df_sorted.set_index("Category")["Total"],
            use_container_width=True
        )

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)
