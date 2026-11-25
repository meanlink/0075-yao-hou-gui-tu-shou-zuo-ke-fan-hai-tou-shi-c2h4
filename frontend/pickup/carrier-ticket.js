import {badge,h} from '/base.js'
import {choices} from './platform.js'
import {locationName,slipStates} from './dictionary.js'

export function ticket(slip,sites,reviewer){
  return `<article class="transfer-slip"><header><div><span>${h(slip.tag)}</span><h2>${h(slip.title)}</h2></div>
    ${badge(slipStates[slip.state],slip.state)}</header>
    <p>${h(locationName(sites,slip.origin))} → ${h(locationName(sites,slip.destination))}</p>
    ${reviewer&&slip.state==='out'?`<form data-slip="${slip.id}"><label>签收站<select name="studio">${choices(sites,'code',r=>r.name,slip.destination)}</select></label>
     <button value="accepted">确认到站</button><button class="quiet" value="returned">退回原点</button><p role="status"></p></form>`:''}</article>`
}
