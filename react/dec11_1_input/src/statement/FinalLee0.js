import React, { useCallback, useState } from 'react'
import './test.css'
const FinalLee0 = () => {
  const [size, setSize] = useState({
    wid: 100,
    hei: 100
  })

  const onChange = useCallback((e) => {
    setSize({
      ...size,
      [e.target.name]: e.target.value*1
    })
  }, [size])

  const tblCSS = { width: size.wid + "px", height: size.hei + "px" }

  return (
    <div>
      <table border='1' style={tblCSS}>
        <thead>
          <tr><td></td><td></td></tr>
        </thead>
        <tbody>
          <tr>
            <td><input value={size.wid} name="wid" onChange={onChange} /></td>
            <td><input value={size.hei} name="hei" onChange={onChange} /></td>
          </tr>
        </tbody>
        <tfoot><tr><td></td><td></td></tr></tfoot>
      </table>
    </div>
  )
}

export default FinalLee0