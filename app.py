import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

st.set_page_config(page_title="League")

st.header("FreqSevModel")
st.subheader("", divider="rainbow")

st.subheader("If you were sent to war, how would you fight your opponents? Pick 3.")

Q1 = st.selectbox("",
    ("-", "Machine Gun", "Remote controlled Drones", "FN P90, I'm cultured.", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate with a Dagger", "Bow and Arrow","Laser Gun", "Lightsaber", "Trowing Axes", "Nuke Them", "I wouldn't fight, I'm a peaceful person."),
    key="q1")

Q1_1 = st.selectbox("",
    ("-", "Machine Gun", "Remote controlled Drones", "FN P90, I'm cultured.", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate with a Dagger", "Bow and Arrow","Laser Gun", "Lightsaber", "Trowing Axes", "Nuke Them", "I wouldn't fight, I'm a peaceful person."),
    key="q1_1")

Q1_2 = st.selectbox("",
    ("-", "Machine Gun", "Remote controlled Drones", "FN P90, I'm cultured.", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate with a Dagger", "Bow and Arrow","Laser Gun", "Lightsaber", "Trowing Axes", "Nuke Them", "I wouldn't fight, I'm a peaceful person."),
    key="q1_2")

st.subheader("Which describes you best? Pick 3.")
st.subheader("", divider="rainbow")

Q2 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", ""),
    key="q2")

