# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8002/execute" 

# st.title("🩺 Doctor Appointment System")

# user_id = st.text_input("Enter your ID number:", "")
# query = st.text_area("Enter your query:", "Can you check if a dentist is available tomorrow at 10 AM?")

# if st.button("Submit Query"):
#     if user_id and query:
#         try:
#             response = requests.post(API_URL, json={'messages': query, 'id_number': int(user_id)},verify=False)
#             if response.status_code == 200:
#                 st.success("Response Received:")
#                 print("**********my response******************")
#                 print(response.json())
#                 st.write(response.json()["messages"])
#             else:
#                 st.error(f"Error {response.status_code}: Could not process the request.")
#         except Exception as e:
#             st.error(f"Exception occurred: {e}")
#     else:
#         st.warning("Please enter both ID and query.")

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8002/execute"

st.title("🩺 Doctor Appointment System")

user_id = st.text_input("Enter your ID number:", "")
query = st.text_area("Enter your query:", "Can you check if a dentist is available tomorrow at 10 AM?")

if st.button("Submit Query"):
    if not user_id or not query:
        st.warning("Please enter both ID and query.")
    else:
        try:
            # Validate user_id as integer
            user_id_int = int(user_id)
            response = requests.post(
                API_URL,
                json={'messages': query, 'id_number': user_id_int},
                verify=False
            )
            response.raise_for_status()  # Raise exception for non-200 status
            data = response.json()
            
            # Check for 'messages' key
            if "messages" in data:
                st.success("Response Received:")
                st.write(data["messages"])
            else:
                st.error("Invalid response format from server.")
                
        except ValueError:
            st.error("Please enter a valid integer for ID number.")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to server: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")