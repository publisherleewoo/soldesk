import { useState } from 'react';
export const Clicker = () => {

    const [num, setNum] = useState(0)

    const clickFnc = (e) => {
       
        setNum(num+1)
    }

    return (
        <>
           <button onClick={clickFnc}>{num}</button>
        </>
    )
}
