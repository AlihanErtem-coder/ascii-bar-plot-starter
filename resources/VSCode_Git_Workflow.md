# VS Code Git/GitHub Cheat Sheet für die Praktika

Ab dieser Session arbeiten wir primär über die **Source-Control-Oberfläche von VS Code**. Die Git-Befehle bleiben wichtig zum Verständnis und zur Diagnose, aber normale Commits müssen nicht mehr jedes Mal über das Terminal ausgeführt werden.

## Repository klonen

1. `Ctrl/Cmd+Shift+P`
2. **Git: Clone**
3. Repository-URL einfügen
4. lokalen Zielordner auswählen
5. **Open Repository**

Terminal-Alternative: `git clone <URL>`

## Branch erstellen

1. unten links auf den aktuellen Branchnamen klicken
2. **Create new branch...**
3. Namen eingeben, z. B. `feature/bar-chart`

Alternativ Command Palette → **Git: Create Branch**.

Terminal-Alternative: `git switch -c feature/bar-chart`

## Änderungen ansehen

Links auf **Source Control** oder `Ctrl/Cmd+Shift+G`.

Unter **Changes** zeigt VS Code geänderte/neue Dateien. Eine Datei anklicken, um den Diff zu sehen.

Terminal-Alternative: `git status` und `git diff`

## Stage

- `+` neben einer einzelnen Datei → nur diese Datei stagen
- `+` neben **Changes** → alle Änderungen stagen

Terminal-Alternative: `git add <datei>` bzw. `git add .`

## Commit

1. staged Änderungen kontrollieren
2. oben Commit Message eingeben
3. **Commit** klicken

Terminal-Alternative: `git commit -m "Describe the change"`

## Branch zum ersten Mal pushen

Nach dem ersten Commit zeigt VS Code meist **Publish Branch**. Darauf klicken.

Terminal-Alternative: `git push -u origin <branch-name>`

Später reicht **Push** oder **Sync Changes**.

## Änderungen vom Remote holen

Source Control → `...` → **Pull**.

Oft kann auch **Sync Changes** verwendet werden; VS Code holt dann Remote-Änderungen und pusht anschließend lokale Commits.

Terminal-Alternative: `git pull`

## Branch wechseln

Unten links auf den Branchnamen klicken und vorhandenen Branch auswählen.

Terminal-Alternative: `git switch main`

## Pull Request

Für dieses Praktikum nutzen wir primär GitHub im Browser:

1. Branch pushen
2. GitHub-Repository öffnen
3. **Compare & pull request**
4. Zielbranch `main` kontrollieren
5. PR erstellen
6. Partner:in reviewed
7. Merge

Optional kann später die VS-Code-Extension **GitHub Pull Requests and Issues** verwendet werden.

## Nach einem Merge

Ein Merge auf GitHub verändert euren lokalen Clone nicht automatisch.

1. lokal auf `main` wechseln
2. **Pull** / **Sync Changes**
3. erst danach den nächsten Branch starten

## Merge Conflict in VS Code

1. Source Control zeigt **Merge Changes**.
2. Konfliktdatei öffnen.
3. Merge Editor bzw. Current / Incoming / Both bewusst verwenden.
4. Datei speichern und stagen.
5. Merge-Commit erstellen.

Terminal-Kontrolle: `git status`

## Wichtigste Routine

```text
Branch erstellen
    ↓
Dateien bearbeiten
    ↓
Diff ansehen
    ↓
Stage
    ↓
Commit
    ↓
Push / Publish Branch
    ↓
Pull Request + Review
    ↓
Merge
    ↓
main lokal aktualisieren (Pull)
```
