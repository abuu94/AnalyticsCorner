### Steps for Installation and Configuration of ODK

#### Step 1 : Cloning
```
docker system prune -a -f
git clone --recurse-submodules -c core.autocrlf=false https://github.com/getodk/central
cd central
```

#### Step 2 : Adjust docker-compose.yml , Keep the below codes for postgres14 and remove other postgres codes
```
  postgres14:
    image: postgres:14
    shm_size: 512m
    volumes:
      - postgres14:/var/lib/odk/postgresql/14
    environment:
      POSTGRES_USER: odk
      POSTGRES_PASSWORD: odk
      POSTGRES_DB: odk
    restart: always
    ports:
      - "5432:5432"
```

#### Step 3 : Adjust docker-compose.yml by adding these ports
```
service:
  ports:
    - "8383:8383"

enketo:
  ports:
    - "8005:8005"

pyxform:
  ports:
    - "8001:80"
```

#### Step 4 : Create secrets file inside docker as shown below
```
mkdir -p files/secrets

# Generate ODK private key
openssl genrsa -out files/secrets/odk.key 2048
# Extract ODK public key
openssl rsa -in files/secrets/odk.key -pubout -out files/secrets/odk.pem

# Generate JWT private key
openssl genrsa -out files/secrets/jwt.key 2048
# Extract JWT public key
openssl rsa -in files/secrets/jwt.key -pubout -out files/secrets/jwt.pem
```
#### Step 5 : Adjust docker-compose.yml by adding paths for secrets of service and nginx.
```
secrets:
  image: alpine:latest
  command: sh -c "echo 'Secrets already generated manually'"
  volumes:
    - ./files/secrets:/etc/secrets

service:
  ...
  volumes:
    - ./files/secrets:/etc/secrets
    - service-data:/data

nginx:
  ...
  volumes:
    - ./files/secrets:/etc/secrets
 
```

#### Step 6 : Copy the secrets created in step 4 from files/secrets to service and nginx.
```
docker cp files/secrets/jwt.key central_service_1:/etc/secrets/jwt.key
docker cp files/secrets/jwt.pem central_service_1:/etc/secrets/jwt.pem
docker cp files/secrets/odk.key central_service_1:/etc/secrets/odk.key
docker cp files/secrets/odk.pem central_service_1:/etc/secrets/odk.pem

docker cp files/secrets/jwt.key central_nginx_1:/etc/secrets/jwt.key
docker cp files/secrets/jwt.pem central_nginx_1:/etc/secrets/jwt.pem
docker cp files/secrets/odk.key central_nginx_1:/etc/secrets/odk.key
docker cp files/secrets/odk.pem central_nginx_1:/etc/secrets/odk.pem

docker-compose exec service ls /etc/secrets
docker-compose exec nginx ls /etc/secrets
```

#### Step 7 : Adjust client-config.json.template  file of nginx that is inside docker, add the api line as shown below
```
nano files/nginx/client-config.json.template
{
  "oidcEnabled": ${OIDC_ENABLED},
  "api": "https://odk.domain.co.tz"
}
```
#### Step 8 : Pull the repo to include all required files.
```
git submodule update --init --recursive
docker-compose down --remove-orphans
docker-compose up -d --build
docker-compose ps
```

#### Step 9 : After that Odk Should be Up and running,Check if docker's nginx is Up ?.
```
docker ps
docker logs central_nginx_1
docker exec -it central_nginx_1 nginx -t
docker exec -it central_nginx_1 ps aux | grep nginx
```

#### Step 10 : That means Frontend and Backend services of odk is ok.

#### Step 11 : Now Do Host Nginx Configuration.
```
sudo ln -s /etc/nginx/sites-available/surveyhub  /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
sudo certbot --nginx -d odk.domain.co.xyz
```


