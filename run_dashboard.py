from dashboard.app import app
from dashboard.layout import create_layout
import dashboard.callbacks # Import to register callbacks

app.layout = create_layout()

if __name__ == "__main__":
    print("Starting AutoInsight Dashboard...")
    app.run_server(debug=True, port=8050)
