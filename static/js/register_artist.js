function showAlertAndFocusing(elem) {
    alert("형식에 맞게 입력해주세요!")
    elem.focus()
    return false
}


function checkForm() {
    const name = document.getElementById("name")
    const nameRe = /.{1,16}$/
    if(!nameRe.test(name.value)) {
        return showAlertAndFocusing(name)
    }

    const birthday = document.getElementById("birthday")
    const birthdayRe = /^[1|2]\d{3}-\d{2}-\d{2}$/
    if(!birthdayRe.test(birthday.value)) {
        return showAlertAndFocusing(birthday)
    }
    const birthdaySplit = birthday.value.split("-")
    const month = parseInt(birthdaySplit[1])
    const date = parseInt(birthdaySplit[2])
    if(month <=0 || month > 12 || date <= 0 || date > 31) {
        alert("올바른 날짜를 입력해주세요!")
        birthday.focus()
        return false
    }
    const birthdayDate = new Date(parseInt(birthdaySplit[0]), month-1, date)
    const now = new Date()
    if(birthdayDate > now) {
        alert("올바른 날짜를 입력해주세요!")
        birthday.focus()
        return false
    }

    const email = document.getElementById("email")
    const emailRe = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/
    if(!emailRe.test(email.value)) {
        return showAlertAndFocusing(email)
    }

    const phone = document.getElementById("phone")
    const phoneRe = /^010-\d{4}-\d{4}$/
    if(!phoneRe.test(phone.value)) {
        return showAlertAndFocusing(phone)
    }

    return true
}


function submitForm() {
    if(checkForm()) {
        document.getElementById("newArtistForm").submit()
    }
}


window.onload = function() {
    const submitBtn = document.getElementById("submitBtn")
    submitBtn.addEventListener("click", submitForm)
}