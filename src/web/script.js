function startLoad(message) {
    var loaderMessage = message
    if (message == undefined) {
        loaderMessage = "불러오는 중"
    }

    document.getElementById("loader-message").innerText = loaderMessage
    $("#loader").fadeIn()
}

function endLoad() {
    $("#loader").fadeOut()
}