### DevOps Schema App - Open Source ###

Sal 401 har blivit 99 procent av vår grupps upplevelse av Nackademin.
När vi inte kunde vara där så tyckte minst en av oss att det var svårt att hitta till rätt sal i morgonstressen.
Så för att vi vill  missa så lite av all bra information vi får under lektionstid tänkte vi underhålla tanken med att få information om nästa lektion. Och eftersom så vädret är så otrevligt för tillfället ville vi även ha information om förhållandena denna dag. Så vi skapade appen DevOps 27.

Open Source. Konkurrens är hälsosamt, men den består ju i verkligheten  framförallt i den marknad som finns i världen som väntar utanför Nackademins portar.  Genom att hjälpa varandra under kursen vilket vi redan ger på ett bra sätt kan vi alla bli bättre programmerare när det är dags för oss att ta steget ut.

Alla är i DevOps25 är alltså välkomna att bidra och uppdatera denna kod.
Har någon ett coolt front-end, user-system med inloggningsfunktion eller en databas-ide? 
Välkomna att ladda ner eller skapa en git.


- Instruktioner

För att köra projektet lokalt behöver du först klona repot och gå in i projektmappen:

git clone https://github.com/edwardbroni-coder/devops-schema-app.git

cd devops-schema-app

Skapa sedan en virtuell miljö och aktivera den:

python3 -m venv venv

source venv/bin/activate # Linux/Mac

python -m venv venv

venv\Scripts\activate # Windows

Installera alla moduller från requirements.txt:

pip install -r requirements.txt

kör sedan skriptet genom att skriva :

python3 app.py # Linux/Mac python app.py # Windows

Öppna sedan i webbläsaren:

http://127.0.0.1:5000
