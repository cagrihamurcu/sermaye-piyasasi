import streamlit as st

st.set_page_config(
    page_title="Sermaye Piyasası Aktörleri Uygulaması",
    page_icon="📈",
    layout="wide",
)

# -----------------------------
# Veri
# -----------------------------
INSTITUTIONS = {
    "SPK": {
        "icon": "🛡️",
        "short": "Düzenler, denetler, yatırımcıyı korur.",
        "detail": """
**SPK**, sermaye piyasasının kurallarını belirleyen ve piyasa disiplinini gözeten yapıdır.  
Halka arz, kamuyu aydınlatma, yatırım kuruluşları, fonlar ve yatırımcı koruması gibi alanlarda
çerçeveyi oluşturur.
        """,
        "role": "Piyasa düzenlemesi ve yatırımcı korunması",
        "color": "#5B8DEF",
    },
    "Borsa İstanbul": {
        "icon": "🏛️",
        "short": "Fiyat oluşumunun merkezidir.",
        "detail": """
**Borsa İstanbul**, alıcı ve satıcıların organize piyasada karşılaştığı yapıdır.  
Pay, borçlanma araçları ve türev ürünler gibi araçlar burada işlem görür.
        """,
        "role": "Organize piyasa ve fiyat oluşumu",
        "color": "#8E6FF7",
    },
    "Takasbank": {
        "icon": "🔄",
        "short": "Takas ve risk yönetimi sağlar.",
        "detail": """
**Takasbank**, işlem sonrası takas süreçlerinde ve belirli piyasalarda merkezi karşı taraf
mantığında kritik rol oynar. İşlem güvenliğini güçlendirir.
        """,
        "role": "Takas, teminat ve işlem güvenliği",
        "color": "#00B894",
    },
    "MKK": {
        "icon": "🗂️",
        "short": "Kaydi sistemde kayıt ve izleme yapar.",
        "detail": """
**MKK**, menkul kıymetlerin yatırımcı bazında elektronik olarak izlenmesini sağlar.  
Fiziki belge yerine kaydi sistem mantığıyla çalışılır.
        """,
        "role": "Merkezi kayıt ve saklama altyapısı",
        "color": "#F39C12",
    },
    "KAP": {
        "icon": "📢",
        "short": "Kamuyu aydınlatma merkezidir.",
        "detail": """
**KAP**, şirketlerin ve piyasa kurumlarının kamuya açıklamak zorunda olduğu bilgi ve belgelerin
duyurulduğu platformdur. Bilgiye eş zamanlı erişim açısından çok önemlidir.
        """,
        "role": "Bilgi paylaşımı ve şeffaflık",
        "color": "#E74C3C",
    },
    "Aracı Kurumlar": {
        "icon": "🤝",
        "short": "Yatırımcı ile piyasa arasında köprüdür.",
        "detail": """
**Aracı kurumlar**, yatırımcıların emirlerini piyasaya iletir, alım-satım aracılığı yapar ve
bazı durumlarda araştırma ya da danışmanlık desteği sunar.
        """,
        "role": "Yatırımcı erişimi ve aracılık hizmeti",
        "color": "#16A085",
    },
    "Portföy Yönetim Şirketleri": {
        "icon": "📊",
        "short": "Fon ve portföyleri profesyonel yönetir.",
        "detail": """
**Portföy yönetim şirketleri**, yatırım fonları, emeklilik fonları ve bireysel portföyleri
risk-getiri dengesi içinde yönetir.
        """,
        "role": "Profesyonel fon yönetimi",
        "color": "#D35400",
    },
    "Yatırımcı": {
        "icon": "👤",
        "short": "Tasarrufu yatırıma dönüştürür.",
        "detail": """
**Yatırımcı**, sermaye piyasasının talep tarafıdır. Bilgiye, risk algısına ve beklentilere göre
yatırım kararları verir.
        """,
        "role": "Fon arzı ve yatırım kararı",
        "color": "#2D3436",
    },
}

PROCESS_STEPS = [
    ("Tasarruf Sahibi", "Yatırım yapma kararı verir."),
    ("Aracı Kurum", "Yatırımcının emirlerini piyasaya taşır."),
    ("Borsa İstanbul", "Emirler eşleşir, fiyat oluşur."),
    ("Takasbank", "İşlem sonrası takas ve güvence süreci işler."),
    ("MKK", "Kayıt ve mülkiyet izleme sağlanır."),
    ("KAP / Bilgi Akışı", "Piyasa bilgisi yatırımcıya şeffaf biçimde ulaşır."),
]

QUIZ = [
    {
        "question": "Türkiye’de sermaye piyasasının düzenleyici otoritesi hangisidir?",
        "options": ["Borsa İstanbul", "SPK", "MKK", "Takasbank"],
        "correct": "SPK",
        "explanation": "SPK düzenleme, denetim ve yatırımcı koruması bakımından merkezî yapıdır.",
    },
    {
        "question": "İşlem sonrası takas ve güvenlik yapısında en kritik kurumlardan biri hangisidir?",
        "options": ["KAP", "TSPB", "Takasbank", "Aracı Kurum"],
        "correct": "Takasbank",
        "explanation": "Takasbank işlem sonrası süreç ve risk yönetiminde öne çıkar.",
    },
    {
        "question": "Şirket açıklamalarının yatırımcıya ulaştığı şeffaflık platformu hangisidir?",
        "options": ["KAP", "MKK", "SPK", "VİOP"],
        "correct": "KAP",
        "explanation": "Kamuyu aydınlatma ve bilgi akışının merkezinde KAP yer alır.",
    },
    {
        "question": "Yatırımcı ile organize piyasa arasındaki bağlantıyı en çok hangi kurum kurar?",
        "options": ["Aracı Kurum", "MKK", "SPK", "Portföy Yönetim Şirketi"],
        "correct": "Aracı Kurum",
        "explanation": "Aracı kurumlar yatırımcının piyasaya erişiminde köprü görevi görür.",
    },
]

MATCHING = {
    "SPK": "Piyasa düzenlemesi ve yatırımcı korunması",
    "Borsa İstanbul": "Organize piyasa ve fiyat oluşumu",
    "Takasbank": "Takas, teminat ve işlem güvenliği",
    "MKK": "Merkezi kayıt ve saklama altyapısı",
    "KAP": "Bilgi paylaşımı ve şeffaflık",
    "Aracı Kurumlar": "Yatırımcı erişimi ve aracılık hizmeti",
    "Portföy Yönetim Şirketleri": "Profesyonel fon yönetimi",
    "Yatırımcı": "Fon arzı ve yatırım kararı",
}

# -----------------------------
# State
# -----------------------------
if "selected_institution" not in st.session_state:
    st.session_state.selected_institution = "SPK"

if "explored" not in st.session_state:
    st.session_state.explored = []

if "matching_checked" not in st.session_state:
    st.session_state.matching_checked = False

if "quiz_checked" not in st.session_state:
    st.session_state.quiz_checked = False

if "challenge_score" not in st.session_state:
    st.session_state.challenge_score = 0

# -----------------------------
# Stil
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #F7F9FC 0%, #FFFFFF 100%);
    }

    .hero {
        padding: 28px;
        border-radius: 24px;
        background: linear-gradient(135deg, #111827 0%, #4F46E5 45%, #06B6D4 100%);
        color: white;
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    .hero h1 {
        margin: 0 0 8px 0;
        font-size: 2.2rem;
    }

    .hero p {
        margin: 0;
        font-size: 1.02rem;
        line-height: 1.7;
        opacity: 0.95;
    }

    .glass-card {
        padding: 18px;
        border-radius: 22px;
        background: rgba(255,255,255,0.9);
        border: 1px solid rgba(0,0,0,0.06);
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        min-height: 220px;
    }

    .metric-card {
        padding: 18px;
        border-radius: 20px;
        background: white;
        border: 1px solid #EEF2F7;
        box-shadow: 0 8px 20px rgba(15,23,42,0.06);
        text-align: center;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #111827;
    }

    .metric-label {
        color: #6B7280;
        font-size: 0.95rem;
    }

    .inst-card {
        padding: 18px;
        border-radius: 20px;
        color: white;
        min-height: 170px;
        box-shadow: 0 12px 24px rgba(0,0,0,0.10);
    }

    .inst-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .inst-short {
        font-size: 0.96rem;
        line-height: 1.55;
        opacity: 0.96;
    }

    .section-head {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .timeline-card {
        padding: 16px;
        border-radius: 18px;
        background: white;
        border-left: 6px solid #4F46E5;
        box-shadow: 0 8px 18px rgba(0,0,0,0.05);
        min-height: 140px;
    }

    .challenge-box {
        padding: 20px;
        border-radius: 22px;
        background: linear-gradient(135deg, #F8FAFF 0%, #EEF4FF 100%);
        border: 1px solid #DCE7FF;
        box-shadow: 0 8px 24px rgba(79,70,229,0.08);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Yardımcılar
# -----------------------------
def add_explored(name: str) -> None:
    if name not in st.session_state.explored:
        st.session_state.explored.append(name)


def overall_progress() -> int:
    explored_ratio = len(st.session_state.explored) / len(INSTITUTIONS)
    quiz_ratio = min(st.session_state.challenge_score / 12, 1)
    return int(((explored_ratio * 0.55) + (quiz_ratio * 0.45)) * 100)


# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>📈 Sermaye Piyasası Aktörleri Uygulaması</h1>
        <p>
            Bu uygulama, Türkiye sermaye piyasasındaki temel aktörleri <b>keşfetme</b>,
            süreçleri <b>simüle etme</b> ve öğrendiklerini <b>uygulama modunda test etme</b>
            amacıyla tasarlanmıştır.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Üst özet alanı
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{len(st.session_state.explored)}</div>
            <div class="metric-label">Keşfedilen Aktör</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{st.session_state.challenge_score}</div>
            <div class="metric-label">Challenge Puanı</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">%{overall_progress()}</div>
            <div class="metric-label">Tamamlanma</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.progress(overall_progress() / 100)

# -----------------------------
# Ana sekmeler
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏛️ Kurum Haritası", "🔄 Süreç Simülatörü", "📢 Bilgi Akışı", "🧠 Challenge Modu"]
)

# -----------------------------
# TAB 1 - Kurum Haritası
# -----------------------------
with tab1:
    st.markdown("## Türkiye Sermaye Piyasası Kurum Haritası")
    st.caption("Kartlardan bir kurumu seç, detay panelinde rolünü incele.")

    names = list(INSTITUTIONS.keys())

    for row_start in range(0, len(names), 4):
        row_items = names[row_start: row_start + 4]
        cols = st.columns(4)

        for col, name in zip(cols, row_items):
            item = INSTITUTIONS[name]
            with col:
                st.markdown(
                    f"""
                    <div class="inst-card" style="background: linear-gradient(135deg, {item['color']} 0%, #111827 140%);">
                        <div style="font-size: 1.8rem;">{item['icon']}</div>
                        <div class="inst-title">{name}</div>
                        <div class="inst-short">{item['short']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(f"{name} İncele", key=f"btn_{name}", use_container_width=True):
                    st.session_state.selected_institution = name
                    add_explored(name)

    st.markdown("---")
    selected = INSTITUTIONS[st.session_state.selected_institution]

    st.markdown(
        f"""
        <div class="glass-card">
            <h3>{selected['icon']} {st.session_state.selected_institution}</h3>
            <p><b>Temel rol:</b> {selected['role']}</p>
            <p>{selected['detail']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# TAB 2 - Süreç Simülatörü
# -----------------------------
with tab2:
    st.markdown("## Süreç Simülatörü")
    st.caption("Aşağıdaki kaydırıcıyı kullanarak işlemin hangi aşamada olduğunu gör.")

    labels = [f"{i+1}. {step[0]}" for i, step in enumerate(PROCESS_STEPS)]
    current = st.select_slider(
        "Aşama seç",
        options=labels,
        value=labels[0],
    )

    idx = labels.index(current)
    title, desc = PROCESS_STEPS[idx]

    st.markdown(
        f"""
        <div class="glass-card">
            <h3>📍 {current}</h3>
            <p style="font-size:1.05rem;"><b>{title}</b></p>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Akış Görünümü")
    cols = st.columns(len(PROCESS_STEPS))
    for i, (col, step) in enumerate(zip(cols, PROCESS_STEPS)):
        active = i == idx
        border = "#4F46E5" if active else "#D1D5DB"
        bg = "#EEF2FF" if active else "#FFFFFF"
        with col:
            st.markdown(
                f"""
                <div class="timeline-card" style="border-left-color:{border}; background:{bg};">
                    <b>{i+1}. {step[0]}</b>
                    <p style="margin-top:8px;">{step[1]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -----------------------------
# TAB 3 - Bilgi Akışı
# -----------------------------
with tab3:
    st.markdown("## Bilgi Akışı ve Şeffaflık")
    st.caption("Bilgi akışı, fiyatlamayı ve yatırımcı kararlarını doğrudan etkiler.")

    flow_cols = st.columns(5)
    info_cards = [
        ("1", "Şirket Açıklaması", "Finansal tablo, faaliyet raporu, önemli kararlar"),
        ("2", "Denetim / Kontrol", "Bilginin güvenilirliğinin desteklenmesi"),
        ("3", "KAP Yayını", "Bilginin tüm yatırımcılara görünür hale gelmesi"),
        ("4", "Analiz", "Piyasa aktörlerinin veriyi yorumlaması"),
        ("5", "Yatırım Kararı", "Bilginin fiyat davranışına dönüşmesi"),
    ]

    for col, item in zip(flow_cols, info_cards):
        with col:
            st.markdown(
                f"""
                <div class="timeline-card">
                    <div style="font-size:1.5rem; font-weight:700; color:#4F46E5;">{item[0]}</div>
                    <div style="font-weight:700; margin:8px 0;">{item[1]}</div>
                    <div>{item[2]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown(
        """
        ### Neden önemli?
        - Bilgi **eş zamanlı** paylaşılmazsa piyasa adaleti bozulur.  
        - Bilgi **eksik** ya da **yanıltıcı** olursa yatırımcı yanlış karar verebilir.  
        - Bilgi akışı güçlü olduğunda fiyatlar daha sağlıklı oluşur.
        """
    )

# -----------------------------
# TAB 4 - Challenge
# -----------------------------
with tab4:
    st.markdown("## Challenge Modu")
    st.markdown(
        """
        <div class="challenge-box">
            Burada iki uygulama var:  
            <b>1.</b> Aktör-Görev eşleştirmesi  
            <b>2.</b> Kısa test  
            Doğru cevapların puanı üstteki skora yansır.
        </div>
        """,
        unsafe_allow_html=True,
    )

    sub1, sub2 = st.tabs(["🎯 Eşleştirme", "📝 Kısa Test"])

    with sub1:
        st.markdown("### Aktör – Görev Eşleştirme")

        roles = list(dict.fromkeys(MATCHING.values()))
        for inst in MATCHING.keys():
            st.selectbox(
                f"{inst} için doğru görevi seç",
                options=roles,
                index=None,
                key=f"match_{inst}",
                placeholder="Bir görev seç",
            )

        if st.button("Eşleştirmeyi kontrol et", use_container_width=True):
            st.session_state.matching_checked = True

            correct = 0
            for inst, expected in MATCHING.items():
                if st.session_state.get(f"match_{inst}") == expected:
                    correct += 1

            st.session_state.challenge_score = correct

        if st.session_state.matching_checked:
            correct = 0
            total = len(MATCHING)

            for inst, expected in MATCHING.items():
                selected_role = st.session_state.get(f"match_{inst}")
                if selected_role == expected:
                    correct += 1

            st.metric("Eşleştirme skoru", f"{correct}/{total}")

            for inst, expected in MATCHING.items():
                selected_role = st.session_state.get(f"match_{inst}")
                if selected_role == expected:
                    st.success(f"{inst}: doğru")
                else:
                    st.error(f"{inst}: yanlış — doğru cevap: {expected}")

    with sub2:
        st.markdown("### Kısa Test")

        for i, q in enumerate(QUIZ, start=1):
            st.radio(
                f"{i}. {q['question']}",
                q["options"],
                index=None,
                key=f"quiz_{i}",
            )
            st.markdown("")

        if st.button("Testi değerlendir", use_container_width=True):
            st.session_state.quiz_checked = True

            score = 0
            for i, q in enumerate(QUIZ, start=1):
                if st.session_state.get(f"quiz_{i}") == q["correct"]:
                    score += 1

            # eşleştirme puanı üstüne ekleniyor
            matching_score = 0
            for inst, expected in MATCHING.items():
                if st.session_state.get(f"match_{inst}") == expected:
                    matching_score += 1

            st.session_state.challenge_score = matching_score + score

            if score >= 3:
                st.balloons()

        if st.session_state.quiz_checked:
            score = 0
            for i, q in enumerate(QUIZ, start=1):
                if st.session_state.get(f"quiz_{i}") == q["correct"]:
                    score += 1

            st.metric("Test skoru", f"{score}/{len(QUIZ)}")

            with st.expander("Açıklamalı cevap anahtarı", expanded=True):
                for i, q in enumerate(QUIZ, start=1):
                    user_answer = st.session_state.get(f"quiz_{i}")
                    st.markdown(f"**{i}. soru**")
                    st.markdown(f"- Senin cevabın: {user_answer}")
                    st.markdown(f"- Doğru cevap: {q['correct']}")
                    st.markdown(f"- Açıklama: {q['explanation']}")

    if st.session_state.challenge_score >= 10:
        st.success("Harika! Konuyu güçlü biçimde kavradın.")
    elif st.session_state.challenge_score >= 6:
        st.info("İyi gidiyorsun. Birkaç kurumu daha keşfedip tekrar deneyebilirsin.")
    else:
        st.warning("Önce kurum haritasını inceleyip sonra challenge moduna dönmen iyi olur.")
