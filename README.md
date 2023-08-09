## Set environment

- Create virtual environment : 
    
    ```python -m venv venv```

- Create virtual environment : 
    
    - on wind: ``` .\venv\Scripts\activate```
    - on linux: ``` source venv/scripts/bin/activate```
  
- Install requirement 

  ```pip install -r requirements.txt```

## Run on local

- **Requirement:** Before running the code in local ensure that, docker and docker-compose are installed in your machine. 
- Create mysql db with docker-compose

  ``docker-compose -f docker/docker-compose.yaml  up -d ``
- Run app 
- Test with postman (load postman collection from [collection](doc/pyapi.postman_collection.json))