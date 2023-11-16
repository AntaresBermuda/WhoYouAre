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
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person."),
    key="q1")

Q1_1 = st.selectbox("",
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person."),
    key="q1_1")

Q1_2 = st.selectbox("",
    ("-", "Gun them dowm from the Trenches", "Remote controlled Mortars", "Sniper", "Tank Opperator", 
    "Throw Grenades", "Swarm of AI-Powered Drones", "Assasinate them at Night", "Satelite Space Lasers", "Slash them with an Axe", "Drop a Nuke", "I wouldn't fight, I'm a peaceful person."),
    key="q1_2")


st.write('\n')
st.write('\n')
st.subheader("Which Positive Traits describes you best? Pick 3.")
st.subheader("", divider="rainbow")

Q2 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2")

Q2_1 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2_1")

Q2_2 = st.selectbox("",
    ("-", "Strategic", "Skillful", "Athletic", "Brute Force", "Helpful", "Patient", "Powerful", "Sneaky", "Genius", "Talented", "Unpredictable", "Rational", "Friendly", "Efficient", "Productive", "Optimistic", "Modest"),
    key="q2_2")


st.write('\n')
st.write('\n')
st.subheader("Which Negative Traits describes you best? Pick 2.")
st.subheader("", divider="rainbow")

Q3 = st.selectbox("",
    ("-", "Impatient", "Revengeful", "Just Crazy", "Pessimistic", "Angry", "Paranoid", "Lazy", "Selfish", "boastful", "Controlling"),
    key="q3")
Q3_1 = st.selectbox("",
    ("-", "Impatient", "Revengeful", "Just Crazy", "Pessimistic", "Angry", "Paranoid", "Lazy", "Selfish", "boastful", "Controlling"),
    key="q3_1")


st.write('\n')
st.write('\n')
st.subheader("What Weapons do you keep just in case. Pick 2.")
st.subheader("", divider="rainbow")

Q4 = st.selectbox("",
    ("-", "Two handguns", "My Fists", "Taser Gun", "FN P90, I'm cultured", "A Mdieval Sword", "An ancient book with Magical Spells", "Bow and Arrow", "Lightsaber", "bazooka"),
    key="q4")

Q4_1 = st.selectbox("",
    ("-", "Two handguns", "My Fists", "Taser Gun", "FN P90, I'm cultured", "A Mdieval Sword", "An ancient book with Magical Spells", "Bow and Arrow", "Lightsaber", "bazooka"),
    key="q4_1")


st.write('\n')
st.write('\n')
st.subheader("What Superpowers would you like to have? Pick 3.")

Q5 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5")
Q5_1 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5_1")
Q5_2 = st.selectbox("",
    ("-", "Indestructible", "Super Strenght", "Teleportation", "Healing/Reviving Powers", "Invisability", "Never Age", "X-ray Vision", "Time-Travel", "Shape-Shifting", "Extreme Intelligence", "Sonic Powers", "Ultra Speed", "Lighting/Electric Powers", "Fire-Bending", "Water-Bending", "Air-Bending", "Earth-Bending", "Magical Spells", "I don't need Superpowers"),
    key="q5_2")


st.write('\n')
st.write('\n')
st.subheader("Choose a pet.")

# Show funny patrick meme if you chose a pet as a rock.
Q5 = st.selectbox("",
    ("-", "Cat", "Dog", "Fish", "Snake", "Bear", "A Rock", "Roach", "Cow", "Hamster", "Rat", "Bird", "Scorpion", "Fox", "Turtle", "Toad", "Monkey", "Humans are the Superior Animal"),
    key="q5")

