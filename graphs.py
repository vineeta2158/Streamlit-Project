def bar_graph(data, go, st):
    df = data
    columns = list(df.columns)
    columns = list(col for col in columns if col != "time" )
    layout = go.Layout(
        title=go.layout.Title(text="Graph"),
    )
    # index = list(index for index, y in df.iterrows())
    Bars = list(go.Bar(name=name, x=df["time"], y=df[name]) for name in columns)

    fig = go.Figure(data=Bars, layout=layout)
    fig.update_xaxes(title_text="Index")
    fig.update_yaxes(title_text="Values", zeroline=True)
    fig.update_layout(barmode='group')
    st.plotly_chart(fig)