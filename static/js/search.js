function checkInputSearch() {
    const inputSearch = document.getElementById("inputSearch")
    const inputSearchTrim = inputSearch.value.trim()
    if(inputSearchTrim) {
        if(inputSearchTrim.length > 30) {
            inputSearch.value = inputSearchTrim.slice(0, 30)
        }
        return true
    }

    return false
}


function submitSearchForm() {
    if(checkInputSearch()) {
        document.getElementById("searchForm").submit()
    }
}