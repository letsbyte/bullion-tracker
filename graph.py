import plotly.graph_objects as go

x = ["Jan", "Feb", "Mar", "Apr"]
y_gold = [12.10, 13.45, 11.20, 9.25]
y_silver = [2.10, 3.45, 1.20, 2.25]

x_gold_text = []
x_silver_text = []

for index, month in enumerate(x):
    gold_value = f"{month} - ${y_gold[index]}"
    silver_value = f"{month} - ${y_silver[index]}"
    x_gold_text.append(gold_value)
    x_silver_text.append(silver_value)
    
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Gold",
        x=x,
        y=y_gold,
        mode="lines+markers+text",
        text=x_gold_text,
        textposition="top center",
        line={
            "color": "#EB9310",
            "width": 4,
        },
    )
)
fig.add_trace(
    go.Scatter(
        name="Silver",
        x=x,
        y=y_silver,
        mode="lines+markers+text",
        text=x_silver_text,
        textposition="top center",
        line={
            "color": "#C5C0B7",
            "width": 4,
        },
    )
)

fig.update_layout(
    title='Change in Gold/Silver Prices',
    xaxis_title='Date',
    yaxis_title='USD',
)
                   
fig.show()