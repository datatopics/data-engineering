import streamlit as st
from services.progress import get_modules

st.title("Learner Dashboard")

st.divider()

modules = get_modules()

completed_modules = sum(module["completed"] for module in modules)

progress_percentage = round((completed_modules / len(modules)) * 100)

next_module = next(
    (module for module in modules if not module["completed"]),
    None,
)


metric_column, next_column = st.columns([1, 2])

with metric_column:
    st.metric(
        "Course Progress",
        f"{progress_percentage}%",
    )

with next_column:
    if next_module:
        st.metric(
            "Next Module",
            (f"Module {next_module['order']:02d}"),
            next_module["title"],
        )


st.progress(progress_percentage)

st.caption(f"{completed_modules} of {len(modules)} modules completed")

st.divider()

st.subheader("Modules")

columns = st.columns(2)

for index, module in enumerate(modules):
    completed = module["completed"]

    status = "✅" if completed else "⬜"

    border_color = "#22C55E" if completed else "#2A2A2A"

    background_color = "#052E16" if completed else "#111827"

    module_label = f"Module {module['order']:02d} • {module['title']}"

    with columns[index % 2]:
        st.html(
            f"""
            <div style="
                border: 1px solid {border_color};
                border-radius: 16px;
                padding: 1rem;
                margin-bottom: 1rem;
                background-color: {background_color};
            ">
                <div style="
                    font-size: 1rem;
                    font-weight: 600;
                    margin-bottom: 0.5rem;
                    color: white;
                ">
                    {status} {module_label}
                </div>

                <div style="
                    color: #9CA3AF;
                    font-size: 0.9rem;
                ">
                    Progress tracked automatically throughout the course.
                </div>
            </div>
            """
        )
