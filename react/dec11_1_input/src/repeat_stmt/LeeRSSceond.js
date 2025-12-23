import { useState } from "react"

const LeeRSSceond = () => {
    const [ar] = useState([432, 576, 45324, 312, 543])

    let h2s= ar.map((a, i) => {
        return <h2 key={i}>{a}</h2>
    })

    return (
        <div>{h2s}</div>
    )
}

export default LeeRSSceond