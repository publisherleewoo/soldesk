function isEmpty(input) {
    return !input.value
}

function lessThan(input, len) {
    return input.value.length < len;
}

function containsHangul(input) {
    var okeSet = "qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM123456789@.-_"
    for (var i = 0; i < input.value.length; i++) {
        if (okeSet.indexOf(input.value[i]) == -1) {
            return true
        }
    }
    return false
}

function notEqual(input1, input2) {
    return input1.value != input2.value;
}

function notContains(input, set) {
    for (var i = 0; i < set.length; i++) {
        if (input.value.indexOf(set[i]) != -1) {
            return false
        }
    }
    return true
}


function isNotNum(input) {
    return isNaN(input.value) || (input.value.indexOf(" ") != -1)
}

function isNotType(input, type) {
    type = "." + type
    return input.value.toLowerCase().indexOf(type) == -1;
}