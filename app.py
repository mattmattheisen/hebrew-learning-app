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
        "conversations": [
            {
                "context": "At the post office",
                "hebrew": "אני צריך לכתוב את הכתובת על המכתב",
                "pronunciation": "ani tzarich likhtov et haktovet al hamikhtav",
                "english": "I need to write the address on the letter"
            },
            {
                "context": "At work",
                "hebrew": "האם זה כתוב בכתב יד או מודפס?",
                "pronunciation": "ha'im ze katuv bekhtav yad o mudpas?",
                "english": "Is this written by hand or printed?"
            },
            {
                "context": "In class",
                "hebrew": "התלמידים כותבים בחוברות שלהם",
                "pronunciation": "hatalmidim kotvim bachuvrot shelahem",
                "english": "The students are writing in their notebooks"
            }
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
        "conversations": [
            {
                "context": "At a restaurant",
                "hebrew": "מה אתה אוכל? האוכל כאן טעים מאוד",
                "pronunciation": "ma ata okhel? ha'okhel kan ta'im me'od",
                "english": "What are you eating? The food here is very tasty"
            },
            {
                "context": "Family dinner",
                "hebrew": "אכלתי יותר מדי, אבל המאכל היה נפלא",
                "pronunciation": "akhalti yoter miday, aval hamaakhal haya nifla",
                "english": "I ate too much, but the food was wonderful"
            },
            {
                "context": "Grocery shopping",
                "hebrew": "האם זה אכיל? מתי פג התוקף?",
                "pronunciation": "ha'im ze akhil? matay pag hatokef?",
                "english": "Is this edible? When does it expire?"
            }
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
        "conversations": [
            {
                "context": "At school",
                "hebrew": "התלמיד הזה לומד מהר מאוד",
                "pronunciation": "hatalmid haze lomed maher me'od",
                "english": "This student learns very quickly"
            },
            {
                "context": "Study session",
                "hebrew": "למדתי תלמוד עם המלמד שלי",
                "pronunciation": "lamadti talmud im hamelamed sheli",
                "english": "I studied Talmud with my teacher"
            },
            {
                "context": "University",
                "hebrew": "התהליך של למידה לוקח זמן",
                "pronunciation": "hatahalich shel lmida lokech zman",
                "english": "The process of learning takes time"
            }
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
        "conversations": [
            {
                "context": "On the phone",
                "hebrew": "אני לא שומע אותך טוב, יש הפרעות",
                "pronunciation": "ani lo shomea otkha tov, yesh hafra'ot",
                "english": "I can't hear you well, there's interference"
            },
            {
                "context": "Gossip",
                "hebrew": "שמעת את השמועה על דוד?",
                "pronunciation": "shamata et hashmuah al David?",
                "english": "Did you hear the rumor about David?"
            },
            {
                "context": "In synagogue",
                "hebrew": "שמע ישראל ה' אלקינו ה' אחד",
                "pronunciation": "shma yisrael adonai eloheinu adonai echad",
                "english": "Hear O Israel, the Lord our God, the Lord is one"
            }
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
    
    # Tabs for different content
    tab1, tab2, tab3, tab4 = st.tabs(["📱 Word Family", "💬 Conversations", "📚 Context", "🎯 Practice"])
    
    with tab1:
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
    
    with tab2:
        st.markdown("**Real-life conversations using this root:**")
        
        for i, conv in enumerate(data['conversations']):
            with st.container():
                st.markdown(f"**{conv['context']}**")
                
                # Hebrew text (larger)
                st.markdown(f"<div style='font-size: 18px; text-align: right; background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 5px 0;'>{conv['hebrew']}</div>", unsafe_allow_html=True)
                
                # Pronunciation
                st.markdown(f"*{conv['pronunciation']}*")
                
                # English translation
                st.markdown(f"**{conv['english']}**")
                
                st.markdown("---")
    
    with tab3:
        # Etymology and Torah connection
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📚 Etymology")
            st.markdown(data['etymology'])
        
        with col2:
            st.subheader("📜 Torah Connection")
            st.markdown(data['torah_connection'])
    
    with tab4:
        # Interactive practice with session state
        st.markdown("**Match the Hebrew word with its meaning:**")
        
        # Initialize session state for this root's practice
        practice_key = f"practice_{root}"
        if practice_key not in st.session_state:
            st.session_state[practice_key] = {
                'word': random.choice(data['words']),
                'answered': False,
                'show_result': False
            }
        
        practice_word = st.session_state[practice_key]['word']
        
        # Create multiple choice
        correct_answer = practice_word['meaning']
        wrong_answers = [w['meaning'] for w in random.choices([w for root_data in ROOTS_DATA.values() for w in root_data['words'] if w['meaning'] != correct_answer], k=2)]
        all_answers = [correct_answer] + wrong_answers
        random.shuffle(all_answers)
        
        st.markdown(f"**{practice_word['hebrew']}** ({practice_word['pronunciation']}) means:")
        
        # Radio button for answer selection
        answer = st.radio("Choose the correct meaning:", all_answers, key=f"answer_{root}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Check Answer", key=f"check_{root}"):
                st.session_state[practice_key]['answered'] = True
                st.session_state[practice_key]['show_result'] = True
                if answer == correct_answer:
                    st.session_state[practice_key]['result'] = 'correct'
                else:
                    st.session_state[practice_key]['result'] = 'incorrect'
        
        with col2:
            if st.button("New Question", key=f"new_{root}"):
                # Reset the practice state for new question
                st.session_state[practice_key] = {
                    'word': random.choice(data['words']),
                    'answered': False,
                    'show_result': False
                }
        
        # Show result if answered
        if st.session_state[practice_key].get('show_result', False):
            if st.session_state[practice_key]['result'] == 'correct':
                st.success(f"🎉 {random.choice(ENCOURAGEMENT)}")
            else:
                st.error(f"😅 {random.choice(GENTLE_CORRECTIONS)} The correct answer is '{correct_answer}'")
        
        # Conversation quiz
        st.markdown("---")
        st.markdown("**Conversation Challenge:**")
        
        conv_key = f"conv_{root}"
        if conv_key not in st.session_state:
            st.session_state[conv_key] = {
                'conversation': random.choice(data['conversations']),
                'answered': False,
                'show_result': False
            }
        
        current_conv = st.session_state[conv_key]['conversation']
        
        st.markdown(f"**Context:** {current_conv['context']}")
        st.markdown(f"**Hebrew:** {current_conv['hebrew']}")
        st.markdown(f"**Pronunciation:** *{current_conv['pronunciation']}*")
        st.markdown("**What does this mean?**")
        
        # Multiple choice for conversation
        correct_conv_answer = current_conv['english']
        wrong_conv_answers = [conv['english'] for conv in random.choices([conv for root_data in ROOTS_DATA.values() for conv in root_data['conversations'] if conv['english'] != correct_conv_answer], k=2)]
        all_conv_answers = [correct_conv_answer] + wrong_conv_answers
        random.shuffle(all_conv_answers)
        
        conv_answer = st.radio("Choose the correct translation:", all_conv_answers, key=f"conv_answer_{root}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Check Translation", key=f"check_conv_{root}"):
                st.session_state[conv_key]['answered'] = True
                st.session_state[conv_key]['show_result'] = True
                if conv_answer == correct_conv_answer:
                    st.session_state[conv_key]['result'] = 'correct'
                else:
                    st.session_state[conv_key]['result'] = 'incorrect'
        
        with col2:
            if st.button("New Conversation", key=f"new_conv_{root}"):
                st.session_state[conv_key] = {
                    'conversation': random.choice(data['conversations']),
                    'answered': False,
                    'show_result': False
                }
        
        # Show conversation result
        if st.session_state[conv_key].get('show_result', False):
            if st.session_state[conv_key]['result'] == 'correct':
                st.success(f"🎉 Excellent! You're getting the hang of real Hebrew conversations!")
            else:
                st.error(f"😅 Not quite! The correct translation is: '{correct_conv_answer}'")

def display_quiz():
    st.subheader("🎯 Quick Root Quiz")
    st.markdown("*Let's see how much you've absorbed while I wasn't looking...*")
    
    # Initialize quiz state with stable questions
    if 'quiz_state' not in st.session_state:
        # Create stable quiz question
        all_words = []
        for root, data in ROOTS_DATA.items():
            for word in data['words'][:2]:
                all_words.append({**word, 'root': root})
        
        selected_word = random.choice(all_words)
        correct_root = selected_word['root']
        wrong_roots = random.sample([r for r in ROOTS_DATA.keys() if r != correct_root], 2)
        all_roots_options = [f"{correct_root} ({ROOTS_DATA[correct_root]['meaning']})"] + [f"{r} ({ROOTS_DATA[r]['meaning']})" for r in wrong_roots]
        random.shuffle(all_roots_options)
        
        st.session_state.quiz_state = {
            'word': selected_word,
            'correct_root': correct_root,
            'all_options': all_roots_options,
            'answered': False,
            'show_result': False
        }
    
    # Get stable quiz data
    quiz_data = st.session_state.quiz_state
    quiz_word = quiz_data['word']
    
    st.markdown(f"**Which root does '{quiz_word['hebrew']}' ({quiz_word['meaning']}) come from?**")
    
    quiz_answer = st.radio("Choose the correct root:", quiz_data['all_options'], key="quiz_answer")
    
    # Extract just the root from the selection
    selected_root = quiz_answer.split(' (')[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Check Quiz Answer"):
            st.session_state.quiz_state['answered'] = True
            st.session_state.quiz_state['show_result'] = True
            st.session_state.quiz_state['user_answer'] = selected_root
    
    with col2:
        if st.button("New Quiz Question"):
            # Generate completely new quiz question
            all_words = []
            for root, data in ROOTS_DATA.items():
                for word in data['words'][:2]:
                    all_words.append({**word, 'root': root})
            
            new_word = random.choice(all_words)
            new_correct_root = new_word['root']
            new_wrong_roots = random.sample([r for r in ROOTS_DATA.keys() if r != new_correct_root], 2)
            new_all_options = [f"{new_correct_root} ({ROOTS_DATA[new_correct_root]['meaning']})"] + [f"{r} ({ROOTS_DATA[r]['meaning']})" for r in new_wrong_roots]
            random.shuffle(new_all_options)
            
            st.session_state.quiz_state = {
                'word': new_word,
                'correct_root': new_correct_root,
                'all_options': new_all_options,
                'answered': False,
                'show_result': False
            }
    
    # Show result if answered
    if quiz_data.get('show_result', False):
        if quiz_data.get('user_answer') == quiz_data['correct_root']:
            st.success(f"🎉 Excellent! You're really getting the hang of this!")
            st.balloons()
        else:
            st.error(f"😅 Not quite! '{quiz_word['hebrew']}' comes from the root {quiz_data['correct_root']} ({ROOTS_DATA[quiz_data['correct_root']]['meaning']})")
    
    # Add conversation quiz
    st.markdown("---")
    st.markdown("**🗣️ Conversation Quiz**")
    
    # Initialize conversation quiz state
    if 'conv_quiz_state' not in st.session_state:
        # Create stable conversation quiz
        all_conversations = []
        for root, data in ROOTS_DATA.items():
            for conv in data['conversations']:
                all_conversations.append({**conv, 'root': root})
        
        selected_conv = random.choice(all_conversations)
        correct_translation = selected_conv['english']
        wrong_translations = [conv['english'] for conv in random.choices([conv for root_data in ROOTS_DATA.values() for conv in root_data['conversations'] if conv['english'] != correct_translation], k=2)]
        all_translations = [correct_translation] + wrong_translations
        random.shuffle(all_translations)
        
        st.session_state.conv_quiz_state = {
            'conversation': selected_conv,
            'correct_answer': correct_translation,
            'all_options': all_translations,
            'answered': False,
            'show_result': False
        }
    
    # Get stable conversation data
    conv_quiz_data = st.session_state.conv_quiz_state
    quiz_conv = conv_quiz_data['conversation']
    
    st.markdown(f"**Context:** {quiz_conv['context']}")
    st.markdown(f"**Hebrew:** {quiz_conv['hebrew']}")
    st.markdown("**What does this mean?**")
    
    conv_quiz_answer = st.radio("Choose the correct translation:", conv_quiz_data['all_options'], key="conv_quiz_answer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Check Translation"):
            st.session_state.conv_quiz_state['answered'] = True
            st.session_state.conv_quiz_state['show_result'] = True
            st.session_state.conv_quiz_state['user_answer'] = conv_quiz_answer
    
    with col2:
        if st.button("New Conversation"):
            # Generate new conversation quiz
            all_conversations = []
            for root, data in ROOTS_DATA.items():
                for conv in data['conversations']:
                    all_conversations.append({**conv, 'root': root})
            
            new_conv = random.choice(all_conversations)
            new_correct_translation = new_conv['english']
            new_wrong_translations = [conv['english'] for conv in random.choices([conv for root_data in ROOTS_DATA.values() for conv in root_data['conversations'] if conv['english'] != new_correct_translation], k=2)]
            new_all_translations = [new_correct_translation] + new_wrong_translations
            random.shuffle(new_all_translations)
            
            st.session_state.conv_quiz_state = {
                'conversation': new_conv,
                'correct_answer': new_correct_translation,
                'all_options': new_all_translations,
                'answered': False,
                'show_result': False
            }
    
    # Show conversation result
    if conv_quiz_data.get('show_result', False):
        if conv_quiz_data.get('user_answer') == conv_quiz_data['correct_answer']:
            st.success(f"🎉 Perfect! You're understanding Hebrew in context!")
        else:
            st.error(f"😅 Close, but the correct translation is: '{conv_quiz_data['correct_answer']}'")

if __name__ == "__main__":
    main()
