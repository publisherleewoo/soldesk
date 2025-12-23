
// ES7+ React/Redux/React-Native snippets
import React from 'react'
import PropTypes from 'prop-types'
//shift alt + O



// rafcp
function LeePropsThird(props) {
  return (
    <div>
        품명:{props.name}<br/>
        가격:{props.price}
    </div>
  )
}


//pt 시리즈
LeePropsThird.propTypes = {
    name:PropTypes.string.isRequired,
    price:PropTypes.number
}

export default LeePropsThird
