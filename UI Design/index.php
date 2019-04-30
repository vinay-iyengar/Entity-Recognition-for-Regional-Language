<?php
              
if(isset($_POST['textdata']))
{
$data=$_POST['textdata'];
$message = "Inserted Sucessfully";
$fp = fopen('./data/kannada_testing.txt', 'w');
fwrite($fp, $data);
fclose($fp);
// echo "<script type='text/javascript'>alert('$message');</script>";
}
if(isset($_POST['text']))
{
$dat=$_POST['text'];
$msg = "Thank you for the feedback";
$fp = fopen('./data/kannada_user.txt', 'a');
fwrite($fp, $dat);
// echo "<script type='text/javascript'>alert('$msg');</script>";
fclose($fp);

}
?>
<!DOCTYPE html>
<html>
    <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Entity Recognition</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
           
            <style>
            body {font-family: Arial, Helvetica, sans-serif;}
            
            
            input[type=text]{
                width: 600px;
                padding: 12px 20px;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid black;
                border-radius: 15px;
            }
            
            button {
                background-color:green;
                color: white;
                padding: 14px 20px;
                margin: 8px 5px;
                border: none;
                cursor: pointer;
                width: 100px;
                border-radius: 15px;
                font-family: 'Courier New', Courier, monospace;
                font-weight: bold;
                font-size: 15px;
            }
            
            button:hover {
                /* opacity: 0.5; */
                
                background-color: #4d9209;
                /* text-decoration: underline; */
            }
            .container-fluid-a   
                {
                  background-color:#336600;
                  color:white;
                  width:300px;
                  border-radius:30px;
                } 
            
                label
                {
                    color:#330066;
                    font-size: 20px;
                    text-allign:center
                }
                body
                {
                    margin: 0;
                    padding: 0;
                    background: url("Evening Night.jpg");
                    background-size:cover;
                    font-family: sans-serif;
                    
                }
              
            
/* ---- reset ---- */ 
body{ margin:0; font:normal 150% Arial, Helvetica, sans-serif; } 
canvas{ display: block; vertical-align: bottom; } 


/* ---- particles.js container ---- */ 
#particles-js{ 
    position:absolute; 
    width: 100%;
    /* background-color: #2aaee2;  */
    background-image: linear-gradient(to top, #ff0844 0%, #ffb199 100%);                                                 red-pink
    /* background-image: linear-gradient( rgba(0,212,231,1) 11.2%, rgba(68,139,222,1) 91.1% );                              blue */
    /* background-image: linear-gradient( 109.6deg,  rgba(84,13,110,1) 11.2%, rgba(238,66,102,1) 100.2% );                  purple-pink */
    /* background-image: linear-gradient( 109.6deg,  rgba(0,212,231,1) 11.2%, rgba(68,139,222,1) 91.1% );                  lightblue-dark bule */
    /* background-image: url("");  */
    background-repeat:no-repeat; 
    background-size: cover; 
    background-position: center; 
    } 
element.style {
    width: 80px;
    height: 48px;
    display: none;
}

#stats{ border-radius: 3px 3px 0 0; overflow: hidden; } 

</style>
    </head>
    <body>
        
            <!-- particles.js container --> 
            <div id="particles-js" >
                    <center>
                    <h1 style= "text-align: center; color:white; margin-top:50px;font-family: 'Courier New', Courier, monospace;font-style: italic;font-weight: bold">Entity Recognition for Kannada Language</h1>
                      <br>
                    <h2 style="text-allign:center; color:rgb(0, 0, 0);font-family: 'Courier New', Courier, monospace;font-weight: bold">Input Data</h2>
                      <form method = post>
                        
                        <input type="text" placeholder="Enter the Input Data" name="textdata" id="textdata" style="font-weight:bold;font-size:12px;font-family: 'Courier New', Courier, monospace">
                           <br> <br>
                        <button type="submit" id="row" >Submit</button><br>
                        <!-- <button type="submit" id="row" onClick="row1visible()">Result</button> -->
                        
                        <?php
                        $command = escapeshellcmd('C:/wamp64/www/Entity Recognition/entity.py');
                        $output = shell_exec($command);
                        
                    ?> 
                    <br>
                    <br>
                    
                    <!-- <div class = "container" id="row1" style="visibility:hidden;"> -->
                    <h2 style="text-allign:center;color:rgb(0, 0, 0);font-family: 'Courier New', Courier, monospace;font-weight: bold;">Output Tags</h2><br>
                    <!-- <label>Your input: </label>
                         <span id="display"></span> -->
                    <div class = "container-fluid-a">
                        
                    
                    
                    
                    <?php
                    $file = "./output/kannada_tags.txt";
                    $f = fopen($file, "r") or exit("Unable to open file!");
                    // read file line by line until the end of file (feof)
                    while(!feof($f))
                    {
                      echo fgets($f)."<br />";
                    }
                    ftruncate($f,0);
                    fclose($f);
                    ?> 
                    </div> 
                    <br>
                    <h3 style="text-allign:center; color:black;font-family: 'Courier New', Courier, monospace;font-weight: bold">Please give the feedback below with the right tag if there is any wrong tag</h2>
                      <form method = post>
                        
                        <input type="text" placeholder="Enter the Input with correct tag" name="text" id="text" style="font-weight:bold;font-size:12px;font-family: 'Courier New', Courier, monospace"><br>
                        <button type="submit" onClick="myFunction()">Update</button><br>
                    
                    </center>
                    </div>
                      
                      <!-- particles.js lib - https://github.com/VincentGarreau/particles.js --> 
                      
                      <script src="http://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>  
                      <!-- stats.js lib --> 
                      <script src="http://threejs.org/examples/js/libs/stats.min.js"></script>
                      <script src="project.js"></script>

    <script>
    function myFunction() {
      //  var x = document.getElementById("textdata").value;
      //  document.getElementById("display").innerHTML = x;
      alert("Thank you for the feedback")       

      
    }
  </script>             
            
        
    </body>
</html>