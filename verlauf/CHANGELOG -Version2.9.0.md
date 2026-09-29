Entwicklungs-Changelog deines **BilingualBridge Pro Workspace** für das mobile.de-Support-Projekt:

# **📜 CHANGELOG: BilingualBridge Pro Workspace**

### **Version 2.9.0 — Live Sentiment Edition (Aktueller Stand)**

* **Feature:** Integrierte Live-Stimmungsanalyse (Sentiment Analysis) über das lokale llama3-Modell.  
* **Funktionsweise:** Analysiert sowohl Text- als auch Audio-Transkripte im Hintergrund und klassifiziert den Tonfall des Kunden in Echtzeit.  
* **UI:** Visuelles Status-Badge im Header (🟢 Ruhig, 🟡 Ungeduldig, 🔴 Verärgert mit Puls-Effekt).  
* **Export:** Die ermittelte Kundenstimmung wird automatisch in den Kopfbereich des .txt-Protokolls übernommen.

### **Version 2.8.1 — Strict Digits Edition**

* **Fix & Optimierung:** Verschärfung des System-Prompts zur absoluten Wahrung von Ziffern, IDs und Kundennummern (z. B. 12345). Das Modell wurde angewiesen, Zahlen niemals textlich auszuschreiben, um Übertragungsfehler bei Support-Daten zu verhindern.

### **Version 2.8.0 — Smart Automation & AHT Pro**

* **Feature:** Automatisierter Gesprächsabschluss. Wenn das Snippet *"8. Gesprächsabschluss"* gewählt wird, spielt das System die Abschlussnachricht ab und führt **nach Ende der Sprachausgabe vollautomatisch** den Export, das Leeren des Workspaces und das Zurückschalten der AHT-Uhr aus.  
* **AHT (Average Handling Time):** Die Stoppuhr startet nun intelligent erst beim ersten Interaktionsschritt (Klick auf Quick Reply, Text absenden oder Mikrofon aktivieren) und misst nicht mehr im Vorfeld die Leerlaufzeit.

### **Version 2.7.0 — Snippet Library & Search**

* **Feature:** Erweiterte, durchsuchbare Quick-Reply-Bibliothek mit 8 praxisnahen Standard-Szenarien für den mobile.de-Support (Begrüßung, Verifizierung, Passwort-Reset, Inserats-Freigabe, Zahlungsstatus etc.).  
* **UI:** Integriertes Live-Suchfeld über den Snippet-Buttons zum schnellen Filtern während des Gesprächs.

### **Version 2.6.0 — Custom Agent Alias**

* **Feature:** Dynamisches Agenten-Profil in der rechten Sidebar.  
* **Funktionsweise:** Der eingetragene Berater-Name (Alias, z. B. *"Benno Engler"*) wird vollautomatisch in den Chat, in die Protokolle, in die Export-Dateinamen sowie in die Begrüßungs-Snippets übernommen.

### **Version 2.5.0 — Smart Text Direction (DE ⇄ EN)**

* **Feature:** Intelligente Sprachweiche für die Texteingabe. Das System erkennt am Inhalt, ob du schreibst (Deutsch \$\\rightarrow\$ Übersetzung ins Englische für den Kunden) oder ob eine Kundenantwort vorliegt (Englisch \$\\rightarrow\$ Übersetzung ins Deutsche für dich).

### **Version 2.4.0 — Pro Workspace Layout (2-Spalten)**

* **Feature:** Umstellung auf ein modernes Zwei-Spalten-Layout (Links: BilingualBridge Chat, Rechts: Agenten-Config & Notizenfeld).  
* **Notizen:** Formloses Mitschreiben während des Telefonats. Beim Klick auf den Export-Button werden Chat und Notizen in einer einzigen timestamped .txt-Datei im Ordner /opt/bilingual-bridge/verlauf zusammengeführt.

### **Version 2.0.0 bis 2.3.0 — Core Architecture**

* **Backend:** Aufsatz auf FastAPI unter Python mit Whisper (base-Modell) für hochpräzise lokale Spracherkennung und Übersetzung via lokalem Ollama (llama3).  
* **Audio:** Anbindung von gTTS (Google Text-to-Speech) mit Akzent-Steuerung (tld) für eine natürliche, flüssige Sprachausgabe.  
* **Deployment:** Konfiguration als stabiler Linux-Hintergrunddienst (systemd) unter /opt/bilingual-bridge auf Kali Linux.