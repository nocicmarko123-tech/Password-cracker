# 🔐 Analiza Složenosti i Ukupnog Broja Kombinacija Šifara (1 – 20 Karaktera)

Tabela prikazuje ukupan broj mogućih kombinacija izračunat po formuli $C = L^N$, gde je **$N$** dužina šifre, a **$L$** veličina skupa karaktera.

| Dužina ($N$) | Samo Mala Slova(26 karaktera)* | Mala + Velika Slova(52 karaktera) | Slova + Brojevi<br>*(62 karaktera)* | Svi Znakovi (Full ASCII)<br>*(95 karaktera)* | Nivo Sigurnosti |
| :---: | ---: | ---: | ---: | ---: | :---: |
| **1** | 26 | 52 | 62 | **95** | 🚨 Instant |
| **2** | 676 | 2,704 | 3,844 | **9,025** | 🚨 Instant |
| **3** | 17.5 K | 140.6 K | 238.3 K | **857.3 K** | 🚨 Instant |
| **4** | 456.9 K | 7.3 M | 14.7 M | **81.4 M** | 🚨 Instant |
| **5** | 11.8 M | 380.2 M | 916.1 M | **7.7 B** | 🚨 Instant |
| **6** | 308.9 M | 19.7 B | 56.8 B | **735.0 B** | ⚠️ Slabo |
| **7** | 8.0 B | 1.0 T | 3.5 T | **69.8 T** | ⚠️ Slabo |
| **8** | 208.8 B | 53.4 T | 218.3 T | **6.6 Quad** | 🟡 Prosečno |
| **9** | 5.4 T | 2.7 Quad | 13.5 Quad | **630.2 Quad** | 🟡 Prosečno |
| **10** | 141.1 T | 144.5 Quad | 839.2 Quad | **59.8 Quint** | 🟢 Jako |
| **11** | 3.6 Quad | 7.5 Quint | 52.0 Quint | **5.6 Sext** | 🟢 Jako |
| **12** | 95.4 Quad | 390.8 Quint | 3.2 Sext | **540.3 Sext** | 🟢 Jako |
| **13** | 2.4 Quint | 20.3 Sext | 200.0 Sext | **51.3 Sept** | 🟢 Veoma Jako |
| **14** | 64.5 Quint | 1.0 Sept | 12.4 Sept | **4.8 Oct** | 🟢 Veoma Jako |
| **15** | 1.6 Sext | 55.0 Sept | 768.8 Sept | **463.2 Oct** | 🟢 Veoma Jako |
| **16** | 43.6 Sext | 2.8 Oct | 47.6 Oct | **44.0 Non** | 🟣 Neprobojno |
| **17** | 1.1 Sept | 149.0 Oct | 2.9 Non | **4.1 Dec** | 🟣 Neprobojno |
| **18** | 29.5 Sept | 7.7 Non | 183.0 Non | **397.0 Dec** | 🟣 Neprobojno |
| **19** | 769.1 Sept | 403.0 Non | 11.3 Dec | **37.7 Undec** | 🟣 Neprobojno |
| **20** | 20.0 Oct | 20.9 Dec | 704.8 Dec | **3.58 × 10³⁹** | 🟣 Neprobojno |

---

### 📊 Objašnjenje Skraćenica Brojeva

| Skraćenica | Naziv (Sistem) | Vrednost u Matematičkom Obliku |
| :--- | :--- | :--- |
| **K** | Hiljada (Thousand) | $10^3 = 1.000$ |
| **M** | Milion (Million) | $10^6 = 1.000.000$ |
| **B** | Milijarda (Billion) | $10^9 = 1.000.000.000$ |
| **T** | Bilion (Trillion) | $10^{12}$ |
| **Quad** | Bilijarda (Quadrillion) | $10^{15}$ |
| **Quint** | Trilion (Quintillion) | $10^{18}$ |
| **Sext** | Trilijarda (Sextillion) | $10^{21}$ |
| **Sept** | Kvadrilion (Septillion) | $10^{24}$ |
| **Oct** | Kvadrilijarda (Octillion) | $10^{27}$ |
| **Non** | Kvintilion (Nonillion) | $10^{30}$ |
| **Dec** | Kvintilijarda (Decillion) | $10^{33}$ |
| **Undec** | Sestilion (Undecillion) | $10^{36}$ |
