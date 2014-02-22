$(document).ready(function() {

	$('label').click(function() {});
	$.ajax({
	  url: "/get_meetings",
	  dataType: "json",
	}).done(function(mm) {
		else {
			$.each(mm.date, function( k, a ) {
			  $('#panlm').append('<div class="mlfix row"><div class="col-xs-11"><p class="f13 meetm">'+a.value+'</p></div></div>');
				$.each(a.meetings, function( k, b ) {
					$('#panlm').append('<div class="mlfix row"><div class="col-xs-2 f13 c">'+b.time+'</div><div class="col-xs-6"><p class="f13 meetm">'+b.name+'</p><p>'+b.position+' from '+b.company+'</p></div><div class="col-xs-3 f13 c">'+b.location+'</div></div>');
				});
			});
		});
});