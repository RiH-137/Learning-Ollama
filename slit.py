#Rambot


import requests
import json
import streamlit as st

# Base URL of the API
url = 'http://localhost:11434/api/generate'  # Adjust based on your actual setup
headers = {'Content-Type': 'application/json'}

# Creating an empty list for displaying information
history = []

def generate_response(prompt):
    try:
        # Append the new prompt to the history
        history.append(prompt)
        final_prompt = "\n".join(history)

        # Prepare the data payload for the API request
        data = {
            "model": "Rambot",  # Replace with the actual model name required by the API
            "prompt": final_prompt, 
            "stream": False
        }

        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

        # Check for successful response
        if response.status_code == 200:
            response_data = response.json()
            actual_response = response_data.get('response', "No response field found in the API response.")
            return actual_response
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
