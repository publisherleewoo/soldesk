import { Route, Routes } from 'react-router-dom'
import './App.css'
import LeeP1 from './pages/LeeP1'
import LeeP2 from './pages/LeeP2'
import LeeP3 from './pages/LeeP3'
import LeeP4 from './pages/LeeP4'
import LeeP5 from './pages/LeeP5'
import LeeP6 from './pages/LeeP6'
import LeeP7 from './pages/LeeP7'
import Leep8 from './pages/Leep8'
import Leep9 from './pages/Leep9'

function App() {

  return (
    <>
      <Routes>
        <Route path='/' element={<LeeP1/>}/>
        <Route path='/p2.go' element={<LeeP2/>}/>
        <Route path='/p3.go' element={<LeeP3/>}/>
        <Route path='/p4.go/:name/:age' element={<LeeP4/>}/>
        <Route path='/p5.go' element={<LeeP5/>}/>
        <Route path='/p6.go' element={<LeeP6/>}/>
        <Route path='/p7.go' element={<LeeP7/>}/>
        <Route path='/p8.go' element={<Leep8/>}/>
        <Route path='/p9.go' element={<Leep9/>}/>
      </Routes>
    </>
  )
}

export default App
