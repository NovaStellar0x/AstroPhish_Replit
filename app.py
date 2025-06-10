import dash
from dash import html, dcc, dash_table
import pandas as pd
from feeds.phishtank import fetch_phishtank_urls
from feeds.openphish import fetch_openphish_urls
from analysis.url_parser import extract_url_info
from analysis.domain_info import resolve_domain

app = dash.Dash(__name__)

def get_data():
    urls = fetch_phishtank_urls() + fetch_openphish_urls()
    data = []
    for url in urls[:200]:
        info = extract_url_info(url)
        info['ip'] = resolve_domain(info.get('domain', ''))
        data.append(info)
    return pd.DataFrame(data)

print("[*] Gathering phishing URLs for AstroPhish dashboard...")
df = get_data()

app.layout = html.Div([
    html.H1("AstroPhish ✨ Phishing Feed Dashboard"),
    dcc.Graph(
        figure={
            'data': [{
                'type': 'pie',
                'labels': df['domain'].apply(lambda d: d.split('.')[-1]).value_counts().index,
                'values': df['domain'].apply(lambda d: d.split('.')[-1]).value_counts().values
            }],
            'layout': {'title': 'Top TLDs in Phishing URLs'}
        }
    ),
    html.H2("Live Feed Table"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=15,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'fontFamily': 'monospace'}
    )
])

if __name__ == '__main__':
    print("App running at http://0.0.0.0:8080")
    app.run_server(host="0.0.0.0", port=8080, debug=True)