import streamlit as st
import random

# Configure the page
st.set_page_config(
    page_title="Hebrew Roots Adventure! 🌟",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for kid-friendly design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .tutor-quote {
        background: linear-gradient(135deg, #FFE082 0%, #FFF176 100%);
        border-radius: 15px;
        padding: 15px;
        border-left: 5px solid #FF9800;
        font-size: 1.1rem;
    }
    .hebrew-text {
        font-size: 2rem;
        color: #2196F3;
        font-weight: bold;
        text-align: center;
        background: #E3F2FD;
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .success-box {
        background: linear-gradient(135deg, #C8E6C9 0%, #A5D6A7 100%);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        font-size: 1.2rem;
    }
    .quiz-button {
        background: linear-gradient(135deg, #FF9800 0%, #FF5722 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Hebrew roots database - kid-friendly version
ROOTS_DATA = {
    "כ-ת-ב": {
        "meaning": "write ✏️",
        "pronunciation": "k-t-v",
        "emoji": "✍️",
        "color": "#2196F3",
        "words": [
            {"hebrew": "כתב", "pronunciation": "katav", "meaning": "he wrote", "type": "verb", "emoji": "✏️"},
            {"hebrew": "כותב", "pronunciation": "kotev", "meaning": "writer", "type": "noun", "emoji": "👨‍💻"},
            {"hebrew": "מכתב", "pronunciation": "mikhtav", "meaning": "letter", "type": "noun", "emoji": "💌"},
            {"hebrew": "כתיבה", "pronunciation": "ktiva", "meaning": "writing", "type": "noun", "emoji": "📝"},
        ],
        "conversations": [
            {
                "context": "📮 At the post office",
                "hebrew": "אני כותב מכתב לסבתא",
                "pronunciation": "ani kotev mikhtav l'savta",
                "english": "I'm writing a letter to grandma",
                "emoji": "👵💌"
            },
            {
                "context": "🏫 At school",
                "hebrew": "התלמידים כותבים בחוברות",
                "pronunciation": "hatalmidim kotvim bachuvrot",
                "english": "The students are writing in notebooks",
                "emoji": "📚✏️"
            }
        ],
        "tutor_intro": "Ah, כ-ת-ב! This is like the superhero of writing! ✨ From three little letters, we get ALL the words about writing. It's like Hebrew magic! 🎩✨",
        "kid_fact": "🌟 Fun fact: Ancient people carved letters into stone - imagine doing your homework on a rock! 🪨",
        "torah_connection": "📜 Moses wrote the Ten Commandments using this root! Even God needed good handwriting! ✍️"
    },
    
    "א-כ-ל": {
        "meaning": "eat 🍎",
        "pronunciation": "a-kh-l",
        "emoji": "🍽️",
        "color": "#4CAF50",
        "words": [
            {"hebrew": "אכל", "pronunciation": "akhal", "meaning": "he ate", "type": "verb", "emoji": "😋"},
            {"hebrew": "אוכל", "pronunciation": "okhel", "meaning": "food", "type": "noun", "emoji": "🍕"},
            {"hebrew": "אכילה", "pronunciation": "akhila", "meaning": "eating", "type": "noun", "emoji": "🍽️"},
            {"hebrew": "תאכל", "pronunciation": "tokhal", "meaning": "you will eat", "type": "verb", "emoji": "🥄"},
        ],
        "conversations": [
            {
                "context": "🍕 At dinner",
                "hebrew": "מה אתה אוכל?",
                "pronunciation": "ma ata okhel?",
                "english": "What are you eating?",
                "emoji": "🤔🍽️"
            },
            {
                "context": "🏠 At home",
                "hebrew": "האוכל טעים מאוד!",
                "pronunciation": "ha'okhel ta'im me'od!",
                "english": "The food is very delicious!",
                "emoji": "😋👌"
            }
        ],
        "tutor_intro": "א-כ-ל is everyone's favorite root! 🍕 It's all about eating - and trust me, I know a LOT about eating! 😅",
        "kid_fact": "🌟 This root appears in the first story of the Torah when Adam and Eve ate the forbidden fruit! 🍎",
        "torah_connection": "📜 The first big eating mistake in history! But hey, we all make food choices we regret! 🤷‍♂️"
    },
    
    "ל-מ-ד": {
        "meaning": "learn 📚",
        "pronunciation": "l-m-d",
        "emoji": "🎓",
        "color": "#9C27B0",
        "words": [
            {"hebrew": "למד", "pronunciation": "lamad", "meaning": "he learned", "type": "verb", "emoji": "🧠"},
            {"hebrew": "תלמיד", "pronunciation": "talmid", "meaning": "student", "type": "noun", "emoji": "👨‍🎓"},
            {"hebrew": "מלמד", "pronunciation": "melamed", "meaning": "teacher", "type": "noun", "emoji": "👩‍🏫"},
            {"hebrew": "תלמוד", "pronunciation": "talmud", "meaning": "Talmud", "type": "noun", "emoji": "📖"},
        ],
        "conversations": [
            {
                "context": "🏫 At school",
                "hebrew": "התלמיד לומד עברית",
                "pronunciation": "hatalmid lomed ivrit",
                "english": "The student is learning Hebrew",
                "emoji": "👨‍🎓🔤"
            },
            {
                "context": "📚 Study time",
                "hebrew": "למדתי הרבה היום",
                "pronunciation": "lamadti harbe hayom",
                "english": "I learned a lot today",
                "emoji": "🧠💡"
            }
        ],
        "tutor_intro": "ל-מ-ד is the learning root! 🎓 I've been using this root to confuse myself for 30 years! But hey, at least I'm consistent! 😅",
        "kid_fact": "🌟 From this root comes 'Talmud' - the biggest homework assignment in Jewish history! 📚",
        "torah_connection": "📜 Moses was always telling people to learn things. Good thing there were no pop quizzes! 📝"
    },
    
    "ש-מ-ע": {
        "meaning": "hear 👂",
        "pronunciation": "sh-m-a",
        "emoji": "👂",
        "color": "#FF5722",
        "words": [
            {"hebrew": "שמע", "pronunciation": "shama", "meaning": "he heard", "type": "verb", "emoji": "👂"},
            {"hebrew": "שומע", "pronunciation": "shomea", "meaning": "listening", "type": "verb", "emoji": "🎧"},
            {"hebrew": "שמועה", "pronunciation": "shmuah", "meaning": "rumor", "type": "noun", "emoji": "🗣️"},
            {"hebrew": "שמע ישראל", "pronunciation": "shma yisrael", "meaning": "Hear O Israel", "type": "prayer", "emoji": "🙏"},
        ],
        "conversations": [
            {
                "context": "📞 On the phone",
                "hebrew": "אני לא שומע אותך טוב",
                "pronunciation": "ani lo shomea otkha tov",
                "english": "I can't hear you well",
                "emoji": "📞❓"
            },
            {
                "context": "🕍 At synagogue",
                "hebrew": "שמע ישראל!",
                "pronunciation": "shma yisrael!",
                "english": "Hear O Israel!",
                "emoji": "🙏✨"
            }
        ],
        "tutor_intro": "ש-מ-ע is the most famous Hebrew root! 🌟 It's in the Shema prayer that every Jewish kid learns. Finally, something you already know! 🎉",
        "kid_fact": "🌟 This is the first word of the most important Jewish prayer! You might already know it! 🙏",
        "torah_connection": "📜 'Shma Yisrael' - the most important sentence in Judaism! No pressure... 😅"
    }
}

# Fun encouragement messages for kids
KID_ENCOURAGEMENT = [
    "🌟 WOW! You're a Hebrew superstar! ⭐",
    "🎉 Amazing! You're getting so good at this! 🎈",
    "👏 Fantastic! Even I'm impressed! 🤩",
    "🚀 You're flying through these roots! ✈️",
    "🏆 Incredible! You're a Hebrew champion! 🥇",
    "✨ Brilliant! You're making this look easy! 💫",
    "🎯 Perfect! You hit the bullseye! 🎯",
    "🌈 Wonderful! You're brightening my day! ☀️"
]

GENTLE_CORRECTIONS = [
    "🤗 Oops! Let me help you with that... 💡",
    "😊 Almost there! Here's the right answer... 🎯",
    "🌟 Good try! Let me show you the way... 🗺️",
    "💙 Don't worry, everyone learns! Here's the answer... 📚",
    "🎈 Close one! The correct answer is... ✨",
    "🌸 Nice effort! Here's what it really means... 🌺"
]

def main():
    # Fun header
    st.markdown('<h1 class="main-header">🌟 Hebrew Roots Adventure! 🔤</h1>', unsafe_allow_html=True)
    st.markdown("### *Learn Hebrew with your favorite neurotic tutor!* 😄")
    
    # Sidebar
    st.sidebar.title("🤓 Your Hebrew Tutor")
    st.sidebar.markdown("*\"I've been confused about Hebrew for 30 years - let's be confused together!\"* 😅")
    
    # Root selection with emojis
    st.sidebar.markdown("### 🌳 Choose a Root to Explore:")
    selected_root = st.sidebar.selectbox(
        "Pick your adventure:",
        options=list(ROOTS_DATA.keys()),
        format_func=lambda x: f"{ROOTS_DATA[x]['emoji']} {x} ({ROOTS_DATA[x]['meaning']})",
        key="root_selector"
    )
    
    # Fun progress with stars
    progress = len([r for r in ROOTS_DATA.keys() if st.session_state.get(f"completed_{r}", False)]) / len(ROOTS_DATA)
    st.sidebar.progress(progress)
    stars = "⭐" * len([r for r in ROOTS_DATA.keys() if st.session_state.get(f"completed_{r}", False)])
    st.sidebar.markdown(f"### 🏆 Your Stars: {stars}")
    st.sidebar.caption(f"Roots mastered: {len([r for r in ROOTS_DATA.keys() if st.session_state.get(f'completed_{r}', False)])}/{len(ROOTS_DATA)}")
    
    # Main content
    if selected_root:
        display_root_lesson(selected_root)
    
    # Quiz section
    st.sidebar.markdown("---")
    if st.sidebar.button("🎯 Take a Quiz!", key="quiz_button"):
        st.session_state.show_quiz = True
    
    if st.session_state.get('show_quiz', False):
        st.markdown("---")
        display_simple_quiz()

def display_root_lesson(root):
    data = ROOTS_DATA[root]
    
    # Header with emoji and color
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"## {data['emoji']} Root: {root}")
        st.markdown(f"### Meaning: {data['meaning']} ({data['pronunciation']})")
    
    with col2:
        if st.button("🌟 I Mastered This!", key=f"master_{root}"):
            st.session_state[f"completed_{root}"] = True
            st.balloons()
            st.success(random.choice(KID_ENCOURAGEMENT))
    
    # Tutor introduction with custom styling
    st.markdown(f"""
    <div class="tutor-quote">
        🤓 <strong>Your Tutor Says:</strong> {data['tutor_intro']}
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different content
    tab1, tab2, tab3, tab4 = st.tabs(["🌳 Word Family", "💬 Conversations", "📚 Fun Facts", "🎯 Practice"])
    
    with tab1:
        st.markdown("### See how this root creates different words! ✨")
        
        for word in data['words']:
            col1, col2, col3, col4 = st.columns([1, 2, 2, 3])
            with col1:
                st.markdown(f"### {word['emoji']}")
            with col2:
                st.markdown(f"<div class='hebrew-text'>{word['hebrew']}</div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"**{word['pronunciation']}**")
            with col4:
                st.markdown(f"*{word['meaning']}* ({word['type']})")
        
    with tab2:
        st.markdown("### 🗣️ Real Hebrew Conversations!")
        
        for conv in data['conversations']:
            st.markdown(f"#### {conv['context']} {conv['emoji']}")
            
            # Hebrew in a special box
            st.markdown(f"<div class='hebrew-text'>{conv['hebrew']}</div>", unsafe_allow_html=True)
            
            # Pronunciation and translation
            st.markdown(f"**🔊 Sounds like:** *{conv['pronunciation']}*")
            st.markdown(f"**🇺🇸 In English:** {conv['english']}")
            st.markdown("---")
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎉 Fun Fact!")
            st.info(data['kid_fact'])
        
        with col2:
            st.markdown("### 📜 Torah Connection")
            st.info(data['torah_connection'])
    
    with tab4:
        display_practice_section(root, data)

def display_practice_section(root, data):
    st.markdown("### 🎯 Practice Time!")
    
    # Simple practice question
    if f"practice_q_{root}" not in st.session_state:
        # Create a simple question
        word = random.choice(data['words'])
        options = [word['meaning']] + [w['meaning'] for w in random.choices([w for r in ROOTS_DATA.values() for w in r['words'] if w['meaning'] != word['meaning']], k=2)]
        random.shuffle(options)
        
        st.session_state[f"practice_q_{root}"] = {
            'word': word,
            'options': options,
            'correct': word['meaning'],
            'answered': False
        }
    
    question = st.session_state[f"practice_q_{root}"]
    
    if not question['answered']:
        st.markdown(f"#### What does {question['word']['emoji']} **{question['word']['hebrew']}** mean?")
        st.markdown(f"*Pronunciation: {question['word']['pronunciation']}*")
        
        # Simple radio buttons
        answer = st.radio("Pick your answer:", question['options'], key=f"answer_{root}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Check My Answer!", key=f"check_{root}"):
                st.session_state[f"practice_q_{root}"]['answered'] = True
                st.session_state[f"practice_q_{root}"]['user_answer'] = answer
        
        with col2:
            if st.button("🔄 New Question", key=f"new_q_{root}"):
                # Reset with new question
                word = random.choice(data['words'])
                options = [word['meaning']] + [w['meaning'] for w in random.choices([w for r in ROOTS_DATA.values() for w in r['words'] if w['meaning'] != word['meaning']], k=2)]
                random.shuffle(options)
                
                st.session_state[f"practice_q_{root}"] = {
                    'word': word,
                    'options': options,
                    'correct': word['meaning'],
                    'answered': False
                }
    else:
        # Show result
        if question['user_answer'] == question['correct']:
            st.markdown(f"""
            <div class="success-box">
                🎉 {random.choice(KID_ENCOURAGEMENT)}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"😊 {random.choice(GENTLE_CORRECTIONS)} The answer is: **{question['correct']}**")
        
        if st.button("🚀 Try Another Question!", key=f"reset_{root}"):
            # Reset for new question
            word = random.choice(data['words'])
            options = [word['meaning']] + [w['meaning'] for w in random.choices([w for r in ROOTS_DATA.values() for w in r['words'] if w['meaning'] != word['meaning']], k=2)]
            random.shuffle(options)
            
            st.session_state[f"practice_q_{root}"] = {
                'word': word,
                'options': options,
                'correct': word['meaning'],
                'answered': False
            }

def display_simple_quiz():
    st.markdown("## 🎯 Quick Quiz Time!")
    st.markdown("*Let's see what you remember!* 🧠✨")
    
    # Initialize quiz
    if 'simple_quiz' not in st.session_state:
        # Pick a random word from all roots
        all_words = []
        for root, data in ROOTS_DATA.items():
            for word in data['words']:
                all_words.append({'word': word, 'root': root, 'root_meaning': data['meaning']})
        
        selected = random.choice(all_words)
        root_options = [f"{selected['root']} ({selected['root_meaning']})"] + [f"{r} ({ROOTS_DATA[r]['meaning']})" for r in random.sample([r for r in ROOTS_DATA.keys() if r != selected['root']], 2)]
        random.shuffle(root_options)
        
        st.session_state.simple_quiz = {
            'selected': selected,
            'options': root_options,
            'answered': False
        }
    
    quiz = st.session_state.simple_quiz
    
    if not quiz['answered']:
        st.markdown(f"### Which root does **{quiz['selected']['word']['hebrew']}** come from?")
        st.markdown(f"*It means: {quiz['selected']['word']['meaning']} {quiz['selected']['word']['emoji']}*")
        
        answer = st.radio("Choose the root:", quiz['options'], key="quiz_answer")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎯 Check My Answer!"):
                st.session_state.simple_quiz['answered'] = True
                st.session_state.simple_quiz['user_answer'] = answer
        
        with col2:
            if st.button("🔄 New Quiz Question"):
                # Reset quiz
                all_words = []
                for root, data in ROOTS_DATA.items():
                    for word in data['words']:
                        all_words.append({'word': word, 'root': root, 'root_meaning': data['meaning']})
                
                selected = random.choice(all_words)
                root_options = [f"{selected['root']} ({selected['root_meaning']})"] + [f"{r} ({ROOTS_DATA[r]['meaning']})" for r in random.sample([r for r in ROOTS_DATA.keys() if r != selected['root']], 2)]
                random.shuffle(root_options)
                
                st.session_state.simple_quiz = {
                    'selected': selected,
                    'options': root_options,
                    'answered': False
                }
    else:
        # Show result
        correct_answer = f"{quiz['selected']['root']} ({quiz['selected']['root_meaning']})"
        if quiz['user_answer'] == correct_answer:
            st.balloons()
            st.markdown(f"""
            <div class="success-box">
                🎉 {random.choice(KID_ENCOURAGEMENT)}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"😊 {random.choice(GENTLE_CORRECTIONS)} **{quiz['selected']['word']['hebrew']}** comes from {correct_answer}")
        
        if st.button("🚀 Another Quiz!"):
            # Reset quiz
            all_words = []
            for root, data in ROOTS_DATA.items():
                for word in data['words']:
                    all_words.append({'word': word, 'root': root, 'root_meaning': data['meaning']})
            
            selected = random.choice(all_words)
            root_options = [f"{selected['root']} ({selected['root_meaning']})"] + [f"{r} ({ROOTS_DATA[r]['meaning']})" for r in random.sample([r for r in ROOTS_DATA.keys() if r != selected['root']], 2)]
            random.shuffle(root_options)
            
            st.session_state.simple_quiz = {
                'selected': selected,
                'options': root_options,
                'answered': False
            }

if __name__ == "__main__":
    main()
