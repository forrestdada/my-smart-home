import plotly.graph_objects as go

class Chart:
    def __init__(self, title):
        self.fig = go.Figure()
        self.title = title
        self.path = "/path" + self.title
        self.x = ['6H', '5H', '4H', '3h', '2H', '1H', 'NOW']
        self.y = [0, 0, 0, 0, 0, 0, 0]
        self.fig.update_layout(title=title)

    def save(self):
        self.fig.add_trace(go.Scatter(x=self.x, y=self.y, mode='lines', name='line'))
        self.fig.write_html(self.path)
