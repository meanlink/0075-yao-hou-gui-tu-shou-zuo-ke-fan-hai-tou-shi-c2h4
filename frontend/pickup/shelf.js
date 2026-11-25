import {api,empty,h} from '/base.js'
import {boot,head,selector,choices,attach} from './platform.js'
import {slots} from './bins.js'
import {locationName} from './dictionary.js'

export async function shelf(root,user,selected){
  const {classes,sites,code,course}=await boot(selected)
  if(!code){root.innerHTML=empty('当前没有课程。');return}
  const items=await api('/api/studio/workshops/'+code+'/pieces')
  const ready=items.filter(row=>row.status==='ready')
  root.innerHTML=head('课程作品架','每件成品有自己的标签。课程主校、当前保管点与代收点分别记录。')
   +`<div class="clay-grid"><section><h2>${h(course.title)} / ${h(locationName(sites,course.home))}</h2>
   <div class="slots">${slots(items,sites)}</div></section><aside>${selector(classes,code)}
   <p>领取日期 ${h(course.end_date)} 至 ${h(course.pickup_through)}</p>
   ${user.role==='operator'&&ready.length?`<form><h2>托运转点</h2><label>作品<select name="tag">${choices(ready,'tag',r=>r.title)}</select></label>
   <label>代收点<select name="destination">${choices(sites,'code',r=>r.name)}</select></label><button>办调拨票</button><p role="status"></p></form>`:''}</aside></div>`
  root.querySelector('#class').onchange=e=>shelf(root,user,e.target.value)
  attach(root.querySelector('form'),data=>api('/api/studio/pieces/'+data.tag+'/move','POST',{destination:data.destination}),()=>shelf(root,user,code))
}
