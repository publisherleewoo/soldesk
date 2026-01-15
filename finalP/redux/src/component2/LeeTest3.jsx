import { useSelector } from 'react-redux';

const LeeTest3 = () => {
  const istate = useSelector((store)=>store.tss);
  
  return (
    <h2>{istate.val}</h2>
  )
}

export default LeeTest3