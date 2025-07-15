import streamlit as st
import random

# Configure the page
st.set_page_config(
    page_title="Hebrew Roots Master",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hebrew roots database
ROOTS_DATA = {
    "כ-ת-ב": {
        "meaning": "write",
        "pronunciation": "k-t-v",
        "words": [
            {"hebrew": "כתב", "pronunciation": "katav", "meaning": "he wrote", "type": "verb (past)"},
            {"hebrew": "כותב", "pronunciation": "kotev", "meaning": "writing/writer", "type": "verb (present)/noun"},
            {"hebrew": "כתיבה", "pronunciation": "ktiva", "meaning": "writing", "type": "noun (feminine)"},
            {"hebrew": "מכתב", "pronunciation": "mikhtav", "meaning": "letter", "type": "noun (masculine)"},
            {"hebrew": "כתובת", "pronunciation": "ktovet", "meaning": "address", "type": "noun (feminine)"},
            {"hebrew": "כתוב", "pronunciation": "katuv", "meaning": "written", "type": "adjective"},
            {"hebrew": "ביכתב", "pronunciation": "bikhtav", "meaning": "in writing", "type": "adverb"}
        ],
        "tutor_intro": "Ah, כ-ת-ב! The root of all your writing anxieties! You think English spelling is hard? Try Hebrew, where three letters become your entire literary universe.",
        "etymology": "From ancient Semitic roots meaning 'to cut' or 'carve' - because originally writing meant carving into stone. Much like how learning Hebrew carves confusion into your brain!",
        "torah_connection": "This root appears over 200 times in Torah. Every time Moses had to write something down, there it is - כתב. Even God couldn't escape paperwork!"
    },
    
    "א-כ-ל": {
        "meaning": "eat",
        "pronunciation": "a-kh-l",
        "words": [
            {"hebrew": "אכל", "pronunciation": "akhal", "meaning": "he ate", "type": "verb (past)"},
            {"hebrew": "אוכל", "pronunciation": "okhel", "meaning": "eating/food", "type": "verb (present)/noun"},
            {"hebrew": "אכילה", "pronunciation": "akhila", "meaning": "eating", "type": "noun (feminine)"},
            {"hebrew": "מאכל", "pronunciation": "maakhal", "meaning": "food", "type": "noun (masculine)"},
            {"hebrew": "אכיל", "pronunciation": "akhil", "meaning": "edible", "type": "adjective"},
            {"hebrew": "תאכל", "pronunciation": "tokhal", "meaning": "you will eat", "type": "verb (future)"}
        ],
        "tutor_intro": "Food! Finally, a root we can all relate to. א-כ-ל has fed the Jewish people linguistically for millennia. Unlike my cooking, this root actually nourishes.",
        "etymology": "From proto-Semitic meaning 'to consume.' Fun fact: it's related to the word for 'destruction' because apparently our ancestors understood that eating and destroying are basically the same thing.",
        "torah_connection": "First appears in Genesis when God tells Adam what he can and cannot eat. Spoiler alert: it doesn't go well."
    },
    
    "ל-מ-ד": {
        "meaning": "learn/teach",
        "pronunciation": "l-m-d",
        "words": [
            {"hebrew": "למד", "pronunciation": "lamad", "meaning": "he learned", "type": "verb (past)"},
            {"hebrew": "לומד", "pronunciation": "lomed", "meaning": "learning/student", "type": "verb (present)/noun"},
            {"hebrew": "למידה", "pronunciation": "lmida", "meaning": "learning", "type": "noun (feminine)"},
            {"hebrew": "תלמיד", "pronunciation": "talmid", "meaning": "student", "type": "noun (masculine)"},
            {"hebrew": "מלמד", "pronunciation": "melamed", "meaning": "teacher", "type": "noun (masculine)"},
            {"hebrew": "תלמוד", "pronunciation": "talmud", "meaning": "study/Talmud", "type": "noun (masculine)"}
        ],
        "tutor_intro": "Ah, ל-מ-ד - the root that's been making Jews anxious about education for 3,000 years! From this humble root comes 'Talmud' - proof that we've been overcomplicating simple concepts since ancient times.",
        "etymology": "Originally meant 'to goad' or 'drive cattle.' Apparently our ancestors understood that learning requires the same approach as herding livestock. Very insightful.",
        "torah_connection": "Moses uses this root constantly when telling the Israelites to learn God's laws. Spoiler: they don't listen very well."
    },
    
    "ש-מ-ע": {
        "meaning": "hear/listen",
        "pronunciation": "sh-m-a",
        "words": [
            {"hebrew": "שמע", "pronunciation": "shama", "meaning": "he heard", "type": "verb (past)"},
            {"hebrew": "שומע", "pronunciation": "shomea", "meaning": "hearing/listener", "type": "verb (present)/noun"},
            {"hebrew": "שמיעה", "pronunciation": "shmiya", "meaning": "hearing", "type": "noun (feminine)"},
            {"hebrew": "שמועה", "pronunciation": "shmuah", "meaning": "rumor", "type": "noun (feminine)"},
            {"hebrew": "משמע", "pronunciation": "mashma", "meaning": "meaning/implication", "type": "noun (masculine)"},
            {"hebrew": "שמע ישראל", "pronunciation": "shma yisrael", "meaning": "Hear O Israel", "type": "prayer"}
        ],
        "tutor_intro": "ש-מ-ע - the most famous Hebrew root you never realized you knew! It's in the Shema prayer, which every Jewish kid learns. Finally, something that connects Sunday school to actual Hebrew!",
        "etymology": "From ancient Semitic meaning 'to hear' or 'perceive.' Same root family as 'shem' (name) because apparently hearing and naming are connected. Hebrew is very philosophical that way.",
        "torah_connection": "The Shema (שמע ישראל) uses this root. It's basically the most important sentence in Judaism, so... no pressure learning this one correctly."
    }
}

# Tutor personality responses
ENCOURAGEMENT = [
    "Look at you, making progress! I'm kvelling over here!",
    "Not bad! You're getting the hang of this Hebrew thing.",
    "Excellent! You're smarter than I was at your stage.",
    "Wonderful! Keep this up and you'll be correcting my pronunciation soon.",
    "Fantastic! You're really getting these patterns down."
]

GENTLE_CORRECTIONS = [
    "Eh, close enough! Let me clarify this for you...",
    "Well, you tried! Here's what's actually happening...",
    "Oy, not quite, but I like your thinking! Actually...",
    "Nice attempt! Let me steer you in the right direction...",
    "Good guess! Here's the real story though..."
]

def main():
    st.title("🔤 Hebrew Roots Master")
    st.markdown("*Learn Hebrew the way it was meant to be learned - through roots, patterns, and a healthy dose of neurosis*")
    
    # Sidebar for navigation
    st.sidebar.title("🤓 Your Neurotic Hebrew Tutor")
    st.sidebar.markdown("*\"I've been studying Hebrew for 30 years and I'm still confused. Let's be confused together!\"*")
    
    # Root selection
    selected_root = st.sidebar.selectbox(
        "Choose a root to explore:",
        options=list(ROOTS_DATA.keys()),
        format_func=lambda x: f"{x} ({ROOTS_DATA[x]['meaning']})"
    )
    
    # Progress tracking (simulated)
    st.sidebar.progress(len([r for r in ROOTS_DATA.keys() if st.session_state.get(f"completed_{r}", False)]) / len(ROOTS_DATA))
    st.sidebar.caption(f"Roots mastered: {len([r for r in ROOTS_DATA.keys() if st.session_state.get(f'completed_{r}', False)])}/{len(ROOTS_DATA)}")
    
    # Main content
    if selected_root:
        display_root_lesson(selected_root)
    
    # Quiz section
    st.sidebar.markdown("---")
    if st.sidebar.button("🎯 Quick Quiz"):
        display_quiz()

def display_root_lesson(root):
    data = ROOTS_DATA[root]
    
    # Header
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header(f"Root: {root}")
        st.subheader(f"Meaning: {data['meaning']} ({data['pronunciation']})")
    
    with col2:
        if st.button("Mark as Mastered ✅"):
            st.session_state[f"completed_{root}"] = True
            st.success(random.choice(ENCOURAGEMENT))
    
    # Tutor introduction
    st.info(f"🤓 **Your Tutor Says:** {data['tutor_intro']}")
    
    # Word family
    st.subheader("📱 Word Family")
    st.markdown("Here's how this root creates different words:")
    
    # Display words in a nice table
    word_data = []
    for word in data['words']:
        word_data.append([
            word['hebrew'],
            word['pronunciation'],
            word['meaning'],
            word['type']
        ])
    
    import pandas as pd
    df = pd.DataFrame(word_data, columns=['Hebrew', 'Pronunciation', 'English', 'Type'])
    st.dataframe(df, use_container_width=True)
    
    # Etymology and Torah connection
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Etymology")
        st.markdown(data['etymology'])
    
    with col2:
        st.subheader("📜 Torah Connection")
        st.markdown(data['torah_connection'])
    
    # Interactive practice
    st.subheader("🎯 Quick Practice")
    
    # Simple matching exercise
    st.markdown("**Match the Hebrew word with its meaning:**")
    
    # Select a random word from this root
    practice_word = random.choice(data['words'])
    
    # Create multiple choice
    correct_answer = practice_word['meaning']
    wrong_answers = [w['meaning'] for w in random.choices([w for root_data in ROOTS_DATA.values() for w in root_data['words'] if w['meaning'] != correct_answer], k=2)]
    all_answers = [correct_answer] + wrong_answers
    random.shuffle(all_answers)
    
    st.markdown(f"**{practice_word['hebrew']}** ({practice_word['pronunciation']}) means:")
    
    answer = st.radio("Choose the correct meaning:", all_answers, key=f"practice_{root}")
    
    if st.button("Check Answer", key=f"check_{root}"):
        if answer == correct_answer:
            st.success(f"🎉 {random.choice(ENCOURAGEMENT)}")
        else:
            st.error(f"😅 {random.choice(GENTLE_CORRECTIONS)} The correct answer is '{correct_answer}'")

def display_quiz():
    st.subheader("🎯 Quick Root Quiz")
    st.markdown("*Let's see how much you've absorbed while I wasn't looking...*")
    
    # Select random words from all roots
    all_words = []
    for root, data in ROOTS_DATA.items():
        for word in data['words'][:2]:  # Take first 2 words from each root
            all_words.append({**word, 'root': root})
    
    quiz_word = random.choice(all_words)
    
    st.markdown(f"**Which root does '{quiz_word['hebrew']}' ({quiz_word['meaning']}) come from?**")
    
    # Create multiple choice with roots
    correct_root = quiz_word['root']
    wrong_roots = random.sample([r for r in ROOTS_DATA.keys() if r != correct_root], 2)
    all_roots = [correct_root] + wrong_roots
    random.shuffle(all_roots)
    
    quiz_answer = st.radio("Choose the correct root:", all_roots, key="quiz_answer")
    
    if st.button("Check Quiz Answer"):
        if quiz_answer == correct_root:
            st.success(f"🎉 Excellent! You're really getting the hang of this!")
            st.balloons()
        else:
            st.error(f"😅 Not quite! '{quiz_word['hebrew']}' comes from the root {correct_root} ({ROOTS_DATA[correct_root]['meaning']})")

if __name__ == "__main__":
    main()
