# reverse-proxy
- 성능
- 부하분산(LB)
- 가상 호스트 및 라우팅

## python server
```bash
$ python -m http.server 8001 --directory pyweb1
$ python -m http.server 8002 --directory pyweb2
$ python -m http.server 8003 --directory blog
```
## nginx
- https://ubuntu.com/tutorials/install-and-configure-nginx#2-installing-nginx

```bash
# install
$ sudo apt install nginx

$ sudo service nginx restart
$ sudo service nginx stop
$ sudo service nginx start
$ sudo service nginx status #-> worker 10ea 
$ sudo nginx -t # syntax check
```
```bash
$ sudo docker exec -it <LB_NAME> bash
$ nginx -s reload
```

## nGrinder
- http://localhost:8080/ (admin/admin)
```bash
$ pwd
~/app
$ tree -L 2
.
├── ngrinder-agent
│   ├── lib
│   ├── run_agent.sh
│   ├── run_agent_bg.sh
│   ├── run_agent_internal.sh
│   └── stop_agent.sh
└── ngrinder-controller
    └── ngrinder-controller-3.5.9-p1.war

$ cd app/ngrinder-controller
$ java -jar ngrinder-controller-3.5.9-p1.war

$ cd app/ngrinder-agent
$ run_agent.sh
```

## Docker
```bash 
$ sudo docker compose up -d  # 백그라운드에서 컨테이너 실행
$ sudo docker compose down   # 컨테이너 중지 및 네트워크 제거
$ sudo docker compose stop   # 컨테이너 중지
$ sudo docker compose start  # 중지된 컨테이너 다시 시작
$ sudo docker compose restart  # 컨테이너 재시작
$ sudo docker compose stats # 성능 모니터링
```

## scale out
```bash
$ sudo docker compose up -d --scale web1=n
```

## FastAPI
```bash
$ fastapi dev main.py
```

## PDM to requirements.txt
```bash
$ pdm export -o requirements.txt --without-haches
```

## Docker build & push & pull run
```bash
$ sudo docker build -t jiwon1118/api:6.1.0 -f docker/fastapi/Dockerfile .
$ sudo docker login
$ sudo docker push jiwon1118/api:6.1.0
$ sudo docker run -d --name api610 -p 8610:80 jiwon1118/api:6.1.0
```