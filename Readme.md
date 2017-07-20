Add your Domain Renewal Dates in a ical to import in google calendar or something else.

# Install (with Docker)
Clon the Project and run the following command to install:

```
docker build -t sspssp/inwx-domain-calendar .
```

Than copy the config.cfg-example to config.cfg and insert your inwx credentials.

# Use (with Docker)
Run the following Command to create a domains.ical in the folder of the Projekt:

```
docker run -v /$(pwd):/usr/src/app sspssp/inwx-domain-calendar
```

# Install (without Docker)
Copy the config.cfg-example to config.cfg and insert your inwx credentials.

Than install the requirements with pip
```
pip install -r requirements.txt
```

# Use (without Docker)
Run the createICAL.py file to create a domains.ical file

```
python3 createICAL.py
```
