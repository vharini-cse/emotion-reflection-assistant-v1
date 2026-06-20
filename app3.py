import streamlit as st
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER sentiment model (first run only)
try:
    nltk.download('vader_lexicon', quiet=True)
except:
    pass

sia = SentimentIntensityAnalyzer()

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Emotion Reflection Assistant",
    page_icon="🧘",
    layout="centered"
)

# ---------------------------------
# Title
# ---------------------------------
st.title("🧘 Emotion Reflection Assistant")
st.write(
    "Celebrate International Yoga Day through self-reflection, mindfulness, and emotional wellness."
)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.title("🌿 About")
st.sidebar.write(
    """
    Emotion Reflection Assistant
    
    Built using:
    - Python
    - Streamlit
    - NLTK Sentiment Analysis
    
    International Yoga Day Project
    """
)

# ---------------------------------
# Emotion Database
# ---------------------------------
emotion_data = {

    "😊 Happiness": {
        "keywords": ["happy", "joyful", "grateful", "cheerful"],
        "questions": [
            "What made you feel happy today?",
            "How can you carry this positive energy forward?"
        ],
        "breathing": "Mindful Breathing",
        "score": 90
    },

    "💪 Confidence": {
        "keywords": ["confident", "capable", "strong", "ready"],
        "questions": [
            "What achievement are you proud of?",
            "How can you use your strengths today?"
        ],
        "breathing": "Power Breathing",
        "score": 85
    },

    "🚀 Motivation": {
        "keywords": ["motivated", "inspired", "excited", "focused"],
        "questions": [
            "What goal excites you the most?",
            "What small step can you take today?"
        ],
        "breathing": "Energizing Breathing",
        "score": 80
    },

    "🤔 Confusion": {
        "keywords": ["confused", "lost", "unclear"],
        "questions": [
            "What part of the situation feels unclear?",
            "What information would help you move forward?"
        ],
        "breathing": "Alternate Nostril Breathing",
        "score": 60
    },

    "😫 Stress": {
        "keywords": ["stress", "tired", "overwhelmed", "pressure"],
        "questions": [
            "What happened today that contributed to this feeling?",
            "What is one thing you can control right now?"
        ],
        "breathing": "Box Breathing (4-4-4-4)",
        "score": 50
    },

    "😟 Anxiety": {
        "keywords": ["worried", "nervous", "fear", "anxious"],
        "questions": [
            "What is worrying you the most right now?",
            "Is this concern within your control?"
        ],
        "breathing": "4-7-8 Breathing",
        "score": 45
    },

    "😞 Disappointment": {
        "keywords": ["disappointed", "failed", "regret"],
        "questions": [
            "What expectation was not met?",
            "What lesson can you learn from this?"
        ],
        "breathing": "Slow Deep Breathing",
        "score": 40
    },

    "😔 Sadness": {
        "keywords": ["sad", "lonely", "hurt", "upset"],
        "questions": [
            "What do you need most right now?",
            "Who can support you during this time?"
        ],
        "breathing": "Mindful Breathing",
        "score": 35
    },

    "🔥 Burnout": {
        "keywords": ["burnout", "exhausted", "drained", "fatigue"],
        "questions": [
            "When did you last take a meaningful break?",
            "What task can you postpone today?"
        ],
        "breathing": "Deep Belly Breathing",
        "score": 30
    },

    "😠 Frustration": {
        "keywords": ["irritated", "angry", "annoyed", "stuck"],
        "questions": [
            "What triggered this frustration?",
            "What can you learn from this situation?"
        ],
        "breathing": "Calming Breath Practice",
        "score": 25
    }
}

# ---------------------------------
# Quotes
# ---------------------------------
quotes = [
    "Peace comes from within.",
    "Your breath is your anchor.",
    "Progress is better than perfection.",
    "One step at a time is enough.",
    "Growth begins with self-awareness.",
    "You are stronger than you think.",
    "Small steps create lasting change.",
    "Every day is a fresh beginning."
]

# ---------------------------------
# User Input
# ---------------------------------
user_input = st.text_area(
    "How are you feeling today?",
    placeholder="Example: I feel overwhelmed and worried about my project..."
)

# ---------------------------------
# Analyze Button
# ---------------------------------
if st.button("Analyze My Feelings"):

    text = user_input.lower()

    detected_emotions = []

    # Emotion Detection
    for emotion, details in emotion_data.items():
        for keyword in details["keywords"]:
            if keyword in text:
                detected_emotions.append(emotion)
                break

    if not detected_emotions:

        st.warning(
            "I couldn't clearly identify your emotion. Try describing your feelings in more detail."
        )

    else:

        # ----------------------------
        # Detected Emotions
        # ----------------------------
        st.subheader("🎯 Detected Emotions")

        for emotion in detected_emotions:
            st.success(emotion)

        # ----------------------------
        # Sentiment Analysis
        # ----------------------------
        st.subheader("📊 Sentiment Analysis")

        sentiment = sia.polarity_scores(user_input)

        compound = sentiment["compound"]

        if compound >= 0.5:
            sentiment_label = "Positive 😊"
        elif compound <= -0.5:
            sentiment_label = "Negative 😟"
        else:
            sentiment_label = "Neutral 😐"

        st.info(f"Overall Sentiment: {sentiment_label}")

        st.write(f"Positive: {round(sentiment['pos'] * 100)}%")
        st.write(f"Neutral: {round(sentiment['neu'] * 100)}%")
        st.write(f"Negative: {round(sentiment['neg'] * 100)}%")

        sentiment_score = int((compound + 1) * 50)

        st.progress(sentiment_score / 100)

        st.write(
            f"**Sentiment Score: {sentiment_score}/100**"
        )

        # ----------------------------
        # Reflection Questions
        # ----------------------------
        st.subheader("📝 Reflection Questions")

        for emotion in detected_emotions:
            for question in emotion_data[emotion]["questions"]:
                st.write(f"• {question}")

        # ----------------------------
        # Breathing Exercise
        # ----------------------------
        st.subheader("🫁 Recommended Yoga Breathing Exercise")

        shown = []

        for emotion in detected_emotions:
            exercise = emotion_data[emotion]["breathing"]

            if exercise not in shown:
                st.info(exercise)
                shown.append(exercise)

        # ----------------------------
        # Daily Quote
        # ----------------------------
        st.subheader("🌟 Positive Daily Quote")

        st.success(random.choice(quotes))

        # ----------------------------
        # Wellness Score
        # ----------------------------
        scores = []

        for emotion in detected_emotions:
            scores.append(emotion_data[emotion]["score"])

        wellness_score = int(sum(scores) / len(scores))

        st.subheader("🌱 Wellness Reflection Score")

        st.progress(wellness_score / 100)

        st.write(
            f"**Wellness Reflection Score: {wellness_score}/100**"
        )

        # ----------------------------
        # Final Message
        # ----------------------------
        st.subheader("💚 Final Encouragement")

        if wellness_score >= 75:
            st.success(
                "You seem to be in a positive emotional state. Keep nurturing these healthy habits."
            )

        elif wellness_score >= 50:
            st.info(
                "You may be facing some challenges today. Focus on what you can control and take one step at a time."
            )

        else:
            st.warning(
                "Today may feel difficult, and that's okay. Give yourself permission to rest, reflect, and seek support when needed."
            )

        st.write(
            "🙏 Thank you for taking a moment to reflect on your emotions today."
        )
