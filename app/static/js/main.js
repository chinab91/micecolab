$(document).ready(function() {

	$('label').click(function() {});
	$.ajax({
	  url: "/get_meetings",
	  dataType: "json",
	}).done(function(mm) {
			$.each(mm.date, function( k, a ) {
			  $('#meetinglist').append('<div class="mlfix row c"><div class="col-xs-12"><b>'+a.value+'</b></div></div>');
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
	
	$.ajax({
	  url: "/activity",
	  dataType: "json",
	}).done(function(mm) {
			$.each(mm.activity, function( k, a ) {
				$('#hn'+k+'').prepend('<b>'+a.time+'</b>');
			});
	});
	
	$('#meetingtab').click(function() {
		if ($('#meetinglist').hasClass('inactive') === true) {
		$('#meetingtab1').addClass('glyphicon-minus').removeClass('glyphicon-plus');
			$('#meetinglist').fadeIn(function() {
				$('#meetinglist').removeClass('inactive');
			});
		} else {
		$('#meetingtab1').addClass('glyphicon-plus').removeClass('glyphicon-minus');
		$('#meetinglist').fadeOut(function() {
				$('#meetinglist').addClass('inactive');
			});
		}
	});
	
	$('#searching').keyup(function() {
		var searchid = $(this).val();
			$.ajax({
			  url: "/search/"+searchid+"",
			  dataType: "json",
			}).done(function(mm) {
				
			});
	});
});