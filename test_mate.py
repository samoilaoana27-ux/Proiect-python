import time
import random
import os

TIMP_LIMITA = 45 
NUMAR_INTREBARI = 6
FISIER_SCOR = "clasament.txt"

def genereaza_intrebare(nivel):
    operatie = random.choice(['+', '-', '*'])
    
    if nivel == 1:
        if operatie == '+':
            a = random.randint(5, 30)
            b = random.randint(5, 30)
            corect = a + b
            text = f"{a} + {b} = ?"
        elif operatie == '-':
            a = random.randint(10, 30)
            b = random.randint(1, a)
            corect = a - b
            text = f"{a} - {b} = ?"
        else: 
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            corect = a * b
            text = f"{a} x {b} = ?"
            
    elif nivel == 2:
        if operatie == '+':
            a = random.randint(30, 100)
            b = random.randint(30, 100)
            corect = a + b
            text = f"{a} + {b} = ?"
        elif operatie == '-':
            a = random.randint(50, 100)
            b = random.randint(10, a)
            corect = a - b
            text = f"{a} - {b} = ?"
        else: 
            a = random.randint(6, 10)
            b = random.randint(6, 10)
            corect = a * b
            text = f"{a} x {b} = ?"

    else:
        if operatie == '+':
            a = random.randint(100, 500)
            b = random.randint(100, 500)
            corect = a + b
            text = f"{a} + {b} = ?"
        elif operatie == '-':
            a = random.randint(200, 600)
            b = random.randint(50, a)
            corect = a - b
            text = f"{a} - {b} = ?"
        else: 
            a = random.randint(11, 20)
            b = random.randint(2, 9)
            corect = a * b
            text = f"{a} x {b} = ?"

    optiuni = {corect} 
    while len(optiuni) < 4:
        gresit = corect + random.randint(-10 - nivel, 10 + nivel)
        if gresit > 0:
            optiuni.add(gresit)
            
    lista_optiuni = list(optiuni)
    random.shuffle(lista_optiuni)
    
    litere = ['a', 'b', 'c', 'd']
    dictionar_optiuni = {}
    lit_bun = ""
    
    for i in range(4):
        litera = litere[i]
        valoare = lista_optiuni[i]
        dictionar_optiuni[litera] = valoare
        if valoare == corect:
            lit_bun = litera
            
    return text, dictionar_optiuni, lit_bun

def salveaza_scor(nume, puncte):
    with open(FISIER_SCOR, "a") as f:
        f.write(f"{nume},{puncte}\n")

def arata_top():
    if not os.path.exists(FISIER_SCOR):
        print("\nÎncă nu există niciun scor salvat.")
        return

    print("\n=== 🏆 CLASAMENT (Top Jucători) ===")
    scoruri = []
    
    with open(FISIER_SCOR, "r") as f:
        for linie in f:
            parts = linie.strip().split(",")
            if len(parts) == 2:
                nume = parts[0]
                pct = int(parts[1])
                scoruri.append((nume, pct))
    
    scoruri.sort(key=lambda x: x[1], reverse=True)
    
    for i, (n, p) in enumerate(scoruri[:5], 1):
        print(f"{i}. {n} -> {p} puncte")
    print("====================================")

def start_joc():
    score = 0
    print(f"--- MATEMATICĂ VITEZĂ ---")
    print(f"Ai {TIMP_LIMITA} secunde pentru fiecare răspuns!")
    print("Pregătește-te...")
    time.sleep(2)
    
    for i in range(1, NUMAR_INTREBARI + 1):
        if i <= 2:
            nivel = 1
            print(f"\n[ NIVEL UȘOR ]")
        elif i <= 4:
            nivel = 2
            print(f"\n[ NIVEL MEDIU ]")
        else:
            nivel = 3
            print(f"\n[ NIVEL GREU ]")

        text_intrebare, optiuni, raspuns_corect = genereaza_intrebare(nivel)
        
        print(f"Întrebarea {i}/{NUMAR_INTREBARI}: {text_intrebare}")
        print("-" * 20)
        for k, v in optiuni.items():
            print(f"  {k}) {v}")
            
        start_time = time.time()
        
        raspuns = input("Răspuns: ").lower().strip()
        
        end_time = time.time()
        timp_scurs = end_time - start_time
        
        if timp_scurs > TIMP_LIMITA:
            print(f"⏰ TIMP EXPIRAT! Ai răspuns în {timp_scurs:.1f} secunde.")
            print(f"Răspunsul corect era: {raspuns_corect}")
        elif raspuns == raspuns_corect:
            print(f"✅ Corect! ({timp_scurs:.1f} sec)")
            score += 1
        else:
            print(f"❌ Greșit. Era: {raspuns_corect}")
            
    print(f"\nJoc gata! Scorul tău: {score}/{NUMAR_INTREBARI}")
    
    salveaza = input("Vrei să salvezi scorul? (da/nu): ").lower()
    if salveaza == "da":
        nume_jucator = input("Scrie-ți numele: ")
        salveaza_scor(nume_jucator, score)
        arata_top()
    else:
        print("Scor nesalvat.")

if __name__ == "__main__":
    start_joc()