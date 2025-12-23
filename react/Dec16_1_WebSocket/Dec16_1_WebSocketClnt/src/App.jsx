// import { useState } from 'react'
import './App.css'

// import LeeWSClnt from './components/leeWSClnt'
// import LeeStateTest from './components/LeeStateTest'
// import Drawing from './components/Drawing'
// import Dec16_4_Design from './components/Dec16_4_Design'
// import Dec16_4_Design from './components/Dec16_4_Design'
import LeeDesignFirst from './ldf/LeeDesignFirst'
import LeeDesignSecond from './lds/LeeDesignSecond'
import LeeDesignThird from './ldt/LeeDesignThird'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>
      {/* <LeeWSClnt></LeeWSClnt> */}
      {/* <LeeStateTest></LeeStateTest> */}
      {/* <Drawing></Drawing> */}
      {/* <Dec16_4_Design></Dec16_4_Design>
       */}
       <LeeDesignFirst></LeeDesignFirst>
       <LeeDesignSecond></LeeDesignSecond>
       <LeeDesignThird></LeeDesignThird>
    </>
  )
}

export default App
