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
.hero h1 { margin: 0; }

.company-card {
    padding: 22px;
    border-radius: 22px;
    color: white;
    min-height: 240px;
    box-shadow: 0 14px 24px rgba(0,0,0,0.14);
}

.card {
    padding: 18px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.05);
    margin-bottom: 14px;
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
    font-size: 1.8rem;
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
    "tagline": "Dengeli büyüme, istikrarlı nakit akışı, kontrollü halka arz.",
    "story": """
Yeni üretim hattı ve kapasite artışı için halka arza çıkıyor.
Sunum dili daha dengeli ve ölçülü.
    """,
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
    "news": [
        {"time": "Öncesi -3", "cls": "news-neutral", "text": "Yeni üretim hattı planı paylaşıldı.", "impact": 2},
        {"time": "Öncesi -1", "cls": "news-good", "text": "Halka arz fiyat aralığına dengeli talep geldi.", "impact": 1},
        {"time": "İlk Gün", "cls": "news-neutral", "text": "Halka arz sonrası dengeli açılış yaptı.", "impact": 2},
        {"time": "Gün 3", "cls": "news-good", "text": "Yatırım takvimi planlandığı şekilde ilerliyor.", "impact": 3},
        {"time": "Gün 6", "cls": "news-good", "text": "Faaliyet görünümü güçlü kaldı.", "impact": 4},
        {"time": "Gün 8", "cls": "news-good", "text": "Piyasa şirketin istikrarlı görünümünü olumlu fiyatladı.", "impact": 4},
    ],
}

company_b = {
    "name": "Lima Teknoloji A.Ş.",
    "tagline": "Agresif büyüme söylemi, yüksek heyecan, güçlü sunum.",
    "story": """
Çok etkileyici bir halka arz anlatımı var.
Pazar fırsatları büyük, anlatım dili iddialı ve dikkat çekici.
    """,
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
    "news": [
        {"time": "Öncesi -3", "cls": "news-good", "text": "Şirket agresif büyüme hedeflerini öne çıkardı.", "impact": 6},
        {"time": "Öncesi -1", "cls": "news-good", "text": "Piyasada yüksek talep beklentisi oluştu.", "impact": 7},
        {"time": "İlk Gün", "cls": "news-good", "text": "Halka arz sonrası güçlü açılış yaptı.", "impact": 5},
        {"time": "Gün 3", "cls": "news-neutral", "text": "Borç yapısı hakkında tartışmalar başladı.", "impact": -10},
        {"time": "Gün 6", "cls": "news-bad", "text": "Halka arz gelirinin önemli kısmının borç baskısını hafiflettiği konuşuldu.", "impact": -18},
        {"time": "Gün 8", "cls": "news-bad", "text": "Şirket zarar açıkladı; hissede sert satış görüldü.", "impact": -25},
    ],
}

# -------------------------------------------------
# Yardımcı fonksiyonlar
# -------------------------------------------------
def build_price_series(news_items, base=100):
    prices = [base]
    for item in news_items:
        prev = prices[-1]
        new_price = round(prev * (1 + item["impact"] / 100), 2)
        prices.append(new_price)
    return prices

def portfolio_series(a_weight, b_weight, a_series, b_series):
    wa = a_weight / 100
    wb = b_weight / 100
    return [round((wa * a) + (wb * b), 2) for a, b in zip(a_series, b_series)]

def ending_text(viewed_b, allocation_b, final_value):
    if allocation_b >= 60 and not viewed_b:
        return (
            "end-bad",
            "Sunuma Kapıldın",
            "Parlak anlatım kararını yönlendirdi. Sonraki haber akışı fiyatı sert biçimde aşağı çekti."
        )
    elif allocation_b >= 40 and viewed_b:
        return (
            "end-mid",
            "Riski Gördün Ama Aldın",
            "Veriyi gördün ama yine de yüksek ağırlık verdin. Sonuç agresif bir tercihin doğal sonucu oldu."
        )
    elif allocation_b <= 20 and viewed_b and final_value >= 105:
        return (
            "end-good",
            "Temkinli Kaldın",
            "Kararın sonradan gelen haber akışına karşı portföyünü korudu."
        )
    else:
        return (
            "end-mid",
            "Karışık Sonuç",
            "Portföyün iki farklı hikâyenin etkisini birlikte taşıdı."
        )

# -------------------------------------------------
# Fiyat serileri
# -------------------------------------------------
timeline = ["Başlangıç"] + [item["time"] for item in company_a["news"]]
a_series = build_price_series(company_a["news"])
b_series = build_price_series(company_b["news"])

# -------------------------------------------------
# Hero
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📈 Halka Arz Arenası</h1>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# İki sekme
# -------------------------------------------------
main_tab, balance_tab = st.tabs(["🎮 Oyun", "📑 Bilançolar"])

# -------------------------------------------------
# OYUN
# -------------------------------------------------
with main_tab:
    if not st.session_state.locked:
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

        st.markdown("### Haber Akışı")

        news_col1, news_col2 = st.columns(2)

        with news_col1:
            st.markdown(f"#### 🟢 {company_a['name']}")
            for item in company_a["news"][:2]:
                st.markdown(
                    f'<div class="{item["cls"]}"><b>{item["time"]}</b><br>{item["text"]}</div>',
                    unsafe_allow_html=True
                )

        with news_col2:
            st.markdown(f"#### 🔴 {company_b['name']}")
            for item in company_b["news"][:2]:
                st.markdown(
                    f'<div class="{item["cls"]}"><b>{item["time"]}</b><br>{item["text"]}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("### Portföy")
        allocation_a = st.slider(
            company_a["name"],
            min_value=0,
            max_value=100,
            value=st.session_state.allocation_a
        )
        allocation_b = 100 - allocation_a

        st.session_state.allocation_a = allocation_a
        st.session_state.allocation_b = allocation_b

        m1, m2 = st.columns(2)
        with m1:
            st.metric(company_a["name"], f"%{allocation_a}")
        with m2:
            st.metric(company_b["name"], f"%{allocation_b}")

        if st.button("Portföyü Kilitle", use_container_width=True):
            st.session_state.locked = True
            st.rerun()

    else:
        a_weight = st.session_state.allocation_a
        b_weight = st.session_state.allocation_b

        p_series = portfolio_series(a_weight, b_weight, a_series, b_series)
        final_value = p_series[-1]
        total_return = round(final_value - 100, 2)

        end_class, end_title, end_text = ending_text(
            st.session_state.viewed_b,
            b_weight,
            final_value
        )

        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">100</div>
                <div class="metric-label">Başlangıç</div>
            </div>
            """, unsafe_allow_html=True)
        with r2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{final_value:.1f}</div>
                <div class="metric-label">Yıl Sonu</div>
            </div>
            """, unsafe_allow_html=True)
        with r3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">%{total_return:.1f}</div>
                <div class="metric-label">Toplam Getiri</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="{end_class}">
            <h3 style="margin-top:0;">🏁 {end_title}</h3>
            <p style="margin-bottom:0;">{end_text}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Piyasa Fiyatları")

        chart_df = pd.DataFrame({
            "Zaman": timeline,
            company_a["name"]: a_series,
            company_b["name"]: b_series,
            "Portföy": p_series,
        }).set_index("Zaman")

        st.line_chart(chart_df, height=420)

        st.markdown("---")
        st.markdown("### Haber Akışı")

        news_col1, news_col2 = st.columns(2)

        with news_col1:
            st.markdown(f"#### 🟢 {company_a['name']}")
            for item in company_a["news"]:
                st.markdown(
                    f'<div class="{item["cls"]}"><b>{item["time"]}</b><br>{item["text"]}</div>',
                    unsafe_allow_html=True
                )

        with news_col2:
            st.markdown(f"#### 🔴 {company_b['name']}")
            for item in company_b["news"]:
                st.markdown(
                    f'<div class="{item["cls"]}"><b>{item["time"]}</b><br>{item["text"]}</div>',
                    unsafe_allow_html=True
                )

        st.markdown("---")
        st.markdown("### Yorum")

        if b_weight > 0 and not st.session_state.viewed_b:
            st.error("""
Yatırım kararında şirket anlatımı daha baskın oldu. Sonraki haber akışı ve bilanço baskısı fiyatı belirgin biçimde bozdu.
            """)
        elif b_weight > 0 and st.session_state.viewed_b:
            st.warning("""
Yatırımın, gördüğün veriye rağmen riskli tarafa anlamlı ağırlık verdi. Haber akışı bu riskin fiyatlara taşınmasına yol açtı.
            """)
        else:
            st.success("""
Portföyün, haber akışı olumsuzlaştığında daha dayanıklı kaldı.
            """)

        if st.button("Yeniden Başlat", use_container_width=True):
            st.session_state.viewed_a = False
            st.session_state.viewed_b = False
            st.session_state.locked = False
            st.session_state.allocation_a = 50
            st.session_state.allocation_b = 50
            st.rerun()

# -------------------------------------------------
# BİLANÇOLAR
# -------------------------------------------------
with balance_tab:
    t1, t2 = st.tabs([company_a["name"], company_b["name"]])

    with t1:
        st.table(company_a["balance_sheet"])
        if st.button("İncelendi", key="mark_a"):
            st.session_state.viewed_a = True
            st.rerun()

    with t2:
        st.table(company_b["balance_sheet"])
        if st.button("İncelendi ", key="mark_b"):
            st.session_state.viewed_b = True
            st.rerun()
