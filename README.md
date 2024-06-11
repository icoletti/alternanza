# Alternanza scuola-lavoro
## Tecnologie usate
Web application realizzata con Flask, Docker, Docker Compose e Tailwind CSS.
## Obiettivi principali
1. **Creazione di un ambiente di lavoro con Docker**: cofigurazione di container Docker per creare un ambiente di sviluppo standardizzato. Ogni componente del progetto sarà isolato in un container, facilitando il deployment e la scalabilità.
2. **Implementazione di un servizio Web con Flask**: utilizzo di flask per sviluppare un'applicazione server-side in Python. Il servizio fornirà API RESTful per la gestione dei dati e interfaccerà il frontend con il database.
3. **Sviluppo della pagina Web**: progettazione dell'interfaccia utente e sviluppo delle funzionalità frontend, garantendo un'esperienza utente intuitiva e responsive. Vanno implementate le richieste specifiche del progetto per soddisfare  gli obbiettivi funzionali.
## Documentazione
### Creazione del File Flask (`app.py`, `form.py` e `config.py`)
#### Struttura del Codice app.py

Per iniziare ho creato una semplice applicazione Flask. Ho creato un file chiamato `app.py`. Questa applicazione gestisce alcune rotte e rende i template HTML corrispondenti. La logica principale include la gestione degli errori di un form e il rendering dei risultati.

1. **Configurazione delle variabili**
   - `actual_purchase`: Viene formattato con 8 cifre decimali.
   - `savings_percentange`: Viene formattato con 2 cifre decimali.
   - `codice_invito`: Stringa che contiene il codice invito.
   - `desc`: Contiene una descrizione.
   - `smart_options`: Opzioni intelligenti, una lista o un dizionario.
   - `choices`: Scelte, un dizionario.

2. **Render Template**
   ```python
   return render_template('result1.html', **data)
   ```
   Questa riga rende il template `result1.html` passando i dati formattati come contesto.

3. **Gestione degli Errori del Form**
   ```python
   else:
       for field, errors in form.errors.items():
          for error in errors:
             flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'error')
   return render_template('upload.html', form=form, price=price)
   ```
   - In caso di errori nel form, vengono iterati tutti i campi e i relativi errori.
   - Viene utilizzata la funzione `flash` di Flask per mostrare i messaggi di errore.
   - Alla fine, viene renderizzato il template `upload.html` con il form e il prezzo passato come contesto.

4. **Rotte dell'Applicazione**
   - **Home Route** (`"/"`)
     ```python
     @app.route("/")
     def home():
         return render_template('base.html')
     ```
     - Questa rotta gestisce la pagina principale della web app. Rende il template `base.html`.

   - **Error Route** (`"/error/"`)
     ```python
     @app.route('/error/')
     def error():
         return render_template('error.html')
     ```
     - Questa rotta gestisce la pagina degli errori, rendendo il template `error.html`.

5. **Esecuzione dell'App**
   ```python
   if __name__ == "__main__":
       """ run app """
       app.run(host=HOST, port=PORT)
   ```
   - Questo blocco verifica se lo script è eseguito direttamente e non importato come modulo.
   - Avvia l'applicazione Flask sul host e la porta specificata dalle variabili `HOST` e `PORT`.

#### Funzionamento Dettagliato

- **Formattazione dei Dati**
  I valori numerici come `actual_purchase` e `savings_percentange` sono formattati per essere presentati con un numero specifico di cifre decimali, garantendo una presentazione uniforme.

- **Gestione degli Errori**
  La gestione degli errori è curata attraverso il loop sui campi del form che contengono errori. Ogni errore viene catturato e mostrato all'utente tramite messaggi flash, migliorando l'esperienza utente e facilitando la correzione degli errori.

- **Routing**
  L'applicazione definisce tre rotte principali: la home, il form e una pagina di errore, ciascuna associata a un template HTML specifico. Questo permette di mantenere il codice organizzato e separato in base alla funzionalità offerta agli utenti.

- **Avvio dell'Applicazione**
  L'applicazione viene avviata solo se il file è eseguito direttamente. Questo è utile durante lo sviluppo e il debug, poiché consente di avviare l'applicazione con un semplice comando.

#### Funzioni del file form.py

Ho creato un file chiamato `form.py`. Questo modulo contiene funzioni per calcolare le commissioni e i risparmi basati su diverse condizioni di input. Utilizza un logger per registrare informazioni rilevanti durante l'esecuzione delle funzioni.

#### `calculate_commission(quantity, invito_boolean, operation, payment, billing_info)`

Calcola la commissione basata su vari parametri di input e aggiustamenti specifici.

#### Parametri:
- `quantity` (int): La quantità su cui calcolare la commissione.
- `invito_boolean` (str): Una stringa che determina se applicare un aggiustamento per 'best_option'.
- `operation` (str): Una stringa che determina se applicare un aggiustamento per 'best_option0'.
- `payment` (str): Una stringa che determina se applicare un aggiustamento per 'best_option1'.
- `billing_info` (str): Una stringa che determina se applicare un aggiustamento per 'best_option2'.

#### Ritorna:
- `float`: La commissione calcolata in base alla quantità e agli aggiustamenti applicabili.

#### Note:
- Viene utilizzato un logger per registrare informazioni sulla quantità, sul range massimo e sulla condizione `quantity < range_max`.
- La commissione viene aggiustata in base a vari parametri specifici.
- Se nessuna condizione è soddisfatta, viene ritornata una commissione di base.

#### `calculate_savings(quantity, invito_boolean, operation, payment, billing_info)`

Calcola i risparmi percentuali rispetto a una commissione standard.

#### Parametri:
- `quantity` (int): La quantità su cui calcolare i risparmi.
- `invito_boolean` (str): Una stringa che determina se applicare un aggiustamento per 'best_option'.
- `operation` (str): Una stringa che determina se applicare un aggiustamento per 'best_option0'.
- `payment` (str): Una stringa che determina se applicare un aggiustamento per 'best_option1'.
- `billing_info` (str): Una stringa che determina se applicare un aggiustamento per 'best_option2'.

#### Ritorna:
- `float`: La percentuale di risparmio rispetto alla commissione standard.

#### Note:
- Calcola la commissione attuale utilizzando la funzione `calculate_commission`.
- Confronta la commissione attuale con una commissione standard (`base_commission`).
- Registra la commissione attuale e quella standard utilizzando un logger.
- Calcola la percentuale di risparmio e la ritorna.

#### Costanti:
- `logger`: Un oggetto logger utilizzato per registrare informazioni durante l'esecuzione delle funzioni.
- `commission_rates` (list): Una lista di tassi di commissione applicabili.
- `best_option_adjustment` (float): Un valore di aggiustamento per 'best_option'.
- `base_commission` (float): La commissione standard utilizzata per calcolare i risparmi.

#### Esempio di Utilizzo

```python
quantity = 100
invito_boolean = 'best_option'
operation = 'best_option0'
payment = 'best_option1'
billing_info = 'best_option2'

commission = calculate_commission(quantity, invito_boolean, operation, payment, billing_info)
savings = calculate_savings(quantity, invito_boolean, operation, payment, billing_info)

print(f"Commissione: {commission}")
print(f"Risparmio percentuale: {savings}%")
```


#### Documentazione del file `config.py`

Il file `config.py` è un file di configurazione per un'applicazione Python. Questo file imposta vari parametri di configurazione necessari per l'esecuzione dell'applicazione, utilizzando principalmente variabili di ambiente per ottenere i valori di configurazione. Qui di seguito è fornita una spiegazione dettagliata del contenuto del file.


```python
import os
import redis
```

- `os`: Il modulo `os` fornisce un modo per interagire con il sistema operativo, in particolare per accedere alle variabili di ambiente.
- `redis`: Questo modulo è utilizzato per interagire con il database Redis.

#### Variabili di Ambiente

```python
REDIS_URL = os.environ["REDIS_URL"]
DEBUG_MODE = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
```

- `REDIS_URL`: Questa variabile legge l'URL di connessione al server Redis dalla variabile di ambiente `REDIS_URL`. È obbligatoria e deve essere definita nell'ambiente in cui l'applicazione viene eseguita.
- `DEBUG_MODE`: Questa variabile legge lo stato del debug dalla variabile di ambiente `DEBUG`. Se `DEBUG` è impostato su `'true'` o `'1'`, `DEBUG_MODE` sarà `True`, altrimenti sarà `False`.

#### Classe `Config`

```python
class Config(object):
    """ config object """
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.environ['SECRET_KEY']

    # redis config
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url(REDIS_URL)

    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 100
    CACHE_REDIS_URL = REDIS_URL

    DEBUG = DEBUG_MODE
```

- `basedir`: Questa variabile definisce la directory di base del progetto, ottenuta in modo assoluto dalla posizione del file `config.py`.
- `SECRET_KEY`: Questa variabile legge il valore della chiave segreta per l'applicazione dalla variabile di ambiente `SECRET_KEY`. È obbligatoria per la sicurezza dell'applicazione.
- `SESSION_TYPE`: Questo parametro è impostato su `'redis'`, indicando che le sessioni utente verranno gestite tramite Redis.
- `SESSION_REDIS`: Questa variabile crea una connessione al server Redis utilizzando l'URL specificato in `REDIS_URL`.
- `CACHE_TYPE`: Indica che il tipo di cache utilizzato è `RedisCache`.
- `CACHE_DEFAULT_TIMEOUT`: Imposta il timeout predefinito della cache a 100 secondi.
- `CACHE_REDIS_URL`: Imposta l'URL del server Redis per la cache.
- `DEBUG`: Imposta lo stato del debug utilizzando il valore della variabile `DEBUG_MODE`.


Le variabili `HOST`, e `PORT` si torvano nel file .env creato.
```
HOST=0.0.0.0
PORT=8702
DEBUG=true
FLASK_DEBUG=1
NAME=Nome
```


### Creazione del File Docker (`Dockerfile`)

Il `Dockerfile` è un file di testo che contiene tutte le istruzioni necessarie per creare un'immagine Docker. Ho creato un file chiamato `Dockerfile` nella stessa directory di `app.py` e ho aggiunto il seguente contenuto:
```Dockerfile
FROM python:3.11-slim-bookworm

WORKDIR /usr/src/app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./app.py"]
```
### Creazione del File dei Requisiti (`requirements.txt`)

Ho creato un file chiamato `requirements.txt` nella stessa directory di `app.py` e ho aggiunto il seguente contenuto:
```
Flask==3.0.3
Flask-WTF==1.2.0
email_validator==2.1.1
requests==2.32.2
redis==5.0.1
Flask-Caching==2.3.0
```
### Creazione del File Docker Compose (`docker-compose.yml`)

Il file `docker-compose.yaml` è utilizzato per definire e gestire applicazioni multi-container con Docker Compose.
Il file `docker-compose.yml` definisce i servizi Docker che compongono la tua applicazione. Il file è strutturato in sezioni principali e sottosezioni, ognuna con uno scopo specifico. Ecco una panoramica del contenuto:
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
    restart: unless-stopped
    volumes:
      - ./backend:/usr/src/app
  redis:
    image: "redis:alpine"
    restart: unless-stopped
    container_name: "container_cache"
```


Il file `docker-compose.yaml` è utilizzato per definire e gestire applicazioni multi-contenitore con Docker Compose. Di seguito è riportata una documentazione dettagliata del file `docker-compose.yaml` che hai fornito.

### Struttura del file `docker-compose.yaml`

Il file è strutturato in sezioni principali e sottosezioni, ognuna con uno scopo specifico. Ecco una panoramica del contenuto:

```yaml
version: '3'

services:
  backend:
    build:
      context: ./backend
    env_file:
      - .env
    ports:
      - ${PORT}:${PORT}
    container_name: "container_flask"
    restart: unless-stopped
    volumes:
      - ./backend:/usr/src/app
  redis:
    image: "redis:alpine"
    restart: unless-stopped
    container_name: "container_cache"
```

#### services
La sezione `services` definisce i vari servizi (contenitori) che compongono l'applicazione. In questo esempio, ci sono due servizi: `backend` e `redis`.
#### backend
Questo servizio rappresenta l'applicazione backend, web application sviluppata con Flask.
#### redis
Questo servizio utilizza un'immagine preesistente di Redis, una soluzione di caching in-memory.

### Creazione dei template e css

All'interno della cartella in cui si trova il mio file `app.py` ho creato due directory `template` e `static`, quest'ultima contenente altre due directory, `style`  e `js`.
Dentro `template` troviamo tutti i file html che "sviluppano" la mia applicazione. Dentro `js`, invece, ho ricopiato il contenuto di https://cdn.tailwindcss.com/3.4.3 nel mio file `tailwind.js`.

### Costruzione e Avvio dei Container

Una volta creati tutti i file necessari, posso costruire e avviare i container utilizzando Docker Compose. Ho aperto il terminale nella directory contenente i file creati e ho eseguito i seguenti comandi:
```sh
docker compose up -d --build && docker compose logs -f --tail 50
```
### Accesso all'Applicazione

Dopo aver avviato i container, l'applicazione Flask sarà accessibile all'indirizzo `http://localhost:8702`, dove `8702` è la porta specificata nel file .env. Ho aperto il mio browser e ho navigato verso questo URL per vedere l'applicazione in esecuzione.

## Risorse aggiuntive
Per ulteriori informazioni su Docker, consultare la [documentazione ufficiale di docker](https://docs.docker.com/).

Per approfondire Docker Compose, vedere la [documentazione ufficiale](https://docs.docker.com/compose/). 

[Documentazione con esempi pratici di docker, docker compose](https://docker-curriculum.com/).

Per ulteriori informazioni riguardanti flask consultare la [documentazione ufficiale](https://flask.palletsprojects.com/en/3.0.x/)

Per ulteriori informazioni riguardanti flask-WTF consultare la [documentazione ufficiale](https://flask-wtf.readthedocs.io/en/1.2.x/)

[Documentazione ufficiale di tailwind CSS](https://tailwindcss.com/docs/installation)