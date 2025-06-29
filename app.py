import streamlit as st

def generate_idea(persona, prompt):
    if persona == "The Dreamer":
        return f"🌙 Imagine this... {prompt} becomes a dreamworld where clouds whisper brand messages."
    elif persona == "The Analyst":
        return f"📊 Statistically, '{prompt}' fits Q2 consumer behavior trends. Launch with targeting precision."
    elif persona == "The Rebel":
        return f"🔥 Oh please. '{prompt}'? Make it chaotic. Make it unforgettable. Break every rule."

st.set_page_config(page_title="JackGPT", page_icon="🌀")

st.title("🌀 JackGPT: The Misfit Creative Generator")
st.subheader("Choose your alter ego and spark a brand idea like no other.")

persona = st.selectbox("🎭 Pick a Personality", ["The Dreamer", "The Analyst", "The Rebel"])
user_prompt = st.text_input("📝 Enter a brand or experience prompt")

if st.button("Generate Idea"):
    if user_prompt.strip():
        idea = generate_idea(persona, user_prompt)
        st.markdown(f"### 💡 {persona} says:\n> {idea}")
    else:
        st.warning("Please enter a prompt to generate an idea.")
