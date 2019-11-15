window.addEventListener('load', getBookData);
document.getElementById('signup').addEventListener('click', createUser);
let httpRequest;

function getBookData() {
    httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
        alert("Couldn't create a request");
        return false;
    }
    httpRequest.onreadystatechange = displayInfo;
    httpRequest.open('GET', 'http://127.0.0.1:8000/book/');
    httpRequest.send();
}

function displayInfo() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        
        if (httpRequest.status === 200) {
            
            let bookData = JSON.parse(httpRequest.responseText)
            let idBookData = document.getElementById('content');
            
            for (let i = 0; i < bookData.length; i++) {
                
                let bookDataObj = bookData[i];

                idBookData.insertAdjacentHTML('beforeend',
                '<div id="content-details-explore">\
                <div class="popup" onclick="myFunction('+"'myPopup"+i+"'"+')">\
                <div id="content-detaials-explore-img" style="background-image:url('+bookDataObj.image+');">\
                </div><br/><b>'+bookDataObj.name+'</b>\
                <div class="popuptext" id="myPopup'+i+'"><div id="content-details-explore-price"><span>\
                $'+bookDataObj.price+'</span><span>4.0</span></div><div id="content-details-explore-heading">\
                <span>'+bookDataObj.short_description+'</span></div><button class="statusButton"\
                 onclick="cartmodal()">Add To Cart</button></div></div></div>'
                );
            }
        } 
        else {
            alert('Error!!!');
        }
    }
}

function createUser(){
    username = document.getElementById('username').value;
    email = document.getElementById('email').value;
    password = document.getElementById('password').value;
    re_password = document.getElementById('re_password').value;
    
    if ( password != re_password){
        alert('Password does not match!!!');
    }

}
