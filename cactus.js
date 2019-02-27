let shown_trs = document.getElementsByClassName('mrh-detail-row');
for (let i = 0; i < shown_trs.length; i++) {
  let tds = shown_trs[i].getElementsByTagName('td');
  let m = tds[4].textContent.match(/Unit count: (\d\d\d?)\s/);
  // hide rows with more than 800 words
  if (!m || parseInt(m[1]) > 800) shown_trs[i].style.display = "none";
}
