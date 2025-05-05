# Core Requirements:
# Interactivity: Allow users to upload or input data, adjust parameters, and explore results.
# Functionality: Implement meaningful data processing, analysis, or visualization routines.
# Usability: Provide clear UI controls, handle errors gracefully, and document user inputs.
# Deployment: Publish your app on Streamlit Community CloudLinks to an external site. and ensure it runs without errors

#  streamlit run /Users/brynnwilary/Desktop/WILARY-PYTHON-PORTFOLIO/StreamlitAppFinal/main.py

#IMPORT NECESSARY PROGRAMS
#import pandas
import pandas as pd
#import streamlit
import streamlit as st
#import spacy and displacy from spacy
import spacy
from spacy import displacy
#set up nlp
from spacy.cli import download
download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
import numpy as np
import pydeck as pdk


#read sp500 data
sp500 = pd.read_csv('StreamlitAppFinal/sp500_companies.csv')

#put sp500 in a data frame
df_sp500 = pd.DataFrame(sp500)

#FUNCTION BANK
#writes a summary for the diff categories
def investment_summary(symbol, market_price, market_cap, ebitda, rev_growth,
                       median_market_price, median_market_cap, median_ebitda, median_rev_growth, market):
    
    summary = f"Here's an investment summary for {symbol} based on the {market}:\n\n"

    # stock price
    if market_price > median_market_price:
        summary += f"- The current stock price (\${round(market_price, 2)}) is **above** the {market} median (\${round(median_market_price, 2)}), suggesting it may be relatively expensive.\n"
    else:
        summary += f"- The current stock price (\${round(market_price, 2)}) is **below** the {market} median (\${round(median_market_price, 2)}), suggesting potential undervaluation.\n"

    # market cap
    if market_cap > median_market_cap:
        summary += f"- The market cap (\${int(market_cap):,}) is **above** the {market} median (\${int(median_market_cap):,}), indicating a larger, potentially more stable company.\n"
    else:
        summary += f"- The market cap (\${int(market_cap):,}) is **below** the {market} median (\${int(median_market_cap):,}), which could imply higher risk or growth potential.\n"

    # ebitda
    if ebitda > median_ebitda:
        summary += f"- The EBITDA (\${int(ebitda):,}) is **above** the {market} median (\${int(median_ebitda):,}), indicating strong earnings performance.\n"
    else:
        summary += f"- The EBITDA (\${int(ebitda):,}) is **below** the {market} median (\${int(median_ebitda):,}), suggesting weaker earnings performance.\n"

    # revenue growth
    if rev_growth > median_rev_growth:
        summary += f"- The revenue growth rate ({round(rev_growth, 2)}%) is **above** the {market} median ({round(median_rev_growth, 2)}%), showing strong sales momentum.\n"
    else:
        summary += f"- The revenue growth rate ({round(rev_growth, 2)}%) is **below** the {market} median ({round(median_rev_growth, 2)}%), which may indicate stagnation.\n"

    # summary interpretation
    score = sum([
        market_price < median_market_price,
        market_cap > median_market_cap,
        ebitda > median_ebitda,
        rev_growth > median_rev_growth
    ])
    
    if score >= 3:
        summary += f"\nOverall, this stock appears favorable compared to {market} medians."
    elif score == 2:
        summary += f"\nThis stock shows a mixed performance relative to the {market}."
    else:
        summary += f"\nThis stock underperforms in key metrics and may require caution compared to the {market}."

    return summary


# create empty lists
symbol = []
company_name = []

#calculate market averages
#market prices
mean_market_price = df_sp500["Currentprice"].mean()
median_market_price = df_sp500["Currentprice"].median()
#marketcap
mean_market_cap = df_sp500["Marketcap"].mean()
median_market_cap = df_sp500["Marketcap"].median()
#ebitda
mean_ebitda = df_sp500["Ebitda"].mean()
median_ebitda = df_sp500["Ebitda"].median()
#rev growth
mean_rev_growth = df_sp500["Revenuegrowth"].mean()
median_rev_growth = df_sp500["Revenuegrowth"].median()

#goes through the dataframe and relabel it to label and pattern for symbol
for x in df_sp500["Symbol"]:
    symbol.append({"label":"Symbol", "pattern":x})

#goes through the dataframe and relabel it to label and pattern for company name
for x in df_sp500["Shortname"]:
    company_name.append({"label":"Name", "pattern":x})

#goes through the dataframe and relabel it to label and pattern for industry name
for x in df_sp500["Exchange"]:
    company_name.append({"label":"Exchange", "pattern":x})

#goes through the dataframe and relabel it to label and pattern for exchange name
for x in df_sp500["Industry"]:
    company_name.append({"label":"Industry", "pattern":x})

#goes through the dataframe and relabel it to label and pattern for sector name
for x in df_sp500["Sector"]:
    company_name.append({"label":"Sector", "pattern":x})


#make sure there isn't an error in putting in ruler
if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
    try:
        ruler = nlp.get_pipe("entity_ruler")
    except Exception:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(symbol)
else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(symbol)
    ner = nlp.add_pipe("ner")

#formatting text
st.title("Stock Analysis App")
st.write("Enter in the stock symbol you want to analyze: ")

#user input
symbol = st.text_input("").upper()
if symbol:
    row = df_sp500[df_sp500['Symbol'] == symbol]

    if not row.empty:
        row = row.iloc[0]
        name = row["Shortname"]
        exchange = row["Exchange"]
        industry = row["Industry"]
        sector = row["Sector"]
        market_cap = row["Marketcap"]
        ebitda = row["Ebitda"]
        market_price = row["Currentprice"]
        rev_growth = row["Revenuegrowth"]

        st.subheader(f"Company Overview for {symbol}")
        st.write(f"**Name:** {name}")
        st.write(f"**Exchange:** {exchange}")
        st.write(f"**Industry:** {industry}")
        st.write(f"**Sector:** {sector}")
        st.write(f"**Market Cap:** ${int(market_cap):,}")
        st.write(f"**EBITDA:** ${int(ebitda):,}")

        st.header("Additional Data Analysis")
        st.subheader("Click the button again to hide the additional information!")
        #initialize toggle state for graphs
        if "show_comparison_charts" not in st.session_state:
            st.session_state.show_comparison_charts = False

        #button to toggle chart visibility
        if st.button("Stock to Market Metrics"):
            st.session_state.show_comparison_charts = not st.session_state.show_comparison_charts

        #if toggle is on, display charts
        if st.session_state.show_comparison_charts:
            #market summary
            summary = investment_summary(symbol, market_price, market_cap, ebitda, rev_growth,
                       median_market_price, median_market_cap, median_ebitda, median_rev_growth, "market")
            st.markdown(summary)
                
            #stock price data       
            st.write("**Stock Price**")
            stock_price_data = {f'{symbol} Current Stock Price': [market_price], 'Mean Market Price': [mean_market_price], 'Median Market Price':[median_market_price]}
            st.bar_chart(stock_price_data, stack=False, y_label= "USD($)", x_label = "Stock Prices")
            
            #market cap data
            st.write("**Market Capitalization**")
            market_cap_data = {f'{symbol} Market Cap': [market_cap], 'Mean Market Cap': [mean_market_cap], 'Median Market Cap':[median_market_cap]}
            st.bar_chart(market_cap_data, stack=False, y_label= "USD($)", x_label = "Market Cap")
        
            #ebitda  data
            st.write("**EBITDA**")
            ebitda_data = {f'{symbol} EBITDA': [ebitda], 'Mean EBITDA': [mean_ebitda], 'Median EBITDA':[median_ebitda]}
            st.bar_chart(ebitda_data, stack=False, y_label= "USD($)", x_label = "EBITDA")

            #rev growth data
            st.write("**Revenue Growth**")
            rev_growth_data = {f'{symbol} Revenue Growth': [rev_growth], 'Mean Revenue Growth': [mean_rev_growth], 'Median Revenue Growth':[median_rev_growth]}
            st.bar_chart(rev_growth_data, stack=False, y_label= "%", x_label = "Revenue Growth")
        
        #INDUSTRY AVERAGES
        #initialize toggle state for graphs
        if "show_industry_charts" not in st.session_state:
            st.session_state.show_industry_charts = False

        #button to toggle chart visibility
        if st.button("Stock to Sector Metrics"):
            st.session_state.show_industry_charts = not st.session_state.show_industry_charts

        #if toggle is on, display charts
        if st.session_state.show_industry_charts:
            #stock price chart
            industry_df = df_sp500[df_sp500["Sector"] == sector]
            
            # calculate industry-specific averages and medians
            st.write(f"Sector: '{sector}'")
            mean_industry_price = industry_df["Currentprice"].mean()
            median_industry_price = industry_df["Currentprice"].median()
            

            mean_industry_cap = industry_df["Marketcap"].mean()
            median_industry_cap = industry_df["Marketcap"].median()

            mean_industry_ebitda = industry_df["Ebitda"].mean()
            median_industry_ebitda = industry_df["Ebitda"].median()

            mean_industry_rev_growth = industry_df["Revenuegrowth"].mean()
            median_industry_rev_growth = industry_df["Revenuegrowth"].median()

            #summary industry
            industry_summary = investment_summary(symbol, market_price, market_cap, ebitda, rev_growth,
                       median_industry_price, median_industry_cap, median_industry_ebitda, median_industry_rev_growth, "sector")
            st.markdown(industry_summary)
            
            # visualize industry-specific comparisons

            # stock price comparison
            st.write("**Stock Price Compared to Sector**")
            stock_price_industry_data = {f'{symbol} Current Stock Price': [market_price], 'Mean Sector Price': [mean_industry_price], 'Median Sector Price':[median_industry_price]}
            st.bar_chart(stock_price_industry_data, stack=False, y_label= "USD($)", x_label = "Stock Prices")
           
            # market cap comparison
            st.write("**Market Capitalization Compared to Sector**")
            market_cap_industry_data = {f'{symbol} Market Cap': [market_cap], 'Mean Sector Market Cap': [mean_industry_cap], 'Median Sector Market Cap':[median_industry_cap]}
            st.bar_chart(market_cap_industry_data, stack=False, y_label= "USD($)", x_label = "Market Cap")
        
            # ebitda comparison
            st.write("**EBITDA Compared to Sector**")
            ebitda_industry_data = {f'{symbol} EBITDA': [ebitda], 'Mean Sector EBITDA': [mean_industry_ebitda], 'Median Sector EBITDA':[median_industry_ebitda]}
            st.bar_chart(ebitda_industry_data, stack=False, y_label= "USD($)", x_label = "EBITDA")

            # revenue growth comparison
            st.write("**Revenue Growth Compared to Sector**")
            rev_growth_industry_data = {f'{symbol} Revenue Growth': [rev_growth], 'Mean Sector Revenue Growth': [mean_industry_rev_growth], 'Median Sector Revenue Growth':[median_industry_rev_growth]}
            st.bar_chart(rev_growth_industry_data, stack=False, y_label= "%", x_label = "Revenue Growth")
        
        #EXCHANGE AVERAGES
        #initialize toggle state for graphs
        if "show_exchange_charts" not in st.session_state:
            st.session_state.show_exchange_charts = False

        #button to toggle chart visibility
        if st.button("Stock to Exchange Metrics"):
            st.session_state.show_exchange_charts = not st.session_state.show_exchange_charts

        #if toggle is on, display charts
        if st.session_state.show_exchange_charts:
            #stock price chart
            exchange_df = df_sp500[df_sp500["Exchange"] == exchange]
            
            # calculate industry-specific averages and medians
            st.write(f"Exchange: '{exchange}'")
            mean_exchange_price = exchange_df["Currentprice"].mean()
            median_exchange_price = exchange_df["Currentprice"].median()
            

            mean_exchange_cap = exchange_df["Marketcap"].mean()
            median_exchange_cap = exchange_df["Marketcap"].median()

            mean_exchange_ebitda = exchange_df["Ebitda"].mean()
            median_exchange_ebitda = exchange_df["Ebitda"].median()

            mean_exchange_rev_growth = exchange_df["Revenuegrowth"].mean()
            median_exchange_rev_growth = exchange_df["Revenuegrowth"].median()

            #summary industry
            exchange_summary = investment_summary(symbol, market_price, market_cap, ebitda, rev_growth,
                       median_exchange_price, median_exchange_cap, median_exchange_ebitda, median_exchange_rev_growth, "exchange")
            st.markdown(exchange_summary)
            
            # visualize industry-specific comparisons

            # stock price comparison
            st.write("**Stock Price Compared to Exchange**")
            stock_price_exchange_data = {f'{symbol} Current Stock Price': [market_price], 'Mean Exchange Price': [mean_exchange_price], 'Median Exchange Price':[median_exchange_price]}
            st.bar_chart(stock_price_exchange_data, stack=False, y_label= "USD($)", x_label = "Stock Prices")
           
            # market cap comparison
            st.write("**Market Capitalization Compared to Exchange**")
            market_cap_exchange_data = {f'{symbol} Market Cap': [market_cap], 'Mean Exchange Market Cap': [mean_exchange_cap], 'Median Exchange Market Cap':[median_exchange_cap]}
            st.bar_chart(market_cap_exchange_data, stack=False, y_label= "USD($)", x_label = "Market Cap")
        
            # ebitda comparison
            st.write("**EBITDA Compared to Exchange**")
            ebitda_exchange_data = {f'{symbol} EBITDA': [ebitda], 'Mean Exchange EBITDA': [mean_exchange_ebitda], 'Median Exchange EBITDA':[median_exchange_ebitda]}
            st.bar_chart(ebitda_exchange_data, stack=False, y_label= "USD($)", x_label = "EBITDA")

            # revenue growth comparison
            st.write("**Revenue Growth Compared to Exchange**")
            rev_growth_exchange_data = {f'{symbol} Revenue Growth': [rev_growth], 'Mean Exchange Revenue Growth': [mean_exchange_rev_growth], 'Median Exchange Revenue Growth':[median_exchange_rev_growth]}
            st.bar_chart(rev_growth_exchange_data, stack=False, y_label= "%", x_label = "Revenue Growth")
        


        #extra info
        #initialize toggle state 
        if "show_extra" not in st.session_state:
            st.session_state.show_extra = False

        #button to toggle chart visibility
        if st.button("Company Deep Dive"):
            st.session_state.show_extra = not st.session_state.show_extra

        #if toggle is on, display charts
        if st.session_state.show_extra:
            # Get the selected company from the S&P 500 dataset
            company = df_sp500[df_sp500["Symbol"] == symbol].iloc[0]

            # display long business summary
            st.write("**Company Information Summary**")
            with st.expander("Business Description"):
                st.markdown(company["Longbusinesssummary"])

            # key metrics calculations
            revenue_growth = company["Revenuegrowth"]
            ebitda_margin = company["Ebitda"] / company["Marketcap"] if company["Marketcap"] else "N/A"
            ebitda_per_employee = company["Ebitda"] / company["Fulltimeemployees"] if company["Fulltimeemployees"] else "N/A"

            st.write("**Key Metrics**")
            st.metric("Current Price", f"${company['Currentprice']:,.2f}")
            st.metric("Market Cap", f"${company['Marketcap']:,}")
            st.metric("EBITDA Margin", f"{ebitda_margin:.2%}" if not np.isnan(ebitda_margin) else "N/A")
            st.metric("Revenue Growth", f"{revenue_growth:.2%}")
            st.metric("EBITDA per Employee", f"${ebitda_per_employee:,.0f}" if not np.isnan(ebitda_per_employee) else "N/A")

            # sector comparison
            st.write("**Sector Comparison**")
            sector_df = df_sp500[df_sp500["Sector"] == company["Sector"]]

            comparison_data = pd.DataFrame({
                'Metric': ['Price', 'Market Cap', 'EBITDA', 'Revenue Growth'],
                f'{company["Symbol"]}': [
                    company["Currentprice"],
                    company["Marketcap"],
                    company["Ebitda"],
                    company["Revenuegrowth"]
                ],
                'Sector Median': [
                    sector_df["Currentprice"].median(),
                    sector_df["Marketcap"].median(),
                    sector_df["Ebitda"].median(),
                    sector_df["Revenuegrowth"].median()
                ]
            })

            st.dataframe(comparison_data)

            #radar chart
            try:
                import plotly.express as px
                radar_data = comparison_data.melt(id_vars='Metric', var_name='Entity', value_name='Value')
                fig = px.line_polar(radar_data, r='Value', theta='Metric', color='Entity', line_close=True)
                st.plotly_chart(fig)
            except:
                st.warning("Radar chart requires Plotly. Install it with `pip install plotly` if you haven't already.")

            # comp table
            st.subheader("Company Comparison with Sector")
            top_peers = sector_df.sort_values(by="Marketcap", ascending=False).head(5)
            st.dataframe(top_peers[["Symbol", "Shortname", "Currentprice", "Marketcap", "Ebitda", "Revenuegrowth"]])
            
    else:
        st.warning("symbol not found. please try another.")



