function showAlertAndFocusing(elem) {
    alert("형식에 맞게 입력해주세요!")
    elem.focus()
}


function checkForm() {
    const name = document.getElementById("name")
    if(!name.value) {
        alert("이름을 입력해주세요!")
        name.focus()
        return false
    }
    if(name.value.length > 16) {
        alert("이름은 16글자 이하로 입력해주세요!")
        name.focus()
        return false
    }

    const birthday = document.getElementById("birthday")
    if(!birthday.value) {
        alert("생년월일을 입력해주세요!")
        birthday.focus()
        return false
    }
    const birthdayRe = /^[1|2]\d{3}-\d{2}-\d{2}$/
    if(!birthdayRe.test(birthday.value)) {
        showAlertAndFocusing(birthday)
        return false
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
    if(!email.value) {
        alert("이메일을 입력해주세요!")
        email.focus()
        return false
    }
    const emailRe = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/
    if(!emailRe.test(email.value)) {
        showAlertAndFocusing(email)
        return false
    }

    const phone = document.getElementById("phone")
    if(!phone.value) {
        alert("연락처를 입력해주세요!")
        phone.focus()
        return false
    }
    const phoneRe = /^010-\d{4}-\d{4}$/
    if(!phoneRe.test(phone.value)) {
        showAlertAndFocusing(phone)
        return false
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