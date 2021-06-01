import dash
import dash_core_components as dcc
import dash_html_components as html


ess1 = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/simplex/bootstrap.min.css'
ess2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
app = dash.Dash(__name__,external_stylesheets=[ess1,ess2], meta_tags=[
    {'name': 'description','content': 'World Covid data vaccine'
    },
    {'name': 'viewport','content': 'width=device-width, initial-scale=1.0'
    }],suppress_callback_exceptions=True)

server = app.server
app.title = "Covid Worldwide Tracker"