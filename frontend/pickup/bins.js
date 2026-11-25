import {badge,h} from '/base.js'
import {states,locationName} from './dictionary.js'

export function slots(pieces,sites){
  return pieces.map(item=>`<article class="slot"><span class="paper-tag">${h(item.tag)}</span>
    <h2>${h(item.title)}</h2><p>${h(locationName(sites,item.site))}</p>${badge(states[item.status],item.status)}</article>`).join('')
}
