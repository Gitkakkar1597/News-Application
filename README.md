# News Recommendation App

## Overview

The **News Recommendation App** is a web application built with Python and Streamlit that provides personalized news recommendations. It utilizes the `News API` to fetch current news articles and `Gemini AI` LLM API to generate recommendations based on the articles. This application offers a clean and interactive interface for users to discover top-rated news articles across various categories.

## Features

- **Dynamic News Fetching**: Retrieves the latest news articles based on user-selected categories.
- **AI-Powered Recommendations**: Uses Gemini AI to generate recommendations based on article data.
- **User Interface**: Displays news articles in a visually appealing format with ratings and source information.
- **Loading Spinner**: Shows a spinner while news articles are being fetched to enhance user experience.

## Tech Stack

- **Python**: Programming language used for backend logic.
- **Streamlit**: Framework for building the web application interface.
- **News API**: Provides news articles from various sources.
- **Gemini AI**: Used for generating recommendations based on news data.
- **Pandas**: Data manipulation and analysis library.

## Project Structure

```arduino
news-recommendation-app/
│
├── .env                  # Environment variables file
├── .gitignore             # Git ignore file
├── README.md             # Project overview and setup instructions
├── requirements.txt      # Project dependencies
├── app.py                # Main Streamlit application script
│
├── config/
│   ├── config.py         # Script to load environment variables
│
└── utils/
    └── fetch_news.py     # Script to fetch news articles from the News API
│
└── assets/
    └── Screenshot.png    # Screenshot or other static assets
```

## Working

- **Screenshot**
  ![NEWS App](assets/Screenshot.png)

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Gitkakkar1597/News-Application.git
   cd news-recommender
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   NEWS_API_KEY=your_news_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501` to access the application.
2. Enter a category in the text input field or type 'all' to get recommendations from all categories.
3. Click the "Get Recommendations" button to fetch and display the top recommended news articles.
4. Use the loading spinner for a smooth user experience while news articles are being fetched.

## Contributing

Contributions to the project are welcome! If you would like to contribute, please follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top right of this repository.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/Gitkakkar1597/News-Application.git
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make Changes**: Implement your changes or new features.
5. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Add a descriptive commit message"
   git push origin feature/your-feature
   ```
6. **Create a Pull Request**: Go to the original repository and create a pull request with a clear description of your changes.
