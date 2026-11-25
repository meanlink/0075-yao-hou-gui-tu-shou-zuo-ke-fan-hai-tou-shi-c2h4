# 窑后归途 · 手作课返还透视

青苔陶社的 4 名教务助理在三个课程点交还成品。助理过去分别在纸架签、托运表和微信提醒中记状态，作品在途被误当到货、实际代收点与开班点混算、取件回执补录丢失。课程讲师和教务主管从透视取得返还正本。

| 角色 | 动作 |
|---|---|
| operator | 看作品架、办理跨点托运、验证领件码、签收实际交付 |
| reviewer | 确认调拨到站或原点退回、归档返还结果 |
| viewer | 查阅在架、在途、领取回执和站点透视 |

1. 11 月 19 日 10:00 CLASS-17《冬日手捏花盏》成品标为 POT-11—13。
2. 11 月 20 日 08:30 青苔主校按回执登记 POT-12。
3. 09:15 为蓝釉花盏 POT-11 开往东桥课点的托运票；在途时不能领取。
4. 10:30 东桥课点签收，使 POT-11 挂到当地作品架。
5. 11:20 按课堂分发码 CX-11，登记作品的真实交付点为 EAST。
6. 15:00 槐树共创坊交付 POT-13，现场码 CX-13。
7. 教务复核后结课，三件全部返还，两件跨校，站点总和守恒。

透视以作品标签为唯一计数键。待领取归实际保管点，在途归计划接收点，已领取归签收站点，与主校不同计跨点领取。未完成返还不能归档，归档后操作冻结。演示全部使用合成取件码，真实生产需接入正式身份和取件码管理。

```sh
cp -n .env.example .env
docker compose up -d --build --wait
docker compose exec backend python -m scripts.seed_demo
docker compose down -v --remove-orphans
```

宿主端口使用 FRONTEND_PORT、BACKEND_PORT、DB_PORT。演示账号 operator@demo.local、reviewer@demo.local、viewer@demo.local，默认 Demo2026!。SEED_DEMO 控制填充，DEMO_PASSWORD、POSTGRES_PASSWORD、JWT_SECRET 为演示配置。原生 ES modules + Nginx、FastAPI、PostgreSQL、Redis、worker。后端本地安装 backend/requirements.txt，配置 DATABASE_URL、REDIS_URL、JWT_SECRET，执行 `uvicorn app:app --reload` 和 `python worker.py`。backend/claim 是课程、调拨、领件和透视，frontend/pickup 是页面。角色和任务枚举在 backend/core.py、frontend/base.js；作品状态及运单状态在 backend/schema.sql、backend/claim/forms.py、frontend/pickup/dictionary.js。MIT 许可。

前端地址为 http://127.0.0.1:18469，API 为 http://127.0.0.1:19469，数据库本机映射端口为 17969。
