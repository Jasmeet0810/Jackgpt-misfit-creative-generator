import streamlit as st

# App Config
st.set_page_config(page_title="JackGPT: Misfit Creative Generator", page_icon="🌀")

# Header
st.title("🌀 JackGPT: The Misfit Creative Generator")
st.caption("Choose your alter ego and spark a brand idea like no other.")

# Persona selection
persona = st.selectbox("🎭 Pick a Personality", ["The Dreamer", "The Analyst", "The Rebel"])

# Prompt input
user_prompt = st.text_input("📝 Enter a brand or experience prompt")

# Function to generate ideas based on persona
def generate_idea(persona, prompt):
    if not prompt.strip():
        return "Please enter a valid prompt."

    if persona == "The Dreamer":
        return (
            f"🌙 *Imagine this...*\n\n"
            f"{prompt} becomes a floating daydream. Picture soft clouds, ambient soundscapes, and poetry tucked into coffee sleeves. "
            f"Every moment in this brand is a whisper, not a scream. The café moves, just like your imagination."
        )

    elif persona == "The Analyst":
        return (
            f"📊 *Strategic Overview:*\n\n"
            f"The concept — '{prompt}' — aligns with Q2 behavioral trends showing a 32% spike in demand for mobile, immersive experiences. "
            f"Targeting Gen Z and urban millennials, a moving café combines novelty with 'destinationless' engagement. "
            f"Recommended: geo-targeted influencer collaborations and real-time heatmapping to track footfall-to-carriage conversions."
        )

    elif persona == "The Rebel":
        return (
            f"🔥 *Forget the rules...*\n\n"
            f"'{prompt}'? Perfect. Let’s serve espresso in motion, with punk bands on train platforms and menus printed on vinyl records. "
            f"No reservations, no Wi-Fi, no mercy. Name it 'Off the Rails'—a café for runaways and rebels only."
        )

# Button logic
if st.button("🚀 Generate My Brand Idea"):
    if user_prompt.strip():
        idea = generate_idea(persona, user_prompt)
        st.markdown(f"### 💡 {persona} says:\n\n{idea}")
    else:
        st.warning("⚠️ Please enter a prompt to generate an idea.")
