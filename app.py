
import time
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Halka Arz Arenası", page_icon="📈", layout="wide")

EVENT_INTERVAL = 7
STARTING_CASH = 100_000.0
IPO_PRICE_A = 100.0
IPO_PRICE_B = 100.0


def tr_num(value, decimals=2):
    s = f"{value:,.{decimals}f}"
    return s.replace(",", "#").replace(".", ",").replace("#", ".")


st.markdown("""
<style>
:root {
    --line: #263247;
    --text: #e5e7eb;
    --muted: #94a3b8;
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
.hero h1 { margin: 0 0 8px 0; font-size: 1.9rem; }
.hero p { margin: 0; color: var(--muted); line-height: 1.6; }
.company-card {
    padding: 20px;
    border-radius: 18px;
    color: var(--text);
    min-height: 220px;
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
.metric-value { font-size: 1.35rem; font-weight: 700; }
.metric-label { font-size: 0.9rem; color: var(--muted); }
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
    background: white;
    color: #0f172a;
    border-left: 8px solid #2563eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
    margin-bottom: 14px;
}
.feed-item, .action-log {
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

COMPANIES = {
    "A": {
        "name": "Marmara Ambalaj Sanayi A.Ş.",
        "short": "Marmara Ambalaj",
        "c1": "#1f2937",
        "c2": "#334155",
        "tagline": "Üretim kapasitesi artışı için halka arz",
        "story": "Ambalaj üretiminde kapasite artırımı ve ihracat kanalını büyütme hedefiyle halka arza çıkıyor.",
        "balance_sheet": pd.DataFrame({
            "Kalem": ["Nakit ve Benzerleri", "Kısa Vadeli Borç", "Uzun Vadeli Borç", "Özkaynak", "Net Kâr", "Cari Oran", "Borç / Özkaynak"],
            "Değer": ["420 mn TL", "180 mn TL", "260 mn TL", "1.150 mn TL", "210 mn TL", "1,85", "0,38"],
        }),
        "income": pd.DataFrame({
            "Kalem": ["Hasılat", "Brüt Kâr", "Esas Faaliyet Kârı", "FAVÖK", "Net Kâr Marjı"],
            "Değer": ["2.480 mn TL", "610 mn TL", "295 mn TL", "362 mn TL", "%8,5"],
        }),
    },
    "B": {
        "name": "Delta Veri Çözümleri A.Ş.",
        "short": "Delta Veri",
        "c1": "#111827",
        "c2": "#1e3a8a",
        "tagline": "Hızlı büyüme ve ölçeklenme hikâyesi",
        "story": "Yazılım ve veri çözümleri alanında büyüme anlatısıyla halka arza çıkıyor.",
        "balance_sheet": pd.DataFrame({
            "Kalem": ["Nakit ve Benzerleri", "Kısa Vadeli Borç", "Uzun Vadeli Borç", "Özkaynak", "Net Kâr / Zarar", "Cari Oran", "Borç / Özkaynak"],
            "Değer": ["95 mn TL", "640 mn TL", "980 mn TL", "310 mn TL", "-145 mn TL", "0,72", "5,23"],
        }),
        "income": pd.DataFrame({
            "Kalem": ["Hasılat", "Brüt Kâr", "Esas Faaliyet Kârı", "FAVÖK", "Net Kâr Marjı"],
            "Değer": ["1.180 mn TL", "342 mn TL", "58 mn TL", "96 mn TL", "-%12,3"],
        }),
    },
}

EVENTS = [
    {"time": "09:30", "ticker": "A", "headline": "Talep toplama sonuçları açıklandı; dağıtım dengeli gerçekleşti.", "impact": 1.4},
    {"time": "09:50", "ticker": "B", "headline": "Talep toplama sonuçları açıklandı; ilk ilgi güçlü göründü.", "impact": 1.9},
    {"time": "10:45", "ticker": "A", "headline": "Şirket üretim hattı yatırım takvimini paylaştı.", "impact": 0.9},
    {"time": "11:10", "ticker": "B", "headline": "Yönetim hızlı büyüme hedeflerini yineledi.", "impact": 0.8},
    {"time": "12:05", "ticker": "B", "headline": "Kısa vadeli finansal borçlara ilişkin sorular öne çıktı.", "impact": -3.2},
    {"time": "13:40", "ticker": "A", "headline": "Yeni tedarik sözleşmesine ilişkin açıklama yayımlandı.", "impact": 1.6},
    {"time": "14:20", "ticker": "B", "headline": "Halka arz gelirinin kullanım dağılımına ilişkin ek açıklama geldi.", "impact": -4.6},
    {"time": "15:10", "ticker": "A", "headline": "Yıl sonu kapasite kullanım beklentisi korundu.", "impact": 1.1},
    {"time": "15:35", "ticker": "B", "headline": "İlk çeyrek marj beklentileri aşağı yönlü güncellendi.", "impact": -5.4},
    {"time": "16:20", "ticker": "A", "headline": "Seans sonu değerlendirmesinde nakit yaratımına vurgu yapıldı.", "impact": 0.7},
    {"time": "16:30", "ticker": "B", "headline": "Yönetim net borç azaltımına odaklanacağını belirtti.", "impact": -2.1},
]

STATE_DEFAULTS = {
    "started": False,
    "finished": False,
    "event_step": 0,
    "timeline": ["09:00"],
    "price_a": [IPO_PRICE_A],
    "price_b": [IPO_PRICE_B],
    "portfolio_hist": [STARTING_CASH],
    "shown_news": [],
    "cash": STARTING_CASH,
    "shares_a": 0,
    "shares_b": 0,
    "avg_cost_a": 0.0,
    "avg_cost_b": 0.0,
    "trade_log": [],
    "viewed_a": False,
    "viewed_b": False,
    "last_event_ts": None,
    "alloc_a": 50,
}
for k, v in STATE_DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v if not isinstance(v, list) else v.copy()


def reset_game():
    for k, v in STATE_DEFAULTS.items():
        st.session_state[k] = v if not isinstance(v, list) else v.copy()


def current_price_a():
    return st.session_state.price_a[-1]


def current_price_b():
    return st.session_state.price_b[-1]


def market_value_a():
    return st.session_state.shares_a * current_price_a()


def market_value_b():
    return st.session_state.shares_b * current_price_b()


def total_equity():
    return st.session_state.cash + market_value_a() + market_value_b()


def unrealized_pnl_a():
    return market_value_a() - st.session_state.shares_a * st.session_state.avg_cost_a


def unrealized_pnl_b():
    return market_value_b() - st.session_state.shares_b * st.session_state.avg_cost_b


def ticker_html():
    if not st.session_state.shown_news:
        return ""
    joined = " • ".join([
        f"{COMPANIES[item['ticker']]['short']} — {item['headline']}" for item in st.session_state.shown_news[-3:]
    ])
    return f'<div class="news-ticker"><span>HABER AKIŞI • {joined} •</span></div>'


def feed_html():
    html = ""
    for item in reversed(st.session_state.shown_news):
        name = COMPANIES[item["ticker"]]["short"]
        html += f'<div class="feed-item"><b>{item["time"]} | {name}</b><br>{item["headline"]}</div>'
    return html


def init_positions_from_allocation(a_pct: int):
    cash = STARTING_CASH
    qty_a = int((cash * (a_pct / 100)) // IPO_PRICE_A)
    spent_a = qty_a * IPO_PRICE_A
    cash -= spent_a

    qty_b = int(cash // IPO_PRICE_B)
    spent_b = qty_b * IPO_PRICE_B
    cash -= spent_b

    st.session_state.shares_a = qty_a
    st.session_state.shares_b = qty_b
    st.session_state.avg_cost_a = IPO_PRICE_A if qty_a else 0.0
    st.session_state.avg_cost_b = IPO_PRICE_B if qty_b else 0.0
    st.session_state.cash = round(cash, 2)
    st.session_state.portfolio_hist = [st.session_state.cash + qty_a * IPO_PRICE_A + qty_b * IPO_PRICE_B]


def reveal_next_event():
    if st.session_state.finished:
        return
    idx = st.session_state.event_step
    if idx >= len(EVENTS):
        st.session_state.finished = True
        return

    event = EVENTS[idx]
    pa = current_price_a()
    pb = current_price_b()
    if event["ticker"] == "A":
        pa = round(max(1.0, pa * (1 + event["impact"] / 100)), 2)
    else:
        pb = round(max(1.0, pb * (1 + event["impact"] / 100)), 2)

    st.session_state.timeline.append(event["time"])
    st.session_state.price_a.append(pa)
    st.session_state.price_b.append(pb)
    st.session_state.shown_news.append(event)
    st.session_state.event_step += 1
    st.session_state.last_event_ts = time.time()
    st.session_state.portfolio_hist.append(total_equity())


def execute_buy(ticker: str, qty: int):
    if qty <= 0:
        return
    price = current_price_a() if ticker == "A" else current_price_b()
    cost = qty * price
    if cost > st.session_state.cash:
        st.session_state.trade_log.append(
            f"AL RED — {COMPANIES[ticker]['short']} {qty} lot için nakit yetersiz ({tr_num(price)})."
        )
        return
    if ticker == "A":
        old_qty = st.session_state.shares_a
        old_avg = st.session_state.avg_cost_a
        new_qty = old_qty + qty
        st.session_state.avg_cost_a = ((old_qty * old_avg) + cost) / new_qty if new_qty else 0.0
        st.session_state.shares_a = new_qty
    else:
        old_qty = st.session_state.shares_b
        old_avg = st.session_state.avg_cost_b
        new_qty = old_qty + qty
        st.session_state.avg_cost_b = ((old_qty * old_avg) + cost) / new_qty if new_qty else 0.0
        st.session_state.shares_b = new_qty
    st.session_state.cash -= cost
    st.session_state.trade_log.append(f"AL — {COMPANIES[ticker]['short']} {qty} lot @ {tr_num(price)}")


def execute_sell(ticker: str, qty: int):
    if qty <= 0:
        return
    price = current_price_a() if ticker == "A" else current_price_b()
    if ticker == "A":
        if qty > st.session_state.shares_a:
            st.session_state.trade_log.append(
                f"SAT RED — {COMPANIES[ticker]['short']} {qty} lot için elde yeterli hisse yok ({tr_num(price)})."
            )
            return
        st.session_state.shares_a -= qty
        if st.session_state.shares_a == 0:
            st.session_state.avg_cost_a = 0.0
    else:
        if qty > st.session_state.shares_b:
            st.session_state.trade_log.append(
                f"SAT RED — {COMPANIES[ticker]['short']} {qty} lot için elde yeterli hisse yok ({tr_num(price)})."
            )
            return
        st.session_state.shares_b -= qty
        if st.session_state.shares_b == 0:
            st.session_state.avg_cost_b = 0.0
    st.session_state.cash += qty * price
    st.session_state.trade_log.append(f"SAT — {COMPANIES[ticker]['short']} {qty} lot @ {tr_num(price)}")


def ending_block():
    eq = total_equity()
    if st.session_state.alloc_a < 50 and not st.session_state.viewed_b and eq < STARTING_CASH:
        return ("end-bad", "Sürpriz Son", "Başlangıç dağılımı ve sonraki akış portföyü baskıladı.")
    if st.session_state.alloc_a < 50 and st.session_state.viewed_b:
        return ("end-mid", "Agresif Son", "Dağılım ve işlemler daha dalgalı tarafta kaldı.")
    if eq >= STARTING_CASH:
        return ("end-good", "Dengeli Son", "Portföy, seans boyunca dayanıklı kaldı.")
    return ("end-mid", "Karışık Sonuç", "Fiyat akışı ve işlem tercihleri birlikte sonucu belirledi.")


@st.fragment(run_every="1s")
def market_fragment():
    if not st.session_state.started:
        return

    now = time.time()
    if not st.session_state.finished and st.session_state.last_event_ts is not None:
        elapsed = now - st.session_state.last_event_ts
        if elapsed >= EVENT_INTERVAL:
            if st.session_state.event_step < len(EVENTS):
                reveal_next_event()
                st.rerun(scope="fragment")
            else:
                st.session_state.finished = True
                st.rerun(scope="fragment")

    remaining = 0
    if st.session_state.last_event_ts is not None and not st.session_state.finished:
        remaining = max(0, EVENT_INTERVAL - int(now - st.session_state.last_event_ts))

    st.markdown(ticker_html(), unsafe_allow_html=True)

    m1, m2, m3, m4, m5 = st.columns(5)
    with m1:
        st.markdown(
            f'<div class="metric-box"><div class="metric-value">{tr_num(current_price_a())}</div><div class="metric-label">{COMPANIES["A"]["short"]} Fiyat</div></div>',
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            f'<div class="metric-box"><div class="metric-value">{tr_num(current_price_b())}</div><div class="metric-label">{COMPANIES["B"]["short"]} Fiyat</div></div>',
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            f'<div class="metric-box"><div class="metric-value">{tr_num(st.session_state.cash)}</div><div class="metric-label">Nakit</div></div>',
            unsafe_allow_html=True,
        )
    with m4:
        st.markdown(
            f'<div class="metric-box"><div class="metric-value">{tr_num(total_equity())}</div><div class="metric-label">Toplam Portföy</div></div>',
            unsafe_allow_html=True,
        )
    with m5:
        st.markdown(
            f'<div class="metric-box"><div class="metric-value">{remaining}</div><div class="metric-label">Sonraki Habere Kalan</div></div>',
            unsafe_allow_html=True,
        )

    left, mid, right = st.columns([1.15, 1.65, 1.0])

    with left:
        if st.session_state.shown_news:
            latest = st.session_state.shown_news[-1]
            st.markdown(
                f'<div class="current-news"><h3 style="margin-top:0;">{latest["time"]} | {COMPANIES[latest["ticker"]]["short"]}</h3><p style="font-size:1.05rem; margin-bottom:0;">{latest["headline"]}</p></div>',
                unsafe_allow_html=True,
            )
        st.markdown("### Haber Akışı")
        st.markdown(feed_html(), unsafe_allow_html=True)

    with mid:
        chart_df = pd.DataFrame({
            "Zaman": st.session_state.timeline,
            COMPANIES["A"]["short"]: st.session_state.price_a,
            COMPANIES["B"]["short"]: st.session_state.price_b,
            "Portföy": st.session_state.portfolio_hist,
        }).set_index("Zaman")
        st.line_chart(chart_df, height=430)
        st.markdown(
            f'<div class="panel"><b>{COMPANIES["A"]["short"]} Pozisyonu:</b> {st.session_state.shares_a} lot | Ortalama: {tr_num(st.session_state.avg_cost_a)} | K/Z: {tr_num(unrealized_pnl_a())}<br>'
            f'<b>{COMPANIES["B"]["short"]} Pozisyonu:</b> {st.session_state.shares_b} lot | Ortalama: {tr_num(st.session_state.avg_cost_b)} | K/Z: {tr_num(unrealized_pnl_b())}</div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown("### Emir Paneli")
        trade_ticker = st.selectbox(
            "Hisse",
            ["A", "B"],
            format_func=lambda x: COMPANIES[x]["name"],
            key="trade_ticker",
        )
        qty = st.number_input("Lot", min_value=1, value=100, step=100, key="trade_qty")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("AL", use_container_width=True, disabled=st.session_state.finished):
                execute_buy(trade_ticker, int(qty))
                st.rerun(scope="fragment")
        with c2:
            if st.button("SAT", use_container_width=True, disabled=st.session_state.finished):
                execute_sell(trade_ticker, int(qty))
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
        if st.session_state.alloc_a < 50 and not st.session_state.viewed_b:
            st.error("Başlangıç dağılımı ve haber akışı birlikte portföy üzerinde baskı yarattı.")
        elif st.session_state.alloc_a < 50 and st.session_state.viewed_b:
            st.warning("Seans boyunca daha dalgalı tarafa ağırlık verdin.")
        else:
            st.success("Dağılım ve sonradan yaptığın işlemler portföyü daha dengeli tuttu.")
        if st.button("Başa Dön", use_container_width=True):
            reset_game()
            st.rerun(scope="app")


st.markdown(
    '<div class="hero"><h1>📈 Halka Arz Arenası</h1><p>Başlangıçta ana paranı iki halka arz arasında paylaştırırsın. Seans başladıktan sonra haberler otomatik akar; fiyatlar güncellenir ve iki hissede de alım-satım yapabilirsin. Finansallar sekmesinde şirketlerin bilanço ve gelir tablosu yer alır.</p></div>',
    unsafe_allow_html=True,
)

main_tab, balance_tab = st.tabs(["🎮 Piyasa Ekranı", "📑 Finansallar"])

with main_tab:
    if not st.session_state.started:
        left, right = st.columns(2)
        with left:
            a = COMPANIES["A"]
            st.markdown(
                f'<div class="company-card" style="background: linear-gradient(135deg, {a["c1"]}, {a["c2"]});"><h2>{a["name"]}</h2><p><b>{a["tagline"]}</b></p><p>{a["story"]}</p></div>',
                unsafe_allow_html=True,
            )
        with right:
            b = COMPANIES["B"]
            st.markdown(
                f'<div class="company-card" style="background: linear-gradient(135deg, {b["c1"]}, {b["c2"]});"><h2>{b["name"]}</h2><p><b>{b["tagline"]}</b></p><p>{b["story"]}</p></div>',
                unsafe_allow_html=True,
            )

        st.markdown("### Başlangıç Dağılımı")
        alloc_a = st.slider(COMPANIES["A"]["name"], min_value=0, max_value=100, value=st.session_state.alloc_a)
        alloc_b = 100 - alloc_a
        st.session_state.alloc_a = alloc_a

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f'<div class="metric-box"><div class="metric-value">{tr_num(STARTING_CASH)}</div><div class="metric-label">Başlangıç Ana Para</div></div>',
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f'<div class="metric-box"><div class="metric-value">%{alloc_a}</div><div class="metric-label">{COMPANIES["A"]["short"]} Ağırlığı</div></div>',
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f'<div class="metric-box"><div class="metric-value">%{alloc_b}</div><div class="metric-label">{COMPANIES["B"]["short"]} Ağırlığı</div></div>',
                unsafe_allow_html=True,
            )

        if st.button("Seansı Başlat", use_container_width=True):
            init_positions_from_allocation(alloc_a)
            st.session_state.started = True
            reveal_next_event()
            st.rerun()
    else:
        market_fragment()

with balance_tab:
    t1, t2 = st.tabs([COMPANIES["A"]["name"], COMPANIES["B"]["name"]])
    with t1:
        st.markdown("### Bilanço")
        st.table(COMPANIES["A"]["balance_sheet"])
        st.markdown("### Gelir Tablosu")
        st.table(COMPANIES["A"]["income"])
        if st.button("İncelendi", key="view_a"):
            st.session_state.viewed_a = True
            st.rerun()
    with t2:
        st.markdown("### Bilanço")
        st.table(COMPANIES["B"]["balance_sheet"])
        st.markdown("### Gelir Tablosu")
        st.table(COMPANIES["B"]["income"])
        if st.button("İncelendi", key="view_b"):
            st.session_state.viewed_b = True
            st.rerun()
