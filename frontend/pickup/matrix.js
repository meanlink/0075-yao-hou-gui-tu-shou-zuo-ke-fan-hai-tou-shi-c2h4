import {h} from '/base.js'
import {locationName} from './dictionary.js'

export function matrix(pivot,sites){
  return `<div class="studio-matrix"><table><thead><tr><th>站点</th><th>待领取</th><th>在途入点</th><th>已领取</th><th>跨校领取</th></tr></thead><tbody>
    ${pivot.sites.map(row=>`<tr><th scope="row">${h(locationName(sites,row.studio))}</th>
    <td>${row.shelf}</td><td>${row.in_transit}</td><td>${row.collected}</td><td>${row.collected_away}</td></tr>`).join('')}</tbody></table></div>
    <p class="pivot-line">${pivot.collected} / ${pivot.pieces} 件已领 · ${pivot.away} 件跨校</p>`
}
