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

st.write('\n')
st.write('\n')

st.subheader("Frequency Distribution", divider="rainbow")

option1 = st.selectbox(
    'Which Frequency distribution would you like to use?',
    ("Poisson: Var(N) = E[N]", "Binomial: Var(N) < E[N]", "Negative Binomial: Var(N) > E[N]"))

Mean = st.number_input("What is the Expected Frequency:  $E[N]$?", min_value=0.01)

if option1=="Poisson: Var(N) = E[N]":
    "Since you have selected Poisson, the variance of your frequency distribution is equal to its mean."
    Variance = Mean
if option1=="Binomial: Var(N) < E[N]":
    Variance = st.number_input("What is the Variance of the Frequency:  $Var(N)$?", min_value=0.0, max_value=Mean-0.005)
if option1=="Negative Binomial: Var(N) > E[N]":
    Variance = st.number_input("What is the Variance of the Frequency:  $Var(N)$?", min_value=Mean+0.01)

st.markdown("**<u>Your selected Frequency distribution is:</u>**", unsafe_allow_html=True)
if option1=="Poisson: Var(N) = E[N]":
    st.latex(r''' P(N=n) = \frac{\lambda^{n}e^{-\lambda}}{n!} \ \ , \ \ \ n \geq 0 ''')
    st.markdown("Where $\lambda=$ "+str(np.round(Mean,2)))

if option1=="Negative Binomial: Var(N) > E[N]":
    st.latex(r''' P(N=n) = \frac{(r-1+n)!}{(r-1)! \ n!} \left(\frac{\beta}{1+\beta}\right)^{n} \left(\frac{1}{1+\beta}\right)^{r} \ \ , \ \ \ n \geq 0 ''')
    beta = Variance/Mean-1
    r = Mean/beta
    st.latex(r'''Where: \ \ \ \ \  \beta = '''+str(round(beta,2))+r''' \ \ , \ \ \ r = '''+str(round(r,2)))

if option1=="Binomial: Var(N) < E[N]":
    st.latex(r''' P(N=n) = \frac{m!}{(m-n)! \ n!}  \ p^{n} (1-p)^{m-n} \ \ , \ \ \ 0 \leq n \leq  m ''')
    p = 1-Variance/Mean
    m = Mean/p
    st.latex(r'''Where: \ \ \ \ \  p = '''+str(round(p,2))+r''' \ \ , \ \ \ m = '''+str(round(m,2)))

st.write('\n')
st.write('\n')

st.subheader("Severity Distribution", divider="rainbow")

option2 = st.selectbox(
    'Which Severity distribution would you like to use?',
    ("LogNormal", "Normal", "Pareto", "Gamma"))

if option2=="LogNormal":
    mu = st.number_input("What is the Expectation of the natural log of the Severity:  $E[\ln(X)]$?", min_value=0.01)
    var = st.number_input("What is the Variance of the natural log of the Severity:  $Var(\ln(X))$?", min_value=0.01)
    Mean2 = np.exp(mu+(var)/2)
    Variance2 = np.exp(2*mu+var)*(np.exp(var)-1)
    
    st.markdown("**<u>Your selected Severity distribution is:</u>**", unsafe_allow_html=True)
    st.latex(r''' f_X(x) = \frac{1}{x \sigma \sqrt{2\pi}}  \exp\left[ {\frac{-1}{2}} \left( \frac{\ln(x)-\mu}{\sigma}    \right )^2  \right] \ \ , \ \ \ x \geq 0 ''')
    st.latex(r'''Where: \ \ \ \ \  \mu = '''+str(round(mu,2))+r''' \ \ , \ \ \ \sigma = '''+str(round(np.sqrt(var),2)))

if option2=="Normal":
    Mean2 = st.number_input("What is the Expected Severity:  $E[X]$?", min_value=0.01)
    Variance2 = st.number_input("What is the Variance of the Severity:  $Var(X)$?", min_value=0.01)

    st.markdown("**<u>Your selected Severity distribution is:</u>**", unsafe_allow_html=True)
    st.latex(r''' f_X(x) = \frac{1}{\sigma \sqrt{2\pi}}  \exp\left[ {\frac{-1}{2}} \left( \frac{x-\mu}{\sigma}    \right )^2  \right] \ \ , \ \ \ x \geq 0 ''')
    st.latex(r'''Where: \ \ \ \ \  \mu = '''+str(round(Mean2,2))+r''' \ \ , \ \ \ \sigma = '''+str(round(np.sqrt(Variance2),2)))

if option2=="Pareto":
    Mean2 = st.number_input("What is the Expected Severity:  $E[X]$?", min_value=0.01)
    Variance2 = st.number_input("What is the Variance of the Severity:  $Var(X)$?", min_value=0.01)

    st.markdown("**<u>Your selected Severity distribution is:</u>**", unsafe_allow_html=True)
    st.latex(r''' f_X(x) = \frac{\alpha \ m^\alpha}{x^{\alpha+1}}''')
    alpha = 1 + np.sqrt(1+(Mean2**2)/Variance2)
    m = Mean2*(alpha-1)/alpha
    st.latex(r'''Where: \ \ \ \ \  \alpha = '''+str(round(alpha,2))+r''' \ \ , \ \ \ m = '''+str(round(m,2)))

if option2=="Gamma":
    Mean2 = st.number_input("What is the Expected Severity:  $E[X]$?", min_value=0.01)
    Variance2 = st.number_input("What is the Variance of the Severity:  $Var(X)$?", min_value=0.01)

    st.markdown("**<u>Your selected Severity distribution is:</u>**", unsafe_allow_html=True)
    st.latex(r''' f_X(x) = \frac{x^{\alpha-1} \ e^{-x/\theta}}{\theta^\alpha \ (\alpha-1)!} ''')
    theta = Variance2/Mean2
    alpha = Mean2/theta
    st.latex(r'''Where: \ \ \ \ \  \theta = '''+str(round(theta,2))+r''' \ \ , \ \ \ \alpha = '''+str(round(np.sqrt(alpha),2)))

# Maybe add Beta distribution eventhough it's kind of lame because it limits x, find practical applications first.
# For Weibull you would have to invert the gamma function which aint easy see.

st.write('\n')
st.write('\n')

st.subheader("Frequency-Severity", divider="rainbow")

st.markdown("The expected aggregate Loss is: $ \ E[S]=$ "+str(np.round(Mean*Mean2,2)))
st.markdown("The expected aggregate Variance is: $ \ Var(S)=$ "+str(np.round(Mean*Variance2+Variance*Mean2**2,2)))

sims = st.selectbox(
    'Select the number of simulations',
    ("100", "1,000", "10,000", "100,000"))

sims = int(sims.replace(",",""))


if st.button("Run Simulation"):
    if option1=="Poisson: Var(N) = E[N]":
        l = np.random.poisson(Mean, sims)
    if option1=="Binomial: Var(N) < E[N]":
        l = np.random.binomial(m,p,sims)
    if option1=="Negative Binomial: Var(N) > E[N]":
        l = np.random.negative_binomial(r, 1/(1+beta), sims)

    sevs = np.sum(l)
    
    if option2=="LogNormal":
        x = np.random.lognormal(mu, np.sqrt(var), sevs)
    if option2=="Normal":
        x = np.random.normal(Mean2, np.sqrt(Variance2), sevs)    
    if option2=="Pareto":
        x = (np.random.pareto(alpha, sevs)+1)*m   
    if option2=="Gamma":
        x = np.random.gamma(alpha, theta, sevs)

    M = np.zeros((sims, np.max(l)))

    row_start = 0
    for i, length in enumerate(l):
        row_end = row_start + length
        M[i, :length] = x[row_start:row_end]
        row_start = row_end

    Ms = np.sum(M,axis=1)

    st.markdown("The average aggregate Loss is: "+str(np.round(np.mean(Ms),2)))
    st.markdown("The sample aggregate Variance is: "+str(np.round(np.var(Ms),2)))

    fig, ax = plt.subplots()
    sns.histplot(Ms)
    plt.title("Histogram")
    plt.xlabel("Aggregate Loss")
    st.pyplot(fig)
    
    def getdata():
        return pd.DataFrame(M).to_csv(index=False).encode('utf-8')

    st.download_button('Download Simulation', data=getdata(), file_name='Simulation.csv')

