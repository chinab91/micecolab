$(document).ready(function() {

	$('label').click(function() {});
	$.ajax({
	  url: "/get_meetings",
	  dataType: "json",
	}).done(function(mm) {
			$.each(mm.date, function( k, a ) {
			  $('#meetinglist').append('<div class="mlfix row c"><div class="col-xs-12"><h4>'+a.value+'</h4></div></div>');
				$.each(a.meetings, function( k, b ) {
					if (b.cell_status === 0) {
					var aa=0.5;
					} else {
					var aa=1;
					};
					$('#meetinglist').append('<div class="mlfix row" style="opacity:'+aa+';"><div class="col-xs-2 f13 c">'+b.time+'</div><div class="col-xs-7"><p class="f13 meetm">'+b.name+'</p><p>'+b.position+' from '+b.company+'</p></div><div class="col-xs-3 f13 c">'+b.location+'</div></div>');
				});
			});
	});
	
	$('#meetingtab').click(function() {
		if ($('#meetinglist').hasClass('inactive') === true) {
			$('#meetinglist').fadeIn(function() {
				$('#meetinglist').removeClass('inactive');
			});
		} else {
		$('#meetinglist').fadeOut(function() {
				$('#meetinglist').addClass('inactive');
			});
		}
	});
});