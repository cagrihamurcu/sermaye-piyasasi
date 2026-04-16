import streamlit as st

st.set_page_config(
    page_title="Halka Arz Süreci",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Stil
# -----------------------------
st.markdown("""
<style>
.hero {
    padding: 24px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1d4ed8, #06b6d4);
    color: white;
    margin-bottom: 20px;
}
.info-card {
    padding: 18px;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    margin-bottom: 14px;
}
.step-card {
    padding: 24px;
    border-radius: 18px;
    background: white;
    border-left: 8px solid #2563eb;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
.step-number {
    font-size: 0.95rem;
    color: #64748b;
    margin-bottom: 8px;
}
.step-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 12px;
}
.actor {
    font-weight: 700;
    color: #1d4ed8;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Firma senaryosu
# -----------------------------
firma_adi = "Nova Teknoloji A.Ş."
fon_ihtiyaci = "250.000.000 TL"
fon_amaci = "Yeni üretim hattı kurmak, kapasite artırmak ve teknoloji yatırımı yapmak"

steps = [
    {
        "title": "Fon İhtiyacının Doğması",
        "actor": "Şirket Yönetimi",
        "what": f"{firma_adi}, büyümek ve yatırım yapmak için {fon_ihtiyaci} tutarında kaynağa ihtiyaç duyar.",
        "why": "Şirketin üretim kapasitesini artırması ve büyüme planlarını finanse etmesi gerekir."
    },
    {
        "title": "Halka Arz Kararının Verilmesi",
        "actor": "Şirket Yönetimi",
        "what": "Şirket, banka kredisi yerine sermaye piyasasından fon toplamaya karar verir.",
        "why": "Halka arz, uzun vadeli fon sağlama ve şirketin kurumsal görünürlüğünü artırma fırsatı sunar."
    },
    {
        "title": "Aracı Kurum ile Sürecin Planlanması",
        "actor": "Aracı Kurum",
        "what": "Şirket, halka arzın fiyatlama, satış ve organizasyon süreci için bir aracı kurumla çalışır.",
        "why": "Aracı kurum, sürecin teknik ve finansal açıdan doğru kurgulanmasını sağlar."
    },
    {
        "title": "İzahname, SPK ve Kamuyu Aydınlatma Süreci",
        "actor": "SPK ve KAP",
        "what": "Şirkete ait finansal ve hukuki bilgiler hazırlanır, izahname oluşturulur ve kamuya gerekli açıklamalar yapılır.",
        "why": "Yatırımcıların doğru bilgiye ulaşması ve sürecin güvenli yürütülmesi için bu aşama zorunludur."
    },
    {
        "title": "Talep Toplama",
        "actor": "Yatırımcılar",
        "what": "Yatırımcılar halka arza katılarak şirket paylarına talepte bulunur.",
        "why": "Şirketin fon toplaması, yatırımcıların gösterdiği ilgiyle mümkün hale gelir."
    },
    {
        "title": "Borsada İşlem Görmeye Başlama",
        "actor": "Borsa İstanbul",
        "what": f"Halka arz tamamlandıktan sonra {firma_adi} payları borsada işlem görmeye başlar.",
        "why": "Bu aşama şirket paylarının alınıp satılabildiği ikincil piyasa yapısını oluşturur."
    },
    {
        "title": "Takas ve Kayıt Sürecinin Tamamlanması",
        "actor": "Takasbank ve MKK",
        "what": "İşlem sonrası takas gerçekleştirilir ve payların mülkiyeti kaydi sistemde yatırımcı bazında izlenir.",
        "why": "İşlemlerin güvenli ve kayıtlı biçimde tamamlanması için bu aşama gereklidir."
    }
]

# -----------------------------
# State
# -----------------------------
if "step_index" not in st.session_state:
    st.session_state.step_index = 0

current = steps[st.session_state.step_index]

# -----------------------------
# Başlık
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>📈 Halka Arz Süreci</h1>
    <p>Bir firmanın fon ihtiyacını halka arz yoluyla nasıl karşıladığı adım adım gösterilmektedir.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Firma bilgisi
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="info-card">
        <b>Firma</b><br>{firma_adi}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-card">
        <b>Fon İhtiyacı</b><br>{fon_ihtiyaci}
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <b>Fonun Kullanım Amacı</b><br>{fon_amaci}
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Adım göstergesi
# -----------------------------
st.progress((st.session_state.step_index + 1) / len(steps))
st.caption(f"Adım {st.session_state.step_index + 1} / {len(steps)}")

# -----------------------------
# Süreç kartı
# -----------------------------
st.markdown(f"""
<div class="step-card">
    <div class="step-number">Halka Arz Süreci</div>
    <div class="step-title">{current['title']}</div>
    <p><span class="actor">Bu aşamadaki temel aktör:</span> {current['actor']}</p>
    <p><b>Ne oluyor?</b><br>{current['what']}</p>
    <p><b>Neden önemli?</b><br>{current['why']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# -----------------------------
# Butonlar
# -----------------------------
left, center, right = st.columns([1, 2, 1])

with left:
    if st.button("⬅ Önceki Adım", use_container_width=True):
        if st.session_state.step_index > 0:
            st.session_state.step_index -= 1
            st.rerun()

with right:
    if st.button("Sonraki Adım ➡", use_container_width=True):
        if st.session_state.step_index < len(steps) - 1:
            st.session_state.step_index += 1
            st.rerun()

# -----------------------------
# Süreç özeti
# -----------------------------
st.markdown("### Kısa Süreç Özeti")
st.markdown(
    "Fon ihtiyacı → Halka arz kararı → Aracı kurum → SPK / KAP → Talep toplama → Borsa İstanbul → Takasbank / MKK"
)
