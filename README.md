
# Student Passing Prediction and Analysis System

This project combines predictive modeling and interactive dashboards to help visualize and predict student academic outcomes. It consists of a FastAPI-powered backend for prediction, a Dash-based dashboard for data visualization, and an HTML form interface for user interaction.

---

![image](https://github.com/user-attachments/assets/8f846bd2-1d4a-4158-9714-23daa58044ef)

![image](https://github.com/user-attachments/assets/6a13fdb4-8cbb-45a5-b4f6-ce581533a5a7)



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Visualization Dashboard](#visualization-dashboard)
- [License](#license)

---

## Overview

The goal of this project is to:
- Predict whether a student is likely to pass based on academic and demographic features.
- Provide interactive visualizations to explore factors impacting student success.
- Offer an easy-to-use interface for both analytics and prediction tasks.

---

## Features

- **Machine Learning Prediction** using a trained neural network (Keras)
- **GraphQL API** via FastAPI and Strawberry for structured and scalable backend integration
- **Interactive Visualization Dashboard** using Dash and Plotly
- **Form-Based Web Interface** for submitting student information and viewing prediction
- **Residency-based Filtering** for data slicing and visualization

---

## Technologies Used

- **Backend**: Python, FastAPI, Strawberry GraphQL
- **Frontend**: HTML, Jinja2 templates, CSS
- **Dashboard**: Dash, Plotly
- **ML Model**: Keras (Neural Network)
- **Visualization**: Pandas, Plotly Express
- **Routing and Hosting**: FastAPI with static/template mounts

---

## Project Structure

```
├── main.py                     # FastAPI backend with GraphQL and routing
├── Viz-Assignment.py          # Dash dashboard application
├── anaylsis-training.ipynb    # Notebook for model training
├── models/
│   └── neural_network_model.keras  # Trained Keras model
├── templates/
│   ├── index.html             # Student input form
│   └── result.html            # Prediction result page
├── static/
│   ├── css/
│   │   └── styles.css         # Styling for HTML pages
│   └── js/
│       └── script.js          # Script for form interaction
└── df2_data.csv               # Dataset used for dashboard
```

---

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/your-username/student-prediction-app.git
cd student-prediction-app

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend (port 8000)
uvicorn main:app --reload --port 8000

# Run Dash dashboard (port 8051)
python student-grade-analysis.py
```

---

## Usage

- Go to `http://127.0.0.1:8000/form` to access the **student form**
- Fill out the details (GPA, gender, residency, etc.)
- Submit to get the **pass/fail prediction**
- Click **Dashboard** to access the Dash dashboard (`http://127.0.0.1:8051`)
- Filter by residency to see visual trends on:
  - Language Distribution
  - Math vs English performance by age group
  - Co-op status by gender
  - Funding distribution

---

## Model Training

- Training is done in `anaylsis-training.ipynb`
- Features include GPA, demographics, academic background, and test scores
- A neural network was built and trained using Keras
- Model is saved to `models/neural_network_model.keras` and loaded in `main.py`

---

## Visualization Dashboard

- Built with Dash and Plotly
- Uses `df2_data.csv` to power:
  - Pie charts, scatter plots, histograms
  - Interactive filtering via dropdown (residency)
  - Age group mapped and animated in scatter plot

---

## License

This project is licensed under the MIT License.
