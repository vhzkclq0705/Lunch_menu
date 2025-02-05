# Lunch-menu

- [x] 팀원들의 점심 메뉴 수집
- [x] 분석
- [ ] 알람(입력하지 않은 사람들에게)
- [x] CSV to DB

## READY

### Install DB with Docker
```bash
$ sudo docker run --name local-postgres \
> -e POSTGRES_USER=<USER_NAME> \
> -e POSTGRES_PASSWORD=<PASSWORD> \
> -e POSTGRES_DB=<DB-NAME> \
> -p 5432:5432 \
> -d postgres:15.10
```

### CREATE Table
- postgres

```sql
CREATE TABLE public.lunch_menu (
	id serial4 NOT NULL,
	menu_name text NOT NULL,
	dt date NOT NULL,
	member_name text NOT NULL,
	CONSTRAINT lunch_menu_pk PRIMARY KEY (id),
	CONSTRAINT lunch_menu_unique UNIQUE (menu_name, member_name, dt)
);
```

## DEV
- DB
```bash
$ sudo docker ps -a
$ sudo docker start local-postgres
$ sudo docker stop local-postgres

# Into Container
$ sudo docker exec -it local-postgres bash
```

- RUN
```bash
# DB 정보에 맞춰 수정
$ cp env.dummy .env

# 서버 시작
$ streamlit run App.py
```
