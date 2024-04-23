import openai
import os

openai.api_key =  os.environ.get("OPENAI_API_KEY")

model="gpt-3.5-turbo"

client = openai.OpenAI()

def get_results(prompt, model=model):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

csv_file_path = './Source_Files/sales.csv'

with open(csv_file_path, 'r') as file:
    csv_text = file.read()

text = f"""
{csv_text}
"""
prompt = f"""
Could you summarize important information for each store in 3 bullet points from sales data presented between triple backticks \
```{text}```
"""

response = get_results(prompt)

print(response)






