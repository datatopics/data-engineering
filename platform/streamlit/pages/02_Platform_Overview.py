import streamlit as st
from services.platform import (
    detect_docker_services,
    detect_languages,
    detect_python_dependencies,
)

st.title("Platform Overview")

st.divider()

st.markdown(
    """
Analyze the repository to detect:

- Languages
- Python dependencies
- Docker services
- Infrastructure evolution

Depending on the project size, this process may take a few seconds.
"""
)

if "repository_analyzed" not in st.session_state:
    st.session_state.repository_analyzed = False


if st.button(
    "Analyze Repository",
    use_container_width=True,
):
    st.session_state.repository_analyzed = True


if st.session_state.repository_analyzed:
    with st.spinner("Analyzing repository..."):
        languages = detect_languages()
        dependencies = detect_python_dependencies()
        services = detect_docker_services()

    st.divider()

    st.header("Detected Languages")

    segments = ""

    for language in languages:
        segments += f"""
        <div style="
            width: {language["percentage"]}%;
            background-color: {language["color"]};
            height: 18px;
        "></div>
        """

    st.html(
        f"""
        <div style="
            display: flex;
            width: 100%;
            border-radius: 999px;
            overflow: hidden;
            margin-bottom: 1.5rem;
            height: 18px;
        ">
            {segments}
        </div>
        """
    )

    legend_columns = st.columns(3)

    for index, language in enumerate(languages):
        with legend_columns[index % 3]:
            st.html(
                f"""
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-bottom: 0.75rem;
                ">
                    <div style="
                        width: 12px;
                        height: 12px;
                        border-radius: 999px;
                        background-color: {language["color"]};
                        flex-shrink: 0;
                    "></div>

                    <span style="
                        color: white;
                        font-size: 0.95rem;
                    ">
                        <strong>{language["language"]}</strong>
                        {language["percentage"]}%
                    </span>
                </div>
                """
            )

    st.divider()

    dependency_column, services_column = st.columns(2)

    with dependency_column:
        st.subheader("Python Dependencies")

        for dependency in dependencies:
            st.code(dependency)

    with services_column:
        st.subheader("Docker Services")

        for service in services:
            st.code(service)
