import time
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
    min-height: 235px;
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

.big-news {
    padding: 18px;
    border-radius: 18px;
    background: white;
    border-left: 8px solid #2563eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.05);
    margin-bottom: 14px;
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

.ticker-wrap {
    overflow: hidden;
    white-space: nowrap;
    background: #0f172a;
    color: white;
    border-radius: 14px;
    padding: 12px 0;
    margin-bottom: 16px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.10);
}
.ticker-text {
    display: inline-block;
    padding-left: 100%;
    animation: ticker 18s linear infinite;
    font-weight: 600;
}
@keyframes ticker {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# State
# -------------------------------------------------
defaults = {
    "viewed_a": False,
    "viewed_b": False,
    "selected": None,
    "played": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------------------------------------
# Veri
# -------------------------------------------------
companies = {
    "A": {
        "name": "Anka Gıda A.Ş.",
        "color_1": "#059669",
        "color_2": "#065f46",
        "tagline": "Dengeli büyüme, kontrollü halka arz.",
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
            {"phase": "Halka arz öncesi", "cls": "news-neutral", "headline": "Yeni üretim hattı planı açıklandı.", "impact": 2},
            {"phase": "Talep dönemi", "cls": "news-good", "headline": "Halka arz fiyat aralığına dengeli talep geldi.", "impact": 1},
            {"phase": "İlk işlem günü", "cls": "news-neutral", "headline": "Hisse sakin ama güçlü açıldı.", "impact": 2},
            {"phase": "Hafta 1", "cls": "news-good", "headline": "Yatırım takviminin planlandığı açıklandı.", "impact": 3},
            {"phase": "Hafta 2", "cls": "news-good", "headline": "Operasyonel görünüm güçlü kaldı.", "impact": 4},
            {"phase": "Ay sonu", "cls": "news-good", "headline": "Piyasa şirketi olumlu fiyatlamaya devam etti.", "impact": 4},
        ],
    },
    "B": {
        "name": "Lima Teknoloji A.Ş.",
        "color_1": "#dc2626",
        "color_2": "#7f1d1d",
        "tagline": "Agresif büyüme söylemi, güçlü heyecan.",
        "story": """
Çok etkileyici bir halka arz anlatımı var.
Pazar fırsatları büyük gösteriliyor, anlatım dili son derece iddialı.
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
            {"phase": "Halka arz öncesi", "cls": "news-good", "headline": "Şirket agresif büyüme hedeflerini öne çıkardı.", "impact": 6},
            {"phase": "Talep dönemi", "cls": "news-good", "headline": "Piyasada yüksek talep beklentisi oluştu.", "impact": 7},
            {"phase": "İlk işlem günü", "cls": "news-good", "headline": "Hisse güçlü açıldı, ilgi yüksekti.", "impact": 5},
            {"phase": "Hafta 1", "cls": "news-neutral", "headline": "Borç yapısına dair soru işaretleri arttı.", "impact": -10},
            {"phase": "Hafta 2", "cls": "news-bad", "headline": "Halka arz gelirinin önemli kısmının borç baskısını hafiflettiği konuşuldu.", "impact": -18},
            {"phase": "Ay sonu", "cls": "news-bad", "headline": "Şirket zarar açıkladı; hissede sert satış görüldü.", "impact": -25},
        ],
    },
}

# -------------------------------------------------
# Yardımcılar
# -------------------------------------------------
def selected_company():
    if st.session_state.selected is None:
        return None
    return companies[st.session_state.selected]

def selected_balance_viewed():
    if st.session_state.selected == "A":
        return st.session_state.viewed_a
    if st.session_state.selected == "B":
        return st.session_state.viewed_b
    return False

def build_state(company, step_count):
    labels = ["Başlangıç"]
    prices = [100.0]
    shown_news = company["news"][:step_count]

    for item in shown_news:
        labels.append(item["phase"])
        prices.append(round(prices[-1] * (1 + item["impact"] / 100), 2))

    return labels, prices, shown_news

def render_ticker(shown_news):
    if not shown_news:
        return ""
    ticker_text = " • ".join([item["headline"] for item in shown_news])
    return f"""
    <div class="ticker-wrap">
        <div class="ticker-text">SON DAKİKA • {ticker_text} •</div>
    </div>
    """

def render_feed_html(shown_news):
    html = ""
    for item in shown_news:
        html += f'<div class="{item["cls"]}"><b>{item["phase"]}</b><br>{item["headline"]}</div>'
    return html

def ending_block(company_key, viewed_balance, final_price):
    if company_key == "B" and not viewed_balance:
        return ("end-bad", "Sürpriz Son", "Seçimin sonradan gelen haberlerle sert biçimde bozuldu.")
    if company_key == "B" and viewed_balance:
        return ("end-mid", "Agresif Son", "Seçimin güçlü hikâyesini koruyamadı; haberler fiyatı aşağı çekti.")
    if company_key == "A" and final_price >= 110:
        return ("end-good", "Dengeli Son", "Haber akışı fiyatı kademeli biçimde yukarı taşıdı.")
    return ("end-mid", "Karışık Sonuç", "Seçimin haber akışına göre dalgalı bir sonuç verdi.")

def reset_game():
    st.session_state.selected = None
    st.session_state.played = False

def autoplay_news(company):
    ticker_ph = st.empty()
    metrics_ph = st.empty()
    current_news_ph = st.empty()
    chart_ph = st.empty()
    feed_title_ph = st.empty()
    feed_ph = st.empty()

    for step in range(1, len(company["news"]) + 1):
        labels, prices, shown_news = build_state(company, step)
        latest = shown_news[-1]

        ticker_ph.markdown(render_ticker(shown_news), unsafe_allow_html=True)

        c1, c2, c3 = metrics_ph.columns(3)
        with c1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{company['name']}</div>
                <div class="metric-label">Seçilen Şirket</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{prices[-1]:.2f}</div>
                <div class="metric-label">Güncel Fiyat Endeksi</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{step}/{len(company['news'])}</div>
                <div class="metric-label">Haber Akışı</div>
            </div>
            """, unsafe_allow_html=True)

        current_news_ph.markdown(
            f"""
            <div class="big-news">
                <h3 style="margin-top:0;">{latest['phase']}</h3>
                <p style="font-size:1.05rem; margin-bottom:0;">{latest['headline']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        chart_df = pd.DataFrame({
            "Zaman": labels,
            "Fiyat": prices,
        }).set_index("Zaman")
        chart_ph.line_chart(chart_df, height=380)

        feed_title_ph.markdown("### Haber Akışı")
        feed_ph.markdown(render_feed_html(shown_news), unsafe_allow_html=True)

        time.sleep(1.4)

# -------------------------------------------------
# Başlık
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📈 Halka Arz Arenası</h1>
</div>
""", unsafe_allow_html=True)

main_tab, balance_tab = st.tabs(["🎮 Oyun", "📑 Bilançolar"])

# -------------------------------------------------
# Oyun
# -------------------------------------------------
with main_tab:
    if not st.session_state.played:
        left, right = st.columns(2)

        with left:
            a = companies["A"]
            st.markdown(f"""
            <div class="company-card" style="background: linear-gradient(135deg, {a["color_1"]}, {a["color_2"]});">
                <h2>🟢 {a["name"]}</h2>
                <p><b>{a["tagline"]}</b></p>
                <p>{a["story"]}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{a['name']} Seç", use_container_width=True):
                st.session_state.selected = "A"
                st.rerun()

        with right:
            b = companies["B"]
            st.markdown(f"""
            <div class="company-card" style="background: linear-gradient(135deg, {b["color_1"]}, {b["color_2"]});">
                <h2>🔴 {b["name"]}</h2>
                <p><b>{b["tagline"]}</b></p>
                <p>{b["story"]}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{b['name']} Seç", use_container_width=True):
                st.session_state.selected = "B"
                st.rerun()

        if st.session_state.selected is not None:
            company = selected_company()
            st.markdown("### Seçim")
            st.markdown(f"**{company['name']}**")
            if st.button("Akışı Başlat", use_container_width=True):
                autoplay_news(company)
                st.session_state.played = True
                st.rerun()

    else:
        company = selected_company()
        labels, prices, shown_news = build_state(company, len(company["news"]))
        final_price = prices[-1]

        st.markdown(render_ticker(shown_news), unsafe_allow_html=True)

        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{company['name']}</div>
                <div class="metric-label">Seçilen Şirket</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{final_price:.2f}</div>
                <div class="metric-label">Final Fiyat Endeksi</div>
            </div>
            """, unsafe_allow_html=True)

        chart_df = pd.DataFrame({
            "Zaman": labels,
            "Fiyat": prices,
        }).set_index("Zaman")
        st.line_chart(chart_df, height=380)

        st.markdown("### Haber Akışı")
        st.markdown(render_feed_html(shown_news), unsafe_allow_html=True)

        end_class, end_title, end_text = ending_block(
            st.session_state.selected,
            selected_balance_viewed(),
            final_price
        )
        st.markdown(f"""
        <div class="{end_class}">
            <h3 style="margin-top:0;">🏁 {end_title}</h3>
            <p style="margin-bottom:0;">{end_text}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Yorum")
        if st.session_state.selected == "B" and not selected_balance_viewed():
            st.error("Seçimin, haber akışı ilerledikçe çok daha kırılgan hale geldi.")
        elif st.session_state.selected == "B" and selected_balance_viewed():
            st.warning("Fiyat, sonraki haberlerle seçiminin risk tarafını açığa çıkardı.")
        else:
            st.success("Haber akışı fiyatı daha dengeli bir patikada tuttu.")

        if st.button("Başa Dön", use_container_width=True):
            reset_game()
            st.rerun()

# -------------------------------------------------
# Bilançolar
# -------------------------------------------------
with balance_tab:
    t1, t2 = st.tabs([companies["A"]["name"], companies["B"]["name"]])

    with t1:
        st.table(companies["A"]["balance_sheet"])
        if st.button("İncelendi", key="mark_a"):
            st.session_state.viewed_a = True
            st.rerun()

    with t2:
        st.table(companies["B"]["balance_sheet"])
        if st.button("İncelendi", key="mark_b"):
            st.session_state.viewed_b = True
            st.rerun()
