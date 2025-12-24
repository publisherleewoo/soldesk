import { useDispatch } from 'react-redux';
import { changeFunc } from "../leeTxtSlice";

const LeeInput = () => {
  const dis = useDispatch();
  return (
    <div>
        <input onChange={(e)=>{
            console.log(e.target.value);
            dis(changeFunc(e.target.value))
        }}/>
    </div>
  )
}

export default LeeInput