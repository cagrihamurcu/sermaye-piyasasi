import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Halka Arz Arenası",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------
# Stil
# -------------------------------------------------
st.markdown("""
<style>
.hero {
    padding: 28px;
    border-radius: 26px;
    background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 45%, #06b6d4 100%);
    color: white;
    margin-bottom: 20px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.16);
}
.hero h1 { margin: 0 0 8px 0; }
.hero p { margin: 0; line-height: 1.7; font-size: 1rem; }

.card {
    padding: 18px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.05);
    margin-bottom: 14px;
}

.company-card {
    padding: 22px;
    border-radius: 22px;
    color: white;
    min-height: 250px;
    box-shadow: 0 14px 24px rgba(0,0,0,0.14);
}

.metric-box {
    padding: 14px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}
.metric-value {
    font-size: 1.9rem;
    font-weight: 700;
    color: #0f172a;
}
.metric-label {
    color: #64748b;
    font-size: 0.92rem;
}

.news-good, .news-bad, .news-neutral {
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    border: 1px solid transparent;
}
.news-good {
    background: #ecfdf5;
    border-color: #a7f3d0;
}
.news-bad {
    background: #fef2f2;
    border-color: #fecaca;
}
.news-neutral {
    background: #eff6ff;
    border-color: #bfdbfe;
}

.end-good, .end-mid, .end-bad {
    padding: 20px;
    border-radius: 18px;
    color: white;
    font-weight: 500;
}
.end-good {
    background: linear-gradient(135deg, #059669, #10b981);
}
.end-mid {
    background: linear-gradient(135deg, #d97706, #f59e0b);
}
.end-bad {
    background: linear-gradient(135deg, #b91c1c, #ef4444);
}

.small-note {
    color: #64748b;
    font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# State
# -------------------------------------------------
defaults = {
    "viewed_a": False,
    "viewed_b": False,
    "locked": False,
    "allocation_a": 50,
    "allocation_b": 50,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------------------------------------
# Şirketler
# -------------------------------------------------
company_a = {
    "name": "Anka Gıda A.Ş.",
    "tagline": "Dengeli büyüme, istikrarlı nakit akışı, daha gerçekçi halka arz hikâyesi.",
    "story": """
Anka Gıda, yeni üretim hattı yatırımı için halka arza çıkıyor.
Sunum dili sakin ve kontrollü. Yönetim, büyüme kadar riskleri de kabul ediyor.
    """,
    "return_series": [100, 102, 104, 106, 107, 110, 114, 118],
    "news": [
        ("news-neutral", "🕘 Gün 1", "Anka Gıda halka arz sonrası dengeli bir açılış yaptı."),
        ("news-good", "🕛 Gün 3", "Yatırımcı sunumlarında hedeflerin makul olduğu vurgulandı."),
        ("news-good", "🕒 Gün 6", "Şirket yeni yatırım planını takvime uygun ilerlettiğini açıkladı."),
        ("news-good", "🕕 Gün 8", "Piyasa şirketin tutarlı iletişimini olumlu fiyatladı."),
    ],
    "balance_sheet": pd.DataFrame({
        "Kalem": [
            "Nakit ve Benzerleri",
            "Kısa Vadeli Borç",
            "Uzun Vadeli Borç",
            "Özkaynak",
            "Net Kâr",
            "Cari Oran",
            "Borç / Özkaynak"
        ],
        "Değer": [
            "420 milyon TL",
            "180 milyon TL",
            "260 milyon TL",
            "1,150 milyar TL",
            "210 milyon TL",
            "1.85",
            "0.38"
        ]
    }),
    "analysis": """
Borçluluk yönetilebilir düzeydedir. Cari oran sağlıklıdır, özkaynak güçlüdür ve şirket kârlıdır.
Halka arz gelirinin üretim yatırımı için kullanılacağı açıklanmaktadır.
    """
}

company_b = {
    "name": "Lima Teknoloji A.Ş.",
    "tagline": "Parlak anlatım, agresif büyüme söylemi, yüksek heyecan.",
    "story": """
Lima Teknoloji çok etkileyici bir halka arz sunumu yapıyor.
Pazar fırsatları çok büyük gösteriliyor, anlatım dili oldukça iddialı.
İlk bakışta çok cazip görünüyor.
    """,
    "return_series": [100, 112, 119, 122, 105, 86, 66, 48],
    "news": [
        ("news-good", "🕘 Gün 1", "Lima Teknoloji halka arzda güçlü talep topladı."),
        ("news-neutral", "🕛 Gün 2", "Şirketin büyüme hikâyesi yatırımcı forumlarında yoğun ilgi gördü."),
        ("news-bad", "🕒 Gün 5", "Bilançodaki yüksek borçluluk yeniden tartışılmaya başlandı."),
        ("news-bad", "🕕 Gün 6", "Halka arz gelirinin önemli kısmının borç baskısını hafiflettiği konuşuluyor."),
        ("news-bad", "🕗 Gün 8", "Şirket zarar açıkladı; hissede sert satış görüldü."),
    ],
    "balance_sheet": pd.DataFrame({
        "Kalem": [
            "Nakit ve Benzerleri",
            "Kısa Vadeli Borç",
            "Uzun Vadeli Borç",
            "Özkaynak",
            "Net Kâr / Zarar",
            "Cari Oran",
            "Borç / Özkaynak"
        ],
        "Değer": [
            "95 milyon TL",
            "640 milyon TL",
            "980 milyon TL",
            "310 milyon TL",
            "-145 milyon TL",
            "0.72",
            "5.23"
        ]
    }),
    "analysis": """
Borç baskısı yüksektir. Kısa vadeli yükümlülükler ağırdır, şirket zarar yazmaktadır ve cari oran zayıftır.
Tanıtım dili ise bu finansal kırılganlığı geri plana itmektedir.
    """
}

# -------------------------------------------------
# Yardımcı fonksiyonlar
# -------------------------------------------------
def due_diligence_score(viewed_a: bool, viewed_b: bool, allocation_b: int) -> int:
    score = 0
    if viewed_a:
        score += 20
    if viewed_b:
        score += 40
    if viewed_b and allocation_b <= 20:
        score += 25
    elif viewed_b and allocation_b <= 40:
        score += 15
    elif allocation_b >= 60 and not viewed_b:
        score -= 20
    score += 15
    return max(0, min(100, score))

def ending_text(viewed_b: bool, allocation_b: int, final_value: float):
    if allocation_b >= 60 and not viewed_b:
        return (
            "Sunuma Kapıldın",
            "end-bad",
            "Lima Teknoloji’ye bilançosunu incelemeden yüksek ağırlık verdin. Parlak halka arz anlatımı seni çekti; ancak yüksek borçluluk ve zarar riski sonradan sert biçimde ortaya çıktı."
        )
    elif allocation_b >= 40 and viewed_b:
        return (
            "Riski Gördün Ama Aldın",
            "end-mid",
            "Lima Teknoloji’nin bilançosunu gördün ve riski bildin; buna rağmen önemli ağırlık verdin. Bu, bilinçli ama agresif bir yatırım kararı oldu."
        )
    elif allocation_b <= 20 and viewed_b and final_value >= 105:
        return (
            "Temkinli Analist",
            "end-good",
            "Bilançoyu inceledin, yüksek borçluluk riskini fark ettin ve ağırlığını sınırladın. Duygudan çok veriye göre karar verdin."
        )
    else:
        return (
            "Dengeli Oyuncu",
            "end-mid",
            "Kararın ne tamamen içgüdüsel ne de tamamen analitik kaldı. Sonuç, iki şirketin etkisini birlikte taşıyan dengeli ama sınırlı bir portföy oldu."
        )

def portfolio_series(a_weight: int, b_weight: int):
    wa = a_weight / 100
    wb = b_weight / 100
    a = company_a["return_series"]
    b = company_b["return_series"]
    portfolio = [round((wa * a_val) + (wb * b_val), 2) for a_val, b_val in zip(a, b)]
    return a, b, portfolio

# -------------------------------------------------
# Hero
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📈 Halka Arz Arenası</h1>
    <p>
        İki farklı halka arz seni bekliyor. Biri dengeli ama daha sakin, diğeri parlak ama riskli.
        Bilançolara bakmadan yatırım yapmak mümkün; fakat sürprizlere hazır olman gerekir.
    </p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Evet' if st.session_state.viewed_a else 'Hayır'}</div>
        <div class="metric-label">Anka bilançosu incelendi mi?</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Evet' if st.session_state.viewed_b else 'Hayır'}</div>
        <div class="metric-label">Lima bilançosu incelendi mi?</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    score_preview = due_diligence_score(
        st.session_state.viewed_a,
        st.session_state.viewed_b,
        st.session_state.allocation_b
    )
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{score_preview}</div>
        <div class="metric-label">Due Diligence Skoru</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Kilitli' if st.session_state.locked else 'Açık'}</div>
        <div class="metric-label">Portföy Durumu</div>
    </div>
    """, unsafe_allow_html=True)

st.progress(score_preview / 100)

# -------------------------------------------------
# Sekmeler
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Halka Arzlar",
    "📑 Bilançolar",
    "💼 Portföy Kararı",
    "🔥 Sonuç ve Haber Akışı"
])

# -------------------------------------------------
# TAB 1
# -------------------------------------------------
with tab1:
    st.subheader("Halka Arz Sunumları")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"""
        <div class="company-card" style="background: linear-gradient(135deg, #059669, #065f46);">
            <h2>🟢 {company_a['name']}</h2>
            <p><b>{company_a['tagline']}</b></p>
            <p>{company_a['story']}</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="company-card" style="background: linear-gradient(135deg, #dc2626, #7f1d1d);">
            <h2>🔴 {company_b['name']}</h2>
            <p><b>{company_b['tagline']}</b></p>
            <p>{company_b['story']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Sadece sunuma bakmak çoğu zaman yetmez. Bilançolar ayrı sekmede seni bekliyor.")

# -------------------------------------------------
# TAB 2
# -------------------------------------------------
with tab2:
    st.subheader("Bilançolar")
    t1, t2 = st.tabs([company_a["name"], company_b["name"]])

    with t1:
        st.table(company_a["balance_sheet"])
        st.success(company_a["analysis"])
        if st.button("Anka bilançosunu inceledim", key="view_a"):
            st.session_state.viewed_a = True
            st.rerun()

    with t2:
        st.table(company_b["balance_sheet"])
        st.error(company_b["analysis"])
        if st.button("Lima bilançosunu inceledim", key="view_b"):
            st.session_state.viewed_b = True
            st.rerun()

# -------------------------------------------------
# TAB 3
# -------------------------------------------------
with tab3:
    st.subheader("Portföy Kararı")
    st.markdown("Toplam 100 birim sermayeni iki halka arz arasında dağıt.")

    allocation_a = st.slider(
        f"{company_a['name']} ağırlığı",
        min_value=0,
        max_value=100,
        value=st.session_state.allocation_a
    )
    allocation_b = 100 - allocation_a

    st.session_state.allocation_a = allocation_a
    st.session_state.allocation_b = allocation_b

    c1, c2 = st.columns(2)
    with c1:
        st.metric(company_a["name"], f"%{allocation_a}")
    with c2:
        st.metric(company_b["name"], f"%{allocation_b}")

    st.markdown("---")
    current_score = due_diligence_score(
        st.session_state.viewed_a,
        st.session_state.viewed_b,
        allocation_b
    )

    st.markdown(f"**Güncel due diligence skoru:** {current_score}/100")
    st.progress(current_score / 100)

    if allocation_b >= 60 and not st.session_state.viewed_b:
        st.warning("Lima Teknoloji’ye yüksek ağırlık veriyorsun ama bilançosunu incelemedin.")
    elif allocation_b >= 40 and st.session_state.viewed_b:
        st.info("Lima Teknoloji riskli görünüyor; buna rağmen önemli ağırlık veriyorsun.")
    elif allocation_b <= 20 and st.session_state.viewed_b:
        st.success("Riskli şirketi sınırladın. Bu daha temkinli bir dağılım.")

    if st.button("Portföyü Kilitle ve Sonucu Gör", use_container_width=True):
        st.session_state.locked = True
        st.rerun()

# -------------------------------------------------
# TAB 4
# -------------------------------------------------
with tab4:
    st.subheader("Sonuç ve Haber Akışı")

    if not st.session_state.locked:
        st.warning("Önce portföyünü kilitlemelisin.")
    else:
        a_weight = st.session_state.allocation_a
        b_weight = st.session_state.allocation_b

        a_series, b_series, p_series = portfolio_series(a_weight, b_weight)
        final_value = p_series[-1]
        total_return = round(final_value - 100, 2)
        dd_score = due_diligence_score(
            st.session_state.viewed_a,
            st.session_state.viewed_b,
            b_weight
        )

        end_title, end_class, end_text = ending_text(
            st.session_state.viewed_b,
            b_weight,
            final_value
        )

        r1, r2, r3 = st.columns(3)
        with r1:
            st.metric("Başlangıç Portföyü", "100 birim")
        with r2:
            st.metric("Yıl Sonu Portföyü", f"{final_value:.1f} birim")
        with r3:
            st.metric("Toplam Getiri", f"%{total_return:.1f}")

        st.markdown(f"""
        <div class="{end_class}">
            <h3 style="margin-top:0;">🏁 Sonun: {end_title}</h3>
            <p style="margin-bottom:0;">{end_text}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Fiyat Hareketi")
        chart_df = pd.DataFrame({
            "Gün": [f"Gün {i}" for i in range(1, 9)],
            company_a["name"]: a_series,
            company_b["name"]: b_series,
            "Portföy": p_series,
        }).set_index("Gün")

        st.line_chart(chart_df, height=380)

        st.markdown("---")
        st.markdown("### Piyasa Haber Akışı")

        news_col1, news_col2 = st.columns(2)

        with news_col1:
            st.markdown(f"#### 🟢 {company_a['name']}")
            for cls, time_label, text in company_a["news"]:
                st.markdown(
                    f'<div class="{cls}"><b>{time_label}</b><br>{text}</div>',
                    unsafe_allow_html=True
                )

        with news_col2:
            st.markdown(f"#### 🔴 {company_b['name']}")
            for cls, time_label, text in company_b["news"]:
                st.markdown(
                    f'<div class="{cls}"><b>{time_label}</b><br>{text}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("---")
        st.markdown("### Oyun Yorumu")

        if b_weight > 0 and not st.session_state.viewed_b:
            st.error("""
Lima Teknoloji’ye bilançosuna bakmadan yatırım yaptın.  
Parlak anlatım seni çekti; ancak yüksek borçluluk ve zayıf finansal yapı sonradan sert biçimde ortaya çıktı.
            """)
        elif b_weight > 0 and st.session_state.viewed_b:
            st.warning("""
Riskli şirketin bilançosunu gördün. Borç baskısını fark ettin ama yine de bu riski portföyüne aldın.
            """)
        else:
            st.success("""
Riskli şirketi ya tamamen dışarıda bıraktın ya da çok sınırlı tuttun. Bu karar, portföyünü korumaya yardımcı oldu.
            """)

        st.info(f"Final due diligence skorun: **{dd_score}/100**")

        if st.button("Oyunu Yeniden Başlat", use_container_width=True):
            st.session_state.viewed_a = False
            st.session_state.viewed_b = False
            st.session_state.locked = False
            st.session_state.allocation_a = 50
            st.session_state.allocation_b = 50
            st.rerun()
