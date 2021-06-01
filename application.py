sys.path.append("/opt/python/current/app/backend/src")
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from app import server
import CovidTracker
import pagenotfound
# import CovidMaharashtraFaciltiesLogistics

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    # content will be rendered in this element
    html.Div(id='page-content')
],)

@app.callback(Output(component_id='page-content',component_property='children'),
              [Input(component_id='url',component_property='pathname')])

def load_page(pathname):
    if pathname=='/covidtracker':
        return CovidTracker.covidtracker_layout
    # if pathname=='/covid-mah-facilities-logistics':
    #     return CovidMaharashtraFaciltiesLogistics.MaharashtraFacilitiesLogistics_layout
    else:
        return pagenotfound.pagenotfound_layout

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
