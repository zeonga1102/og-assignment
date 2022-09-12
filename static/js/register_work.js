function checkForm() {
    const title = document.getElementById("title")
    const titleRe = /.{1,64}$/
    if(!titleRe.test(title.value)) {
        return showAlertAndFocusing(title)
    }

    const price = document.getElementById("price")
    const priceRe = /^\d{1,}$/
    if(!priceRe.test(price.value.replace(/\,/g, ""))) {
        return showAlertAndFocusing(price)
    }

    const size = document.getElementById("size")
    const sizeRe = /^\d{1,3}$/
    if(!sizeRe.test(size.value)) {
        console.log('sd')
        return showAlertAndFocusing(size)
    }
    if(parseInt(size.value) < 1 || parseInt(size.value) > 500) {
        console.log('sss')
        return showAlertAndFocusing(size)
    }

    return true
}


function submitForm() {
    if(checkForm()) {
        document.getElementById("newWorkForm").submit()
    }
}


function addComma(e) {
    e.target.value = e.target.value.replace(/[^0-9]/g, "")
    if(e.target.value) {
        e.target.value = parseInt(e.target.value.replace(/\,/g, "")).toLocaleString()
    }
}


function checkSize(e) {
    if(e.target.value < 1) {
        e.target.value = 1
        return
    }

    if(e.target.value > 500) {
        e.target.value = 500
        return
    }
}


window.onload = function() {
    const submitBtn = document.getElementById("submitBtn")
    submitBtn.addEventListener("click", submitForm)

    document.getElementById("price").addEventListener("keyup", (e) => { addComma(e) })
    document.getElementById("size").addEventListener("input", (e) => { checkSize(e) })
}