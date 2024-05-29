# Alternanza scuola-lavoro
## Tecnologie usate
Web application realizzata con Flask, Docker, Docker Compose e Tailwind CSS.
## Obiettivi principali
1. **Creazione di un ambiente di lavoro con Docker**: cofigurazione di container Docker per creare un ambiente di sviluppo standardizzato. Ogni componente del progetto sarà isolato in un container, facilitando il deployment e la scalabilità.
2. **Implementazione di un servizio Web con Flask**: utilizzo di flask per sviluppare un'applicazione server-side in Python. Il servizio fornirà API RESTful per la gestione dei dati e interfaccerà il frontend con il database.
3. **Selezione del Framework Frontend**: analisi delle esigenze del progetto per scegliere il framework frontend ottimale tra React, Angular e Vue.js. La scelta terrà conto di criteri come la facilità d'uso, la performance e la compatibilità con il backend.
4. **Sviluppo della pagina Web**: progettazione dell'interfaccia utente e sviluppo delle funzionalità frontend, garantendo un'esperienza utente intuitiva e responsive. Vanno implementate le richieste specifiche del progetto per soddisfare  gli obbiettivi funzionali.
## Documentazione
1. Creazione del File Flask (`app.py` e `form.py`)
Per iniziare ho creato una semplice applicazione Flask. Ho creato un file chiamato `app.py` e ho aggiunto il seguente codice:
```python

```
Ho creato un file chiamato `form.py` e ho aggiunto il seguente codice:
```python

```
Le variabili `HOST`, e `PORT` si torvano all'interno del file .env creato.
```
HOST=0.0.0.0
PORT=8702
DEBUG=true
FLASK_DEBUG=1
NAME=Nome
```
2. Creazione del File Docker (`Dockerfile`)
Il `Dockerfile` è un file di testo che contiene tutte le istruzioni necessarie per creare un'immagine Docker. Ho creato un file chiamato `Dockerfile` nella stessa directory di `app.py` e ho aggiunto il seguente contenuto:
```Dockerfile
FROM python:3.11-slim-bookworm

WORKDIR /usr/src/app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./app.py"]
```
3. Creazione del File dei Requisiti (`requirements.txt`)
Ho creato un file chiamato `requirements.txt` nella stessa directory di `app.py` e ho aggiunto il seguente contenuto:
```
Flask==3.0.3
Flask==3.0.3
Flask-WTF==1.2.0
```
4. Creazione del File Docker Compose (`docker-compose.yml`)
Il file `docker-compose.yml` definisce i servizi Docker che compongono la tua applicazione. Ho creato un file chiamato `docker-compose.yml` e ho aggiunto il seguente contenuto:
```yaml
services:
  backend:
    build:
      context: ./backend
    env_file:
      - .env
    ports:
      - ${PORT}:${PORT}
    container_name: "container_flask"
    volumes:
      - ./backend:/usr/src/app
```
5. Creazione dei template e css
All'interno della cartella in cui si trova il mio file `app.py` ho creato due directory `template` e `static`, quest'ultima contenente altre due directory, `style`  e `js`.
Dentro `template` troviamo tutti i file html che "sviluppano" la mia applicazione. Dentro `js`, invece, ho ricopiato il contenuto di https://cdn.tailwindcss.com/3.4.3 nel mio file `tailwind.js`.
6. Costruzione e Avvio dei Container
Una volta creati tutti i file necessari, posso costruire e avviare i container utilizzando Docker Compose. Ho aperto il terminale nella directory contenente i file creati e ho eseguito i seguenti comandi:
```sh
docker compose up -d --build && docker compose logs -f --tail 50
```
7. Accesso all'Applicazione
Dopo aver avviato i container, l'applicazione Flask sarà accessibile all'indirizzo `http://localhost:8702`, dove `8702` è la porta specificata nel file .env. Ho aperto il mio browser e ho navigato verso questo URL per vedere l'applicazione in esecuzione.
### Color Palette 
[Link dei colori](https://colorhunt.co/palette/fffae6ff9f66ff5f00002379)
## Risorse aggiuntive
Per ulteriori informazioni su Docker, consultare la [documentazione ufficiale di docker](https://docs.docker.com/).

Per approfondire Docker Compose, vedere la [documentazione ufficiale](https://docs.docker.com/compose/). 

[Documentazione con esempi pratici di docker, docker compose](https://docker-curriculum.com/).

Per ulteriori informazioni riguardanti flask consultare la [documentazione ufficiale](https://flask.palletsprojects.com/en/3.0.x/)

Per ulteriori informazioni riguardanti flask-WTF consultare la [documentazione ufficiale](https://flask-wtf.readthedocs.io/en/1.2.x/)

[Documentazione ufficiale di tailwind CSS](https://tailwindcss.com/docs/installation)