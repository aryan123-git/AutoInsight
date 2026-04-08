from dash import Input, Output
import pandas as pd
import requests
import plotly.express as px
from dashboard.app import app
from core.logger import get_logger

logger = get_logger(__name__)

API_BASE_URL = "http://127.0.0.1:8000/api/v1"

@app.callback(
    [Output("total-sales", "children"),
     Output("total-transactions", "children"),
     Output("sales-over-time-chart", "figure"),
     Output("category-pie-chart", "figure")],
    [Input("interval-component", "n_intervals")]
)
def update_dashboard(n):
    # Fetch metrics
    try:
        metrics_resp = requests.get(f"{API_BASE_URL}/metrics")
        if metrics_resp.status_code == 200:
            data = metrics_resp.json()
            total_sales = f"${data.get('total_sales', 0):,.2f}"
            total_transactions = f"{data.get('total_transactions', 0):,}"
        else:
            total_sales, total_transactions = "$0.00", "0"
            
        # Fetch transactions for charting
        trans_resp = requests.get(f"{API_BASE_URL}/transactions?limit=1000")
        if trans_resp.status_code == 200:
            df = pd.DataFrame(trans_resp.json())
        else:
            df = pd.DataFrame()
    except Exception as e:
        logger.error(f"Dashboard failed to fetch from API: {e}")
        total_sales, total_transactions = "$0.00", "0"
        df = pd.DataFrame()

    fig_line = px.line(title="Sales Over Time")
    fig_pie = px.pie(title="Sales by Category")

    if not df.empty:
        df_date = df.groupby('date', as_index=False)['total_amount'].sum()
        df_date = df_date.sort_values(by='date')
        fig_line = px.line(df_date, x='date', y='total_amount', title="Sales Over Time", markers=True)
        
        df_cat = df.groupby('category', as_index=False)['total_amount'].sum()
        fig_pie = px.pie(df_cat, names='category', values='total_amount', title="Sales by Category")
        fig_pie.update_traces(hole=.4)

    fig_line.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=40, b=20))
    fig_pie.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=40, b=20))

    return total_sales, total_transactions, fig_line, fig_pie
