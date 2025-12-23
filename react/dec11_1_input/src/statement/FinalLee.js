import React, { useState } from 'react'
import './test.css'
const FinalLee = () => {
  const [wid, setWid] = useState(100)
  const [hei, setHei] = useState(100)

  const onChangeW = (e) => {
    setWid(e.target.value*1)
  }
  const onchangeH = (e) => {
    setHei(e.target.value*1)
  }

  return (
    <div>
      <table border='1' style={{ width: wid + "px", height: hei + "px" }}>
        <thead>
          <tr><td></td><td></td></tr>
        </thead>
        <tbody>
        <tr>
          <td><input value={wid} onChange={onChangeW} /></td>
          <td><input value={hei} onChange={onchangeH} /></td>
        </tr>
        </tbody>
        <tfoot><tr><td></td><td></td></tr></tfoot>
      </table>
    </div>
  )
}

export default FinalLee