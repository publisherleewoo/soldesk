
const LeeRSFirst = () => {
    const ar = [432, 576, 45324, 312, 543]
    const rsTest = () => {

        //반복문속에서 변수 만드는거 자제
        //그러면 a 메모리가 자꾸 생김
        //그러므로 반복문 밖에서 만들기
        let a;
        for (let i = 0; i < ar.length; i++) {
            a = ar[i]
            alert(a)
        }
    }


    const rsTest2 = () => {
        ar.map((v, i) => alert(v, i) )
        return 0
    }

    return (
        <>
            <button onClick={rsTest}>반복문</button>
            <button onClick={rsTest2}>반복문2</button>
        </>
    )
}

export default LeeRSFirst