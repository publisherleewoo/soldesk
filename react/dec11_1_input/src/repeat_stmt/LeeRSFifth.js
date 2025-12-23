import { useState } from 'react'

const LeeRSFifth = () => {
    const [snacks] = useState([
        { "name": "초코파이", "price": 3500, "color": "red" },
        { "name": "새우깡", "price": 1500, "color": "blue" },
        { "name": "포카칩", "price": 2500, "color": "green" },
        { "name": "오징어땅콩", "price": 2200, "color": "orange" },
        { "name": "꼬깔콘", "price": 1700, "color": "yellow" },
        { "name": "홈런볼", "price": 3000, "color": "brown" },
        { "name": "빼빼로", "price": 1200, "color": "pink" },
        { "name": "맛동산", "price": 2800, "color": "darkbrown" },
        { "name": "카스타드", "price": 4000, "color": "lightyellow" },
        { "name": "프링글스", "price": 3800, "color": "black" }
    ])

    const filteredSnacks = snacks.filter(s => s.price >= 2000)
    const snackLi = filteredSnacks.map((s, i) => { return <li key={i}>{s.name}</li> })

    const sortedSnakcs = snacks.sort((a, b) => {
        if (a.name > b.name) {
            return 1
        }
        return -1
    }
    )

    console.log(sortedSnakcs);
    const sortedSnackLi = sortedSnakcs.map((s, i) => { return <li key={i}>{s.name}</li> })


    return (
        <ul>
            {snackLi}
            <hr></hr>
            {sortedSnackLi}
        </ul>
    )
}

export default LeeRSFifth