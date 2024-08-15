import streamlit as st
import pandas as pd
import random
from utils.fetch_news import fetch_articles
from config.config import load_env_vars
import google.generativeai as genai
import time

# Load environment variables
env_vars = load_env_vars()
gemini_api_key = env_vars.get('GEMINI_API_KEY')
news_api_key = env_vars.get('NEWS_API_KEY')

# Initialize the Gemini API
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

# Generate popular categories of news using the Gemini API
categories_response = model.generate_content("List major NEWS categories for a large dataset. Only include one-word answers in response.")
categories_list = categories_response.text.splitlines()

# Fetch news articles
df = pd.DataFrame(fetch_articles(categories_list, news_api_key))

# Assign random ratings
df['Ratings'] = df.apply(lambda row: round(random.uniform(1.0, 5.0), 2), axis=1)

# Streamlit app
st.title("News Recommendation System")

# Dropdown for category selection
category_options = ['All'] + [category.capitalize() for category in categories_list]
user_input = st.selectbox("Select a news category for recommendations:", category_options)

# Button to trigger recommendation
if st.button("Get Recommendations"):
    # Show spinner while processing
    with st.spinner('Generating news recommendations...'):
        # Simulate some delay for demonstration
        time.sleep(1)
        
        # Process recommendation logic
        if user_input.lower() != 'all':
            recommended_news = df[df['Category'].str.lower() == user_input.lower()].sort_values(by='Ratings', ascending=False)
        else:
            recommended_news = df.sort_values(by='Ratings', ascending=False)

        # Display recommended news
        st.subheader("Top Recommended News:")
        for index, row in recommended_news.head(5).iterrows():
            st.write(f"**Title:** {row['Title']}")
            if row['Image']:
                st.image(row['Image'], use_column_width=True)
            st.write(f"**Description:** {row['Description']}")
            st.write(f"**Ratings:** {row['Ratings']}")
            st.write(f"**Source:** {row['Source']}")
            st.write(f"**Author:** {row['Author'] if row['Author'] else 'N/A'}")
            st.write(f"**Category:** {row['Category'].capitalize()}")
            st.write(f"[Read Full Article]({row['URL']})")
            st.write("---")  # Separator between articles
