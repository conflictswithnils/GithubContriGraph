# TestGithubContriGraph

Erstellt „Hello World"-Pixel-Art im GitHub-Contributions-Graph durch automatische Commits auf vordefinierten Datum.

---

## Lokal auf dem Mac ausführen

### Voraussetzungen

- Python 3 installiert (`python3 --version`)
- Repo geklont und SSH/HTTPS-Push eingerichtet

### Einmalig: Script ausführbar machen

```bash
chmod +x run_local.sh
```

### Manuell ausführen

```bash
./run_local.sh
```

Das Script zieht zuerst die neuesten Änderungen, führt dann `commit_script.py` aus und pusht neue Commits automatisch.

---

## Automatisch täglich starten (launchd)

1. **Plist anpassen** – öffne `com.pixelart.autocommit.plist` und ersetze alle `CHANGE_ME`-Platzhalter durch deinen macOS-Benutzernamen und den korrekten Repo-Pfad.

2. **In LaunchAgents kopieren:**

   ```bash
   cp com.pixelart.autocommit.plist ~/Library/LaunchAgents/
   ```

3. **Laden und aktivieren:**

   ```bash
   launchctl load ~/Library/LaunchAgents/com.pixelart.autocommit.plist
   ```

   Der Job läuft nun täglich um **12:00 Uhr lokaler Zeit**, solange du angemeldet bist.

4. **Deaktivieren (falls gewünscht):**

   ```bash
   launchctl unload ~/Library/LaunchAgents/com.pixelart.autocommit.plist
   ```

> **Hinweis:** Der Mac muss zu dieser Zeit eingeschaltet und angemeldet sein. Wenn er ausgeschaltet war, führt macOS den Job beim nächsten Login **nicht** nach – für zuverlässige tägliche Ausführung eignet sich alternativ die GitHub-Actions-Variante (`.github/workflows/auto_commit.yml`).

---

## GitHub Actions (Alternative)

Die Datei `.github/workflows/auto_commit.yml` enthält einen Workflow, der das Script täglich auf GitHub-Servern ausführt.