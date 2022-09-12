function checkForm() {
    const name = document.getElementById("name")
    if(!nameRe.test(name.value)) {
        return showAlertAndFocusing(name)
    }

    const birthday = document.getElementById("birthday")
    if(!dateRe.test(birthday.value)) {
        return showAlertAndFocusing(birthday)
    }
    if(!checkDate(birthday)) {
        return false
    }

    const email = document.getElementById("email")
    if(!emailRe.test(email.value)) {
        return showAlertAndFocusing(email)
    }

    const phone = document.getElementById("phone")
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