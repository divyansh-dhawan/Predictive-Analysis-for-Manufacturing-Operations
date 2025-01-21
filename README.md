# Predictive Analysis for Manufacturing Operations

This repository contains a predictive analysis model for manufacturing operations. The goal of this project is to predict machine downtime based on temperature and run time data using a logistic regression model.

## Repository Structure

- **app.py**: Flask application that exposes an API endpoint for making predictions.
- **model.py**: Script to train and save the logistic regression model and label encoder.
- **synthetic_dataset.py**: Script to generate a synthetic dataset for training the model.
- **synthetic_machine_data.csv**: Generated synthetic dataset used for training the model.
- **logistic_regression_model.pkl**: Trained logistic regression model.
- **label_encoder.pkl**: Label encoder for encoding categorical machine IDs.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- scikit-learn
- joblib
- pandas
- numpy

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/divyansh-dhawan/Predictive-Analysis-for-Manufacturing-Operations.git
    cd Predictive-Analysis-for-Manufacturing-Operations
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Training the Model

1. Generate the synthetic dataset:
    ```bash
    python synthetic_dataset.py
    ```

2. Train the logistic regression model:
    ```bash
    python model.py
    ```

### Running the Flask Application

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. The application will be running at `http://127.0.0.1:5000`.

### Making Predictions

To make predictions, you can use the `/predict` endpoint of the Flask application. Below is a sample input and output using PowerShell.

#### Sample Input

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" `
-Method POST `
-Headers @{"Content-Type" = "application/json"} `
-Body '{"Temperature": 100, "Run_Time": 227}' `
-UseBasicParsing
```

#### Sample Output

```powershell
StatusCode        : 200
StatusDescription : OK
Content           : {"Confidence":1.0,"Downtime":"Yes"}

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 36
                    Content-Type: application/json
                    Date: Tue, 21 Jan 2025 17:26:51 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"Confidence":1.0,"Downtime":"Yes"}
Forms             :
Headers           : {[Connection, close], [Content-Length, 36], [Content-Type, application/json], [Date, Tue, 21 Jan 2025 17:26:51 GMT]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        :
RawContentLength  : 36
