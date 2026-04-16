import time
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Halka Arz Arenası", page_icon="📈", layout="wide")

EVENT_INTERVAL = 7  # seconds
STARTING_CASH = 100_000.0

st.markdown("""
<style>
:root {
    --bg: #0b1220;
    --panel: #111827;
    --panel-2: #182133;
    --line: #263247;
    --text: #e5e7eb;
    --muted: #94a3b8;
    --accent: #60a5fa;
}

.stApp {
    background: linear-gradient(180deg, #0b1220 0%, #0f172a 100%);
}

.hero {
    padding: 24px;
    border-radius: 22px;
    background: linear-gradient(135deg, #111827 0%, #1f2937 55%, #0f172a 100%);
    color: var(--text);
    border: 1px solid var(--line);
    box-shadow: 0 12px 28px rgba(0,0,0,0.24);
    margin-bottom: 18px;
}
.hero h1 { margin: 0; font-size: 1.9rem; }

.company-card {
    padding: 20px;
    border-radius: 18px;
    color: var(--text);
    min-height: 230px;
    border: 1px solid var(--line);
    box-shadow: 0 12px 24px rgba(0,0,0,0.18);
}

.metric-box {
    padding: 14px;
    border-radius: 16px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--line);
    text-align: center;
    color: var(--text);
}
.metric-value {
    font-size: 1.5rem;
    font-weight: 700;
}
.metric-label {
    font-size: 0.9rem;
    color: var(--muted);
}

.panel {
    padding: 16px;
    border-radius: 16px;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--line);
    color: var(--text);
    margin-bottom: 14px;
}

.news-ticker {
    overflow: hidden;
    white-space: nowrap;
    border-radius: 14px;
    background: #0f172a;
    border: 1px solid var(--line);
    color: var(--text);
    padding: 12px 0;
    margin-bottom: 14px;
}
.news-ticker span {
    display: inline-block;
    padding-left: 100%;
    animation: ticker 18s linear infinite;
    font-weight: 600;
}
@keyframes ticker {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}

.current-news {
    padding: 18px;
    border-radius: 16px;
    background: #ffffff;
    color: #0f172a;
    border-left: 8px solid #2563eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    margin-bottom: 14px;
}

.feed-item {
    padding: 12px 14px;
    border-radius: 12px;
    background: rgba(255,255,255,0.03);
    border: 1px solid var(--line);
    color: var(--text);
    margin-bottom: 8px;
}

.end-good, .end-mid, .end-bad {
    padding: 18px;
    border-radius: 16px;
    color: white;
    margin-top: 10px;
}
.end-good { background: linear-gradient(135deg, #047857, #10b981); }
.end-mid { background: linear-gradient(135deg, #b45309, #f59e0b); }
.end-bad { background: linear-gradient(135deg, #991b1b, #ef4444); }
</style>
""", unsafe_allow_html=True)

companies = {
    "A": {
        "name": "Marmara Ambalaj Sanayi A.Ş.",
        "c1": "#1f2937",
        "c2": "#334155",
        "tagline": "Üretim kapasitesi artışı için halka arz",
        "story": "Ambalaj üretiminde kapasite artırımı ve ihracat kanalını büyütme hedefiyle halka arza çıkıyor.",
        "balance_sheet": pd.DataFrame({
            "Kalem": ["Nakit ve Benzerleri", "Kısa Vadeli Borç", "Uzun Vadeli Borç", "Özkaynak", "Net Kâr", "Cari Oran", "Borç / Özkaynak"],
            "Değer": ["420 mn TL", "180 mn TL", "260 mn TL", "1.150 mn TL", "210 mn TL", "1.85", "0.38"]
        }),
        "income": pd.DataFrame({
            "Kalem": ["Hasılat", "Brüt Kâr", "Esas Faaliyet Kârı", "FAVÖK", "Net Kâr Marjı"],
            "Değer": ["2.480 mn TL", "610 mn TL", "295 mn TL", "362 mn TL", "%8.5"]
        }),
        "events": [
            {"time": "09:30", "headline": "Talep toplama sonuçları açıklandı; dağıtım dengeli gerçekleşti.", "impact": 1.4},
            {"time": "10:45", "headline": "Şirket üretim hattı yatırım takvimini paylaştı.", "impact": 0.9},
            {"time": "12:05", "headline": "Aracı kurum istikrar işlemleri çerçevesini duyurdu.", "impact": 0.4},
            {"time": "13:40", "headline": "Yeni tedarik sözleşmesine ilişkin açıklama yayımlandı.", "impact": 1.6},
            {"time": "15:10", "headline": "Yıl sonu kapasite kullanım beklentisi korundu.", "impact": 1.1},
            {"time": "16:20", "headline": "Seans sonu değerlendirmesinde nakit yaratımına vurgu yapıldı.", "impact": 0.7},
        ],
    },
    "B": {
        "name": "Delta Veri Çözümleri A.Ş.",
        "c1": "#111827",
        "c2": "#1e3a8a",
        "tagline": "Hızlı büyüme ve ölçeklenme hikâyesi",
        "story": "Yazılım ve veri çözümleri alanında büyüme anlatısıyla halka arza çıkıyor.",
        "balance_sheet": pd.DataFrame({
            "Kalem": ["Nakit ve Benzerleri", "Kısa Vadeli Borç", "Uzun Vadeli Borç", "Özkaynak", "Net Kâr / Zarar", "Cari Oran", "Borç / Özkaynak"],
            "Değer": ["95 mn TL", "640 mn TL", "980 mn TL", "310 mn TL", "-145 mn TL", "0.72", "5.23"]
        }),
        "income": pd.DataFrame({
            "Kalem": ["Hasılat", "Brüt Kâr", "Esas Faaliyet Kârı", "FAVÖK", "Net Kâr Marjı"],
            "Değer": ["1.180 mn TL", "342 mn TL", "58 mn TL", "96 mn TL", "-%12.3"]
        }),
        "events": [
            {"time": "09:30", "headline": "Talep toplama sonuçları açıklandı; ilk ilgi güçlü göründü.", "impact": 1.9},
            {"time": "10:45", "headline": "Yönetim hızlı büyüme hedeflerini yineledi.", "impact": 0.8},
            {"time": "12:05", "headline": "Kısa vadeli finansal borçlara ilişkin sorular öne çıktı.", "impact": -3.2},
            {"time": "13:40", "headline": "Halka arz gelirinin kullanım dağılımına ilişkin ek açıklama geldi.", "impact": -4.6},
            {"time": "15:10", "headline": "İlk çeyrek marj beklentileri aşağı yönlü güncellendi.", "impact": -5.4},
            {"time": "16:20", "headline": "Yönetim net borç azaltımına odaklanacağını belirtti.", "impact": -2.1},
        ],
    },
}

state_defaults = {
    "selected": None,
    "started": False,
    "finished": False,
    "news_step": 0,
    "price_history": [100.0],
    "timeline": ["09:00"],
    "shown_news": [],
    "cash": STARTING_CASH,
    "shares": 0,
    "avg_cost": 0.0,
    "trade_log": [],
    "viewed_a": False,
    "viewed_b": False,
    "last_event_ts": None,
}
for k, v in state_defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset_game():
    for k, v in state_defaults.items():
        st.session_state[k] = v if not isinstance(v, list) else v.copy()


def selected_company():
    return companies.get(st.session_state.selected)


def current_price():
    return st.session_state.price_history[-1]


def market_value():
    return st.session_state.shares * current_price()


def unrealized_pnl():
    return market_value() - (st.session_state.shares * st.session_state.avg_cost)


def equity_value():
    return st.session_state.cash + market_value()


def viewed_selected_balance():
    if st.session_state.selected == "A":
        return st.session_state.viewed_a
    if st.session_state.selected == "B":
        return st.session_state.viewed_b
    return False


def reveal_next_event():
    company = selected_company()
    if company is None or st.session_state.finished:
        return
    idx = st.session_state.news_step
    if idx >= len(company["events"]):
        st.session_state.finished = True
        return

    event = company["events"][idx]
    prev = current_price()
    new_price = round(max(1.0, prev * (1 + event["impact"] / 100)), 2)

    st.session_state.price_history.append(new_price)
    st.session_state.timeline.append(event["time"])
    st.session_state.shown_news.append(event)
    st.session_state.news_step += 1
    st.session_state.last_event_ts = time.time()

    if st.session_state.news_step >= len(company["events"]):
        # one last window for trading after final event
        pass


def execute_buy(qty: int):
    price = current_price()
    cost = qty * price
    if qty <= 0:
        return
    if cost > st.session_state.cash:
        st.session_state.trade_log.append(f"AL RED — {qty} lot için nakit yetersiz ({price:.2f}).")
        return

    old_qty = st.session_state.shares
    old_cost = st.session_state.avg_cost
    new_qty = old_qty + qty
    new_avg = ((old_qty * old_cost) + cost) / new_qty if new_qty > 0 else 0.0

    st.session_state.cash -= cost
    st.session_state.shares = new_qty
    st.session_state.avg_cost = round(new_avg, 4)
    st.session_state.trade_log.append(f"AL — {qty} lot @ {price:.2f}")


def execute_sell(qty: int):
    price = current_price()
    if qty <= 0:
        return
    if qty > st.session_state.shares:
        st.session_state.trade_log.append(f"SAT RED — {qty} lot için elde yeterli hisse yok ({price:.2f}).")
        return

    st.session_state.cash += qty * price
    st.session_state.shares -= qty
    if st.session_state.shares == 0:
        st.session_state.avg_cost = 0.0
    st.session_state.trade_log.append(f"SAT — {qty} lot @ {price:.2f}")


def ticker_html():
    if not st.session_state.shown_news:
        return ""
    joined = " • ".join([n["headline"] for n in st.session_state.shown_news[-3:]])
    return f'<div class="news-ticker"><span>SON DAKİKA • {joined} •</span></div>'


def feed_html():
    html = ""
    for item in reversed(st.session_state.shown_news):
        html += f'<div class="feed-item"><b>{item["time"]}</b><br>{item["headline"]}</div>'
    return html


def ending_block():
    val = equity_value()
    key = st.session_state.selected
    if key == "B" and not viewed_selected_balance() and val < STARTING_CASH:
        return ("end-bad", "Sürpriz Son", "Fiyat akışı pozisyonunu belirgin biçimde aşağı taşıdı.")
    if key == "B" and viewed_selected_balance():
        return ("end-mid", "Agresif Son", "Riskli hikâye seans boyunca fiyat üzerinde baskı yarattı.")
    if key == "A" and val >= STARTING_CASH:
        return ("end-good", "Dengeli Son", "Akış daha istikrarlı kaldı; fiyat seans boyunca korunabildi.")
    return ("end-mid", "Karışık Sonuç", "Haber akışı ve işlemler birlikte sonucu belirledi.")


@st.fragment(run_every="1s")
def market_fragment():
    company = selected_company()
    if company is None or not st.session_state.started:
        return

    now = time.time()
    if not st.session_state.finished and st.session_state.last_event_ts is not None:
        elapsed = now - st.session_state.last_event_ts
        if elapsed >= EVENT_INTERVAL:
            if st.session_state.news_step < len(company["events"]):
                reveal_next_event()
                st.rerun(scope="fragment")
            else:
                st.session_state.finished = True
                st.rerun(scope="fragment")

    remaining = 0
    if st.session_state.last_event_ts is not None and not st.session_state.finished:
        remaining = max(0, EVENT_INTERVAL - int(now - st.session_state.last_event_ts))

    st.markdown(ticker_html(), unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{company["name"]}</div><div class="metric-label">Şirket</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{current_price():.2f}</div><div class="metric-label">Fiyat</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{st.session_state.cash:,.0f}</div><div class="metric-label">Nakit</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{st.session_state.shares}</div><div class="metric-label">Lot</div></div>', unsafe_allow_html=True)
    with c5:
        st.markdown(f'<div class="metric-box"><div class="metric-value">{remaining}</div><div class="metric-label">Sonraki Habere Kalan</div></div>', unsafe_allow_html=True)

    left, mid, right = st.columns([1.25, 1.55, 1.0])

    with left:
        if st.session_state.shown_news:
            latest = st.session_state.shown_news[-1]
            st.markdown(
                f'<div class="current-news"><h3 style="margin-top:0;">{latest["time"]}</h3><p style="font-size:1.05rem; margin-bottom:0;">{latest["headline"]}</p></div>',
                unsafe_allow_html=True,
            )
        st.markdown("### Haber Akışı")
        st.markdown(feed_html(), unsafe_allow_html=True)

    with mid:
        chart_df = pd.DataFrame({"Zaman": st.session_state.timeline, "Fiyat": st.session_state.price_history}).set_index("Zaman")
        st.line_chart(chart_df, height=430)
        pnl = unrealized_pnl()
        st.markdown(f'<div class="panel"><b>Ortalama Maliyet:</b> {st.session_state.avg_cost:.2f}<br><b>Pozisyon Değeri:</b> {market_value():,.0f}<br><b>Gerçekleşmemiş K/Z:</b> {pnl:,.0f}</div>', unsafe_allow_html=True)

    with right:
        st.markdown("### Emir Paneli")
        qty = st.number_input("Lot", min_value=1, value=100, step=100, key="order_qty")
        b1, b2 = st.columns(2)
        with b1:
            if st.button("AL", use_container_width=True, disabled=st.session_state.finished):
                execute_buy(int(qty))
                st.rerun(scope="fragment")
        with b2:
            if st.button("SAT", use_container_width=True, disabled=st.session_state.finished):
                execute_sell(int(qty))
                st.rerun(scope="fragment")

        if st.button("BEKLE", use_container_width=True, disabled=st.session_state.finished):
            st.session_state.trade_log.append(f"BEKLE — {current_price():.2f}")
            st.rerun(scope="fragment")

        st.markdown("### İşlem Geçmişi")
        if st.session_state.trade_log:
            for item in reversed(st.session_state.trade_log[-8:]):
                st.markdown(f'<div class="action-log">{item}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="action-log">Henüz işlem yok.</div>', unsafe_allow_html=True)

    if st.session_state.finished:
        end_class, end_title, end_text = ending_block()
        st.markdown(f'<div class="{end_class}"><h3 style="margin-top:0;">🏁 {end_title}</h3><p style="margin-bottom:0;">{end_text}</p></div>', unsafe_allow_html=True)
        st.markdown("### Yorum")
        if st.session_state.selected == "B" and not viewed_selected_balance():
            st.error("Seans boyunca gelen açıklamalar fiyatı belirgin biçimde aşağı taşıdı.")
        elif st.session_state.selected == "B" and viewed_selected_balance():
            st.warning("Riskli hikâye, seans ilerledikçe fiyat üzerinde baskı oluşturdu.")
        else:
            st.success("Seçilen hisse haber akışına karşı daha dayanıklı kaldı.")

        if st.button("Başa Dön", use_container_width=True):
            reset_game()
            st.rerun(scope="app")


st.markdown('<div class="hero"><h1>📈 Halka Arz Arenası</h1></div>', unsafe_allow_html=True)

main_tab, balance_tab = st.tabs(["🎮 Piyasa Ekranı", "📑 Finansallar"])

with main_tab:
    if not st.session_state.started:
        left, right = st.columns(2)
        with left:
            a = companies["A"]
            st.markdown(
                f'<div class="company-card" style="background: linear-gradient(135deg, {a["c1"]}, {a["c2"]});"><h2>{a["name"]}</h2><p><b>{a["tagline"]}</b></p><p>{a["story"]}</p></div>',
                unsafe_allow_html=True,
            )
            if st.button(f'{a["name"]} Seç', use_container_width=True):
                st.session_state.selected = "A"
                st.rerun()
        with right:
            b = companies["B"]
            st.markdown(
                f'<div class="company-card" style="background: linear-gradient(135deg, {b["c1"]}, {b["c2"]});"><h2>{b["name"]}</h2><p><b>{b["tagline"]}</b></p><p>{b["story"]}</p></div>',
                unsafe_allow_html=True,
            )
            if st.button(f'{b["name"]} Seç', use_container_width=True):
                st.session_state.selected = "B"
                st.rerun()

        if st.session_state.selected is not None:
            st.markdown(f"### Seçim\n**{selected_company()['name']}**")
            if st.button("Seansı Başlat", use_container_width=True):
                st.session_state.started = True
                reveal_next_event()
                st.rerun()
    else:
        market_fragment()

with balance_tab:
    t1, t2 = st.tabs([companies["A"]["name"], companies["B"]["name"]])
    with t1:
        st.markdown("### Bilanço")
        st.table(companies["A"]["balance_sheet"])
        st.markdown("### Gelir Tablosu")
        st.table(companies["A"]["income"])
        if st.button("İncelendi", key="view_a"):
            st.session_state.viewed_a = True
            st.rerun()
    with t2:
        st.markdown("### Bilanço")
        st.table(companies["B"]["balance_sheet"])
        st.markdown("### Gelir Tablosu")
        st.table(companies["B"]["income"])
        if st.button("İncelendi", key="view_b"):
            st.session_state.viewed_b = True
            st.rerun()
