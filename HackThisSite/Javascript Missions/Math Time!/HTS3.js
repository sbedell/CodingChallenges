function check(x) {
	let foo = 5 + 6 * 7;
	document.getElementById("test").innerText = foo;

    let bar = foo % 8;
	document.getElementById("test2").innerText = bar;

    let moo = bar * 2;
	document.getElementById("test3").innerText = moo;

    let rar = moo / 3;
	document.getElementById("test4").innerText = rar;

    if (x.length == moo) {
		alert("win!");
		alert("?lvl_password=" + x);
	} else {
		alert("fail D:");
	}
}
