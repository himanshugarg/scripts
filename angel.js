for (let i = 0; i < 100; i++) {
	setTimeout( () => {
		window.scrollTo(0, document.body.scrollHeight);	
	}, getRandomIntInclusive(1000, 10000));
}


function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}

	Array.from(document.querySelectorAll('[data-test="StartupResult"]')).forEach((el) => {
		let jobs = [];
		let retain = false;
		el.querySelectorAll('a').forEach((a) => {
			if (a.href.includes('/jobs/')) {
				console.log(a.href);
				a.querySelectorAll('div:nth-child(1) > span:nth-child(2)').forEach((salary) => {
					if (salary.innerText.includes('?')) {
						let matches = /-\s*?((\d+)(\.\d+)?)L/.exec(salary.innerText);
						if (matches && matches[1] >= 36) {
							retain = true;
						} else {
							console.warn(salary.innerText);
						}
					} else {
						retain = true;
					}
				});
			}
		});
		if (!retain) {
			console.warn("removing " + el.innerText);
			let hide = el.querySelector('button:nth-child(3)');
			if (!hide) {
				console.error("No button for " + el.innerText);
			} else {
				setTimeout(() => {
					hide.click();
					
				}, getRandomIntInclusive(1000, 10000));
			
			}
		}
	});


