var htm = ''

function Pendingusers(n) 
{
  i=0;
htm = `

<div class="container-fluid" style="max-width:600px;">
<table class="table" style="background-color:white;margin-top:120px;"align="center">
  <thead class="thead-dark">
    <tr align="center">
      <th scope="col" style="font-weight: bolder;">Username</th>
      <th scope="col" style="font-weight: bolder;">City</th>
      <th scope="col" style="font-weight: bolder;">View</th>
    </tr>
  </thead>
  <tbody>`

  for(i=0;i<n;i++) {
    htm = htm + 
   `<tr align="center">
      <th scope="row">Username</th>
      <th>Kottayam</th>
      <td><button class = "btn" name="user${i}" onclick="enlarge(${i});" style="background-color:#2dc997">view More</button></td>
    </tr>
    <tr id = "null${i}" style="display:none;">
    <th colspan="3">
    <div>Time:00.00.00</div>
    <div>Date:22/22/11</div>
    <div>file:<input type="file"/>
    <div><button class = "btn">Upload</button>&nbsp;<button name="reject${i}"class = "btn" onclick="Reject(${i});">Reject</button></div>
    <div id = "reject${i}"> </div>
    </th>
    </tr>`
    }
    htm = htm +
  `</tbody>
</table>
</div>
`

document.getElementById("pending").innerHTML = htm;

}


function enlarge(i)
{
    document.getElementById("null"+i).style.display = 'block'

}



function Reject(i)
{

var t =''
t = 
`
<div class="form-group">
			<input type="text" name="query${i}" placeholder="Enter Your response" class="form-control" value="" pattern="([a-zA-Z]*)" title="It contains alphabets only"  required />
      <input type = "submit" name="reject${i}" class="btn btn-primary"/>
</div>
      `  
document.getElementById("reject"+i).innerHTML = t;
}


function Liverecording()
{


}


function Editprofile()
{


}

function Updatepassword()
{
htm = 
`

<style>
    
  input::placeholder {
  color:black;
}

  </style>

<div class="container-fluid" style="margin-top: 100px; margin-bottom: 100px;padding: 2%; border-style: solid;
border-color:#2dc997; border-radius: 7%; max-width: 650px;background-color: aliceblue;">
  <h2 style="text-align: center;font-weight: bold;"id ="login">UPDATE PASSWORD </h2>
 <center>
  
  <div class="container"> 
    <form action="" id ="update" method ="POST">
    <div class="col-xs-12 col-sm-6 col-md-9"> 
    <br>
    <div class="form-group">
        <input class="form-control" style="color: black;" type="password" placeholder="Enter the current Password" id ="psw1" name="psw1"  pattern="[0-9a-zA-Z].{8,}" maxlength="12" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required >
    </div>

    <div class="form-group">
        <input class="form-control" style="color: black;" type="password" placeholder="Enter the new Password" id ="psw2" name="psw2"  pattern="[0-9a-zA-Z].{8,}" maxlength="12" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required >
    </div>
    <div class="form-group">
        <input class="form-control" style="color: black;" type="password" placeholder="Re-type the new Password" id ="psw3" name="psw3  pattern="[0-9a-zA-Z].{8,}" maxlength="12" title="It includes  numbers , uppercase,lowercase letter, and at least 8 or more characters required (Max length:12)" required >
    </div>

    <button class="btn btn-primary" type="submit" id="updatepassword" style="background-color:#2dc997;" >Update</button><br>
    <br>
  </div>
</form>
</div>
</center> 
 </div>


`
document.getElementById("updatepassword").innerHTML = htm;
}