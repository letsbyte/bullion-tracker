import os
from collections import defaultdict

import plotly.graph_objects as go

GOLD_COLOR = "#EB9310"
SILVER_COLOR = "#C5C0B7"
LINE_WIDTH = 4


class Graph:
    
    def __init__(self, x, y_gold, y_silver):
        self.x = x
        self.y_gold = y_gold
        self.y_silver = y_silver
        
    def _gen_friendly_text(self):
        friendly_text = defaultdict(list)

        for index, month in enumerate(self.x):
            gold_value = f"{month} - ${self.y_gold[index]}"
            silver_value = f"{month} - ${self.y_silver[index]}"
            friendly_text["gold"].append(gold_value)
            friendly_text["silver"].append(silver_value)
        
        return friendly_text
        
    def render(self, export=False):
        friendly_text = self._gen_friendly_text()
        
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                name="Gold",
                x=self.x,
                y=self.y_gold,
                mode="lines+markers+text",
                text=friendly_text["gold"],
                textposition="top center",
                line={
                    "color": GOLD_COLOR,
                    "width": LINE_WIDTH,
                },
            )
        )
        fig.add_trace(
            go.Scatter(
                name="Silver",
                x=self.x,
                y=self.y_silver,
                mode="lines+markers+text",
                text=friendly_text["silver"],
                textposition="top center",
                line={
                    "color": SILVER_COLOR,
                    "width": LINE_WIDTH,
                },
            )
        )

        fig.update_layout(
            title='Change in Gold/Silver Prices',
            xaxis_title='Date',
            yaxis_title='USD',
        )

        fig.show()

        if export:
            if not os.path.exists("images"):
                os.mkdir("images")

            fig.write_image("images/gold_silver_chart.png")


if __name__ == "__main__":
    x = ["Jan", "Feb", "Mar", "Apr"]
    y_gold = [12.10, 13.45, 11.20, 9.25]
    y_silver = [2.10, 3.45, 1.20, 2.25]
    
    g = Graph(x, y_gold, y_silver)
    g.render(export=True)