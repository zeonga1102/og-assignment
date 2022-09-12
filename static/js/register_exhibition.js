function checkForm() {
    const title = document.getElementById("title")
    const titleRe = /.{1,64}$/
    if(!titleRe.test(title.value)) {
        return showAlertAndFocusing(title)
    }

    const startDate = document.getElementById("startDate")
    const dateRe = /^[1|2]\d{3}-\d{2}-\d{2}$/
    if(!dateRe.test(startDate.value)) {
        return showAlertAndFocusing(startDate)
    }
    if(!checkDate(startDate)) {
        return false
    }

    const endDate = document.getElementById("endDate")
    if(!dateRe.test(endDate.value)) {
        return showAlertAndFocusing(endDate)
    }
    if(!checkDate(endDate)) {
        return false
    }

    if(stringToDate(startDate.value) > stringToDate(endDate.value)) {
        alert("종료일은 시작일보다 빠를 수 없습니다!")
        endDate.focus()
        return false
    }

    const query = "input[name='work']:checked"
    const selected = document.querySelectorAll(query)
    if(selected.length < 1) {
        alert("작품을 하나 이상 선택해주세요!")
        return false
    }

    return true
}


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


function submitForm() {
    if(checkForm()) {
        document.getElementById("newExhibitionForm").submit()
    }
}


window.onload = function() {
    const submitBtn = document.getElementById("submitBtn")
    submitBtn.addEventListener("click", submitForm)
}