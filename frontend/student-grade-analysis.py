from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df2 = pd.read_csv('df2_data.csv')

app = Dash(__name__)
app.config.suppress_callback_exceptions = True 

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    
    html.H1("Student Grade Analysis", style={'textAlign': 'center'}),

    html.Div([
        html.A("Custom Prediction", href="http://127.0.0.1:8000/form", style={
            'marginBottom': '20px',
            'fontSize': '16px',
            'padding': '10px',
            'backgroundColor': '#007BFF',
            'color': 'white',
            'border': 'none',
            'cursor': 'pointer',
            'textDecoration': 'none'
        })
    ], style={'textAlign': 'end', 'margin-right': '50px'}),

    html.Label("Residency Filter:", style={'fontSize': '16px', 'marginLeft': '10px'}),
    dcc.Dropdown(
        id="residency-slicer",
        options=[{"label": res, "value": res} for res in df2["Residency"].unique()],
        value=df2["Residency"].unique()[0],  # Default value
        clearable=False,
        style={'margin': '10px', 'width': '50%'}
    ),

    html.Div([
        dcc.Graph(id="visual-1", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-2", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-3", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-4", style={"display": "inline-block", "width": "48%"})
    ])
])

@app.callback(
    [
        Output("visual-1", "figure"),
        Output("visual-2", "figure"),
        Output("visual-3", "figure"),
        Output("visual-4", "figure")
    ],
    Input("residency-slicer", "value")
)
def update_dashboard(selected_residency):
    filtered_df = df2[df2["Residency"] == selected_residency]

    fig1 = px.pie(
        filtered_df,
        names="First Language",
        title="First Language Distribution",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    age_group_mapping = {
        "0 to 18": 1,
        "19 to 20": 2,
        "21 to 25": 3,
        "26 to 30": 4,
        "31 to 35": 5,
        "36 to 40": 6,
        "41 to 50": 7,
        "51 to 60": 8,
        "61 to 65": 9,
        "66+": 10
    }

    filtered_df["Age Group Number"] = filtered_df["Age Group"].map(age_group_mapping)
    filtered_df["Age Group Number"] = pd.to_numeric(filtered_df["Age Group Number"], errors="coerce")
    filtered_df = filtered_df.dropna(subset=["Age Group Number"])
    filtered_df["Age Group Number"] = filtered_df["Age Group Number"].astype(int)
    fig2 = px.scatter(
        filtered_df,
        x="Math Score",
        y="English Grade",
        size="Age Group Number", 
        color="Gender",
        animation_frame="Age Group", 
        title="Age Group v/s English and Math score",
        labels={"Age Group": "Age Group"}, 
        color_discrete_sequence=px.colors.qualitative.Set1
    )

    fig2.update_layout(
        xaxis_title="Math Score",
        yaxis_title="English Grade",
        sliders=[
            {
                "steps": [
                    {
                        "label": step["args"][0][0],
                        "method": step["method"],
                        "args": step["args"]
                    }
                    for step in fig2["layout"]["sliders"][0]["steps"]
                ]
            }
        ]
    )

    fig3 = px.histogram(
        filtered_df,
        x="Gender",
        color="Coop",
        barmode="group",
        title="Coop Status by Gender",
        labels={"Coop": "Coop Status", "Gender": "Gender"},
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig3.update_layout(
        xaxis_title="Gender",
        yaxis_title="Count",
        legend_title="Coop Status",
        template="plotly_white"
    )

    fig4 = px.histogram(
        filtered_df,
        x="Funding", 
        title="Funding Distribution",
        color_discrete_sequence=px.colors.qualitative.Vivid, 
        labels={"Funding": "Funding Type"} 
    )

    fig4.update_layout(
        xaxis_title="Funding Type",
        yaxis_title="Count",
        template="plotly_white"
    )

    return fig1, fig2, fig3, fig4

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
