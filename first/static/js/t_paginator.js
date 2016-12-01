function getj(arg)
{	
	if (arg<0) arg=0;
	var s='http://127.0.0.1:8000/tournaments_json+from'+arg + '/';
	$.ajax({

	  url: s ,
	  dataType : "json", 
	  success: function(data) {
	  	var my_out="<h3 align='center'>Турниры</h3><br><table cellspacing='10' width='30%'><tr><th>Id</th><th>Название</th><th>Платформа</th>"

	  	for ( i in data)
	  	{
	  		st=data[i]
	  		
	  		my_out+="<tr>"
	  		for ( j in st)
	  		{
	  			my_out+="<td height='10'>"+st[j]+"</td>"
	  		}

	  		my_out+="</tr>"
	  	}
	  	my_out+="</table>"
	    $("div.scr").html(my_out)
	    
	  }

	});

cur=arg;
}
var cur=0;
getj(cur);
