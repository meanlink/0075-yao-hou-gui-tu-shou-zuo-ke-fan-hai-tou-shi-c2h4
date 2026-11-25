import {api,empty,h} from '/base.js'
import {attach,boot,head,selector} from './platform.js'
import {matrix} from './matrix.js'

export async function closing(root,user,selected){
  const {classes,sites,code,course}=await boot(selected)
  if(!code){root.innerHTML=empty('暂无课程。');return}
  const path='/api/studio/workshops/'+code
  const {pivot,published}=await api(path+'/pivot')
  root.innerHTML=head('返还透视','待领归当前保管站点，在途归计划接收点，已领归真实交付站点。')
   +`<div class="clay-grid"><section><h2>${h(course.title)}</h2>${matrix(pivot,sites)}</section>
   <aside>${selector(classes,code)}<p>${published?'已归档':'核对进度'} · ${pivot.transit} 件在途</p>
   ${!published&&user.role==='reviewer'?'<p>作品都已返还后可关闭课程台账。</p><form><button>归档透视</button><p role="status"></p></form>':''}</aside></div>`
  root.querySelector('#class').onchange=e=>closing(root,user,e.target.value)
  attach(root.querySelector('form'),()=>api(path+'/archive','POST',{}),()=>closing(root,user,code))
}
