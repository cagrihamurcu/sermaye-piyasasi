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
    animation: ticker 14s linear infinite;
    font-weight: 600;
}
@keyframes ticker {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

.action-log {
    padding: 12px 14px;
    border-radius: 12px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

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
            {"phase": "Talep dönemi", "cls": "news-good", "headline": "Fiyat aralığına dengeli talep geldi.", "impact": 1},
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
# State
# -------------------------------------------------
defaults = {
    "viewed_a": False,
    "viewed_b": False,
    "selected": None,
    "started": False,
    "news_step": 0,
    "price_history": [100.0],
    "timeline": ["Başlangıç"],
    "shown_news": [],
    "cash": 100.0,
    "shares": 0.0,
    "action_done": False,
    "trade_log": [],
    "finished": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------------------------------------
# Yardımcılar
# -------------------------------------------------
def reset_game():
    st.session_state.selected = None
    st.session_state.started = False
    st.session_state.news_step = 0
    st.session_state.price_history = [100.0]
    st.session_state.timeline = ["Başlangıç"]
    st.session_state.shown_news = []
    st.session_state.cash = 100.0
    st.session_state.shares = 0.0
    st.session_state.action_done = False
    st.session_state.trade_log = []
    st.session_state.finished = False

def selected_company():
    if st.session_state.selected is None:
        return None
    return companies[st.session_state.selected]

def current_price():
    return st.session_state.price_history[-1]

def portfolio_value():
    return round(st.session_state.cash + (st.session_state.shares * current_price()), 2)

def viewed_selected_balance():
    if st.session_state.selected == "A":
        return st.session_state.viewed_a
    if st.session_state.selected == "B":
        return st.session_state.viewed_b
    return False

def render_ticker():
    if not st.session_state.shown_news:
        return ""
    current_headline = st.session_state.shown_news[-1]["headline"]
    return f"""
    <div class="ticker-wrap">
        <div class="ticker-text">SON DAKİKA • {current_headline} • {current_headline} •</div>
    </div>
    """

def render_feed_html():
    html = ""
    for item in st.session_state.shown_news:
        html += f'<div class="{item["cls"]}"><b>{item["phase"]}</b><br>{item["headline"]}</div>'
    return html

def price_chart_df():
    return pd.DataFrame({
        "Zaman": st.session_state.timeline,
        "Fiyat": st.session_state.price_history
    }).set_index("Zaman")

def reveal_next_news():
    company = selected_company()
    if company is None:
        return
    if st.session_state.news_step >= len(company["news"]):
        st.session_state.finished = True
        return

    next_news = company["news"][st.session_state.news_step]

    with st.spinner("Piyasa fiyatlıyor..."):
        time.sleep(1.2)

    new_price = round(current_price() * (1 + next_news["impact"] / 100), 2)

    st.session_state.shown_news.append(next_news)
    st.session_state.price_history.append(new_price)
    st.session_state.timeline.append(next_news["phase"])
    st.session_state.news_step += 1
    st.session_state.action_done = False

    if st.session_state.news_step >= len(company["news"]):
        st.session_state.finished = True

def buy_all():
    if st.session_state.cash > 0:
        shares_bought = st.session_state.cash / current_price()
        st.session_state.shares += shares_bought
        st.session_state.trade_log.append(
            f"AL — {current_price():.2f} fiyattan pozisyon açıldı."
        )
        st.session_state.cash = 0.0
    else:
        st.session_state.trade_log.append(
            f"AL — {current_price():.2f} seviyesinde ek alım yapılamadı."
        )
    st.session_state.action_done = True

def sell_all():
    if st.session_state.shares > 0:
        st.session_state.cash += st.session_state.shares * current_price()
        st.session_state.trade_log.append(
            f"SAT — {current_price():.2f} fiyattan pozisyon kapatıldı."
        )
        st.session_state.shares = 0.0
    else:
        st.session_state.trade_log.append(
            f"SAT — {current_price():.2f} seviyesinde elde hisse yoktu."
        )
    st.session_state.action_done = True

def hold_position():
    st.session_state.trade_log.append(
        f"BEKLE — {current_price():.2f} seviyesinde pozisyon korunuyor."
    )
    st.session_state.action_done = True

def ending_block():
    final_value = portfolio_value()
    selected = st.session_state.selected

    if selected == "B" and not viewed_selected_balance() and final_value < 100:
        return ("end-bad", "Sürpriz Son", "Haber akışı ilerledikçe seçimin sert biçimde bozuldu.")
    if selected == "B" and viewed_selected_balance():
        return ("end-mid", "Agresif Son", "Seçimin, sonraki haberlerle baskı altında kaldı.")
    if selected == "A" and final_value >= 100:
        return ("end-good", "Dengeli Son", "Haber akışı fiyatı daha dengeli taşıdı.")
    return ("end-mid", "Karışık Sonuç", "Haberler ve hamlelerin birlikte sonucu belirledi.")

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
    if not st.session_state.started:
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
            if st.button("Başlat", use_container_width=True):
                st.session_state.started = True
                reveal_next_news()
                st.rerun()

    else:
        company = selected_company()

        st.markdown(render_ticker(), unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
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
                <div class="metric-value">{current_price():.2f}</div>
                <div class="metric-label">Fiyat</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{st.session_state.cash:.2f}</div>
                <div class="metric-label">Nakit</div>
            </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{portfolio_value():.2f}</div>
                <div class="metric-label">Portföy Değeri</div>
            </div>
            """, unsafe_allow_html=True)

        if st.session_state.shown_news:
            latest = st.session_state.shown_news[-1]
            st.markdown(
                f"""
                <div class="big-news">
                    <h3 style="margin-top:0;">{latest['phase']}</h3>
                    <p style="font-size:1.05rem; margin-bottom:0;">{latest['headline']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.line_chart(price_chart_df(), height=360)

        st.markdown("### Haber Akışı")
        st.markdown(render_feed_html(), unsafe_allow_html=True)

        st.markdown("### Hamle")
        a1, a2, a3 = st.columns(3)

        with a1:
            if st.button("AL", use_container_width=True, disabled=st.session_state.action_done or st.session_state.finished):
                buy_all()
                st.rerun()

        with a2:
            if st.button("BEKLE", use_container_width=True, disabled=st.session_state.action_done or st.session_state.finished):
                hold_position()
                st.rerun()

        with a3:
            if st.button("SAT", use_container_width=True, disabled=st.session_state.action_done or st.session_state.finished):
                sell_all()
                st.rerun()

        if st.session_state.trade_log:
            st.markdown("### İşlem Geçmişi")
            for item in reversed(st.session_state.trade_log[-6:]):
                st.markdown(f'<div class="action-log">{item}</div>', unsafe_allow_html=True)

        if not st.session_state.finished:
            if st.session_state.action_done:
                if st.button("Sonraki Haber", use_container_width=True):
                    reveal_next_news()
                    st.rerun()
        else:
            end_class, end_title, end_text = ending_block()
            st.markdown("---")
            st.markdown(f"""
            <div class="{end_class}">
                <h3 style="margin-top:0;">🏁 {end_title}</h3>
                <p style="margin-bottom:0;">{end_text}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Yorum")
            if st.session_state.selected == "B" and not viewed_selected_balance():
                st.error("Seçimin, ilerleyen haberlerle fiyat üzerinde sert baskı yarattı.")
            elif st.session_state.selected == "B" and viewed_selected_balance():
                st.warning("Fiyat akışı, seçiminin riskini zaman içinde açığa çıkardı.")
            else:
                st.success("Haber akışı ve hamlelerin portföyü daha dengeli taşıdı.")

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
