
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
	
	$('#searching').keyup(function(e) {
			
		var searchid = $(this).val();
		if (searchid === "") {
			$("#content").animate({ scrollTop: 0 }, "slow");
		} else {
			$.ajax({
			  url: "/search/"+searchid+"",
			  dataType: "json",
			}).done(function(mm) {
				 $("#content").animate({ scrollTop: 2000 }, "slow");
				$.each(mm.search, function( k, b ) {
					$('#st'+k+'').text(''+b.companyname+'');
					$('#sp'+k+'').empty().append('<div class="row"><h4 class="col-xs-12">'+b.companyname+'</h4></div><div class="row"><p class="col-xs-12">'+b.companyinfo+'<br/>Contact Person: '+b.fullname+', '+b.position+'</p></div><div id="sn'+k+'" class="row" style="height:200px;"><div class="col-xs-12"><img src="static/img/unnamed.png" style="width:200%;"></div></div>');
					//$('#sn'+k+'').kinetic();
				});
			});
		};
	});
	
	$('td').click(function() {
		$('#searching').val(''+$(this).find('span').text()+'').keyup();
	});
	
	$('form').submit(function(event){                                    
               ws.send($('#data').val()) 
			   $('#chatlog').append('<div class="row"><div class="col-xs-3"></div><div style="padding:10px;margin-bottom:5px;background-color:grey;color:white;" class="col-xs-9"><i>You says..</i><br/>'+$('#data').val()+'</div></div>');
               return false;                                                    
           });                                                                  
           if ("WebSocket" in window) {           
           console.log(document.domain)                                
               ws = new WebSocket("ws://" + document.domain + ":8000/api");  

               ws.onmessage = function (msg) {                                  
                   $("#chatlog").append('<div class="row"><div style="padding:10px;margin-bottom:5px;background-color:orange;color:white;" class="col-xs-9"><i>Araine says..</i><br/>'+msg.data+'</div></div>')                      
               };                                                               
           } else {                                                             
               alert("WebSocket not supported");                                
           }                    
	
});