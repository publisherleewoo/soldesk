
const LeeCssSecond = (props) => {
  const c = props.c
  const bgc = props.bgc
  const w = props.w
  const h = props.h
  const children = props.children
  const tblCSS ={ color: c, backgroundColor: bgc, width: w + 'px', height: h + 'px' }

  return (
    <table border='1' style={tblCSS}>
      <tbody>
      <tr>
        <td>{children}</td>
      </tr>
      </tbody>
    </table>
  )
}

export default LeeCssSecond