# app.py
from fetch_news import fetch_news
from summarize import summarize_headlines
import gradio as gr
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read from environment variables
api_key = os.getenv("NEWS_API_KEY")
api_key2 = os.getenv("OPENAI_API_KEY")
def summarize_news_for_topic(topic):
    headlines = fetch_news(topic, api_key)
    summarize = summarize_headlines(headlines, api_key2)
    return summarize 
demo = gr.Interface(
    fn=summarize_news_for_topic,
    inputs=gr.Textbox(label="Enter a news topic"),
    outputs=gr.Textbox(label="Summary"),
    title="📰 Real-Time News Summarizer",
    description="Enter any topic and get a GPT-generated summary of live headlines."
)
demo.launch()
