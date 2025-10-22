import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wieviel Fungirl bist du?", page_icon="", layout="centered")

st.title("Wieviel Fungirl bist du?")
st.subheader("Bist du ein Fungirl (oder doch mehr Becky oder Peter)?")

st.image("images/Quiz-Banner.png")

st.write("""
Gebe deine Anworten für die 5 Fragen ein **A**, **B**, or **C**.
und finde heraus, wie viel Fungirl du bist!
""")

# Define the mapping legend
mapping = {
    1: {"A": "Fungirl", "B": "Becky", "C": "Peter"},
    2: {"A": "Peter", "B": "Becky", "C": "Fungirl"},
    3: {"A": "Peter", "B": "Fungirl", "C": "Becky"},
    4: {"A": "Becky", "B": "Peter", "C": "Fungirl"},
    5: {"A": "Becky", "B": "Peter", "C": "Fungirl"},
}

# Collect answers
answers = {}
for q in range(1, 6):
    answers[q] = st.radio(
        f"Question {q}",
        options=["A", "B", "C"],
        horizontal=True,
        key=f"q{q}"
    )

st.divider()

if st.button("Show My Type Results 🚀"):
    # Map answers to types
    type_results = [mapping[i][answers[i]] for i in answers]
    counts = pd.Series(type_results).value_counts().reindex(["Fungirl", "Becky", "Peter"], fill_value=0)
    
    # Final result
    top_type = counts.idxmax()
    st.success(f"🎉 Du bist ein **{top_type}**!")
    
    # Display result-specific image
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Show result image based on type
        if top_type == "Fungirl":
            st.image("images/Fungirl-Result.png", width=300)
        elif top_type == "Becky":
            st.image("images/Becky-Result.png", width=300)
        else:  # Peter
            st.image("images/Peter-Result.png", width=300)
    
    with col2:
        # Plot bigger pie chart
        fig, ax = plt.subplots(figsize=(10, 8))  # Increased size
        
        # Define colors for each type
        colors = []
        for label in counts.index:
            if label == "Fungirl":
                colors.append("#f57d20")  # Fungirl red
            elif label == "Becky":
                colors.append("#f7aec3")  # Pink
            else:  # Peter
                colors.append("#9fdced")  # Blue
        
        # Make pie chart bigger with larger font sizes
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=colors,
               textprops={'fontsize': 14}, labeldistance=1.1)
        ax.axis('equal')
        ax.set_title('Deine Ergebnisse', fontsize=16, fontweight='bold', pad=20)
        st.pyplot(fig)

    
