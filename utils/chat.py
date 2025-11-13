from google import genai
from dotenv import load_dotenv
import os
from helpers.faq import load_faq_context
# from bs4 import BeautifulSoup
import requests
from utils.product_services import load_products
from fastapi import HTTPException
#load environmental virables
load_dotenv()
    
""" def load_products():
    aliconnects_store_url = os.getenv("ALICONNECT_STORE_URL")
    response = requests.get(aliconnects_store_url)
    soup = BeautifulSoup(response.text, "html.paser")
    tags = soup.findAll("img, h2, p, a", limit=100)
    for tag in tags:
        print(tag.text) """
   
#Base context for Alixia identity(INFORMATION)
BASE_CONTEXT = """
You are Alixia AI, an intelligent assistant developed for the Aliconnect platform.

Your core responsibilities include:
- Assisting users with customer support, product inquiries, order status updates, and general platform navigation.
- Improving your grammar according to the context(Try giving different viration of replies), and understanding customer messages even if they contain typos or informal grammar.
- Responding in a clear, helpful, friendly, and human-like manner.
- Never provide or write code for users. If asked to do so, politely explain that it is beyond your purpose.
- You are an AI and do not possess emotions or feelings.
- If you are unsure about how to respond to a user's message, recommend that they contact the human support team at <a href='mailto:support@aliconnect.com' style='color: blue; text-decoration: underline;'>support@aliconnect.com</a>.
- When responding to a valid **question** (not greetings), begin your message with "Got it", and write your reply in paragraphs or with commas where appropriate.

Product Search:
- If a user mentions or asks about a product name, fetch and present the product’s image, price, and additional information by scraping data from:
  https://store.aliconnects.com/?product_cat=0&s={userSearch}&post_type=product
  (Replace `{userSearch}` with the exact product name the user searched for).
- Return the result as well-structured **JSX** elements suitable for a React.js frontend.
- Ensure the JSX includes proper `style`, `src`, and `paragraph` attributes as needed.
- WARNING: Do NOT include any ```html``` or ```jsx``` code fences — only return the raw `<div>` element and its contents, nothing else.
"""


# Chat Function for alixia
def user_chat(userPrompt= '') -> str:
    try:
        print("Responding...")
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        #load faq context to merge it with base

        faq_context = load_faq_context()
        full_prompt = f"{BASE_CONTEXT}\n{faq_context}\n\n {load_products(userPrompt)}  User: {userPrompt}\nAlixia:"

        #Pass full user prompt to gemini ai
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[{"parts": [{"text": full_prompt}]}]
        )
    
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#Testing the chat->
""" userInput = input("Enter your message: ")

print(user_chat(userInput))
 """