from google import genai
from dotenv import load_dotenv
import os
from utils.helpers.faq import load_faq_context
from  utils.helpers.getResponsibilities import getResponsibilities
# from bs4 import BeautifulSoup
# import requests
from utils.product_services import load_products
from fastapi import HTTPException
#load environmental virables
load_dotenv()


async def Alixia_Chat(userPrompt='') -> str:
    try:
        print("Responding...")
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        BASE_CONTEXT = getResponsibilities()
        faq_context = load_faq_context()

        # Only load products when user is shopping-related
        product_html = ""
        if any(x in userPrompt.lower() for x in ["buy", "product", "price", "shop", "store", "get me"]):
            product_html = load_products(userPrompt)

        full_prompt = (
            f"{BASE_CONTEXT}\n"
            f"{faq_context}\n"
            f"{product_html}\n\n"
            f"User: {userPrompt}\nAlixia:"
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )

        return response.text

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#Testing the chat->
""" userInput = input("Enter your message: ")

print(user_chat(userInput))
 """