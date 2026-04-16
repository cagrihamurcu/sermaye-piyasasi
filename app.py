import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Halka Arz Karar Oyunu",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------
# Stil
# -------------------------------------------------
st.markdown("""
<style>
.hero {
    padding: 26px;
    border-radius: 24px;
    background: linear-gradient(135deg, #0f172a, #1d4ed8, #06b6d4);
    color: white;
    margin-bottom: 20px;
}
.card {
    padding: 18px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.06);
    margin-bottom: 14px;
}
.company-card {
    padding: 20px;
    border-radius: 18px;
    color: white;
    min-height: 240px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.10);
}
.metric-box {
    padding: 14px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    text-align: center;
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
.note-good {
    padding: 14px;
    border-radius: 14px;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
}
.note-bad {
    padding: 14px;
    border-radius: 14px;
    background: #fef2f2;
    border: 1px solid #fecaca;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# State
# -------------------------------------------------
if "viewed_a" not in st.session_state:
    st.session_state.viewed_a = False
if "viewed_b" not in st.session_state:
    st.session_state.viewed_b = False
if "invested" not in st.session_state:
    st.session_state.invested = False
if "allocation_a" not in st.session_state:
    st.session_state.allocation_a = 50
if "allocation_b" not in st.session_state:
    st.session_state.allocation_b = 50

# -------------------------------------------------
# Şirket verileri
# -------------------------------------------------
company_a = {
    "name": "Anka Gıda A.Ş.",
    "tagline": "Dengeli büyüme, güçlü nakit akışı, ölçülü halka arz hikâyesi.",
    "story": """
Anka Gıda, son yıllarda düzenli büyüyen, faaliyet kârlılığı istikrarlı seyreden ve
yeni üretim hattı yatırımı için halka arza çıkan bir şirkettir. Yönetim sunumlarında
daha ölçülü ve gerçekçi bir dil kullanmaktadır.
    """,
    "return_pct": 18,
    "after_news": "Şirket yıl sonunda kârını artırdı ve yatırım planına büyük ölçüde sadık kaldı.",
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
Bu firmada borçluluk yönetilebilir düzeydedir. Cari oran sağlıklıdır, özkaynak yapısı görece güçlüdür
ve kârlılık pozitiftir. Halka arz gelirinin yeni yatırım ve kapasite artırımı için kullanılacağı belirtilmektedir.
    """
}

company_b = {
    "name": "Lima Teknoloji A.Ş.",
    "tagline": "Parlak sunumlar, agresif büyüme vaadi, güçlü reklam dili.",
    "story": """
Lima Teknoloji, yatırımcı sunumlarında hızlı büyüme, büyük pazar fırsatı ve yüksek getiri potansiyeli
vurgulamaktadır. Kamuya açık anlatımı çok caziptir; ancak bilanço detaylarına bakılmadığında riskler
kolayca gözden kaçabilir.
    """,
    "return_pct": -52,
    "after_news": "Şirket yıl sonunda zarar açıkladı; halka arz gelirinin önemli kısmının borç baskısını hafifletmeye gittiği anlaşıldı.",
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
Bu firmada borç baskısı yüksektir. Kısa vadeli yükümlülükler ve toplam borç seviyesi özkaynağa göre ağırdır.
Cari oran zayıftır ve şirket zarar yazmaktadır. Buna rağmen tanıtım dili oldukça parlaktır; bu da dikkatli
olmayan yatırımcıyı yanıltabilir.
    """
}

# -------------------------------------------------
# Üst alan
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🎮 Halka Arz Karar Oyunu</h1>
    <p>
        Önünde iki halka arz adayı firma var. İkisi de ilk bakışta cazip görünebilir.
        Ancak yatırım yapmadan önce bilanço incelemek kritik olabilir.
        Bilançoya bakmadan yatırım yapanları sürprizler bekleyebilir.
    </p>
</div>
""", unsafe_allow_html=True)

top1, top2, top3 = st.columns(3)
with top1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Evet' if st.session_state.viewed_a else 'Hayır'}</div>
        <div class="metric-label">Anka bilançosu incelendi mi?</div>
    </div>
    """, unsafe_allow_html=True)
with top2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Evet' if st.session_state.viewed_b else 'Hayır'}</div>
        <div class="metric-label">Lima bilançosu incelendi mi?</div>
    </div>
    """, unsafe_allow_html=True)
with top3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{'Yapıldı' if st.session_state.invested else 'Bekliyor'}</div>
        <div class="metric-label">Yatırım kararı</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# Sekmeler
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🏢 Halka Arzlar",
    "📑 Bilançolar",
    "💸 Yatırım Kararı",
    "📉 Sonuç"
])

# -------------------------------------------------
# TAB 1 - Halka arz sunumları
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

    st.info("Not: Buradaki tanıtım dili tek başına yeterli olmayabilir. Gerçek risk için bilanço tarafına da bakmak gerekir.")

# -------------------------------------------------
# TAB 2 - Bilançolar
# -------------------------------------------------
with tab2:
    st.subheader("Bilançolar")

    balance_tab1, balance_tab2 = st.tabs([company_a["name"], company_b["name"]])

    with balance_tab1:
        st.markdown("### Basitleştirilmiş bilanço görünümü")
        st.table(company_a["balance_sheet"])
        st.markdown(f"""
        <div class="note-good">
            <b>Analiz:</b> {company_a['analysis']}
        </div>
        """, unsafe_allow_html=True)

        if st.button("Anka bilançosunu inceledim", key="view_a"):
            st.session_state.viewed_a = True
            st.success("Anka bilançosu incelendi.")

    with balance_tab2:
        st.markdown("### Basitleştirilmiş bilanço görünümü")
        st.table(company_b["balance_sheet"])
        st.markdown(f"""
        <div class="note-bad">
            <b>Analiz:</b> {company_b['analysis']}
        </div>
        """, unsafe_allow_html=True)

        if st.button("Lima bilançosunu inceledim", key="view_b"):
            st.session_state.viewed_b = True
            st.warning("Lima bilançosu incelendi. Borçluluk dikkat çekiyor.")

# -------------------------------------------------
# TAB 3 - Yatırım kararı
# -------------------------------------------------
with tab3:
    st.subheader("Yatırım Kararı")

    st.markdown("Toplam 100 birim paran var. Bunu iki halka arz arasında dağıt.")

    allocation_a = st.slider(
        f"{company_a['name']} için yatırım oranı",
        min_value=0,
        max_value=100,
        value=st.session_state.allocation_a
    )
    allocation_b = 100 - allocation_a

    st.session_state.allocation_a = allocation_a
    st.session_state.allocation_b = allocation_b

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(company_a["name"], f"%{allocation_a}")
    with col_b:
        st.metric(company_b["name"], f"%{allocation_b}")

    st.markdown("---")

    if st.button("Yatırımı Onayla", use_container_width=True):
        st.session_state.invested = True
        st.success("Yatırım kararın kaydedildi. Sonuç sekmesine geçebilirsin.")

    if not st.session_state.viewed_a or not st.session_state.viewed_b:
        st.info("Bilançoların tamamını incelemeden de yatırım yapabilirsin. Ama bu durumda sürprizlerle karşılaşabilirsin.")

# -------------------------------------------------
# TAB 4 - Sonuç
# -------------------------------------------------
with tab4:
    st.subheader("Sonuç")

    if not st.session_state.invested:
        st.warning("Önce yatırım kararını tamamlamalısın.")
    else:
        invest_a = st.session_state.allocation_a
        invest_b = st.session_state.allocation_b

        result_a = invest_a * (1 + company_a["return_pct"] / 100)
        result_b = invest_b * (1 + company_b["return_pct"] / 100)
        total_final = result_a + result_b

        r1, r2, r3 = st.columns(3)
        with r1:
            st.metric("Başlangıç Portföyü", "100 birim")
        with r2:
            st.metric("Yıl Sonu Portföyü", f"{total_final:.1f} birim")
        with r3:
            st.metric("Toplam Getiri", f"%{total_final - 100:.1f}")

        st.markdown("---")
        st.markdown("### Firma Bazlı Sonuçlar")

        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"""
            <div class="card">
                <h3>🟢 {company_a['name']}</h3>
                <p><b>Yıl sonu değişim:</b> %{company_a['return_pct']}</p>
                <p>{company_a['after_news']}</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="card">
                <h3>🔴 {company_b['name']}</h3>
                <p><b>Yıl sonu değişim:</b> %{company_b['return_pct']}</p>
                <p>{company_b['after_news']}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Oyun Yorumu")

        if invest_b > 0 and not st.session_state.viewed_b:
            st.error("""
Lima Teknoloji’ye bilançosuna bakmadan yatırım yaptın.  
Parlak halka arz anlatımı dikkat çekiciydi; ancak bilanço tarafındaki yüksek borç baskısı ve zayıf yapı gözden kaçtı.
Bu nedenle yıl sonunda gelen zarar açıklaması senin için sürpriz oldu.
            """)
        elif invest_b > 0 and st.session_state.viewed_b:
            st.warning("""
Lima Teknoloji’nin bilançosunu gördün; borçluluk riskini biliyordun.  
Buna rağmen yatırım yaptın ve bu risk gerçekleşti.
            """)
        elif invest_b == 0 and st.session_state.viewed_b:
            st.success("""
Bilançoyu inceledin ve yüksek borçluluk riskini fark ettin.  
Bu sayede daha temkinli bir yatırım kararı verdin.
            """)
        else:
            st.info("""
Yatırım kararını verirken bilanço tarafını yeterince kullanmadın.  
Bu oyun, halka arzlarda tanıtım metni kadar finansal tabloların da önemli olduğunu göstermektedir.
            """)
