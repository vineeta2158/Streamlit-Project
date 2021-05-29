import SessionState
from time_convert import hour_behind, end_time

session_state = SessionState.get(
    root_node="",
    file_name="Node06.csv",
    start=0,
    End=0,
    start_date=hour_behind(),
    start_time=hour_behind(),
    end_date=end_time(),
    end_time=end_time(),
    display_type="Graph",
    graph_type="Bar Chart",
    data_type="Historian",
    column=[],
    column_statistic=[],
    dynamic=False,
    Live_exlude_graph=['Trend Chart', 'Area Chart',
                       'X-Y Plotter'],
    column1="",
    column2=[]
)
