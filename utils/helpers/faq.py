import json

def load_faq_context(json_file_path="faq_context.json"):
    try:
        with open(json_file_path, "r") as file:
            faq_list = json.load(file)
            faq_context = "\n".join(
                [f"Q: {item['question']} \nA: {item['answer']}" for item in faq_list]
            )
            return faq_context
    except Exception as e:
        return (f"Error loading FAQ context: {e}")