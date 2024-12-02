import streamlit as st
import yfinance as yf

st.title('Hedging Transition Risks')

st.write("""
We propose 
an approach to building climate transition risks hedge portfolios using publicly traded assets. 
In this approach, rather than buying a security that directly pays off in the event of a future abrupt shift towards 
a low-carbon economy, one can construct portfolios whose short-term returns hedge news about transition. 
These surprises can be, for example, a text mining index designed to proxy for the arrival of transition risks 
information in financial markets (Apel et al., 2023). The purpose of the approach is to provide 
a methodology for constructing portfolios 
that use relatively easy-to-trade (equities) to hedge against risks that are otherwise difficult to insure. 
         
We can use this investable tool in combination with an initial portfolio to form a new portfolio, hedged against transition risks, 
and with improved risk-return profile.
""")



etfs = {
    "IWRD.L": "iShares MSCI World UCITS ETF",
    "SPY" : "SPDR S&P 500 ETF Trust",
        "EEM" : "iShares MSCI Emerging Markets ETF",
        "IWM" : "iShares Russell 2000 ETF"
}

list_tickers = list(etfs.values())

name_etf = st.sidebar.selectbox('Select ETF', list_tickers)

# find the corresponding key
ticker = [key for key, value in etfs.items() if value == name_etf][0]

prices = (yf.download(
    tickers=ticker, 
    progress=False
  )
  .reset_index()
  .assign(name = lambda x: name_etf)
  .rename(columns={
      "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Adj Close": "adjusted",
    "Volume": "volume"
  })
  )

st.write(prices)

st.write("""
### Measure of Transition Risks
         
We use the Transition Risks Index (TRI) innovations from Apel et al. (2023) to measure the arrival of news related to transition risks.
the TRI serves as a valuable proxy for the arrival of news related to transition risks, 
capturing moments when investors may update their subjective probabilities 
regarding climate-related uncertainties. 
Its ability to reflect shifts in sentiment and key policy announcements makes it an effective tool for analyzing how 
market participants react to new information about climate commitments and their implications for economic activities.
         """)

st.write("""
### Green Assets to form a Hedging Portfolio

Apel et al. (2023) confirmed empirically our findings that the revenue component is the most significant source of transition risks.

Apel et al. (2023) distinguish between two different construction approaches for available
green investment: (i) decarbonized portfolios and (ii) pure-play approaches.
Decarbonized portfolios typically reduce carbon exposure while preserving diversification by exclusion 
         or reweighting constituents on emissions relative to a financial metric.
Pure-play approaches, on the other hand, focus on companies that derive a significant portion of their
            revenue from products and services related to the transition to a low-carbon economy.
They analyzed the return sensitivity of those portfolios to climate transition risks, without **a priori** assumptions 
about the "right" approach to determine the "green credentials" of firm characteristics. 
The objective was to seek clarification of which type of climate investment approaches provide exposure to the risk 
and opportunities associated with the transition to a low-carbon economy. 
Investors who want to hedge transition risks will want portfolios that perform well if the public demand to confront
the adverse effects of climate change increases.
The authors' results show that the short-term transition
risk tends to affect the returns of the portfolios of stocks based on the business activity of the firms but not the emissions. 
We will therefore restrict
our basis assets to green-play indices.
            """)

st.markdown("""
<table>
    <caption>Index description.</caption>
    <thead>
        <tr>
            <th>Name</th>
            <th>Benchmark</th>
            <th>History</th>
            <th>Rationale</th>
        </tr>
    </thead>
    <tbody>
        <tr><td colspan="4"><strong>Pure-play indices</strong></td></tr>
        <tr>
            <td>MSCI Global Environment Index</td>
            <td>MSCI ACWI IMI</td>
            <td>Nov 08</td>
            <td>Comprised of companies that derive at least 50% of their revenues from environmentally beneficial products and services. Constituent selection is based on data from MSCI ESG Research.</td>
        </tr>
        <tr>
            <td>MSCI Global Alt. Energy Index</td>
            <td>MSCI ACWI IMI</td>
            <td>Jan 09</td>
            <td>Thematic sub-index of the MSCI Global Environment Index and includes companies that derive 50% or more of their revenues from products and services in Alternative Energy.</td>
        </tr>
        <tr>
            <td>S&amp;P Global Clean Energy Index</td>
            <td>S&amp;P Global BMI</td>
            <td>Nov 03</td>
            <td>Index inclusion is based on factors like company’s business description and most recent reported revenue by segment. Companies which exceed a certain carbon emissions threshold are excluded.</td>
        </tr>
        <tr>
            <td>Solactive Climate Change Index</td>
            <td>Solactive GBS LMC</td>
            <td>Nov 05</td>
            <td>Includes 30 largest companies active in sectors like solar and wind energy. Companies are classified according to the percentage of total revenues associated with activities that generate CO₂ avoidance.</td>
        </tr>
        <tr>
            <td>FTSE EO Renewable and Alt. Energy Index</td>
            <td>FTSE Global All Cap</td>
            <td>Nov 08</td>
            <td>Environmental Opportunities (EO) Index requires companies to have at least 20% of their revenues derived from significant involvement in business activities related to Renewable &amp; Alternative Energy.</td>
        </tr>
        <tr>
            <td>FTSE Environmental Technology Index</td>
            <td>FTSE Global All Cap</td>
            <td>Oct 03</td>
            <td>Constituents are required to have at least 50% of their business derived from environmental markets &amp; technologies as defined by FTSE EMCS. Longest-running environmental technology index available.</td>
        </tr>
    </tbody>
</table>
<p style="text-align: right; font-style: italic; font-size: 0.9em;">Source: Apel et al. (2023)</p>
""", unsafe_allow_html=True)

st.write("""
### Methods
         
We use the hedging portfolio in combination with the initial portfolio to form a new portfolio, hedged against transition risks.
         
This implies to:
1. Offer an investable tool to hedge for transition risks
2. Provides a methodology to combine the hedging portfolio with the initial portfolio of the investor
         
         """)

st.write("""
### Main Result
         
In period of high negative exposure of the initial portfolio to transition risks, the hedged portfolio 
offers a substantial improvement in the risk-return profile.
            
            """)
