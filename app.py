import streamlit as st

st.set_page_config(
    page_title="Halka Arz Oyunu",
    page_icon="🎮",
    layout="wide"
)

# -----------------------------
# Stil
# -----------------------------
st.markdown("""
<style>
.hero {
    padding: 24px;
    border-radius: 22px;
    background: linear-gradient(135deg, #111827, #2563eb, #06b6d4);
    color: white;
    margin-bottom: 20px;
}
.game-card {
    padding: 22px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}
.choice-card {
    padding: 18px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    margin-bottom: 10px;
}
.metric-box {
    padding: 16px;
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
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Oyun state
# -----------------------------
def init_game():
    if "stage" not in st.session_state:
        st.session_state.stage = 0
    if "trust" not in st.session_state:
        st.session_state.trust = 50
    if "readiness" not in st.session_state:
        st.session_state.readiness = 50
    if "demand" not in st.session_state:
        st.session_state.demand = 50
    if "log" not in st.session_state:
        st.session_state.log = []
    if "company_name" not in st.session_state:
        st.session_state.company_name = "Nova Teknoloji A.Ş."
    if "fund_need" not in st.session_state:
        st.session_state.fund_need = 250

def reset_game():
    st.session_state.stage = 0
    st.session_state.trust = 50
    st.session_state.readiness = 50
    st.session_state.demand = 50
    st.session_state.log = []

def choose(trust_delta, readiness_delta, demand_delta, message):
    st.session_state.trust += trust_delta
    st.session_state.readiness += readiness_delta
    st.session_state.demand += demand_delta
    st.session_state.log.append(message)
    st.session_state.stage += 1
    st.rerun()

init_game()

# -----------------------------
# Başlık
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎮 Halka Arz Oyunu</h1>
    <p>
        Bu oyunda bir firma sahibisin. Şirketinin fon ihtiyacını halka arz ile karşılamaya çalışıyorsun.
        Her aşamada karar vereceksin. Kararların, yatırımcı güvenini, hazırlık seviyeni ve talebi etkileyecek.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Üst bar
# -----------------------------
top1, top2, top3, top4 = st.columns([1, 1, 1, 1])

with top1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.trust}</div>
        <div class="metric-label">Yatırımcı Güveni</div>
    </div>
    """, unsafe_allow_html=True)

with top2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.readiness}</div>
        <div class="metric-label">Hazırlık Seviyesi</div>
    </div>
    """, unsafe_allow_html=True)

with top3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.demand}</div>
        <div class="metric-label">Talep Gücü</div>
    </div>
    """, unsafe_allow_html=True)

with top4:
    if st.button("🔄 Oyunu Sıfırla", use_container_width=True):
        reset_game()
        st.rerun()

st.progress(min(st.session_state.stage / 5, 1.0))

# -----------------------------
# Oyun ekranı
# -----------------------------
company_name = st.session_state.company_name
fund_need = st.session_state.fund_need

if st.session_state.stage == 0:
    st.markdown(f"""
    <div class="game-card">
        <h2>🏢 Bölüm 1: Fon İhtiyacı Doğuyor</h2>
        <p>
            Sen, <b>{company_name}</b> şirketinin sahibisin.
            Şirketin büyümek için <b>{fund_need} milyon TL</b> kaynağa ihtiyaç duyuyor.
            Yeni üretim hattı kurmak ve pazarda büyümek istiyorsun.
        </p>
        <p>
            Banka kredisi yerine <b>halka arz</b> seçeneğini değerlendiriyorsun.
            İlk önemli kararın: süreci kiminle yöneteceğin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("İlk kararın ne?")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="choice-card"><b>Güçlü aracı kurum</b><br>Tecrübeli, pahalı ama güven veriyor.</div>', unsafe_allow_html=True)
        if st.button("Bu seçeneği seç", key="stage0_opt1", use_container_width=True):
            choose(+10, +15, +5, "Güçlü aracı kurum seçildi. Piyasa güveni arttı.")

    with c2:
        st.markdown('<div class="choice-card"><b>Orta seviye aracı kurum</b><br>Daha dengeli ama sınırlı etki.</div>', unsafe_allow_html=True)
        if st.button("Bu seçeneği seç ", key="stage0_opt2", use_container_width=True):
            choose(+5, +5, 0, "Orta seviye aracı kurum seçildi. Süreç dengeli ilerliyor.")

    with c3:
        st.markdown('<div class="choice-card"><b>Ucuz ama zayıf aracı kurum</b><br>Maliyet düşük, güven etkisi zayıf.</div>', unsafe_allow_html=True)
        if st.button("Bu seçeneği seç  ", key="stage0_opt3", use_container_width=True):
            choose(-5, -10, -5, "Zayıf aracı kurum seçildi. Hazırlık seviyesi düştü.")

elif st.session_state.stage == 1:
    st.markdown("""
    <div class="game-card">
        <h2>📑 Bölüm 2: İzahname ve Hazırlık Süreci</h2>
        <p>
            Halka arz öncesinde şirketin finansal yapısı, riskleri ve büyüme planları yatırımcılara anlatılmalı.
            Şimdi açıklamaların ne kadar şeffaf olacağına karar vereceksin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="choice-card"><b>Tam şeffaf açıklama</b><br>Riskleri ve güçlü yönleri açıkça paylaş.</div>', unsafe_allow_html=True)
        if st.button("Şeffaf ol", key="stage1_opt1", use_container_width=True):
            choose(+15, +10, +5, "Şeffaf açıklama yapıldı. Yatırımcı güveni yükseldi.")

    with c2:
        st.markdown('<div class="choice-card"><b>Sadece iyi tarafları anlat</b><br>Riskleri geri planda bırak.</div>', unsafe_allow_html=True)
        if st.button("Riskleri geri planda bırak", key="stage1_opt2", use_container_width=True):
            choose(-15, -5, -10, "Yetersiz açıklama yatırımcı güvenini düşürdü.")

elif st.session_state.stage == 2:
    st.markdown("""
    <div class="game-card">
        <h2>💰 Bölüm 3: Fiyatlama Kararı</h2>
        <p>
            Şimdi şirket paylarının hangi seviyeden halka arz edileceğine karar vereceksin.
            Fiyat çok yüksek olursa talep düşebilir; çok düşük olursa daha az kaynak toplayabilirsin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="choice-card"><b>Dengeli fiyat</b><br>Yatırımcı ilgisini korur.</div>', unsafe_allow_html=True)
        if st.button("Dengeli fiyatı seç", key="stage2_opt1", use_container_width=True):
            choose(+10, 0, +20, "Dengeli fiyatlama talebi artırdı.")

    with c2:
        st.markdown('<div class="choice-card"><b>Yüksek fiyat</b><br>Daha fazla fon hedefle ama riskli.</div>', unsafe_allow_html=True)
        if st.button("Yüksek fiyatı seç", key="stage2_opt2", use_container_width=True):
            choose(-10, 0, -20, "Aşırı fiyatlama talebi zayıflattı.")

    with c3:
        st.markdown('<div class="choice-card"><b>Düşük fiyat</b><br>Talep artabilir ama gelir sınırlı kalır.</div>', unsafe_allow_html=True)
        if st.button("Düşük fiyatı seç", key="stage2_opt3", use_container_width=True):
            choose(+5, 0, +10, "Düşük fiyat yatırımcı ilgisini artırdı ama potansiyel gelir sınırlandı.")

elif st.session_state.stage == 3:
    st.markdown("""
    <div class="game-card">
        <h2>📣 Bölüm 4: Yatırımcı Sunumu ve Talep Toplama Öncesi</h2>
        <p>
            Şirketini yatırımcılara nasıl anlatacağın çok önemli. Güçlü bir iletişim talebi artırabilir.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="choice-card"><b>Yoğun yatırımcı turu yap</b><br>Sunumlar, görüşmeler, güçlü iletişim.</div>', unsafe_allow_html=True)
        if st.button("Roadshow yap", key="stage3_opt1", use_container_width=True):
            choose(+10, +5, +15, "Yatırımcı iletişimi güçlü kuruldu. Talep arttı.")

    with c2:
        st.markdown('<div class="choice-card"><b>Minimum iletişimle ilerle</b><br>Zaman kazan ama ilgi düşük kalabilir.</div>', unsafe_allow_html=True)
        if st.button("Minimum iletişim", key="stage3_opt2", use_container_width=True):
            choose(-10, 0, -15, "Yetersiz iletişim yatırımcı ilgisini düşürdü.")

elif st.session_state.stage == 4:
    st.markdown("""
    <div class="game-card">
        <h2>📊 Bölüm 5: Talep Toplama Sonucu</h2>
        <p>
            Talep toplama tamamlandı. Şimdi kararlarının sonucunu göreceksin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    total_score = st.session_state.trust + st.session_state.readiness + st.session_state.demand

    if total_score >= 210:
        result = "🚀 Çok Başarılı Halka Arz"
        detail = "Yatırımcı ilgisi çok yüksek. Halka arz güçlü tamamlandı ve şirket piyasada güçlü başladı."
        box = st.success
    elif total_score >= 170:
        result = "✅ Başarılı Halka Arz"
        detail = "Halka arz başarılı geçti. Şirket hedeflediği fonun büyük bölümünü topladı."
        box = st.info
    elif total_score >= 130:
        result = "⚠️ Zayıf Talep"
        detail = "Halka arz tamamlandı ancak talep beklentinin altında kaldı."
        box = st.warning
    else:
        result = "❌ Başarısız Halka Arz"
        detail = "Yatırımcı ilgisi yetersiz kaldı. Halka arz ertelendi ya da zayıf sonuçlandı."
        box = st.error

    box(f"Sonuç: {result}")
    st.markdown(f"**Toplam performans puanın:** {total_score}")
    st.markdown(detail)

    st.markdown("### Karar Geçmişin")
    for item in st.session_state.log:
        st.markdown(f"- {item}")

    if st.button("Final ekranına geç", use_container_width=True):
        st.session_state.stage = 5
        st.rerun()

elif st.session_state.stage == 5:
    st.markdown("""
    <div class="game-card">
        <h2>🏁 Oyun Bitti</h2>
        <p>
            Halka arz sürecini tamamladın. Bu oyunun amacı, halka arzın sadece bir finansman kararı olmadığını;
            aynı zamanda güven, hazırlık, fiyatlama ve yatırımcı iletişimi gerektiren bir süreç olduğunu göstermektir.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Tekrar Oyna", use_container_width=True):
        reset_game()
        st.rerun()
