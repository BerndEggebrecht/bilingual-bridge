# BilingualBridge Pro Workspace

**BilingualBridge Pro** ist ein lokal betriebenes, datenschutzfreundliches Echtzeit-Übersetzungs- und Support-Tool, speziell entwickelt für mehrsprachigen Kundenservice (DE ⇄ EN) in Support- und Callcenter-Umgebungen (z. B. mobile.de).

Das System läuft vollständig lokal auf Linux-Systemen, kombiniert hochpräzise Spracherkennung mit lokalem KI-gestützten Sentiment-Monitoring und bietet Beratern eine nahtlose, ablenkungsfreie Arbeitsumgebung.

---

## 🚀 Hauptfeatures

* **🌐 Intelligente Echtzeit-Sprachweiche (DE ⇄ EN):** 
  * Erkennt automatisch, ob Deutsch gesprochen/geschrieben wird (Übersetzung ins Englische für den Kunden) oder Englisch (Übersetzung ins Deutsche für den Agenten).
* **🎙️ Flexible Aufnahme-Modi:**
  * **Manuell (Push-to-Stop):** Präzise Kontrolle über Sprachaufnahmen.
  * **Auto-Modus (Stille-Erkennung):** Erkennt automatisch Sprechpausen und verarbeitet die Audio-Nachricht ohne manuelle Klicks.
* **⚡ Live-Stimmungsanalyse (Sentiment Analysis):**
  * Analysiert jede Kundennachricht im Hintergrund über ein lokales `llama3`-Modell.
  * Visuelles Status-Badge im Header: 🟢 *Ruhig*, 🟡 *Ungeduldig*, 🔴 *Verärgert* (mit Alarm-Puls).
* **🛡️ Strenger Zahlenschutz (Strict Digits):**
  * Verhindert zuverlässig, dass das LLM Zahlen oder Kundennummern ausschreibt. Ziffern und IDs bleiben zu 100% als Zahlen erhalten.
* **⏱️ Intelligente AHT-Stoppuhr (Average Handling Time):**
  * Startet automatisch erst beim ersten Interaktionsschritt (Klick, Text oder Mikrofon) und misst exakt die Bearbeitungszeit.
* **⚡ Quick-Reply-Bibliothek & Live-Suche:**
  * Vorkonfigurierte Support-Standard-Szenarien (Begrüßung, Verifizierung, Passwort-Reset etc.) mit Echtzeit-Suchfilter.
* **💾 Automatisierter Export & Session-Cleanup:**
  * Zusammenführung von Chat-Verlauf und Notizen in einer timestamped `.txt`-Datei. Bei Nutzung des Abschluss-Snippets schließt und speichert das System vollautomatisch.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **Speech-to-Text:** OpenAI Whisper (`base`-Modell)
* **LLM (Translation & Sentiment):** Ollama running `llama3`
* **Text-to-Speech:** `gTTS` (Google TTS) mit Akzent-Steuerung (`tld`)
* **Frontend:** HTML5, CSS3 (Modern Dark Mode UI)
* **Deployment:** Linux `systemd` Service

---

## ⚙️ Installation & Start (Linux / Kali Linux)

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/BerndEggebrecht/bilingual-bridge.git](https://github.com/BerndEggebrecht/bilingual-bridge.git)
   cd bilingual-bridge
