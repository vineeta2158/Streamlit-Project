import math
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.subplots import make_subplots


def bar_graph(data: DataFrame) -> None:
    """
    Displays Bar graph for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    columns = list(df.columns)
    columns = list(column for column in columns if column != "Timestamp")
    layout = go.Layout(
        title=go.layout.Title(text="Bar Graph"),
    )

    # List of Graphical Object bars to be provided to figure
    Bars = list(
        go.Bar(name=name, x=df["Timestamp"].astype(str), y=df[name].astype(np.float64)) for name in columns
    )

    fig = go.Figure(data=Bars, layout=layout)
    fig.update_xaxes(title_text="Timestamp")
    fig.update_yaxes(title_text="Values")
    fig.update_layout(barmode='group',
                      height=600,
                      width=1000,
                      )
    st.plotly_chart(fig,use_container_width=True)


def pie_graph(data: DataFrame) -> None:
    """
    Displays Pie graph for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    total_pies = df["Timestamp"].count()

    no_col = int(3)

    no_row = math.ceil(total_pies / no_col)

    columns = list(col for col in list(df.columns) if col != "Timestamp")
    spec = list(list({'type': 'domain'} for J in range(no_col)) for I in range(no_row))
    fig = make_subplots(rows=no_row, cols=no_col, specs=spec)
    Pies = list(
        go.Pie(labels=columns, values=list(row[col] for col in columns), name=row["Timestamp"]) for index, row in
        df.iterrows())
    k = 0
    for i in range(1, no_row + 1):
        for j in range(1, no_col + 1):
            if len(Pies) > k:
                fig.add_trace(Pies[k], row=i, col=j)
                k += 1
    fig.update_traces(hoverinfo="label+percent+name")
    # fig.update_traces(hole=.4, hoverinfo="label+percent+name") # For Doughnut Graph
    fig.update_layout(
        title_text="PIE CHART",
    )
    st.plotly_chart(fig,use_container_width=True)


def trend_line_chart(data: DataFrame) -> None:
    """
    Displays Trend line chart for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    columns = list(df.columns)
    columns = list(column for column in columns if column != "Timestamp")
    layout = go.Layout(
        title=go.layout.Title(text="Line Chart"),
    )
    Lines = list(
        go.Scatter(name=name, x=df["Timestamp"].astype(str), y=df[name].astype(np.float64), mode="lines") for name in
        columns
    )

    fig = go.Figure(data=Lines, layout=layout)
    fig.update_xaxes(title_text="Timestamp")
    fig.update_yaxes(title_text="Values")
    st.plotly_chart(fig,use_container_width=True)


def doughnut_graph(data: DataFrame) -> None:
    """
    Displays Doughnut graph for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    total_pies = df["Timestamp"].count()

    no_col = int(3)

    no_row = math.ceil(total_pies / no_col)

    columns = list(col for col in list(df.columns) if col != "Timestamp")
    spec = list(list({'type': 'domain'} for J in range(no_col)) for I in range(no_row))
    fig = make_subplots(rows=no_row, cols=no_col, specs=spec)
    Pies = list(
        go.Pie(labels=columns, values=list(row[col] for col in columns), name=row["Timestamp"]) for index, row in
        df.iterrows())
    k = 0
    for i in range(1, no_row + 1):
        for j in range(1, no_col + 1):
            if len(Pies) > k:
                fig.add_trace(Pies[k], row=i, col=j)
                k += 1
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")  # For Doughnut Graph
    st.plotly_chart(fig,use_container_width=True)


def point_chart(data: DataFrame) -> None:
    """
    Displays Point chart for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    columns = list(df.columns)
    columns = list(column for column in columns if column != "Timestamp")
    layout = go.Layout(
        title=go.layout.Title(text="Point Chart"),
    )
    Area = list(
        go.Scatter(name=name, x=df["Timestamp"].astype(str), y=df[name].astype(np.float64), mode="markers") for name in
        columns
    )

    fig = go.Figure(data=Area, layout=layout)
    fig.update_xaxes(title_text="Timestamp")
    fig.update_yaxes(title_text="Values")
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='Black')))
    st.plotly_chart(fig,use_container_width=True)


def area_chart(data: DataFrame) -> None:
    """
    Displays Area line chart for provided Data

    :param data: Dataframe for which graph is to be plotted
    :return: It doesnt return anything
    """
    df = data
    columns = list(df.columns)
    columns = list(column for column in columns if column != "Timestamp")
    layout = go.Layout(
        title=go.layout.Title(text="Area Chart"),
    )
    Lines = list(
        go.Scatter(name=name, x=df["Timestamp"].astype(str), y=df[name].astype(np.float64),
                   mode="none", fill="tonexty") for name in
        columns
    )

    fig = go.Figure(data=Lines, layout=layout)
    fig.update_xaxes(title_text="Timestamp")
    fig.update_yaxes(title_text="Values")
    st.plotly_chart(fig,use_container_width=True)


def x_y_graph(data: DataFrame, column_name_1: str, column_list: list):
    df = data
    layout = go.Layout(
        title=go.layout.Title(text="X - Y  Plotter"),
    )
    columns = list(column for column in column_list if column != column_name_1)
    Line = list(go.Scatter(name=col, x=sorted(df[column_name_1].astype(np.float64)),
                           y=df[col].astype(np.float64),
                           mode="lines+markers") for col in columns)

    fig = go.Figure(data=Line, layout=layout)
    fig.update_xaxes(title_text=column_name_1)
    fig.update_yaxes(title_text="Columns")
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='Black')))
    st.plotly_chart(fig,use_container_width=True)


def x_y_plot(data: DataFrame, column_name_1: str, column_list: list):
    df = data
    total_graphs = len(column_list)
    no_col = int(3)
    no_row = math.ceil(total_graphs / no_col)
    spec = list(list({'type': 'domain'} for J in range(no_col)) for I in range(no_row))
    fig = make_subplots(rows=no_row, cols=no_col)
    PLOTS = list(go.Scatter(name=col, x=sorted(df[column_name_1].astype(np.float64)),
                            y=df[col].astype(np.float64),
                            mode="lines+markers") for col in column_list)
    k = 0
    for i in range(1, no_row + 1):
        for j in range(1, no_col + 1):
            if len(PLOTS) > k:
                fig.add_trace(PLOTS[k], row=i, col=j)
                k += 1
            fig.update_xaxes(title_text=column_name_1)
            # fig.update_yaxes(title_text=column_list[k])
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='Black')))
    st.plotly_chart(fig,use_container_width=True)
