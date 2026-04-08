import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app with a modern Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)
app.title = "AutoInsight Dashboard"
server = app.server
