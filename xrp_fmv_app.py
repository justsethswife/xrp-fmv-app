import streamlit as st
import pandas as pd

# Function to calculate value based on user input
def calculate_xrp_fmv(xrp_amount):
    data = {
        "Scenario": [
            "Athey & Mitchnick $1Q",
            "Athey & Mitchnick $100T",
            "Athey & Mitchnick $530T",
            "Bakkes Pipeline Flow",
            "Collateralization (100%)",
            "Collateralization (10%)",
            "Discounted Cash Flow 1%",
            "Discounted Cash Flow 2%",
            "Discounted Cash Flow 3%",
            "Golden Eagle 99 Year",
            "Golden Eagle 2030",
            "Quantum Liquidity"
        ],
        "Predicted Value per XRP ($)": [
            908,
            9000,
            4800,
            3500,
            122000,
            15000,
            18000,
            13300,
            21900,
            9.81,
            513,
            61231
        ],
        "Predicted Date and Rationale": [
            "2025-2028: This value is within reach if XRP achieves significant adoption in cross-border payments and if regulatory clarity improves.",
            "2030-2035: This higher valuation assumes more widespread adoption and integration into global financial systems, potentially influenced by major partnerships and technology improvements.",
            "2028-2032: Intermediate adoption and increased use cases for XRP in various financial sectors could drive this value.",
            "2026-2030: Achieving this value would likely require steady growth in transaction volume and continued positive market sentiment.",
            "2045-2050: Full tokenization of global assets is an ambitious goal that would require significant advancements in technology, regulatory approval, and global adoption.",
            "2035-2040: Tokenizing 10% of global assets is more feasible and could be driven by increased trust in blockchain technology and regulatory support.",
            "2032-2038: This valuation relies on significant transaction utility and sustained economic growth, achievable with steady adoption.",
            "2030-2035: Slightly more conservative, but achievable with strong market participation and technological integration.",
            "2035-2040: High adoption rates and transaction volume increases would drive this valuation.",
            "2120: This is a long-term projection, assuming XRP maintains value over a century.",
            "By 2030: Moderate growth driven by gradual adoption and improved market sentiment.",
            "2040-2045: This high valuation assumes significant global adoption and extensive liquidity requirements, feasible with major technological and regulatory breakthroughs."
        ]
    }
    
    # Calculate the value of the given amount of XRP
    df = pd.DataFrame(data)
    df["Predicted Value per XRP ($)"] = df["Predicted Value per XRP ($)"].apply(lambda x: "${:,.2f}".format(x))
    df["Value of your XRP holdings ($)"] = df["Predicted Value per XRP ($)"].apply(lambda x: float(x.replace('$','').replace(',','')) * xrp_amount)
    df["Value of your XRP holdings ($)"] = df["Value of your XRP holdings ($)"].apply(lambda x: "${:,.2f}".format(x))
    
    return df

# Streamlit app
st.title("XRP Fair Market Value Calculator")

xrp_amount = st.number_input("Enter the amount of XRP you hold:", min_value=1, value=100)

if st.button("Calculate"):
    df = calculate_xrp_fmv(xrp_amount)
    st.write(df.style.set_properties(**{'text-align': 'left'}).set_table_styles({
        'Predicted Date and Rationale': [
            {'selector': 'td', 'props': 'text-align: left; white-space: pre-wrap;'}
        ]
    }))
