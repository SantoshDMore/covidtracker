import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import GetData
from app import app


df = GetData.owid_all()
print(df.columns.values)

country_select = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Select the contries ", xs=10, sm=8, md=5, lg=6, xl=5),
                dcc.Dropdown(
                    id="country-variable",
                    options=[
                        {"label": col, "value": col} for col in df['location'].unique()
                    ], multi=True, value=["United States", "United Kingdom", "China", "Russia", "India"],
                    className="mb-2"),
            ]
        ),
    ],style={"border": "0px"},
    body=True
)

data_source = dbc.Card(
    [

    ],
    style={"border": "0px"},
)


covidtracker_layout = dbc.Container(
    [
        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")),
        dbc.Row(
            [
                dcc.Markdown("# ** Worldwide Covid Trajectories **"),
                dbc.Col(data_source, xs=10, sm=8, md=5, lg=6, xl=5),

            ],
        ),
        dbc.Row(
            [
                dbc.Col(country_select, xs=10, sm=8, md=5, lg=6, xl=5),

            ], style={"border": "0px"}, no_gutters=True

        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="recovered_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                'modeBarButtonsToAdd': ['drawline', 'drawopenpath',
                                                                                        'drawclosedpath', 'drawcircle',
                                                                                        'drawrect', 'eraseshape']}),
                        xs=10, sm=8, md=5, lg=6, xl=5),

                dbc.Col(dcc.Graph(id="reproductionrate_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                'modeBarButtonsToAdd': ['drawline', 'drawopenpath',
                                                                                        'drawclosedpath', 'drawcircle',
                                                                                        'drawrect', 'eraseshape']}),
                        xs=10, sm=8, md=5, lg=6, xl=5),

                dbc.Col(dcc.Graph(id="confirmed_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                'modeBarButtonsToAdd': ['drawline', 'drawopenpath',
                                                                                        'drawclosedpath', 'drawcircle',
                                                                                        'drawrect', 'eraseshape']}),
                        xs=10, sm=8, md=5, lg=6, xl=5),
                dbc.Col(dcc.Graph(id="fatalities_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                 'modeBarButtonsToAdd': ['drawline', 'drawopenpath',
                                                                                         'drawclosedpath', 'drawcircle',
                                                                                         'drawrect', 'eraseshape']}),
                        xs=10, sm=8, md=5, lg=6, xl=5),
                dbc.Col(dcc.Graph(id="vaccination_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                  'modeBarButtonsToAdd': ['drawline', 'drawopenpath',
                                                                                          'drawclosedpath',
                                                                                          'drawcircle', 'drawrect',
                                                                                          'eraseshape']}), xs=10, sm=8,
                        md=5, lg=6, xl=5),
                dbc.Col(dcc.Graph(id="vaccinationbubble_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                        'modeBarButtonsToAdd': ['drawline',
                                                                                                'drawopenpath',
                                                                                                'drawclosedpath',
                                                                                                'drawcircle',
                                                                                                'drawrect',
                                                                                                'eraseshape']}), xs=10,
                        sm=8, md=5, lg=6, xl=5),

                dbc.Col(dcc.Graph(id="populationdensity_graph", config={"displaylogo": False, "displayModeBar": False,
                                                                        'modeBarButtonsToAdd': ['drawline',
                                                                                                'drawopenpath',
                                                                                                'drawclosedpath',
                                                                                                'drawcircle',
                                                                                                'drawrect',
                                                                                                'eraseshape']}), xs=10,
                        sm=8, md=5, lg=6, xl=5)

            ], no_gutters=True

        ),

        dbc.Row(
            [
                dbc.Col(dbc.Label("Datasource courtesy OurWorldInData", xs=10, sm=8, md=5, lg=6, xl=5))
            ], no_gutters=True
        ),

        html.Hr(),
    ],
    fluid=True,

)

@app.callback(
    Output("confirmed_graph", "figure"),
    Output("reproductionrate_graph", "figure"),
    Output("recovered_graph", "figure"),
    Output("fatalities_graph", "figure"),
    Output("vaccination_graph", "figure"),
    Output("vaccinationbubble_graph", "figure"),
    Output("populationdensity_graph", "figure"),
    [Input("country-variable", "value")])


def make_graph(x):
    print(x)
    active_layout = {"xaxis": {"title": "Date"},"yaxis": {"title": "New cases per million"}}
    reproductionrate_layout = {"xaxis": {"title": "Date"},"yaxis": {"title": "R Naught"}}
    fatalities_layout = {"xaxis": {"title": "Date"}, "yaxis": {"title": "Total fatalities"}}
    confirmed_layout = {"xaxis": {"title": "Date"}, "yaxis": {"title": "Total detected"}}
    vaccination_layout = {"xaxis": {"title": "Country"}, "yaxis": {"title": "Total vaccinations"}}
    vaccinationbubble_layout = {"xaxis": {"title": "Total Vaccinations"},"yaxis": {"title": "% Population Vaccinations"}}
    populationdensity_layout = {"xaxis": {"title": "Country "},"yaxis": {"title": "Population density"}}



    active_fig = go.Figure(layout=active_layout)
    reproductionrate_fig = go.Figure(layout=reproductionrate_layout)
    fatalities_fig = go.Figure(layout=fatalities_layout)
    confirmed_fig = go.Figure(layout=confirmed_layout)
    vaccination_fig = go.Figure(layout=vaccination_layout)
    vaccinationbubble_fig = go.Figure(layout=vaccinationbubble_layout)
    populationdensity_fig = go.Figure(layout=populationdensity_layout)

    # active_fig.layout.images = [dict(source="/assets/glogo.jpg",
    #         xref="paper", yref="paper",
    #         x=1, y=1.05,
    #         sizex=0.4, sizey=0.4,
    #         xanchor="right", yanchor="bottom")]
    #
    # fatalities_fig.layout.images = [dict(source="/assets/glogo.jpg",
    #                                  xref="paper", yref="paper",
    #                                  x=1, y=1.05,
    #                                  sizex=0.4, sizey=0.4,
    #                                  xanchor="right", yanchor="bottom")]
    #
    # confirmed_fig.layout.images = [dict(source="/assets/glogo.jpg",
    #                                      xref="paper", yref="paper",
    #                                      x=1, y=1.05,
    #                                      sizex=0.4, sizey=0.4,
    #                                      xanchor="right", yanchor="bottom")]
    #
    # vaccination_fig.layout.images = [dict(source="/assets/glogo.jpg",
    #                                     xref="paper", yref="paper",
    #                                     x=1, y=1.05,
    #                                     sizex=0.4, sizey=0.4,
    #                                     xanchor="right", yanchor="bottom")]
    #
    # vaccinationbubble_fig.layout.images = [dict(source="/assets/glogo.jpg",
    #                                       xref="paper", yref="paper",
    #                                       x=1, y=1.05,
    #                                       sizex=0.4, sizey=0.4,
    #                                       xanchor="right", yanchor="bottom")]

    vaccinationbubble_fig.update_xaxes(type="log", range=[0, 12])
    # vaccinationbubble_fig.update_yaxes(type="log", range=[0, 12])

    for i in x:
        df1 = df[df['location'] == i]
        df3 = df1[df1['reproduction_rate'] > 0]
        df2 = df1.groupby(['location'], as_index=False)[
            'total_vaccinations', 'total_vaccinations_per_hundred', 'total_cases', 'population','population_density'].max()
        df2 = df2.reset_index()
        active_fig.add_trace(go.Scatter(mode='lines', x=df1['date'], y=df1['new_cases_smoothed_per_million'], name=i))
        reproductionrate_fig.add_trace(go.Scatter(mode='lines', x=df3['date'], y=df3['reproduction_rate'], name=i))
        fatalities_fig.add_trace(go.Scatter(mode='lines', x=df1['date'], y=df1['total_deaths'], name=i))
        confirmed_fig.add_trace(go.Scatter(mode='lines', x=df1['date'], y=df1['total_cases'], name=i))
        vaccination_fig.add_trace(
            go.Bar(x=df2['location'], y=df2['total_vaccinations'], width=0.5, name=i, text=df2['total_vaccinations'],
                   textposition='auto'))
        vaccinationbubble_fig.add_trace(
            go.Scatter(mode='markers', x=df2['total_vaccinations'], y=df2['total_vaccinations_per_hundred'], name=i,
                       marker=dict(size=0.0000001 * df2['population']))),
        populationdensity_fig.add_trace(go.Bar(x=df2['location'], y=df2['population_density'], width=0.5, name=i))

    active_fig.update_layout(
        title="<b> New cases per million </b> ",
        template="plotly_white",
        legend=dict(
            x=0,
            y=1,
            traceorder="reversed",
            title_font_family="Calibri")
    )

    reproductionrate_fig.update_layout(
        title="<b> R Naught </b> ",
        template="plotly_white",
        legend=dict(
            x=1,
            y=1,
            traceorder="reversed",
            title_font_family="Calibri")
    )

    fatalities_fig.update_layout(
        title="<b>Total fatalities</b>", template="plotly_white",
        legend=dict(
            x=0,
            y=1,
            traceorder="reversed",
            title_font_family="Calibri")
    )

    confirmed_fig.update_layout(
        title="<b>Total Confirmed Cases</b>", template="plotly_white",
        legend=dict(
            x=0,
            y=1,
            traceorder="reversed",
            title_font_family="Calibri",
            )
    )

    vaccination_fig.update_layout(xaxis={'categoryorder': 'total descending'},
                                  title="<b>Total vaccinations</b>", template="plotly_white",
                                  margin=dict(l=100, r=20, t=70, b=70),
                                  legend=dict(
                                      x=1,
                                      y=1,
                                      traceorder="reversed",
                                      title_font_family="Calibri")

                                  )
    vaccinationbubble_fig.update_layout(xaxis={'categoryorder': 'total descending'},
                                        title="<b>% vaccinated</b> "
                                              "<br>size=population "
                                              "</br>x=total vaccinations "
                                              "</br>y=% vaccinated",
                                        template="plotly_white",
                                        margin=dict(l=100, r=20, t=70, b=70),
                                        legend=dict(
                                            x=1,
                                            y=1,
                                            traceorder="reversed",
                                            title_font_family="Calibri")

                                        )

    populationdensity_fig.update_layout(
        title="<b> Population density </b> ",
        template="plotly_white",
        legend=dict(
            x=1,
            y=1,
            traceorder="reversed",
            title_font_family="Calibri")
    )

    return confirmed_fig,reproductionrate_fig, active_fig, fatalities_fig, vaccination_fig,vaccinationbubble_fig,populationdensity_fig
