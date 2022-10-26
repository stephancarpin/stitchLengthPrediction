console.log('load script');

function loadImage(){
   

    document.getElementById('lime_report').src="/assets/images/lime_report.jpg";

}   


function refreshPage(){
    console.log('clieck');
    document.getElementById("Count").value='';
    document.getElementById("Density").value='';
    document.getElementById("Width").value='';
    document.getElementById("Shade").value='';
    document.getElementById("shrinkage_length").value='';
    document.getElementById("shrinkage_width").value='';
    document.getElementById("Diameter").value='';
    document.getElementById("Gauge").value='';
    document.getElementById("Needles").value='';
    document.getElementById("Feeders").value='';
    document.getElementById("Rpm").value='';

    document.getElementById("basic-url").value='';
    document.getElementById("tightness_factor").value='';
    document.getElementById("LFA").value='';
    document.getElementById("lime_report").src='';
} 
