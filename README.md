# Device interface configuration

This task was developed for FRINX s.r.o.
The program parses the data from the configClear_v2.json file
and then sends the data to a database running in the local container.

Entered by: Daniel Zlacký

Assignment made by: Martin Revaj

## Prerequisites

- Python 3.6+ 
[Instalation guide for python.](https://opensource.com/article/20/4/install-python-linux)

- PostgreSQL 10+ 

- Docker 
[Instalation guide for docker.](https://docs.docker.com/desktop/linux/install/ubuntu/)

- pgAdmin 4
[Instalation guid for pgAdmin](https://www.pgadmin.org/download/pgadmin-4-python/)

### Run docker and database

Open a terminal and type:

```bash
cd device_interface_configuration/docker
```

```bash
docker-compose up
```

### Run the python script

Open new terminal window and go to the parent folder:

```bash
cd device_interface_configuration
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install psycopg2
```

```bash
python3 main.py
```

### Check result in database

```bash
sudo mkdir /var/lib/pgadmin
```

```bash
sudo mkdir /var/log/pgadmin
```

```bash
sudo chown $USER /var/lib/pgadmin
```

```bash
sudo chown $USER /var/log/pgadmin
```

```bash
pip install pgadmin4
```

```bash
pgadmin4
```

Add email address and password.
After this copy the url address and paste to your web browser.
Log in and add server, and database credentials.
You can find it in postgresql/database.ini.
Then navigate to the database schemas and under tables you should
find the device_interface_configuration table.
Then click tools > query tools and type:

```postgres-sql
select * from device_interface_configuration;
```