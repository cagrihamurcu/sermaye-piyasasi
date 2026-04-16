import streamlit as st

st.set_page_config(
    page_title="Halka Arz Kriz Oyunu",
    page_icon="🎮",
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
    background: linear-gradient(135deg, #111827, #1d4ed8, #06b6d4);
    color: white;
    margin-bottom: 20px;
}
.panel {
    padding: 20px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 18px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}
.choice {
    padding: 16px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    min-height: 120px;
}
.metric-box {
    padding: 14px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    text-align: center;
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
.small-note {
    color: #64748b;
    font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Başlangıç state
# -------------------------------------------------
def init_game():
    defaults = {
        "stage": 0,
        "trust": 55,          # yatırımcı güveni
        "compliance": 20,     # uyum / hukuki risk
        "cash": 0,            # toplanan para (milyon TL)
        "debt_pressure": 70,  # borç baskısı
        "share_price": 100,   # halka arz sonrası baz fiyat endeksi
        "log": [],
        "misled_market": False,
        "used_cash_for_debt": False,
        "hid_bad_results": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_game():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    init_game()

def next_stage():
    st.session_state.stage += 1
    st.rerun()

def apply_effects(
    *,
    trust=0,
    compliance=0,
    cash=0,
    debt_pressure=0,
    share_price=0,
    log="",
    misled_market=None,
    used_cash_for_debt=None,
    hid_bad_results=None,
):
    st.session_state.trust += trust
    st.session_state.compliance += compliance
    st.session_state.cash += cash
    st.session_state.debt_pressure += debt_pressure
    st.session_state.share_price += share_price

    # Sınırlar
    st.session_state.trust = max(0, min(100, st.session_state.trust))
    st.session_state.compliance = max(0, min(100, st.session_state.compliance))
    st.session_state.debt_pressure = max(0, min(100, st.session_state.debt_pressure))
    st.session_state.share_price = max(1, st.session_state.share_price)

    if log:
        st.session_state.log.append(log)

    if misled_market is not None:
        st.session_state.misled_market = misled_market
    if used_cash_for_debt is not None:
        st.session_state.used_cash_for_debt = used_cash_for_debt
    if hid_bad_results is not None:
        st.session_state.hid_bad_results = hid_bad_results

    next_stage()

init_game()

COMPANY = "Nova Teknoloji A.Ş."
TARGET = 250  # milyon TL

# -------------------------------------------------
# Üst alan
# -------------------------------------------------
st.markdown(f"""
<div class="hero">
    <h1>🎮 Halka Arz Kriz Oyunu</h1>
    <p>
        Sen, <b>{COMPANY}</b> şirketinin sahibisin. Şirketin büyümek için <b>{TARGET} milyon TL</b> kaynağa ihtiyacı var.
        Halka arza gidiyorsun. Kararların kısa vadede para toplamanı sağlayabilir; ama yanlış bilgi, gizli fon kullanımı
        ve geç açıklanan zararlar sonunda şirkete ağır bedel ödetebilir.
    </p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.trust}</div>
        <div class="metric-label">Yatırımcı Güveni</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.compliance}</div>
        <div class="metric-label">Uyum Riski</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.cash}</div>
        <div class="metric-label">Toplanan Para (milyon TL)</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.debt_pressure}</div>
        <div class="metric-label">Borç Baskısı</div>
    </div>
    """, unsafe_allow_html=True)

with m5:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{st.session_state.share_price}</div>
        <div class="metric-label">Fiyat Endeksi</div>
    </div>
    """, unsafe_allow_html=True)

st.progress(min(st.session_state.stage / 4, 1.0))

top_left, top_right = st.columns([4, 1])
with top_right:
    if st.button("🔄 Oyunu Sıfırla", use_container_width=True):
        reset_game()
        st.rerun()

# -------------------------------------------------
# Oyun sahneleri
# -------------------------------------------------
if st.session_state.stage == 0:
    st.markdown("""
    <div class="panel">
        <h2>1. İzahname Hazırlığı</h2>
        <p>
            Halka arz öncesi şirkete dair hikâyeyi yatırımcıya nasıl anlatacağına karar veriyorsun.
            Şirketin aslında ciddi borç baskısı var. Buna rağmen çok parlak bir büyüme hikâyesi kurabilir,
            ya da daha dengeli ve gerçekçi bir anlatım seçebilirsin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="choice">
            <h4>✅ Dengeli ve gerçekçi anlatım</h4>
            <p>Yatırımcılara büyüme fırsatlarını anlat ama riskleri de saklama.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Gerçekçi anlatımı seç", key="s0_a", use_container_width=True):
            apply_effects(
                trust=5,
                compliance=-10,
                log="İzahname daha dengeli hazırlandı. Kısa vadeli heyecan sınırlı kaldı ama güven korundu.",
                misled_market=False,
            )

    with c2:
        st.markdown("""
        <div class="choice">
            <h4>⚠️ Aşırı parlak / yanıltıcı hikâye</h4>
            <p>Riskleri arka plana it, büyümeyi öne çıkar, yatırımcı ilgisini yükselt.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Parlak hikâyeyi seç", key="s0_b", use_container_width=True):
            apply_effects(
                trust=18,
                compliance=30,
                log="Şirket aşırı parlak bir hikâyeyle yatırımcı ilgisini yükseltti. Uyum riski belirgin arttı.",
                misled_market=True,
            )

elif st.session_state.stage == 1:
    st.markdown("""
    <div class="panel">
        <h2>2. Halka Arz ve Para Toplama</h2>
        <p>
            Talep toplama aşamasına geldin. Şimdi fiyatlamayı nasıl yapacağına karar vereceksin.
            Buradaki seçim, ne kadar para toplayacağını ve ilk piyasa algısını etkileyecek.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="choice">
            <h4>📊 Dengeli fiyatlama</h4>
            <p>Daha güvenli, daha istikrarlı bir halka arz.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Dengeli fiyatı seç", key="s1_a", use_container_width=True):
            apply_effects(
                cash=220,
                trust=5,
                share_price=3,
                log="Dengeli fiyatlama sayesinde halka arz makul ilgi gördü.",
            )

    with c2:
        st.markdown("""
        <div class="choice">
            <h4>🚀 Agresif fiyatlama</h4>
            <p>Daha çok para toplamaya çalış ama talep kırılgan olabilir.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Agresif fiyatı seç", key="s1_b", use_container_width=True):
            if st.session_state.misled_market:
                apply_effects(
                    cash=300,
                    trust=8,
                    compliance=10,
                    share_price=8,
                    log="Parlak hikâye ve agresif fiyatlama ile güçlü para toplandı. Kısa vadede başarılı görünüm oluştu.",
                )
            else:
                apply_effects(
                    cash=240,
                    trust=-5,
                    compliance=5,
                    share_price=-2,
                    log="Agresif fiyatlama yatırımcıyı zorladı. Beklenen kadar güçlü karşılık bulmadı.",
                )

    with c3:
        st.markdown("""
        <div class="choice">
            <h4>🪙 İskontolu fiyatlama</h4>
            <p>Talebi artır ama daha az kaynak topla.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("İskontolu fiyatı seç", key="s1_c", use_container_width=True):
            apply_effects(
                cash=200,
                trust=10,
                share_price=10,
                log="İskontolu fiyatlama yatırımcıyı memnun etti; talep canlı kaldı ama daha az kaynak toplandı.",
            )

elif st.session_state.stage == 2:
    st.markdown("""
    <div class="panel">
        <h2>3. Halka Arz Sonrası: Parayı Nereye Koyuyorsun?</h2>
        <p>
            Para kasaya girdi. Yatırımcılar bu kaynağın büyüme planlarında kullanılmasını bekliyor.
            Ancak şirketin borç baskısı da devam ediyor. Şimdi en kritik kararlarından birini vereceksin.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="choice">
            <h4>🏭 Açıklanan projelere yatırım yap</h4>
            <p>Kaynağı üretim hattı ve büyüme planı için kullan.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Projeye yatır", key="s2_a", use_container_width=True):
            apply_effects(
                trust=8,
                compliance=-5,
                debt_pressure=-10,
                share_price=5,
                log="Toplanan kaynak, açıklanan yatırım planına uygun biçimde kullanıldı.",
                used_cash_for_debt=False,
            )

    with c2:
        st.markdown("""
        <div class="choice">
            <h4>⚠️ Parayı gizlice borca kaydır</h4>
            <p>Kısa vadede nefes al ama yatırımcı beklentisi ile kullanım arasında fark oluşsun.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Borca kaydır", key="s2_b", use_container_width=True):
            apply_effects(
                trust=-10,
                compliance=35,
                debt_pressure=-35,
                share_price=2,
                log="Şirket, halka arz gelirinin önemli bölümünü açıklanan amaç dışında borç baskısını hafifletmek için kullandı.",
                used_cash_for_debt=True,
            )

    with c3:
        st.markdown("""
        <div class="choice">
            <h4>📄 Kısmi yön değişikliği açıkla</h4>
            <p>Bir kısmını yatırımda kullan, bir kısmını borç yönetimine kaydır ve bunu duyur.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Karma çözüm", key="s2_c", use_container_width=True):
            apply_effects(
                trust=-3,
                compliance=8,
                debt_pressure=-20,
                share_price=0,
                log="Şirket fon kullanımında değişikliğe gitti; piyasa bunu temkinli karşıladı.",
                used_cash_for_debt=False,
            )

elif st.session_state.stage == 3:
    st.markdown("""
    <div class="panel">
        <h2>4. İlk Çeyrek Sonu: Sonuçlar Zayıf</h2>
        <p>
            Operasyonlar beklendiği kadar iyi gitmedi. Şirket zarar açıklayacak gibi görünüyor.
            Şimdi iletişim biçimine karar vereceksin: erken ve şeffaf açıklama mı, yoksa kötü tabloyu geciktirip
            piyasayı bir süre daha olumlu tutmaya çalışma mı?
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="choice">
            <h4>🟢 Zararı açık ve erken duyur</h4>
            <p>Piyasa ilk anda olumsuz tepki verebilir ama güveni koruyabilirsin.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Şeffaf şekilde açıkla", key="s3_a", use_container_width=True):
            apply_effects(
                trust=5,
                compliance=-10,
                share_price=-12,
                log="Şirket beklenenden zayıf sonuçları gecikmeden açıkladı. Kısa vadeli fiyat baskısı oluştu ama güven korundu.",
                hid_bad_results=False,
            )

    with c2:
        st.markdown("""
        <div class="choice">
            <h4>🔴 Zararı geciktir / yumuşat</h4>
            <p>Kısa vadede fiyatı korumaya çalış ama risk katlanabilir.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Geç ve yumuşak açıkla", key="s3_b", use_container_width=True):
            apply_effects(
                trust=-12,
                compliance=25,
                share_price=5,
                log="Şirket zayıf tabloyu geç ve yumuşatılmış biçimde aktarmaya çalıştı. Kısa vadeli görüntü korundu ama risk çok yükseldi.",
                hid_bad_results=True,
            )

elif st.session_state.stage == 4:
    st.markdown("""
    <div class="panel">
        <h2>🏁 Final: Piyasa Gerçeği Görüyor</h2>
        <p>
            Artık oyunun sonucu oluştu. Kısa vadede para toplamış olabilirsin; ama yatırımcı güveni,
            fon kullanımının niteliği ve açıklamaların doğruluğu şimdi birleşik biçimde etkisini gösteriyor.
        </p>
    </div>
    """, unsafe_allow_html=True)

    total_risk = st.session_state.compliance
    bad_combo = (
        st.session_state.misled_market
        and st.session_state.used_cash_for_debt
        and st.session_state.hid_bad_results
    )

    st.markdown("### Oyun Sonucu")

    if bad_combo:
        st.error("""
**Kriz Senaryosu:**  
Yanıltıcı hikâye ile güçlü para topladın, fonu ağırlıklı olarak borç baskısını azaltmak için kullandın
ve ardından zayıf sonuçları geç açıkladın. Kısa vadede başarılı görünsen de sonunda güven sert biçimde kırıldı,
fiyat çöktü ve şirket ağır itibar kaybına uğradı.
        """)
        st.session_state.share_price = max(10, st.session_state.share_price - 45)

    elif total_risk >= 75:
        st.error("""
**Sert Çöküş Senaryosu:**  
Uyum riski çok yükseldi. Şirketin iletişimi ile gerçek performansı arasındaki fark büyüdü.
Piyasa güveni bozuldu, sert satış geldi ve şirket ciddi kriz yaşadı.
        """)
        st.session_state.share_price = max(15, st.session_state.share_price - 35)

    elif total_risk >= 45:
        st.warning("""
**Kırılgan Halka Arz Senaryosu:**  
Şirket halka arzı tamamladı ve para topladı; ancak fon kullanımı ve sonuç açıklamaları soru işareti yarattı.
Piyasa şirketi artık daha temkinli fiyatlıyor.
        """)
        st.session_state.share_price = max(25, st.session_state.share_price - 20)

    else:
        st.success("""
**Kontrollü Yönetim Senaryosu:**  
Şirket halka arz sonrasında zor bir dönem yaşasa da süreçte şeffaf kaldı.
Fiyat baskısı oldu ama güven tamamen kaybolmadı.
        """)

    st.markdown("### Final Göstergeleri")
    f1, f2, f3 = st.columns(3)

    with f1:
        st.metric("Toplanan Para", f"{st.session_state.cash} milyon TL")
    with f2:
        st.metric("Son Güven", st.session_state.trust)
    with f3:
        st.metric("Final Fiyat Endeksi", st.session_state.share_price)

    st.markdown("### Karar Geçmişi")
    for item in st.session_state.log:
        st.markdown(f"- {item}")

    if st.button("Tekrar Oyna", use_container_width=True):
        reset_game()
        st.rerun()
