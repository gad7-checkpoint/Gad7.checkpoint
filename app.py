import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Well-Being Checkpoint", layout="centered", initial_sidebar_state="collapsed")

# 2. Custom CSS for a clean, mobile-friendly interface
st.markdown("""
    <style>
    /* Calming background */
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Styling the large, touch-friendly answer buttons */
    div.stButton > button {
        background-color: #FFFFFF;
        color: #2C3E50;
        border: 2px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px 24px;
        font-size: 18px;
        font-weight: 500;
        width: 100%;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 10px;
    }
    
    /* Hover/Tap state for visual feedback */
    div.stButton > button:hover {
        border-color: #008080; /* Teal accent */
        color: #008080;
        box-shadow: 0 10px 15px -3px rgba(0, 128, 128, 0.1);
    }
    
    /* Adjust top padding for mobile screens */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Center the main text */
    .center-text {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Define the GAD-7 Questions and Scoring
questions = [
    "Feeling nervous, anxious or on edge?",
    "Not being able to stop or control worrying?",
    "Worrying too much about different things?",
    "Trouble relaxing?",
    "Being so restless that it is hard to sit still?",
    "Becoming easily annoyed or irritable?",
    "Feeling afraid as if something awful might happen?"
]

options = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3
}

# 4. Initialize Session State (Memory for the app)
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
    st.session_state.total_score = 0

# Helper function to record score and move to the next card
def record_answer(score_value):
    st.session_state.total_score += score_value
    st.session_state.current_step += 1

def reset_game():
    st.session_state.current_step = 0
    st.session_state.total_score = 0

# 5. Main UI Logic
step = st.session_state.current_step

# State A: Showing Questions (Cards 1 to 7)
if step < len(questions):
    st.markdown("<h2 class='center-text'>Mental Health Checkpoint</h2>", unsafe_allow_html=True)
    
    # Progress bar
    st.progress((step) / len(questions))
    st.caption(f"Question {step + 1} of {len(questions)}")
    
    st.write("Over the past 2 weeks, how often have you been bothered by:")
    st.subheader(questions[step])
    st.write("---")
    
    # Generate buttons for each option. Clicking one triggers the record_answer function.
    for text, value in options.items():
        st.button(text, on_click=record_answer, args=(value,), key=f"q{step}_{value}")

# State B: The Results Dashboard (After question 7)
else:
    score = st.session_state.total_score
    st.markdown("<h1 class='center-text'>Your Results</h1>", unsafe_allow_html=True)
    
    # Display the final score large and centered
    st.metric(label="Total GAD-7 Score", value=score)
    st.write("---")
    
    # Categorize the result based on clinical thresholds
    if score <= 4:
        st.success("### Minimal Anxiety\nYour score suggests minimal anxiety symptoms. Keep prioritizing your daily well-being and self-care routines!")
    elif score <= 9:
        st.warning("### Mild Anxiety\nYour score suggests mild anxiety. Consider reviewing our brochure for helpful stress management and breathing techniques.")
    elif score <= 14:
        st.error("### Moderate Anxiety\nYour score indicates moderate anxiety symptoms that may be impacting your day. We recommend exploring the support resources and counseling information at our booth.")
    else:
        st.error("### Severe Anxiety\nYour score indicates severe anxiety symptoms. We strongly recommend reaching out to a healthcare professional or campus counseling services for support.")
        
    st.write("---")
    st.caption("**Disclaimer:** This tool is for educational and awareness purposes only. It is a screening tool, not a clinical diagnosis. Please consult a qualified mental health professional for an accurate assessment.")
    
    st.write("") # Spacer
    
    # Button to reset for the next TA
    st.button("Start Over for Next Person", on_click=reset_game, type="primary", use_container_width=True)