#Roaster_Monkey

import requests
import json
import streamlit as st

# Base URL of the API
url = 'http://localhost:11434/api/generate'  # Adjust as needed
headers = {'Content-Type': 'application/json'}

# Initialize prompt history
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "Roaster_Monkey",  # Adjust based on your API requirements
        "prompt": final_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get('response', "No response found.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except json.JSONDecodeError:
        return "Error: Unable to parse the response as JSON."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Streamlit app layout
st.title("AI Response Generator")

prompt = st.text_input("Enter prompt")

if st.button("Generate Response"):
    if prompt:
        response = generate_response(prompt)
        st.write(response)
    else:
        st.write("Please enter a prompt.")
