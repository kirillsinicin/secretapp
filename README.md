# secretapp

Нужно сделать HTTP сервис для одноразовых секретов наподобие [https://onetimesecret.com/](https://onetimesecret.com/?locale=ru).

Он должен позволить создать секрет, задать кодовую фразу для его открытия и cгенерировать код, по которому можно прочитать секрет только один раз. UI не нужен, это должен быть JSON API сервис.

- Метод `/generate` должен принимать секрет и кодовую фразу и отдавать `secret_key` по которому этот секрет можно получить.
- Метод `/secrets/{secret_key}` принимает на вход кодовую фразу и отдает секрет.

## Как какать

```bash
cp .env.local .env
docker compose up
```
