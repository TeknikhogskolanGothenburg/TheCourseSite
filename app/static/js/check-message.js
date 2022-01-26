setInterval(checkMsg, 10000);

function checkMsg() {
     const xhttp = new XMLHttpRequest();
        xhttp.open('GET', "http://127.0.0.1:5000/ajax/check_msg", true);
        xhttp.setRequestHeader('Content-type', 'application/json');
        xhttp.send();
        xhttp.onload = function () {
            let respObj = JSON.parse(this.responseText)
            let msgSymbol = document.getElementById("message-symbol");
            let msgCount = document.getElementById("message-count");
            if(respObj.unread_msg_count > 0) {
                msgSymbol.classList.remove("no-new-msg");
                msgSymbol.classList.add("new-msg");
                msgSymbol.classList.remove("fa-envelope-open");
                msgSymbol.classList.add("fa-envelope");
                msgCount.innerHTML = respObj.unread_msg_count;
            }
            else {
                msgSymbol.classList.remove("new-msg");
                msgSymbol.classList.add("no-new-msg");
                msgSymbol.classList.remove("fa-envelope");
                msgSymbol.classList.add("fa-envelope-open");
                msgCount.innerHTML = "";
            }
        }
}