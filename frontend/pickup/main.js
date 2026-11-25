import {mount} from '/base.js'
import {shelf} from './shelf.js'
import {transfer} from './transfer.js'
import {pickup} from './pickup.js'
import {closing} from './closing.js'
const pages={shelf,transfer,pickup,closing}
mount({title:'窑后归途 · 手作课返还透视',kicker:'青苔陶社 / 成品领取',
  pages:{shelf:'课程作品架',transfer:'调拨到货',pickup:'到点领取',closing:'返还透视'},
  render:(page,root,user)=>pages[page](root,user)})
