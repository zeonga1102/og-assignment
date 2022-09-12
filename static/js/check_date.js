function stringToDate(strDate) {
    const splits = strDate.split("-")
    for(let i=0; i<3; i++) {
        splits[i] = parseInt(splits[i])
    }

    const month = splits[1]
    const date = splits[2]

    if(month < 1 || month > 12 || date < 1 || date > 31) {
        alert("올바른 날짜를 입력해주세요!")
        return false
    }

    return new Date(splits[0], month-1, date)
}


function checkDate(dateElem) {
    const dateObj = stringToDate(dateElem.value)
    if(!dateObj) {
        dateElem.focus()
        return false
    }

    const now = new Date()
    if(dateObj > now) {
        alert("올바른 날짜를 입력해주세요!")
        dateElem.focus()
        return false
    }

    return true
}