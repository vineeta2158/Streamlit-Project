import math
def bar_graph(data, go, st):
    df = data
    columns = list(df.columns)
    columns = list(col for col in columns if col != "time" )
    layout = go.Layout(
        title=go.layout.Title(text="Graph"),
    )
    Bars = list(go.Bar(name=name, x=df["time"], y=df[name]) for name in columns)

    fig = go.Figure(data=Bars, layout=layout)
    fig.update_xaxes(title_text="Timestamp")
    fig.update_yaxes(title_text="Values", zeroline=True)
    fig.update_layout(barmode='group')
    st.plotly_chart(fig)
    
def pie_graph(data,go,st,make_subplots):
    df = data
    total_pies = df["time"].count()

    no_col = int(3)
 
    no_row = math.ceil(total_pies/no_col)
   
    
    columns = list(col for col in list(df.columns) if col != "time" )
    spec = list(list({'type':'domain'} for J in range(no_col)) for I in range(no_row))
    fig = make_subplots(rows=no_row, cols=no_col, specs=spec)
    Pies = list(go.Pie(labels=columns, values = list(row[col] for col in columns), name=row["time"] ) for index, row in df.iterrows())
    # print(Pies)
    k=0
    for i in range(1,no_row+1):
        for j in range(1,no_col+1):
                if len(Pies) > k:    
                    fig.add_trace(Pies[k],row=i,col=j)
                    k += 1
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_layout(
        title_text="PIE CHART",
    )
    st.plotly_chart(fig)

