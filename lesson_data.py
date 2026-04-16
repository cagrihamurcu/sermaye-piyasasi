APP_TITLE = "Sermaye Piyasasındaki Aktörler: Türkiye Uygulaması"
APP_SUBTITLE = (
    "Ders notu + uygulama + ölçme-değerlendirme içeren Streamlit tabanlı öğretim aracı"
)

NOTE_OVERVIEW = """
Sermaye piyasası, orta ve uzun vadeli fonların el değiştirdiği, tasarruf sahipleri ile
fon ihtiyacı duyan kurumların karşılaştığı finansal alandır. Bu piyasada hisse senetleri,
tahviller, yatırım fonları, kira sertifikaları ve türev araçlar gibi çok sayıda finansal
ürün işlem görür. Sermaye piyasasının temel işlevi, ekonomide atıl durumda bulunan
tasarrufların üretken yatırımlara yönlendirilmesidir.

Sermaye piyasasının etkin biçimde çalışabilmesi için yalnızca yatırımcı ve şirketlerin
varlığı yeterli değildir. İhraççılar, aracı kurumlar, borsa, takas ve saklama sistemi,
kamuyu aydınlatma altyapısı, portföy yönetim şirketleri ve düzenleyici kurumlar
birlikte çalışır. Bu nedenle sermaye piyasasında “aktörler” konusu, finansal sistemin
işleyişini anlamada merkezi bir öneme sahiptir.

Türkiye örneği, bu aktörlerin gerçek kurumsal karşılıklarını görmek açısından öğretici
bir çerçeve sunar. Öğrenci, böylece yalnızca genel kavramları değil; bu kavramların
Türkiye’de hangi kurumlarla somutlaştığını da öğrenir.
"""

TURKEY_INTRO = """
Türkiye’de sermaye piyasası; düzenleyici kurum, organize piyasa, takas ve merkezi karşı
taraf yapısı, merkezi saklama, kamuyu aydınlatma sistemi, aracı kurumlar, portföy yönetim
şirketleri ve yatırımcılardan oluşan çok katmanlı bir kurumsal yapıya sahiptir.

Bu yapı, bir yandan ihraççıların finansmana erişimini sağlarken diğer yandan yatırımcıların
bilgiye erişimini, işlemlerin güvenle sonuçlanmasını ve piyasa disiplininin korunmasını
amaçlar. Bu nedenle Türkiye’de sermaye piyasasının işleyişi, yalnızca “alış-satış” mantığıyla
değil; kurumlar arası koordinasyon, gözetim ve veri akışı çerçevesinde değerlendirilmelidir.
"""

INSTITUTIONS = [
    {
        "name": "SPK",
        "role_short": "Düzenleme ve denetim",
        "importance_short": "Piyasa güveni ve yatırımcı koruması",
        "role_long": (
            "Sermaye piyasasının hukuki ve kurumsal çerçevesini belirleyen düzenleyici otoritedir."
        ),
        "detail": (
            "SPK; sermaye piyasası kurumlarının faaliyet esaslarını, ihraç süreçlerini, "
            "kamuyu aydınlatma yükümlülüklerini, kurumsal yönetim ilkelerini ve yatırımcı "
            "koruma mekanizmalarını düzenler. Bu nedenle piyasanın hem norm koyucu hem de "
            "gözetleyici merkezidir."
        ),
        "bullets": [
            "Halka arz süreçlerini ve sermaye piyasası faaliyetlerini düzenler.",
            "Yatırımcı korunmasına yönelik ilke ve kurallar geliştirir.",
            "Piyasa bozucu eylemlerle mücadele eder.",
        ],
        "importance_long": (
            "SPK olmadan piyasa kurallarının uygulanması, yatırımcı güveni ve kurumsal disiplin "
            "zayıflar; bu da piyasa derinliği ve sürdürülebilirliği olumsuz etkiler."
        ),
    },
    {
        "name": "Borsa İstanbul",
        "role_short": "Organize piyasa işletimi",
        "importance_short": "Şeffaf fiyat oluşumu",
        "role_long": (
            "Pay, borçlanma araçları, türev ürünler ve kıymetli madenler gibi piyasalarda "
            "işlem altyapısı sunar."
        ),
        "detail": (
            "Borsa İstanbul, alıcı ve satıcıyı organize bir piyasa yapısı içinde buluşturur. "
            "Bu işlev yalnızca emir eşleştirmeyi değil, fiyat oluşumu, piyasa verisi üretimi "
            "ve düzenli işlem ortamı sağlamayı da kapsar."
        ),
        "bullets": [
            "Pay Piyasası, Borçlanma Araçları Piyasası ve VİOP gibi ana piyasa segmentlerini içerir.",
            "Fiyatların görünür ve karşılaştırılabilir biçimde oluşmasını sağlar.",
            "Likidite ve piyasa derinliği açısından merkezi rol oynar.",
        ],
        "importance_long": (
            "Borsa, sermaye piyasasının görünür yüzüdür; ancak asıl önemi, güvenilir ve kurallı "
            "işlem yapısını mümkün kılmasında ortaya çıkar."
        ),
    },
    {
        "name": "Takasbank",
        "role_short": "Takas ve merkezi karşı taraf",
        "importance_short": "İşlem güvenliği ve karşı taraf riskinin azaltılması",
        "role_long": (
            "İşlem sonrası takas, teminat ve merkezi karşı taraf süreçlerini yürüten temel piyasa altyapısıdır."
        ),
        "detail": (
            "Takasbank, işlemlerin sonuçlanmasını sağlamakla kalmaz; belirli piyasalarda "
            "merkezi karşı taraf olarak alıcıya karşı satıcı, satıcıya karşı alıcı konumuna "
            "geçerek sistemik riskin azaltılmasına katkı verir."
        ),
        "bullets": [
            "Takas sürecini yürütür.",
            "Teminat ve garanti fonu mantığıyla risk yönetimi sağlar.",
            "Fon ve pazar altyapılarına da teknik destek sunar.",
        ],
        "importance_long": (
            "Özellikle yoğun işlem ve türev ürün piyasalarında, işlem güvenliğinin ve "
            "piyasa istikrarının korunması bakımından kritik öneme sahiptir."
        ),
    },
    {
        "name": "MKK",
        "role_short": "Merkezi saklama ve kayıt sistemi",
        "importance_short": "Mülkiyet ve yatırımcı bazında izleme",
        "role_long": (
            "Sermaye piyasası araçlarının kaydi sistemde tutulmasını ve yatırımcı bazında izlenmesini sağlar."
        ),
        "detail": (
            "MKK, kıymetlerin fiziki teslim yerine elektronik kayıt düzeninde izlenmesini "
            "mümkün kılar. Böylece paylar, fonlar, borçlanma araçları ve çeşitli sermaye "
            "piyasası ürünleri yatırımcı bazında güvenli biçimde kayıt altında tutulur."
        ),
        "bullets": [
            "Kaydi sistemin merkezidir.",
            "Yatırımcı bazında kayıt düzeni sağlar.",
            "Şeffaflık ve izlenebilirlik kapasitesini güçlendirir.",
        ],
        "importance_long": (
            "Merkezi kayıt sistemi, modern sermaye piyasasında güvenli mülkiyet takibi ve "
            "operasyonel doğruluk açısından vazgeçilmezdir."
        ),
    },
    {
        "name": "KAP",
        "role_short": "Kamuyu aydınlatma ve elektronik bildirim",
        "importance_short": "Eş zamanlı bilgi erişimi",
        "role_long": (
            "Şirketlerin ve sermaye piyasası kurumlarının kamuya açıklamak zorunda olduğu bilgileri yayımlayan sistemdir."
        ),
        "detail": (
            "KAP üzerinden finansal tablolar, özel durum açıklamaları, yönetim kurulu kararları, "
            "sermaye artırımları ve benzeri duyurular tüm yatırımcılara iletilir. Bu mekanizma, "
            "bilginin merkezî ve izlenebilir şekilde dolaşıma girmesini sağlar."
        ),
        "bullets": [
            "Kamuyu aydınlatma sisteminin ana platformudur.",
            "Bilgi asimetrisinin azaltılmasına katkı sunar.",
            "Geçmişe dönük erişim ve arşivleme imkânı sağlar.",
        ],
        "importance_long": (
            "Sermaye piyasalarında fiyatlama davranışının kalitesi, büyük ölçüde doğru ve zamanında "
            "açıklanan bilgiye bağlıdır."
        ),
    },
    {
        "name": "Aracı Kurumlar",
        "role_short": "Yatırımcı ile piyasa arasında aracılık",
        "importance_short": "Piyasaya erişim ve hizmet sunumu",
        "role_long": (
            "Emir iletimi, alım-satım aracılığı, halka arz aracılığı ve yatırım danışmanlığı gibi hizmetler sunar."
        ),
        "detail": (
            "Aracı kurumlar, sermaye piyasasında yatırımcının ilk temas noktalarından biridir. "
            "Hem teknik işlem altyapısı hem de araştırma, raporlama ve danışmanlık boyutuyla "
            "yatırımcı davranışını etkileyebilir."
        ),
        "bullets": [
            "Emir iletimini ve aracılık faaliyetini yürütür.",
            "Halka arzlarda aktif görev alabilir.",
            "Araştırma ve danışmanlık hizmetleri verebilir.",
        ],
        "importance_long": (
            "Aracı kurumlar olmadan piyasanın tabana yayılması ve yatırımcının düzenli erişimi "
            "çok daha güç hale gelir."
        ),
    },
    {
        "name": "Portföy Yönetim Şirketleri",
        "role_short": "Profesyonel fon yönetimi",
        "importance_short": "Tasarrufların uzman yönetimi",
        "role_long": (
            "Yatırım fonları, emeklilik fonları ve bireysel/kurumsal portföylerin profesyonelce yönetilmesini sağlar."
        ),
        "detail": (
            "Portföy yönetim şirketleri, yatırım kararlarını profesyonel analiz çerçevesinde alır. "
            "Bu yapı, yatırımcının tek tek menkul kıymet seçmek yerine uzman yönetimden "
            "yararlanmasını mümkün kılar."
        ),
        "bullets": [
            "Kolektif yatırım araçlarının gelişimini destekler.",
            "Risk-getiri dengesi çerçevesinde varlık dağılımı yapar.",
            "Kurumsal yatırımcı tabanını güçlendirir.",
        ],
        "importance_long": (
            "Kurumsal fon yönetimi, sermaye piyasasının derinliğini ve profesyonelleşme düzeyini artırır."
        ),
    },
    {
        "name": "TSPB",
        "role_short": "Meslek örgütü ve sektör temsili",
        "importance_short": "Mesleki standartlar ve sektör koordinasyonu",
        "role_long": (
            "Sermaye piyasası kurumlarını temsil eden ve mesleki gelişime katkı sunan kamu kurumu niteliğinde bir meslek kuruluşudur."
        ),
        "detail": (
            "TSPB, sektörün temsilini, mesleki standartların gelişimini, etik ilkelerin "
            "yaygınlaşmasını ve sermaye piyasası kültürünün güçlenmesini destekler."
        ),
        "bullets": [
            "Sektörel temsil sağlar.",
            "Mesleki eğitim ve farkındalık çalışmalarına katkı sunar.",
            "Etik ve kurumsal standartların gelişimini destekler.",
        ],
        "importance_long": (
            "Piyasa yalnızca mevzuatla değil, aynı zamanda mesleki kültür ve sektör disipliniyle de güçlenir."
        ),
    },
]

FLOW_STEPS = [
    {
        "step_no": 1,
        "title": "Tasarruf Sahibi / Yatırımcı",
        "description": (
            "Fonunu değerlendirmek isteyen kişi veya kurum, sermaye piyasasına yönelir."
        ),
    },
    {
        "step_no": 2,
        "title": "Aracı Kurum",
        "description": (
            "Yatırımcı hesabı üzerinden emir alınır ve ilgili piyasaya iletilir."
        ),
    },
    {
        "step_no": 3,
        "title": "Borsa İstanbul",
        "description": (
            "Emirler organize piyasada eşleşir ve fiyat oluşumu gerçekleşir."
        ),
    },
    {
        "step_no": 4,
        "title": "Takasbank",
        "description": (
            "İşlem sonrası takas, teminat ve merkezi karşı taraf süreçleri yürütülür."
        ),
    },
    {
        "step_no": 5,
        "title": "MKK / KAP",
        "description": (
            "Kıymetin kaydi takibi yapılır; gerekli kamuyu aydınlatma bilgileri sistemde görünür olur."
        ),
    },
    {
        "step_no": 6,
        "title": "İhraççı / Diğer Yatırımcılar",
        "description": (
            "Fon aktarımı tamamlanır ve sermaye piyasası işleyişi ekonomik amaçla sonuçlanır."
        ),
    },
]

INFO_FLOW_STEPS = [
    {
        "title": "1. Şirket Açıklaması",
        "text": (
            "Şirket, finansal tablolarını, özel durum açıklamalarını veya diğer önemli "
            "kararlarını kamuya açıklamak üzere hazırlar."
        ),
    },
    {
        "title": "2. Denetim ve Doğrulama",
        "text": (
            "Açıklanan finansal verilerin güvenilirliği bağımsız denetim ve düzenleyici "
            "çerçeve ile desteklenir."
        ),
    },
    {
        "title": "3. KAP Üzerinden Yayın",
        "text": (
            "Bilgiler KAP üzerinden tüm piyasa katılımcılarına görünür hale gelir."
        ),
    },
    {
        "title": "4. Analiz ve Yorum",
        "text": (
            "Analistler, portföy yöneticileri ve yatırımcılar açıklanan bilgileri "
            "yorumlayarak beklenti oluşturur."
        ),
    },
    {
        "title": "5. Yatırım Kararı ve Fiyatlama",
        "text": (
            "Bilgi akışı, alım-satım kararlarını etkiler; bu da piyasa fiyatlarına yansır."
        ),
    },
]

ETHICS_TOPICS = [
    {
        "title": "Bilgi Asimetrisi",
        "text": (
            "Piyasadaki bazı aktörlerin diğerlerine göre daha fazla veya daha nitelikli bilgiye "
            "sahip olması, karar alma sürecinde eşitsizlik yaratır. Bu durum yatırımcı koruması "
            "ve piyasa etkinliği bakımından önemli bir sorundur."
        ),
    },
    {
        "title": "Manipülasyon",
        "text": (
            "Fiyatları veya yatırımcı algısını yapay yollarla etkilemeye yönelik işlemler ve "
            "davranışlar manipülasyon olarak değerlendirilir. Bu tür eylemler piyasanın doğal "
            "işleyişini bozar."
        ),
    },
    {
        "title": "İçeriden Öğrenenlerin Ticareti",
        "text": (
            "Henüz kamuya açıklanmamış bilgilerin kullanılmasıyla işlem yapılması, diğer "
            "yatırımcılar açısından adaletsizlik yaratır ve piyasaya olan güveni zedeler."
        ),
    },
    {
        "title": "Çıkar Çatışmaları",
        "text": (
            "Araştırma, danışmanlık veya satış süreçlerinde tarafların aynı anda birden fazla "
            "menfaati temsil etmesi, yatırımcının yanlış yönlendirilmesine yol açabilir."
        ),
    },
    {
        "title": "Yanlış Yönlendirme ve Etik Dışı Sunum",
        "text": (
            "Risklerin açık biçimde belirtilmemesi, aşırı iyimser sunumlar veya eksik bilgi "
            "verilmesi, yatırımcı kararlarının sağlıklı oluşmasını engelleyebilir."
        ),
    },
]

MATCHING_EXERCISE = {
    "SPK": "Piyasanın düzenlenmesi ve yatırımcı korunması",
    "Borsa İstanbul": "Organize piyasada fiyat oluşumu ve işlem altyapısı",
    "Takasbank": "Takas, teminat ve merkezi karşı taraf hizmeti",
    "MKK": "Kaydi sistemde mülkiyet ve yatırımcı bazında kayıt",
    "KAP": "Kamuyu aydınlatma ve elektronik bildirim",
    "Aracı Kurum": "Yatırımcı ile piyasa arasında emir ve hizmet aracılığı",
    "Portföy Yönetim Şirketi": "Fonların ve portföylerin profesyonel yönetimi",
    "TSPB": "Mesleki temsil ve sektörel koordinasyon",
}

QUIZ_QUESTIONS = [
    {
        "question": "Türkiye’de sermaye piyasasının temel düzenleyici otoritesi hangisidir?",
        "options": ["Borsa İstanbul", "SPK", "MKK", "TSPB"],
        "correct": "SPK",
        "explanation": (
            "SPK, sermaye piyasasının düzenlenmesi, denetlenmesi ve yatırımcı korunması açısından "
            "merkezî otoritedir."
        ),
    },
    {
        "question": "Aşağıdakilerden hangisi işlem sonrası takas ve merkezi karşı taraf işleviyle öne çıkar?",
        "options": ["KAP", "TSPB", "Takasbank", "Portföy Yönetim Şirketi"],
        "correct": "Takasbank",
        "explanation": (
            "Takasbank, işlem sonrası altyapıda takas ve belirli piyasalarda merkezi karşı taraf "
            "hizmeti sunar."
        ),
    },
    {
        "question": "Kamuyu aydınlatma açısından en kritik elektronik platform hangisidir?",
        "options": ["MKK", "KAP", "VİOP", "TEFAS"],
        "correct": "KAP",
        "explanation": (
            "KAP, kamuya açıklanması gereken bildirimlerin yayımlandığı elektronik sistemdir."
        ),
    },
    {
        "question": "Aracı kurumların temel işlevi aşağıdakilerden hangisidir?",
        "options": [
            "Yalnızca vergi denetimi yapmak",
            "Merkezi kayıt tutmak",
            "Yatırımcı ile piyasa arasında aracılık etmek",
            "Devlet tahvili ihraç etmek",
        ],
        "correct": "Yatırımcı ile piyasa arasında aracılık etmek",
        "explanation": (
            "Aracı kurumlar, emir iletimi ve yatırım hizmetleri bakımından yatırımcının piyasaya "
            "erişiminde temel rol oynar."
        ),
    },
    {
        "question": "Aşağıdakilerden hangisi bilgi akışının fiyatları etkilediğini en iyi açıklar?",
        "options": [
            "Bilgi yalnızca geçmişi anlatır.",
            "Şirket açıklamaları yatırımcı beklentilerini değiştirir.",
            "Fiyatlar sadece rastgele hareket eder.",
            "Kamuyu aydınlatma fiyatlarla ilişkili değildir.",
        ],
        "correct": "Şirket açıklamaları yatırımcı beklentilerini değiştirir.",
        "explanation": (
            "Yatırımcılar kamuya açıklanan bilgileri yorumlar ve buna göre alım-satım kararı verir; "
            "bu da fiyatlara yansır."
        ),
    },
]

IPO_CASE = {
    "scenario": """
Bir üretim şirketi, yeni bir fabrika yatırımı yapmak için uzun vadeli finansmana ihtiyaç
duymaktadır. Şirket, banka kredisine alternatif olarak halka arz yoluyla fon toplamayı
değerlendirmektedir. Süreçte aracı kurumla çalışılması, gerekli açıklamaların yapılması,
yatırımcıların talep toplama sürecine katılması ve payların borsada işlem görmesi
planlanmaktadır.
""",
    "questions": [
        "Şirket neden halka arz yolunu tercih ediyor olabilir?",
        "Aracı kurum bu süreçte hangi görevleri üstlenir?",
        "Yatırımcı açısından hangi bilgiler kritik önemdedir?",
        "Borsa, Takasbank, MKK ve KAP bu süreçte nerede devreye girer?",
        "Sürecin başarısı neden yalnızca şirketin kararına bağlı değildir?",
    ],
    "model_answer": [
        "Şirket halka arzla uzun vadeli kaynak sağlayabilir, ortaklık tabanını genişletebilir ve kurumsallaşma sürecini güçlendirebilir.",
        "Aracı kurum fiyatlama, satış organizasyonu, yatırımcıya sunum ve teknik süreç yönetiminde rol alır.",
        "Yatırımcı şirketin finansalları, büyüme potansiyeli, sektör görünümü ve kamuya açıklanan belgeleri değerlendirir.",
        "Borsa İstanbul işlem görecek organize piyasayı sağlar; Takasbank işlem sonrası takası yürütür; MKK kıymetin kaydi takibini sağlar; KAP bilgi akışının merkezidir.",
        "Süreç; şirket, aracı kurum, düzenleyici yapı, yatırımcı, piyasa altyapısı ve bilgi akışının birlikte işlemesine bağlıdır.",
    ],
}

GLOSSARY = {
    "İhraççı": "Sermaye piyasasından fon sağlamak amacıyla menkul kıymet ihraç eden şirket veya kurum.",
    "Yatırımcı": "Tasarrufunu sermaye piyasası araçlarında değerlendiren gerçek veya tüzel kişi.",
    "Kamuyu Aydınlatma": "Yatırımcıların karar verebilmesi için gerekli bilgilerin zamanında ve eşit biçimde kamuya açıklanması.",
    "Kaydi Sistem": "Menkul kıymetlerin fiziki belge yerine elektronik kayıt düzeni içinde izlenmesi.",
    "Merkezi Karşı Taraf": "Alıcıya karşı satıcı, satıcıya karşı alıcı olarak işlemin gerçekleşmesini güvenceleyen altyapı mantığı.",
    "Likidite": "Bir finansal varlığın değer kaybı yaşamadan hızlıca nakde çevrilebilme kapasitesi.",
    "Manipülasyon": "Fiyatları veya yatırımcı davranışını yapay biçimde etkileyen işlem ve eylemler.",
}
