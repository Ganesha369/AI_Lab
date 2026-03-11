import streamlit as st
import json

# Simulating an API Response
def get_mock_api_data():
    return {
        "status": "success",
        "data": {
            "user_id": 101,
            "username": "CodeMaster_99",
            "subscription": "Premium",
            "preferences": {
                "theme": "Dark Mode",
                "notifications": True
            },
            "recent_activity": ["Login", "Watched 'Inception'", "Updated Profile"]
        }
    }

st.title("📦 API Response Structuring")
st.write("Click the button below to simulate an API call and see how we structure the JSON response.")

if st.button("Fetch API Data"):
    response = get_mock_api_data()
    
    # Section 1: Raw JSON (The "Bento Box")
    st.subheader("1. The Raw JSON Response")
    st.code(json.dumps(response, indent=4), language="json")
    
    st.divider()
    
    # Section 2: How the UI uses that structure
    st.subheader("2. How the App Displays This")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("User", response["data"]["username"])
        st.write(f"**Status:** {response['status'].upper()}")
        
    with col2:
        st.metric("Tier", response["data"]["subscription"])
        st.write(f"**Theme:** {response['data']['preferences']['theme']}")

    st.write("### Recent Activity")
    for activity in response["data"]["recent_activity"]:
        st.write(f"- {activity}")

st.info("💡 Notice how we can access specific parts of the data using keys like `response['data']['username']`. This is why structuring is powerful!")