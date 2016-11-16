	alert("ZZZ")
	$.ajax({
2	
	  url: 'response.php?action=sample1',
3
	  success: function(data) {
4
	    $('.results').html(data);
5
	  }
6
	});