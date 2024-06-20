import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from data_fetching import fetch_covid_data
from data_preprocessing import preprocess_covid_data

covid_data = fetch_covid_data()
country = 'India'
country_data = preprocess_covid_data(covid_data, country)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('COVID-19 Dashboard'),

    html.Div([
        html.Label('Select Metric:'),
        dcc.Dropdown(
            id='metric-dropdown',
            options=[
                {'label': 'Total Cases', 'value': 'total_cases'},
                {'label': 'Total Deaths', 'value': 'total_deaths'},
                {'label': 'Total Vaccinations', 'value': 'total_vaccinations'}
            ],
            value='total_cases'
        ),
    ], style={'width': '30%', 'display': 'inline-block'}),

    dcc.Graph(id='total-cases-graph'),
])

@app.callback(
    Output('total-cases-graph', 'figure'),
    [Input('metric-dropdown', 'value')]
)
def update_graph(metric):
    return {
        'data': [
            go.Scatter(
                x=country_data['date'],
                y=country_data[metric],
                mode='lines+markers',
                marker=dict(color='blue'),
                name=metric.replace('_', ' ').title()
            )
        ],
        'layout': go.Layout(
            title=f'{metric.replace("_", " ").title()} over Time',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Count'),
            plot_bgcolor='#f0f0f0'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
