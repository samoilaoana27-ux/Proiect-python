# 🧮 Matematică Viteză (Math Speed Quiz)

Un joc interactiv de matematică mentală scris în **Python**, care rulează direct în consolă. Testează viteza de calcul și precizia sub presiune!

## 🌟 Funcționalități Principale

* **🔢 Generare Procedurală:** Întrebările sunt create pe loc (nu sunt predefinite), asigurând că jocul este diferit de fiecare dată.
* **📈 Dificultate Progresivă:** Jocul devine mai greu pe măsură ce avansezi:
  * *Nivel Ușor:* Calcule simple (5-30).
  * *Nivel Mediu:* Numere până la 100.
  * *Nivel Greu:* Calcule complexe (sute, operații multiple).
* **⏳ Cronometru:** Ai la dispoziție **45 de secunde** per întrebare. Timpul se scurge!
* **🧠 Algoritm de "Capcane":** Răspunsurile greșite sunt generate inteligent (valori apropiate de rezultatul corect) pentru a descuraja ghicitul.
* **🏆 Leaderboard (Clasament):** Scorurile sunt salvate automat într-un fișier local (`clasament.txt`) pentru a păstra evidența celor mai buni jucători.

## 🚀 Cum să rulezi jocul

### Cerințe
* Ai nevoie doar de **Python 3.x** instalat.
* Nu sunt necesare biblioteci externe (folosește doar librăriile standard: `time`, `random`, `os`).

### Instalare și Rulare

1. Descarcă sau clonează acest repository.
2. Deschide un terminal (CMD/PowerShell) în folderul proiectului.
3. Rulează comanda:

```bash
python main.py

