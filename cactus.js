let shown_trs = document.getElementsByClassName('mrh-detail-row');
let hidden_trs = document.getElementsByClassName('dash-collapse-row');
for (let i = 0; i < shown_trs.length; i++) {
  let subject   = hidden_trs[i].getElementsByClassName('dash-collapse-lft')[0].getElementsByTagName('li')[0].textContent.match(/Subject area:(.*)/);  
  let jobcode   = shown_trs[i].getElementsByTagName('span')[0].textContent.trim();  
  let date      = shown_trs[i].getElementsByTagName('td')[3].textContent.match(/(.*)\(IST\)/);
  let unitcount = shown_trs[i].getElementsByTagName('td')[4].textContent.match(/Unit count: ([,\d]+)/);
  console.log((subject?subject[1].trim():"unknown") + ", " + jobcode + ', "' + (date?date[1].trim().replace(/,/, ''):"unknown") + '", "' + (unitcount?unitcount[1].trim().replace(/,/, ''):"unknown") + '"');  
}
for (let i = 0; i < shown_trs.length; i++) {
  let tds = shown_trs[i].getElementsByTagName('td');
  let m = tds.length < 5?"":tds[4].textContent.match(/Unit count: (\d\d\d?)\s/);
  // hide rows with more than 800 words
  if (!m || parseInt(m[1]) > 800) shown_trs[i].style.display = "none";
}

