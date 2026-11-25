import {api,empty} from '/base.js'
import {attach,boot,head,selector} from './platform.js'
import {ticket} from './carrier-ticket.js'

export async function transfer(root,user,selected){
  const {classes,sites,code}=await boot(selected)
  if(!code){root.innerHTML=empty('当前没有课程。');return}
  const rows=await api('/api/studio/workshops/'+code+'/carriage')
  root.innerHTML=head('调拨到货','调拨票在到站验收或原点接回后关闭。在途中作品不可领取。')
    +`<div class="clay-grid"><section class="transfer-list">${rows.length?rows.map(row=>ticket(row,sites,user.role==='reviewer')).join(''):empty('本课尚无调拨。需要跨点时从作品架开票。')}</section>
      <aside>${selector(classes,code)}<p>到货角色须核对实际接收点。将原点与代收点区分后再签。</p><a href="#shelf">返回作品架</a></aside></div>`
  root.querySelector('#class').onchange=e=>transfer(root,user,e.target.value)
  for(const form of root.querySelectorAll('[data-slip]'))attach(form,(data,button)=>api('/api/studio/carriage/'+form.dataset.slip,'PUT',{...data,decision:button.value}),()=>transfer(root,user,code))
}
