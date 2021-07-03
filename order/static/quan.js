var sell_price;
var amount;

function init () {
	sell_price = document.form.sell_price.value;
	amount = document.form.amount.value;
	document.form.sum.value = sell_price;
	change();
}

function add () {
	quan = document.form.amount;
	sum = document.form.sum;
	quan.value ++ ;

	sum.value = parseInt(quan.value) * sell_price;
}

function del () {
	quan = document.form.amount;
	sum = document.form.sum;
		if (quan.value > 1) {
			quan.value -- ;
			sum.value = parseInt(quan.value) * sell_price;
		}
}

function change () {
	quan = document.form.amount;
	sum = document.form.sum;

		if (quan.value < 0) {
			quan.value = 0;
		}
	sum.value = parseInt(quan.value) * sell_price;
}  