import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

st.set_page_config(page_title="Antares Bermuda")
st.title("Frequency-Severity Modelling")

Q1 = st.selectbox(
    'If you were sent to war, how would you fight your opponents?',
    ("-", "Machine Gun", "Remote controlled bomber", "Sniper", "Tank Opperator", "Swarm of AI-Powered Drones", "Assasinate with a Dagger", "Laser Gun", "Lightsaber", "Trowing Axes"))

Q2 = st.selectbox(
    'Which describes you best?',
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky"))