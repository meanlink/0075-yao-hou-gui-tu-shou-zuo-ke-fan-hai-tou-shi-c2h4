import {h} from '/base.js'
import {choices} from './platform.js'
export function receiptForm(available,sites,day){
  return `<form><label>作品<select name="tag">${choices(available,'tag',r=>r.title)}</select></label>
    <label>实际站点<select name="studio">${choices(sites,'code',r=>r.name,available[0]?.site)}</select></label>
    <label>取件码<input name="code" required pattern="[A-Z0-9-]{3,24}"></label>
    <label>领取人<input name="receiver" required minlength="2" maxlength="80"></label>
    <label>领取日期<input name="local_day" type="date" value="${h(day)}" required></label>
    <button>登记领取</button><p role="status"></p></form>`
}
