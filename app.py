
import gradio as gr
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load("sales_prediction_model.pkl")


# Function to predict sales
def predict_sales(tv, radio, newspaper):
    campaign = pd.DataFrame({
        "TV": [tv],
        "Radio": [radio],
        "Newspaper": [newspaper]
    })

    prediction = model.predict(campaign)[0]

    return round(float(prediction), 2)


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
    description="Enter advertising budgets to estimate sales using a trained Random Forest model."
)


# Launch the application
if __name__ == "__main__":
    demo.launch()
