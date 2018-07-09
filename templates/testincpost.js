function testSnow()
{
//var requestBody = "{\"assignment_group\":\"Service Desk\",\"short_description\":\"Test inc 4\"}"; 

var incgroup = document.getElementById("group").value;
var inctitle = document.getElementById("title").value;

var requestBody = "{\"assignment_group\":\"" + incgroup + ",\"short_description\":\"" + inctitle + "\"}"; 

var client=new XMLHttpRequest();
client.open("post","https://dev47165.service-now.com/api/now/table/incident");

client.setRequestHeader('Accept','application/json');
client.setRequestHeader('Content-Type','application/json');

//Eg. UserName="admin", Password="admin" for this code sample.
client.setRequestHeader('Authorization', 'Basic '+btoa('admin'+':'+'Lab@12345'));

client.onreadystatechange = function() { 
	if(this.readyState == this.DONE) {

		//document.getElementById("response").innerHTML=this.status + this.response;
                var res=this.response;
                parsedData = JSON.parse(res);
                alert("You have Successfully created incident : " + parsedData.result.number); 
	}
}; 
client.send(requestBody);

}
