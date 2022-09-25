window.onload = function() {
    const prev = document.getElementById("prev")
    const next = document.getElementById("next")

    const search_splits_keyword = window.location.search.split("&keyword=")
    const filter = search_splits_keyword[0].split("filter=")[1]
    const keyword = search_splits_keyword[1]

    if(prev) {
        prev.setAttribute("href", prev.getAttribute("href") + `&filter=${filter}&keyword=${keyword}`)
    }

    if(next) {
        next.setAttribute("href", next.getAttribute("href") + `&filter=${filter}&keyword=${keyword}`)
    }
}