import {api,h,notice} from '/base.js'

export const head=(title,detail)=>`<header class="clay-head"><h1>${h(title)}</h1><p>${h(detail)}</p></header>`
export const choices=(items,key,label,value)=>items.map(row=>`<option value="${h(row[key])}" ${row[key]===value?'selected':''}>${h(label(row))}</option>`).join('')
export const selector=(classes,code)=>`<label>课程<select id="class">${choices(classes,'code',row=>row.title,code)}</select></label>`
export async function boot(selected){
  const [classes,sites]=await Promise.all([api('/api/studio/workshops'),api('/api/studio/locations')])
  const code=selected??classes.find(row=>row.code==='CLASS-17')?.code??classes[0]?.code
  return {classes,sites,code,course:classes.find(row=>row.code===code)}
}
export function attach(form,handle,repaint){
  if(!form)return
  form.onsubmit=async event=>{
    event.preventDefault()
    const b=event.submitter
    b.disabled=true
    try{await handle(Object.fromEntries(new FormData(form)),b);await repaint()}
    catch(error){notice(form.querySelector('[role=status]'),error.message,true)}
    finally{b.disabled=false}
  }
}
