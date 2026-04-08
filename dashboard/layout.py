from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("AutoInsight Dashboard", className="text-center text-primary mt-4 mb-4"), width=12)
        ]),
        
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Total Sales", className="card-title text-center"),
                    html.H2(id="total-sales", className="text-success text-center")
                ])
            ], className="mb-4 shadow-sm"), width=6),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Total Transactions", className="card-title text-center"),
                    html.H2(id="total-transactions", className="text-info text-center")
                ])
            ], className="mb-4 shadow-sm"), width=6)
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id="sales-over-time-chart"), width=12, lg=8),
            dbc.Col(dcc.Graph(id="category-pie-chart"), width=12, lg=4)
        ], className="mb-4"),
        
        # A trigger interval for real-time-ish updates (every 10 seconds)
        dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0)
    ], fluid=True)
