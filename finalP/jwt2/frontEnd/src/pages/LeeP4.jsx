import { Link, useParams } from "react-router-dom";

const LeeP4 = () => {
   const student = useParams();

   return (
      <div>
         <h1>P4</h1>
         나이: {student.name}
         이름: {student.age}
         <hr></hr>
         <Link to="/p5.go?name=짜장면&price=6000">p5로(짜장면)</Link>
         <br />
         <Link to="/p5.go?name=짬뽕&price=6500">p5로(짬뽕)</Link>
      </div>
   );
};

export default LeeP4;
