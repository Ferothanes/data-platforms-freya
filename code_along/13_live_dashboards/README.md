# the table created in container # psql -U postgres, \l, \c your database, \dt = shows the tables
select * from bitcoin;

1. make sure enviroment is activated
2. docker compose up -d by docker you want to start (create container)
    **docker-compose.yml**
        hostname: schema-registry
        container_name: schema-registry
        image: postgres:latest
        container_name: postgres
3. start python producer.py
4. start python consumer.py 
5. after feeding data into consumer you can turn of API producer 
6. docker exec -it "database_name(postgres)" bash
7. psql -U(User) postgres
    - \l = lists databases
        - \c (vald databas )= connectar till vald databas
            - \dt  = kollar tabellerna i databas 
            - select * from database;

8. **Connecta till dashboard**
- create dashboard.py 
- run - **streamlit run scr/dashboard.py**

9. PRESS "Always re-run" for latest data (on web)



