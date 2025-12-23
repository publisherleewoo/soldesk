import { useState } from 'react'

const LeeRSFourth = () => {
    const [numbers] = useState([123, 65, 4, 12, 43, 44])
    const liNum = numbers.map((n, i) => <li key={i}>{n}</li>)
    const numA = numbers.filter(n => n % 2 === 0);
    const numB = numA.sort((a, b) => { return a - b })
    const liNum2 = numB.map((n, i) => <li key={i}>{n}</li>)

    // numbers.sort((n1, n2) => {
    //     if (n1 > n2) {
    //         return -1;   //앞의 값이 더 클때 1 : 오름차순 
    //                      //앞의 값이 더 클때 -1 : 내림차순
    //     }
    //     return 1
    // })

    return (
        <ul>
            {liNum}
            <br />
            {liNum2}

        </ul>
    )
}

export default LeeRSFourth