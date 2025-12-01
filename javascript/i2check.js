function i2check() {

    var idField = document.i2joinForm.id;
    var pwField = document.i2joinForm.pw;
    var pwchkField = document.i2joinForm.pwChk;
    var ageField = document.i2joinForm.age;
    var photoField = document.i2joinForm.photo;

    if (isEmpty(idField) || lessThan(idField, 4) || containsHangul(idField)) {
        alert("ID?")
        idField.value = "";
        idField.focus();
        return false;
    }


    if (isEmpty(pwField) || lessThan(pwField, 5) || notEqual(pwField, pwChkField) || notContains(pwField, "1234567890") || notContains(pwField, "soldesk")) {
        alert("PW?")
        pwField.value = "";
        pwchkField.value = "";
        pwField.focus();
        return false;
    }


    if (isEmpty(ageField) || isNaN(ageField.value)) {
        alert('나이')
        ageField.value = "";
        ageField.focus();
        return false;
    }


    if (isEmpty(ageField || isNotNum(ageField))) {
        alert("나이?");
        ageField.value = "";
        ageField.focus();
        return false;
    }

    if (isEmpty(photoField || isNotType(photoField,"png"))) {
        alert("프사?");
        return false;
    }





    return true
}