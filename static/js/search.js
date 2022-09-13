function checkInputSearch() {
    if(document.getElementById("inputSearch").value.trim()) {
        return true
    }

    return false
}


function submitForm() {
    if(checkInputSearch()) {
        document.getElementById("searchForm").submit()
    }
}


window.onload = function() {
    document.getElementById("searchBtn").addEventListener("click", submitForm)
}