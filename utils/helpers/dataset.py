import json
from datasets import Dataset

with open('faq.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

dataset = Dataset.from_dict({
    "question": [item["question"] for item in data],
    "answer": [item["answer"] for item in data]
})


dataset.save_to_disk("faq_dataset")

print("Dataset saved successfully!")