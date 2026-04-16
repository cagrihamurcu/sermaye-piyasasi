import streamlit as st

st.set_page_config(
    page_title="Halka Arz Süreci Uygulaması",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Sayfa stili
# -----------------------------
st.markdown("""
<style>
.hero {
    padding: 24px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1d4ed8, #06b6d4);
    color: white;
    margin-bottom: 20px;
}
.card {
    padding: 18px;
    border-radius: 18px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    margin-bottom: 12px;
}
.step-card {
    padding: 20px;
    border-radius: 18px;
    background: white;
    border-left: 6px solid #2563eb;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.small-title {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 4px;
}
.big-value {
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f172a;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar - firma bilgileri
# -----------------------------
st.sidebar.header("Firma Senaryosu")

firma_adi = st.sidebar.text_input("Firma adı", value="Nova Teknoloji A.Ş.")
sektor = st.sidebar.selectbox(
    "Sektör",
    ["Yazılım", "Üretim", "Enerji", "Lojistik", "Perakende"]
)
fon_ihtiyaci = st.sidebar.number_input(
    "Fon ihtiyacı (TL)",
    min_value=10_000_000,
    max_value=5_000_000_000,
    value=250_000_000,
    step=10_000_000,
)
fon_amaci = st.sidebar.text_area(
    "Fonun kullanım amacı",
    value="Yeni üretim hattı kurmak, teknoloji yatırımı yapmak ve kapasite artırmak."
)

# -----------------------------
# Senaryo verisi
# -----------------------------
steps = [
    {
        "title": "1. Fon İhtiyacının Doğması",
        "actor": "Firma Sahibi / Şirket Yönetimi",
        "what": f"{firma_adi}, {sektor.lower()} alanında büyümek istemektedir. Şirketin {fon_ihtiyaci:,.0f} TL tutarında kaynağa ihtiyacı vardır.",
        "why": "Şirket büyüme, yatırım, borç azaltma veya kapasite artırımı için finansman arar.",
    },
    {
        "title": "2. Halka Arz Kararı",
        "actor": "Şirket Yönetimi",
        "what": f"Şirket, banka kredisi yerine sermaye piyasasından fon toplamak için halka arz seçeneğini değerlendirir.",
        "why": "Halka arz, uzun vadeli kaynak sağlama ve şirketin bilinirliğini artırma açısından avantaj sağlayabilir.",
    },
    {
        "title": "3. Aracı Kurum ile Çalışma",
        "actor": "Aracı Kurum",
        "what": "Şirket, halka arz sürecini planlamak için bir aracı kurumla çalışır. Fiyatlama, talep toplama yapısı ve satış yöntemi belirlenir.",
        "why": "Aracı kurum, yatırımcıya ulaşma ve süreci teknik olarak yönetme açısından kritik rol oynar.",
    },
    {
        "title": "4. SPK, İzahname ve KAP Süreci",
        "actor": "SPK ve KAP",
        "what": "Şirketin finansal ve hukuki bilgileri hazırlanır, izahname oluşturulur ve gerekli açıklamalar kamuya duyurulur.",
        "why": "Bu aşama yatırımcının doğru bilgiye ulaşması ve sürecin güvenli işlemesi için gereklidir.",
    },
    {
        "title": "5. Talep Toplama",
        "actor": "Yatırımcılar",
        "what": "Yatırımcılar halka arza katılarak şirketin paylarına talepte bulunur.",
        "why": "Şirketin aradığı fon, yatırımcıların gösterdiği ilgiyle toplanır.",
    },
    {
        "title": "6. Borsada İşlem Görme",
        "actor": "Borsa İstanbul",
        "what": f"Halka arz tamamlandıktan sonra {firma_adi} payları borsada işlem görmeye başlar.",
        "why": "Borsa, şeffaf fiyat oluşumu ve ikincil piyasa likiditesi sağlar.",
    },
    {
        "title": "7. Takas ve Kayıt Süreci",
        "actor": "Takasbank ve MKK",
        "what": "İşlem sonrası takas yapılır, payların mülkiyeti kaydi sistemde yatırımcı bazında izlenir.",
        "why": "İşlem güvenliği, kayıt düzeni ve mülkiyetin doğru takibi açısından bu aşama zorunludur.",
    },
]

quiz = [
    {
        "question": "Şirket neden halka arz yolunu seçmiş olabilir?",
        "options": [
            "Yalnızca vergi ödememek için",
            "Uzun vadeli fon sağlamak için",
            "KAP’ı kapatmak için",
            "Takasbank yerine geçmek için",
        ],
        "correct": "Uzun vadeli fon sağlamak için",
    },
    {
        "question": "Halka arz sürecinde fiyatlama ve satış organizasyonunda kim öne çıkar?",
        "options": ["MKK", "Aracı Kurum", "KAP", "Yatırımcı"],
        "correct": "Aracı Kurum",
    },
    {
        "question": "Kamuyu aydınlatma ve bilgi paylaşımı açısından hangi yapı önemlidir?",
        "options": ["KAP", "Borsa İstanbul", "Takasbank", "Portföy Yönetim Şirketi"],
        "correct": "KAP",
    },
    {
        "question": "İşlem sonrası takas ve kayıt sürecinde hangi kurumlar öne çıkar?",
        "options": [
            "SPK ve Yatırımcı",
            "Takasbank ve MKK",
            "Borsa İstanbul ve KAP",
            "Aracı Kurum ve Portföy Yönetim Şirketi",
        ],
        "correct": "Takasbank ve MKK",
    },
]

# -----------------------------
# Hero
# -----------------------------
st.markdown(f"""
<div class="hero">
    <h1>📈 Halka Arz Süreci Uygulaması</h1>
    <p>
        Bu uygulamada bir firma sahibinin fon ihtiyacını <b>halka arz</b> yoluyla
        karşılaması adım adım gösterilmektedir.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Üst bilgi kartları
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="small-title">Firma</div>
        <div class="big-value">{firma_adi}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="small-title">Sektör</div>
        <div class="big-value">{sektor}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="small-title">Fon İhtiyacı</div>
        <div class="big-value">{fon_ihtiyaci:,.0f} TL</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Fonun Kullanım Amacı")
st.info(fon_amaci)

# -----------------------------
# Sekmeler
# -----------------------------
tab1, tab2 = st.tabs(["🔄 Süreç Akışı", "🧠 Mini Quiz"])

# -----------------------------
# TAB 1 - Süreç
# -----------------------------
with tab1:
    st.subheader("Halka Arz Sürecinin Akışı")

    step_titles = [step["title"] for step in steps]
    current_step = st.select_slider(
        "Aşamayı seç",
        options=step_titles,
        value=step_titles[0]
    )

    index = step_titles.index(current_step)
    selected = steps[index]

    st.progress((index + 1) / len(steps))

    st.markdown(f"""
    <div class="step-card">
        <h3>{selected['title']}</h3>
        <p><b>Bu aşamadaki ana aktör:</b> {selected['actor']}</p>
        <p><b>Senaryoda ne oluyor?</b><br>{selected['what']}</p>
        <p><b>Neden önemli?</b><br>{selected['why']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Sürecin Kısa Özeti")
    st.markdown(
        "Firma Sahibi → Aracı Kurum → SPK / KAP → Yatırımcı → Borsa İstanbul → Takasbank / MKK"
    )

# -----------------------------
# TAB 2 - Quiz
# -----------------------------
with tab2:
    st.subheader("Mini Quiz")

    answers = []
    for i, q in enumerate(quiz):
        answer = st.radio(
            f"{i+1}. {q['question']}",
            q["options"],
            index=None,
            key=f"quiz_{i}"
        )
        answers.append(answer)

    if st.button("Sonuçları Göster"):
        score = 0
        for answer, q in zip(answers, quiz):
            if answer == q["correct"]:
                score += 1

        st.success(f"Puanın: {score}/{len(quiz)}")

        if score == len(quiz):
            st.balloons()

        for i, q in enumerate(quiz):
            st.write(f"**{i+1}. soru doğru cevap:** {q['correct']}")
