var swapActive = function( s ){
	$('.components li').each(function(){
		$(this).removeClass('active');
	});

	$('.components li').each(function(){
		let href = $(this).find('a').attr('href');

		if( href == s ){
			$( this ).addClass('active');
			return false;
		}
	});
};

var callAjax = function( o, u, m, f, a = true ){
	let ajax = {};
	ajax.data = o;
	ajax.method = m;
	ajax.url = u;
	ajax.async = a;
	ajax.beforeSend = function(){

	};

	ajax.done = function(){

	};

	ajax.error = function(e, err, error){
		console.log( e, err, error );
	}

	ajax.success = f;

	$.ajax(ajax);
};