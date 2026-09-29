# **CHANGELOG: BilingualBridge (mobile.de Edition)**

### **Version 2.2.0 – Auto Smart Edition (Aktuelle Version)**

* **Automatische Spracherkennung (Auto-Detect):** Entfernung der manuellen Richtungs-Buttons (DE ➔ EN / EN ➔ DE). Whisper erkennt die gesprochene Sprache nun vollendet selbstständig, und das System antwortet dynamisch in der jeweils anderen Sprache.  
* **Audio-Geschwindigkeits-Schalter:** Integration einer Checkbox für eine verlangsamte Audio-Ausgabe (slow=True in gTTS) – ideal zum Mitschreiben von Zahlen und E-Mail-Adressen.  
* **Hardware- & Puffer-Sicherheit:** Perfektes Zurücksetzen und Leeren der Audio-Puffer sowie ein hartes Stoppen des Mikrofon-Streams (mediaStream.getTracks().forEach(track \=\> track.stop())), um "Geister-Aufnahmen" und dauerhafte Aufnahme-Indikatoren im Browser-Reiter komplett auszuschließen.

### **Version 2.1.0 – Pro Edition & Formatierung**

* **Strikte Prompt-Regeln:** Optimierung der Ollama-System-Prompts, um die Generierung von Anführungszeichen (") im Antworttext zu unterbinden (verhindert hängende Quotes).  
* **Ziffern-Ausprache:** Zwangsanweisung für das Sprachmodell, Konto-, Kunden- und Telefonnummern klar ziffernbasiert oder getrennt auszugeben, damit gTTS sie verständlich vorliest (statt als lange, unleserliche Zahlwörter).

### **Version 2.0.0 – Server-Logged Edition**

* **Automatisches Audit-Trail-Logging:** Jede eingehende und ausgehende Nachricht wird in Echtzeit im Server-Verzeichnis unter /opt/bilingual-bridge/verlauf/session\_YYYY-MM-DD.txt mit Zeitstempel und Session-ID persistent festgehalten.  
* **Quick Replies (Standard-Antworten):** Integration einer Klick-Leiste im Frontend mit den 4 wichtigsten mobile.de-Standards (Begrüßung, Verifizierung via ID/Mail, Adressabgleich und technische Nutzung).

### **Version 1.8.0 bis 1.9.0 – UI & UX Redesign**

* **Visuelle Unterscheidung:** Farbliche und positionelle Trennung im Chatfenster (Betreuer-Nachrichten rechts in Blau, Kunden-Nachrichten/Übersetzungen links in Dunkelgrau/Türkis).  
* **Export- & Auto-Reset-Funktion:** Button zum Herunterladen des Browser-Verlaufs als .txt-Datei mit anschließendem automatischen Zurücksetzen (Schließen) des Chats für den nächsten Kunden.  
* **VAD (Stille-Erkennung):** Implementierung der automatischen Aufnahme-Beendigung bei Gesprächspausen über die Web-Audio-API.

### **Version 1.0.0 bis 1.7.0 – Grundstein & Architektur**

* **Setup auf Kali Linux:** Lokale Installation im Verzeichnis /opt/bilingual-bridge mit aktivierter Python-Virtual-Environment (venv) und dauerhafter Einbindung als systemd-Hintergrunddienst (bilingual-bridge.service).  
* **Tech-Stack Integration:** Anbindung von FastAPI (Port 8000), Ollama (Port 11434 mit llama3), OpenAI-Whisper (base) für die Transkription und gTTS für die Server-seitige MP3-Erstellung und \-Wiedergabe.

