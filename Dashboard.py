from Manual import manual
import streamlit as st
import os
from streamlit.server.server import Server
from streamlit.report_thread import get_report_ctx
from automate import automate
from state import session_state

# Page config defines the layout of page which includes params like layout, sidebar_status, title of page.
# Page config should run only once while executing code
st.set_page_config(layout="wide", initial_sidebar_state="auto", page_title="ADMIN PORTAL")

# Session state maintains data that defines the state of our program
# Values are initialized in Session.get

ctx = get_report_ctx()
# get session id
session_id = ctx.session_id

# get session
server = Server.get_current()
session_info = server._session_info_by_id.get(session_id)
session = session_info.session

# register watcher
session._local_sources_watcher._register_watcher(
    os.path.join(os.path.dirname(__file__), session_state.file_name),
    'dummy:' + session_state.file_name
)


def main() -> None:
    """
    This is the root function that runs first before any other code.
    As Streamlit requires proper structured flow of functions main function is required.

    :return: It doesn't return anything
    """
    session_state.root_node = st.sidebar.selectbox("Operation Type", ["Automated", "Manual"])
    if session_state.root_node == "Manual":
        manual()
    elif session_state.root_node == "Automated":
        automate()


if __name__ == "__main__":  # this defines that main function is root function
    main()
