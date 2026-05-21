import streamlit as st
from services.docs import (
    get_available_languages,
    load_markdown,
)

st.set_page_config(
    page_title="DataTopics • Data Engineering",
    page_icon="⚽",
    layout="wide",
)


languages = get_available_languages()


if "language" not in st.session_state:
    st.session_state.language = "en"


language_options = {
    f"{language['emoji']} {language['label']}": language["code"]
    for language in languages
}


language_columns = st.columns(len(language_options))

selected_language_label = None

for index, label in enumerate(language_options.keys()):
    with language_columns[index]:
        if st.button(
            label,
            use_container_width=True,
        ):
            selected_language_label = label


if selected_language_label is not None:
    st.session_state.language = language_options[selected_language_label]


content = load_markdown(
    st.session_state.language,
    "home.md",
)


st.markdown(content)

st.divider()

st.header("Platform Status")

st.success("Streamlit is running successfully.")
