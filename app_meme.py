import streamlit as st
import requests

# Replace with your actual ngrok URL printed in Colab
API_URL = "https://5fc0-34-143-225-12.ngrok-free.app"  

st.title("Math Meme Repair 🤖")
st.write("Give a math meme, and I'll repair it for you!")

# Example riddles
example_memes = {
    "Select an example meme": "",
    "Meme 1": "According to PEMDAS, 8+2×3=30!",
    "Meme 2": "I divided 9 by 3 and got 6! Math is easy.",
    "Meme 3": "Zero divided by any number is infinity!",
    "Meme 4": "The sum of angles in a triangle is 360 degrees!",
    "Meme 5": "To subtract fractions, just subtract the numerators: 43-21=22=1",
}

selected_example = st.selectbox("Try an example meme:", list(example_memes.keys()))


meme = st.text_area("Enter your math meme:", value=example_memes[selected_example], height=100)

if st.button("Correct Meme"):
    if meme:
        try:
            with st.spinner("Thinking..."):
                response = requests.post(f"{API_URL}/generate", json={"meme": meme})  # Fixed endpoint

                if response.status_code == 200:
                    solution = response.json().get("corrected_meme", "No correction!")
                    st.success("### Correction:")
                    st.write(solution)
                else:
                    st.error(f"API Error: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter a meme first!")
