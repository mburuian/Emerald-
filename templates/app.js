const SD = document.getElementById('sidebar')

function toggleNavbar(){
    if(SD.style.display === 'none'|| SD.style.display === ''){
        SD.style.display = 'flex'
    }
    else{
        SD.style.display = 'none'
    }
}


