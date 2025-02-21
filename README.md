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
