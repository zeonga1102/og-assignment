function getSelectedArtists() {
    const query = "input[name='artist']:checked"
    const selected = document.querySelectorAll(query)
    if(selected.length < 1) {
        alert("아무것도 선택되지 않았습니다!")
        return false
    }

    let selectedValueList = []
    selected.forEach((elem) => {
        selectedValueList.push(elem.value)
    })

    return selectedValueList
}


async function putArtistStatus(e) {
    const selectedArtists = getSelectedArtists()
    if(!selectedArtists) {
        return
    }

    const csrftoken = getCookie("csrftoken")
    const response = await fetch (`/manager/register-list/${e.target.value}`, {
        headers: { "X-CSRFToken": csrftoken,
                   "Content-Type": "application/json" },
        method: "PUT",
        body: JSON.stringify({ "selectedArtists": selectedArtists })
    })

    if(response.status == 200) {
        window.location.reload()
    }
}


window.onload = function() {
    document.getElementById("approvalBtn").addEventListener("click", (e) => { putArtistStatus(e) })
    document.getElementById("rejectBtn").addEventListener("click", (e) => { putArtistStatus(e) })
}