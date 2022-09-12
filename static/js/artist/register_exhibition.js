function checkForm() {
    const title = document.getElementById("title")
    if(!titleRe.test(title.value)) {
        return showAlertAndFocusing(title)
    }

    const startDate = document.getElementById("startDate")
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


function submitForm() {
    if(checkForm()) {
        document.getElementById("newExhibitionForm").submit()
    }
}


window.onload = function() {
    document.getElementById("submitBtn").addEventListener("click", submitForm)
}