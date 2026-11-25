import {api,h,empty} from '/base.js'
import {attach,boot,head,selector} from './platform.js'
import {receiptForm} from './claim-form.js'
import {locationName} from './dictionary.js'

export async function pickup(root,user,selected){
  const {classes,sites,code,course}=await boot(selected)
  if(!code){root.innerHTML=empty('无可办理的课程。');return}
  const path='/api/studio/workshops/'+code
  const [pieces,rows]=await Promise.all([api(path+'/pieces'),api(path+'/claims')])
  const available=pieces.filter(row=>row.status==='ready')
  root.innerHTML=head('到点领取','按当前实物保管点签收，领取人的课程取件码须与作品匹配。')
    +`<div class="clay-grid"><section><h2>已交付回执</h2><ol class="receipts">
    ${rows.map(row=>`<li><div><strong>${h(row.title)}</strong><small>${h(row.tag)}</small></div>
    <div>${h(row.receiver)}<small>${h(locationName(sites,row.studio))}</small></div><time>${h(row.local_day)}</time></li>`).join('')}</ol>
    ${rows.length?'':empty('尚无领取记录。')}</section><aside>${selector(classes,code)}
    ${user.role==='operator'&&available.length?receiptForm(available,sites,course.end_date):'<p>签收后在左侧保留返还凭据。</p>'}</aside></div>`
  root.querySelector('#class').onchange=e=>pickup(root,user,e.target.value)
  attach(root.querySelector('form'),({tag,...data})=>api('/api/studio/pieces/'+tag+'/claim','POST',data),()=>pickup(root,user,code))
}
