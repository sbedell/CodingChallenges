function check( x ) {
	var foo = 5 + 6 * 7;
	document.getElementById("test").innerHTML = foo;
	
    var bar = foo % 8;
	document.getElementById("test2").innerHTML = bar;
	
    var moo = bar * 2;
	document.getElementById("test3").innerHTML = moo;
	
    var rar = moo / 3;
	document.getElementById("test4").innerHTML = rar;

    if (x.length == moo) {
		alert("win!");
		window.location += "?lvl_password=" + x;
	} else {
		alert("fail D:");
	}
}
