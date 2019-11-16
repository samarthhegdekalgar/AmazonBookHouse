window.addEventListener('load', getBookData);
document.getElementById('signup').addEventListener('click', createUser);
document.getElementById('login').addEventListener('click', loginUser);
let httpRequest;
let userName;
let password;

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
                <div class="popup" onclick="myFunction(' + "'myPopup" + i + "'" + ')">\
                <div id="content-detaials-explore-img" style="background-image:url(' + bookDataObj.image + ');">\
                </div><br/><b>' + bookDataObj.name + '</b>\
                <div class="popuptext" id="myPopup' + i + '"><div id="content-details-explore-price"><span>\
                $' + bookDataObj.price + '</span><span>4.0</span></div><div id="content-details-explore-heading">\
                <span>' + bookDataObj.short_description + '</span></div><button class="statusButton"\
                 onclick="cartmodal()">Add To Cart</button></div></div></div>'
                );
            }
        } else {
            alert('Error!!!');
        }
    }
}

function createUser() {
    create_username = document.getElementById('registerusername').value;
    create_email = document.getElementById('registeremail').value;
    create_password = document.getElementById('registerpassword').value;
    create_re_password = document.getElementById('registerre_password').value;

    if (create_password != create_re_password) {
        alert('Password does not match!!!');
        return false;
    }

    httpRequest.onreadystatechange = userCreationAck;
    httpRequest.open('POST', 'http://127.0.0.1:8000/user/create/');
    httpRequest.setRequestHeader("Content-Type", "application/json");

    let body = JSON.stringify({
        name: create_username,
        email: create_email,
        password: create_password,

    });
    httpRequest.send(body);

}

function userCreationAck() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 201 || httpRequest.status === 204) {
            alert('User created! Please login.');
        } else {
            alert('User exist, please log in!!!');
        }
    }
}

function loginUser() {
    userName = document.getElementById('loginemail').value;
    password = document.getElementById('loginpassword').value;

    httpRequest.onreadystatechange = userloginAck;
    httpRequest.open('GET', 'http://127.0.0.1:8000/user/');
    httpRequest.setRequestHeader("Content-Type", "application/json");

    let body = JSON.stringify({
        name: userName,
    });
    httpRequest.send(body);
}

function userloginAck() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {

        if (httpRequest.status === 200) {

            let userData = JSON.parse(httpRequest.responseText)
            for (let i = 0; i < userData.length; i++) {
                let userDataObj = userData[i];
                console.log(userDataObj.name)
            }

            if (userDataObj.name === userName && userDataObj.password === password) {
                alert('Login Successful!');
            } else {
                alert("Username and password doesn't match!")
            }
        } else {
            alert('Error!!!');
        }
    }
}