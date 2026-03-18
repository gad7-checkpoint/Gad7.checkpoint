import streamlit as st

# 1. Page Configuration for mobile view
st.set_page_config(page_title="Well-Being Checkpoint", layout="centered", initial_sidebar_state="collapsed")

# 2. Injecting New, Multi-Color "Card" UI CSS for perfect balance and readability
st.markdown("""
    <style>
    /* Calming background to make the cards 'pop' */
    .stApp {
        background-color: #F0F4F8; /* Very light cool blue/grey */
    }
    
    /* Explicitly make main headers and questions dark and large */
    h1, h2, h3, .question-text {
        color: #2C3E50; /* A soft dark grey/blue for max readability */
        font-family: 'Roboto', sans-serif;
        text-align: center;
        margin-top: 0;
    }

    h2 { font-size: 24px; font-weight: 600; }
    .question-text { font-size: 20px; font-weight: 500; padding: 20px 10px; }

    /* The Question Card: Clean, centered, with soft shadow and color bars */
    .question-card {
        background-color: #FFFFFF;
        border-radius: 16px;
        box-shadow: 0 10px 25px -3px rgba(0, 0, 0, 0.08);
        padding: 0; /* Let the color bar define the top padding */
        overflow: hidden; /* Important for the color bar */
        margin-bottom: 20px;
        position: relative; /* for centering icon placeholders */
    }

    /* Progress bar styling to make it part of the card */
    .stProgress {
        margin-top: 10px;
    }
    .stProgress div[role='progressbar'] > div {
        background-color: #008080 !important; /* Teal accent */
    }

    /* Large, touch-friendly answer buttons in simple white */
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
    
    /* Hover/Tap state with colored icons in buttons */
    div.stButton > button:hover {
        border-color: #008080;
        color: #008080;
        box-shadow: 0 10px 15px -3px rgba(0, 128, 128, 0.1);
        transform: translateY(-1px);
    }
    
    /* Result screen headers: Different colors for each category, similar to infographic */
    .result-minimal { background-color: #4CAF50; color: #FFFFFF; padding: 15px; border-radius: 10px; } /* Green */
    .result-mild { background-color: #FFC107; color: #333; padding: 15px; border-radius: 10px; } /* Yellow */
    .result-moderate { background-color: #FF9800; color: #FFFFFF; padding: 15px; border-radius: 10px; } /* Orange */
    .result-severe { background-color: #F44336; color: #FFFFFF; padding: 15px; border-radius: 10px; } /* Red */

    /* Disclaimer styling */
    .disclaimer-text {
        font-size: 14px;
        color: #7F8C8D;
        text-align: justify;
        padding: 10px;
        line-height: 1.4;
    }

    /* Mobile scaling optimization */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Define Dynamic Color Header Bars for each Question */
    .card-header-0 { height: 15px; background-color: #4285F4; } /* Blue (Nervous) */
    .card-header-1, .card-header-2 { height: 15px; background-color: #34A853; } /* Green (Worry Control) */
    .card-header-3, .card-header-4 { height: 15px; background-color: #FBBC05; } /* Orange (Relaxing) */
    .card-header-5, .card-header-6 { height: 15px; background-color: #A13FEF; } /* Purple (Easily Annoyed) */

    </style>
""", unsafe_allow_html=True)

# 3. Define the GAD-7 Questions and Scoring (Shortened for Card Format)
questions = [
    "Nervous, anxious or on edge?",
    "Unable to stop or control worrying?",
    "Worry too much about different things?",
    "Having trouble relaxing?",
    "So restless that you can't sit still?",
    "Become easily annoyed or irritable?",
    "Feeling afraid something awful might happen?"
]

options = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3
}

# 4. Initialize Session State
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
    st.session_state.total_score = 0

# Helper function to advance the card
def record_answer_and_next(score_value):
    st.session_state.total_score += score_value
    st.session_state.current_step += 1

# Helper to reset for next person
def reset_checkpoint():
    st.session_state.current_step = 0
    st.session_state.total_score = 0

# 5. Main UI Logic
step = st.session_state.current_step

# State A: Showing Questions (Cards 1 to 7)
if step < len(questions):
    st.markdown("<h2 class='center-text'>Mental Health Checkpoint</h2>", unsafe_allow_html=True)
    
    # Question Card Container
    # Create the color-coded header bar for this specific step
    st.markdown(f"<div class='card-header-{step}'></div>", unsafe_allow_html=True)
    
    # Progress bar and progress text (inside the card)
    st.progress((step) / len(questions))
    st.caption(f"Question {step + 1} of {len(questions)}")
    
    # Question Text (Large and Dark)
    st.markdown(f"<div class='question-text'>{questions[step]}</div>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Large Answer Buttons
    for text, value in options.items():
        st.button(text, on_click=record_answer_and_next, args=(value,), key=f"q{step}_{value}", use_container_width=True)

# State B: The Results Dashboard (Card 8)
else:
    score = st.session_state.total_score
    st.markdown("<h1 class='center-text'>Your Results</h1>", unsafe_allow_html=True)
    
    # Displays the final score clearly
    st.metric(label="Total GAD-7 Score", value=score)
    st.write("---")
    
    # GAD-7 Scoring Bins with colored panels mirroring the infographic categories
    if score <= 4:
        st.markdown("<div class='result-minimal'><h3>Minimal Anxiety</h3>Your score suggests minimal symptoms. Keep prioritizing your well-being!</div>", unsafe_allow_html=True)
    elif score <= 9:
        st.markdown("<div class='result-mild'><h3>Mild Anxiety</h3>Your score indicates mild anxiety. Consider reviewing our brochure for daily management and breathing techniques.</div>", unsafe_allow_html=True)
    elif score <= 14:
        st.markdown("<div class='result-moderate'><h3>Moderate Anxiety</h3>Your score indicating moderate anxiety symptoms. We recommend exploring the support resources and counseling information at our booth.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-severe'><h3>Severe Anxiety</h3>Your score indicate severe anxiety symptoms. Please consider reaching out to a healthcare professional or campus counseling services for support.</div>", unsafe_allow_html=True)
        
    st.write("---")
    
    # Disclaimer Text (Small but bold and distinct)
    st.markdown("<div class='disclaimer-text'><strong>Disclaimer:</strong> This tool is for educational and awareness purposes only. It is a screening tool, not a clinical diagnosis. It does not replace a professional evaluation. Please consult a qualified mental health professional for an accurate assessment.</div>", unsafe_allow_html=True)
    
    st.write("") # Spacer
    
    # Reset button for the next TA at the table
    if st.button("Start Over for Next Person", on_click=reset_checkpoint, type="primary", use_container_width=True):
        st.rerun()
