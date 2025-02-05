# Lunch-menu

- [x] 팀원들의 점심 메뉴 수집
- [x] 분석
- [ ] 알람(입력하지 않은 사람들에게)

## Install DB with Docker
```bash
$ sudo docker run --name local-postgres \
> -e POSTGRES_USER=sunsin \
> -e POSTGRES_PASSWORD=mysecretpassword \
> -e POSTGRES_DB=sunsindb \
> -p 5432:5432 \
> -d postgres:15.10
```

## CREATE Table
- postgres

```sql
CREATE TABLE lunch_menu (
	id serial4 NOT NULL,
	menu_name text NOT NULL,
	dt date NOT NULL,
	member_name text NOT NULL,
	CONSTRAINT lunch_menu_pk PRIMARY KEY (id),
	CONSTRAINT lunch_menu_unique UNIQUE (menu_name, member_name, dt)
);
```
