
import gradio as gr
import pandas as pd
import joblib
import sqlite3

# Load the trained Random Forest model
model = joblib.load("sales_prediction_model.pkl")

# Create the SQLite database and table
def setup_database():
    conn = sqlite3.connect("sales_predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tv_budget REAL NOT NULL,
            radio_budget REAL NOT NULL,
            newspaper_budget REAL NOT NULL,
            predicted_sales REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# Predict sales and save the result
def predict_sales(tv, radio, newspaper):
    if tv < 0 or radio < 0 or newspaper < 0:
        raise gr.Error("Advertising budgets cannot be negative.")

    campaign = pd.DataFrame({
        "TV": [tv],
        "Radio": [radio],
        "Newspaper": [newspaper]
    })

    prediction = float(model.predict(campaign)[0])

    # Save this prediction to the database
    conn = sqlite3.connect("sales_predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prediction_history
        (tv_budget, radio_budget, newspaper_budget, predicted_sales)
        VALUES (?, ?, ?, ?)
    """, (tv, radio, newspaper, prediction))

    conn.commit()
    conn.close()

    return round(prediction, 2)


# Ensure the table exists before launching the app
setup_database()

# Create the Gradio interface
demo = gr.Interface(
    fn=predict_sales,
    inputs=[
        gr.Number(label="TV Advertising Budget", value=150),
        gr.Number(label="Radio Advertising Budget", value=25),
        gr.Number(label="Newspaper Advertising Budget", value=20)
    ],
    outputs=gr.Number(label="Predicted Sales"),
    title="Sales Prediction System",
    description=(
        "Enter advertising budgets to estimate sales. "
        "Each prediction is saved in an SQLite database."
    )
)

demo.launch()
