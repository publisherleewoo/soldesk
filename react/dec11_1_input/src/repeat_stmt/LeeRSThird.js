import { useState } from "react"

const LeeRSThird = () => {
    const [snacks] = useState([
        { name: "초코파이", price: 3500, color: "red" },
        { name: "새우깡", price: 1500, color: "blue" },
        { name: "포카칩", price: 2500, color: "green" },
        { name: "오징어땅콩", price: 2200, color: "orange" },
    ])

    const snackTrs = snacks.map((s, i) => {
        return (
            <tr key={s.name} style={{ color: s.color }}>
                <td>{s.name}</td>
                <td>{s.price}</td>
            </tr>)
    })

    return (
        <table border={1}>
            <thead>
                <tr>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
            </thead>
            <tbody>
                {snackTrs}
            </tbody>
        </table>
    )
}

export default LeeRSThird