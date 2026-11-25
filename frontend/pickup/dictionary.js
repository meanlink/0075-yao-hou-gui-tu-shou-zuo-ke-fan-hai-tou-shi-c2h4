export const states={ready:'在架等领取',moving:'在途',collected:'已领取'}
export const slipStates={out:'在途待验收',accepted:'已到站',returned:'退回原校'}
export const locationName=(sites,code)=>sites.find(site=>site.code===code)?.name??code
