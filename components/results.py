import streamlit as st

from services.predictor import predict_style
from services.retrieval import find_similar_paintings


def render_results(image, mode):

    result = predict_style(image)

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Результат анализа")

        st.write(f"**Определённый стиль:** {result['label']}")
        st.write(f"**Уверенность:** {result['confidence']}%")

        st.markdown("### Распределение вероятностей")

        # сортируем от большего к меньшему
        sorted_probs = sorted(
            result["all_probs"].items(),
            key=lambda x: x[1],
            reverse=True
        )

        for label, prob in sorted_probs:

            st.write(f"{label}: {prob:.2f}%")
            st.progress(prob / 100)

    with col2:

        st.markdown(
            f"""
            <div class="score-box">
                <div class="score-number">
                    {result["confidence"]:.0f}%
                </div>
                <div class="score-label">
                    {result["label"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ======================================
    # ПОХОЖИЕ КАРТИНЫ
    # ======================================

    if result["label"] == "барокко":

        st.success(f"Обнаружено: Барокко ({result['confidence']}%)")

        st.markdown("### Похожие произведения")

        similar = find_similar_paintings(image)

        cols = st.columns(5)

        for col, img in zip(cols, similar):
            with col:
                st.image(img, use_container_width=True)

    else:

        st.warning(
            f"Основной стиль: {result['label']} ({result['confidence']}%)"
        )