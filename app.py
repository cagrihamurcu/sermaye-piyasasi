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
    animation: ticker 28s linear infinite;
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
    "started": False,
    "news_index": 0,
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
            {"time": "Öncesi -3", "cls": "news-neutral", "headline": "Yeni üretim hattı planı açıklandı.", "impact": 2},
            {"time": "Öncesi -1", "cls": "news-good", "headline": "Halka arz fiyat aralığına dengeli talep geldi.", "impact": 1},
            {"time": "İlk Gün", "cls": "news-neutral", "headline": "Hisse sakin ama güçlü açıldı.", "impact": 2},
            {"time": "Gün 3", "cls": "news-good", "headline": "Yatırım takviminin planlandığı açıklandı.", "impact": 3},
            {"time": "Gün 6", "cls": "news-good", "headline": "Operasyonel görünüm güçlü kaldı.", "impact": 4},
            {"time": "Gün 8", "cls": "news-good", "headline": "Piyasa şirketi olumlu fiyatlamaya devam etti.", "impact": 4},
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
            {"time": "Öncesi -3", "cls": "news-good", "headline": "Şirket agresif büyüme hedeflerini öne çıkardı.", "impact": 6},
            {"time": "Öncesi -1", "cls": "news-good", "headline": "Piyasada yüksek talep beklentisi oluştu.", "impact": 7},
            {"time": "İlk Gün", "cls": "news-good", "headline": "Hisse güçlü açıldı, ilgi yüksekti.", "impact": 5},
            {"time": "Gün 3", "cls": "news-neutral", "headline": "Borç yapısına dair soru işaretleri arttı.", "impact": -10},
            {"time": "Gün 6", "cls": "news-bad", "headline": "Halka arz gelirinin önemli kısmının borç baskısını hafiflettiği konuşuldu.", "impact": -18},
            {"time": "Gün 8", "cls": "news-bad", "headline": "Şirket zarar açıkladı; hissede sert satış görüldü.", "impact": -25},
        ],
    },
}

# -------------------------------------------------
# Yardımcılar
# -------------------------------------------------
def current_company():
    if st.session_state.selected is None:
        return None
    return companies[st.session_state.selected]

def viewed_selected_balance():
    if st.session_state.selected == "A":
        return st.session_state.viewed_a
    if st.session_state.selected == "B":
        return st.session_state.viewed_b
    return False

def price_path(news_items, revealed_count):
    prices = [100.0]
    shown_news = news_items[:revealed_count]
    for item in shown_news:
        next_price = round(prices[-1] * (1 + item["impact"] / 100), 2)
        prices.append(next_price)
    return prices

def timeline_labels(revealed_count):
    base = ["Başlangıç"]
    if st.session_state.selected is None:
        return base
    company = current_company()
    return base + [item["time"] for item in company["news"][:revealed_count]]

def ending_block(selected_key, viewed_balance, final_price):
    if selected_key == "B" and not viewed_balance:
        return (
            "end-bad",
            "Sürpriz Son",
            "Seçimin sonradan gelen haber akışıyla sert biçimde sarsıldı."
        )
    if selected_key == "B" and viewed_balance:
        return (
            "end-mid",
            "Agresif Son",
            "Veriyi görerek girdin; haber akışı seçiminin riskini büyüttü."
        )
    if selected_key == "A" and final_price >= 110:
        return (
            "end-good",
            "Dengeli Son",
            "Haber akışı fiyatı kademeli biçimde yukarı taşıdı."
        )
    return (
        "end-mid",
        "Karışık Sonuç",
        "Seçimin haber akışına göre dalgalı bir sonuç üretti."
    )

def reset_game():
    st.session_state.selected = None
    st.session_state.started = False
    st.session_state.news_index = 0

# -------------------------------------------------
# Hero
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>📈 Halka Arz Arenası</h1>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Sekmeler
# -------------------------------------------------
main_tab, balance_tab = st.tabs(["🎮 Oyun", "📑 Bilançolar"])

# -------------------------------------------------
# OYUN
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
            selected = current_company()
            st.markdown("### Seçim")
            st.markdown(f"**{selected['name']}**")
            if st.button("Yatırıma Başla", use_container_width=True):
                st.session_state.started = True
                st.session_state.news_index = 1
                st.rerun()

    else:
        company = current_company()
        shown_news = company["news"][:st.session_state.news_index]
        prices = price_path(company["news"], st.session_state.news_index)
        labels = timeline_labels(st.session_state.news_index)
        current_price = prices[-1]
        current_news = shown_news[-1] if shown_news else None

        # Haber bandı
        if shown_news:
            ticker_text = "   •   ".join([f"{n['time']} — {n['headline']}" for n in shown_news])
            st.markdown(
                f"""
                <div class="ticker-wrap">
                    <div class="ticker-text">SON DAKİKA • {ticker_text} •</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Üst metrikler
        m1, m2, m3 = st.columns(3)
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
                <div class="metric-value">{current_price:.2f}</div>
                <div class="metric-label">Güncel Fiyat Endeksi</div>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{st.session_state.news_index}/{len(company['news'])}</div>
                <div class="metric-label">Akan Haber Sayısı</div>
            </div>
            """, unsafe_allow_html=True)

        # Son haber
        if current_news:
            st.markdown(
                f"""
                <div class="big-news">
                    <h3 style="margin-top:0;">{current_news['time']}</h3>
                    <p style="font-size:1.05rem; margin-bottom:0;">{current_news['headline']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Grafik
        chart_df = pd.DataFrame({
            "Zaman": labels,
            "Fiyat": prices,
        }).set_index("Zaman")
        st.line_chart(chart_df, height=380)

        # Haber listesi
        st.markdown("### Haber Akışı")
        for news_item in shown_news:
            st.markdown(
                f'<div class="{news_item["cls"]}"><b>{news_item["time"]}</b><br>{news_item["headline"]}</div>',
                unsafe_allow_html=True
            )

        # Oyun akışı
        if st.session_state.news_index < len(company["news"]):
            c1, c2 = st.columns([4, 1])
            with c2:
                if st.button("Sonraki Haber", use_container_width=True):
                    st.session_state.news_index += 1
                    st.rerun()
        else:
            final_price = prices[-1]
            end_class, end_title, end_text = ending_block(
                st.session_state.selected,
                viewed_selected_balance(),
                final_price
            )
            st.markdown("---")
            st.markdown(f"""
            <div class="{end_class}">
                <h3 style="margin-top:0;">🏁 {end_title}</h3>
                <p style="margin-bottom:0;">{end_text}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Yorum")
            if st.session_state.selected == "B" and not viewed_selected_balance():
                st.error("""
Seçtiğin şirketin fiyatı, ilk heyecandan sonra gelen haberlerle sert biçimde çözüldü.
                """)
            elif st.session_state.selected == "B" and viewed_selected_balance():
                st.warning("""
Seçimin, baştan itibaren daha kırılgan bir hikâyeye dayanıyordu; sonraki haberler bunu fiyatlara taşıdı.
                """)
            else:
                st.success("""
Seçtiğin hissede haber akışı fiyatı kademeli biçimde destekledi.
                """)

            if st.button("Başa Dön", use_container_width=True):
                reset_game()
                st.rerun()

# -------------------------------------------------
# BİLANÇOLAR
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
