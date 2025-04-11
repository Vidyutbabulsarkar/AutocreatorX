import streamlit as st

st.set_page_config(page_title="AutoCreatorX", layout="centered")
st.title("AutoCreatorX")
st.subheader("AI-Powered Content-to-Cash Generator")

st.markdown("### Step 1: Choose a Niche")
niche = st.selectbox("Pick a niche:", [
    "Brain Boost Hacks", "Fat Loss Secrets", 
    "Passive Income Ideas", "Spiritual Awakening", 
    "Sarkari Job Scams"
])

st.markdown("### Step 2: One Click to Auto Generate Everything")

if st.button("Start Automation"):
    with st.spinner("Generating..."):
        # Placeholder AI-generated script
        script = f"""
HOOK: Did you know your brain can reprogram itself in 10 seconds?
VALUE: Try 'neuroplastic journaling' daily — it boosts focus, memory & clarity.
CTA: Want more hacks? Check our top tools & supplements here:
Amazon: https://www.amazon.in/dp/B09YH8WGRN?tag=healthboostpr-20
Digistore: https://www.digistore24.com/redir/428393/healthboostpro-20/
"""

        title = f"3 {niche} That Actually Work | AI-Generated Hacks"
        description = f"Boost your {niche.lower()} using science-backed AI tools. Includes affiliate tools for smarter living. #MindFuelByVidyut"

        st.success("Content Generated!")
        st.markdown("### AI Script:")
        st.code(script, language='markdown')

        st.markdown("### YouTube Title:")
        st.write(title)

        st.markdown("### YouTube Description:")
        st.write(description)

        st.markdown("### Affiliate Links Embedded:")
        st.markdown("""
- Amazon Link: [Health Product](https://www.amazon.in/dp/B09YH8WGRN?tag=healthboostpr-20)
- Digistore24 Link: [Digital Brain Hack](https://www.digistore24.com/redir/428393/healthboostpro-20/)
        """)
