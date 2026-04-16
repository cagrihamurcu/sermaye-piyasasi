import pandas as pd
import streamlit as st

from lesson_data import (
    APP_TITLE,
    APP_SUBTITLE,
    NOTE_OVERVIEW,
    TURKEY_INTRO,
    INSTITUTIONS,
    FLOW_STEPS,
    INFO_FLOW_STEPS,
    ETHICS_TOPICS,
    MATCHING_EXERCISE,
    QUIZ_QUESTIONS,
    IPO_CASE,
    GLOSSARY,
)

st.set_page_config(
    page_title="Sermaye Piyasası Aktörleri",
    page_icon="📈",
    layout="wide",
)

CUSTOM_CSS = """
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.note-card {
    border: 1px solid #E6EAF0;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 14px;
    background: #FFFFFF;
}
.small-muted {
    color: #5B6573;
    font-size: 0.95rem;
}
.section-title {
    margin-top: 0.5rem;
    margin-bottom: 0.75rem;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def init_state() -> None:
    defaults = {
        "show_model_answer": False,
        "matching_checked": False,
        "quiz_checked": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_header() -> None:
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown("---")


def render_sidebar() -> str:
    with st.sidebar:
        st.header("Ders Uygulaması")
        section = st.radio(
            "Bölüm seçin",
            options=[
                "Ders Notu",
                "Türkiye’de Kurumsal Yapı",
                "Aktörler Arası İşleyiş",
                "Halka Arz Örneği",
                "Bilgi Akışı",
                "Riskler ve Etik",
                "Uygulama",
                "Kavramlar Sözlüğü",
            ],
            index=0,
        )
        st.markdown("---")
        st.markdown(
            """
            **Amaç:**  
            Öğrencinin sermaye piyasasındaki aktörleri yalnızca tanım düzeyinde değil,
            Türkiye’deki kurumsal karşılıkları ve işleyiş süreçleriyle birlikte
            kavramasını sağlamak.
            """
        )
    return section


def render_note_page() -> None:
    st.subheader("Ders Notu")
    st.markdown(NOTE_OVERVIEW)

    col1, col2 = st.columns(2)
    with col1:
        st.info(
            "Bu bölüm, öğrencinin konuya giriş yapmasını ve temel aktörleri çerçeve "
            "olarak görmesini sağlar."
        )
    with col2:
        st.success(
            "Daha sonra Türkiye’deki kurumsal yapı, işleyiş akışı ve uygulama "
            "bölümleri ile konu somutlaştırılır."
        )


def render_turkey_page() -> None:
    st.subheader("Türkiye’de Sermaye Piyasasının Kurumsal Yapısı")
    st.markdown(TURKEY_INTRO)

    summary_df = pd.DataFrame(
        [
            {
                "Aktör / Kurum": item["name"],
                "Temel Rol": item["role_short"],
                "Neden Önemli?": item["importance_short"],
            }
            for item in INSTITUTIONS
        ]
    )
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    st.markdown("### Kurum Bazında İnceleme")
    tabs = st.tabs([item["name"] for item in INSTITUTIONS])

    for tab, item in zip(tabs, INSTITUTIONS):
        with tab:
            st.markdown(f"#### {item['name']}")
            st.markdown(f"**Temel rolü:** {item['role_long']}")
            st.markdown("**Detaylı açıklama:**")
            st.markdown(item["detail"])
            st.markdown("**Öne çıkan işlevler:**")
            for bullet in item["bullets"]:
                st.markdown(f"- {bullet}")
            st.markdown(f"**Neden önemlidir?** {item['importance_long']}")


def render_flow_page() -> None:
    st.subheader("Aktörler Arası İşleyiş")
    st.markdown(
        """
        Aşağıdaki akış, Türkiye sermaye piyasasında yatırım kararının verilmesinden
        işlemin sonuçlanmasına kadar olan temel süreci göstermektedir.
        """
    )

    flow_text = " → ".join([step["title"] for step in FLOW_STEPS])
    st.markdown(f"### {flow_text}")

    cols = st.columns(len(FLOW_STEPS))
    for col, step in zip(cols, FLOW_STEPS):
        with col:
            st.markdown(
                f"""
                <div class="note-card">
                    <h4 class="section-title">{step['step_no']}. {step['title']}</h4>
                    <p>{step['description']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### Sürecin Yorumu")
    st.markdown(
        """
        Bu akış, sermaye piyasasının tek bir kurumdan oluşmadığını; düzenleme,
        piyasa işletimi, takas, saklama, kamuyu aydınlatma ve aracılık
        faaliyetlerinin birbirine bağlı biçimde çalıştığını gösterir.
        """
    )


def render_ipo_page() -> None:
    st.subheader("Halka Arz Süreci Üzerinden Aktör Analizi")

    st.markdown("### Senaryo")
    st.markdown(IPO_CASE["scenario"])

    st.markdown("### Öğrenciye Yöneltilebilecek Sorular")
    for q in IPO_CASE["questions"]:
        st.markdown(f"- {q}")

    st.markdown("### Öğrenci Çalışma Alanı")
    student_answer = st.text_area(
        "Kısa analizini buraya yaz:",
        height=220,
        placeholder="Şirketin neden halka arz olmak istediğini, aracı kurumun rolünü, yatırımcıyı, borsayı, takas ve bilgi akışını açıklayınız.",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Örnek çözümü göster"):
            st.session_state.show_model_answer = True
    with col2:
        if st.button("Örnek çözümü gizle"):
            st.session_state.show_model_answer = False

    if student_answer:
        st.caption("Not: Bu metin otomatik değerlendirilmez; ders içi tartışma için kullanılır.")

    if st.session_state.show_model_answer:
        st.markdown("### Örnek Çözüm Çerçevesi")
        for item in IPO_CASE["model_answer"]:
            st.markdown(f"- {item}")


def render_info_flow_page() -> None:
    st.subheader("Sermaye Piyasasında Bilgi Akışı")

    st.markdown(
        """
        Sermaye piyasalarında fiyat oluşumu yalnızca alım-satım hacmine bağlı değildir.
        Şirketlerden başlayan bilgi akışı; denetim, kamuyu aydınlatma ve piyasa yorumu
        aşamalarından geçerek yatırımcı kararlarına yansır.
        """
    )

    for step in INFO_FLOW_STEPS:
        with st.expander(f"{step['title']}", expanded=True):
            st.markdown(step["text"])

    st.warning(
        "Bilginin geç, eksik veya yanıltıcı olması durumunda fiyatlama kalitesi bozulur "
        "ve yatırımcı güveni zedelenir."
    )


def render_ethics_page() -> None:
    st.subheader("Riskler ve Etik Sorunlar")

    st.markdown(
        """
        Sermaye piyasalarında güven, hukuki düzenleme kadar etik standartlara da bağlıdır.
        Aşağıdaki başlıklar, piyasada sık tartışılan temel risk alanlarını özetlemektedir.
        """
    )

    for topic in ETHICS_TOPICS:
        st.markdown(f"### {topic['title']}")
        st.markdown(topic["text"])


def render_matching_tab() -> None:
    st.markdown("### 1. Aktör – Görev Eşleştirme")
    st.markdown(
        """
        Aşağıda her kurum için en uygun görevi seçin. Ardından **Eşleştirmeyi kontrol et**
        düğmesine basın.
        """
    )

    all_roles = list(dict.fromkeys(MATCHING_EXERCISE.values()))

    for institution in MATCHING_EXERCISE.keys():
        st.selectbox(
            f"{institution} için doğru rolü seçin",
            options=all_roles,
            index=None,
            key=f"match_{institution}",
            placeholder="Bir rol seçin",
        )

    if st.button("Eşleştirmeyi kontrol et"):
        st.session_state.matching_checked = True

    if st.session_state.matching_checked:
        correct = 0
        total = len(MATCHING_EXERCISE)

        for institution, expected_role in MATCHING_EXERCISE.items():
            selected = st.session_state.get(f"match_{institution}")
            if selected == expected_role:
                correct += 1

        st.metric("Doğru eşleştirme", f"{correct} / {total}")

        for institution, expected_role in MATCHING_EXERCISE.items():
            selected = st.session_state.get(f"match_{institution}")
            if selected == expected_role:
                st.success(f"{institution}: doğru")
            else:
                st.error(
                    f"{institution}: yanlış. Doğru cevap: {expected_role}"
                )


def render_quiz_tab() -> None:
    st.markdown("### 2. Kısa Test")

    for idx, question in enumerate(QUIZ_QUESTIONS, start=1):
        st.radio(
            f"{idx}. {question['question']}",
            options=question["options"],
            index=None,
            key=f"quiz_{idx}",
        )
        st.markdown("")

    if st.button("Testi değerlendir"):
        st.session_state.quiz_checked = True

    if st.session_state.quiz_checked:
        score = 0
        for idx, question in enumerate(QUIZ_QUESTIONS, start=1):
            user_answer = st.session_state.get(f"quiz_{idx}")
            if user_answer == question["correct"]:
                score += 1

        st.metric("Test puanı", f"{score} / {len(QUIZ_QUESTIONS)}")

        with st.expander("Açıklamalı cevap anahtarı", expanded=True):
            for idx, question in enumerate(QUIZ_QUESTIONS, start=1):
                user_answer = st.session_state.get(f"quiz_{idx}")
                st.markdown(f"**{idx}. soru**")
                st.markdown(f"- Senin cevabın: {user_answer}")
                st.markdown(f"- Doğru cevap: {question['correct']}")
                st.markdown(f"- Açıklama: {question['explanation']}")


def render_case_tab() -> None:
    st.markdown("### 3. Vaka Analizi")
    st.markdown(
        """
        Aşağıdaki kısa vakayı değerlendirip kendi yorumunu yaz. Sonrasında örnek çözüm
        mantığıyla karşılaştır.
        """
    )
    st.markdown(IPO_CASE["scenario"])

    st.text_area(
        "Vaka analizin",
        height=220,
        key="case_analysis",
        placeholder="Fon ihtiyacının nedeni, kurumların sürece katkısı, bilgi akışı ve yatırımcı açısından değerlendirme...",
    )

    with st.expander("Örnek çözüm mantığı", expanded=False):
        for item in IPO_CASE["model_answer"]:
            st.markdown(f"- {item}")


def render_practice_page() -> None:
    st.subheader("Uygulama Bölümü")
    st.markdown(
        """
        Bu bölüm dersin ölçme-değerlendirme ve sınıf içi uygulama kısmı olarak
        kullanılabilir.
        """
    )

    tab1, tab2, tab3 = st.tabs(
        ["Aktör Eşleştirme", "Kısa Test", "Vaka Analizi"]
    )

    with tab1:
        render_matching_tab()

    with tab2:
        render_quiz_tab()

    with tab3:
        render_case_tab()


def render_glossary_page() -> None:
    st.subheader("Kavramlar Sözlüğü")
    for term, explanation in GLOSSARY.items():
        with st.expander(term):
            st.markdown(explanation)


def main() -> None:
    init_state()
    render_header()
    section = render_sidebar()

    if section == "Ders Notu":
        render_note_page()
    elif section == "Türkiye’de Kurumsal Yapı":
        render_turkey_page()
    elif section == "Aktörler Arası İşleyiş":
        render_flow_page()
    elif section == "Halka Arz Örneği":
        render_ipo_page()
    elif section == "Bilgi Akışı":
        render_info_flow_page()
    elif section == "Riskler ve Etik":
        render_ethics_page()
    elif section == "Uygulama":
        render_practice_page()
    elif section == "Kavramlar Sözlüğü":
        render_glossary_page()


if __name__ == "__main__":
    main()
