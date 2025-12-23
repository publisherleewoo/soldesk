// export 변수명 -> 여러개 export
//      import {변수명,...} from "경로";
// export default 변수명 -> 변수명만 export
//      import 변수명 from "경로";

// 빈글자면 true, 뭐라고 적혀있으면 false
export const isEmpaty = value => value.trim() === "";

export const lessThan = (input, len) => input.value.length < len;

export const containHangul = (input) => {
    var okSet = "qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM123456789@.-_"
    for (var i = 0; i < input.value.length; i++) {
        if (okSet.indexOf(input.value[i]) == -1) {
            return true
        }
    }
    return false
}

export const notEqual = (input1, input2) => input1.value != input2.value;

export const notContains = (input, set) => {
    for (var i = 0; i < set.length; i++) {
        if (input.value.indexOf(set[i]) != -1) {
            return false
        }
    }
    return true
}

export const isNotNum = (value) => { isNaN(value) || (value.indexOf("") != -1) }

export const isNotType = (file, type) => {
    type = '.' + type
    return file.name.toLowerCase().indexOf(type) == -1;
} 