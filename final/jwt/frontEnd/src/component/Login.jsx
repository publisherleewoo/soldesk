import axios from "axios";
import React, { useState } from "react";

const Login = () => {
   const [student, setStudent] = useState({
      name: "",
      age: "",
   });

   //    const [leeJWT, setLeeJWT] = useState("")
   const onChangeFunc = (e) => {
      setStudent({ ...student, [e.target.name]: e.target.value });
   };
   const clickBtn = () => {
      const { name, age } = student;
      axios
         .get(`http://localhost:9999/student.reg?name=${name}&age=${age}`)
         .then((res) => {
            // setLeeJWT(res.data.leeJWT)  리덕스같은 전역으로 실행가능할듯
            sessionStorage.setItem("myJWT", res.data.leeJWT);
            setStudent({ name: "", age: "" });
            alert("만들었음");
         })
         .catch((err) => {
            alert(err);
         });
   };

   //서버에서
   // result = {
   //         "name": name,
   //         "age": age,
   //         "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
   //     }  # 마음대로 (exp=시간제한)

   const showStudent = () => {
      alert(sessionStorage.getItem("myJWT")); //서버에서 exp처리했다고, 시간제한 지나면 없어지는것이 아니고, 복호화가 불가능하게됨
   };

   const showStudent2 = () => {
      axios
         .get(
            `http://localhost:9999/student2.reg?jwt=${sessionStorage.getItem(
               "myJWT"
            )}`
         )
         .then((res) => console.log(res.data))
         .catch((err) => alert(err));
   };

   const updateJWT = () => {
     axios
         .get(
            `http://localhost:9999/student.jwt.update?jwt=${sessionStorage.getItem(
               "myJWT"
            )}`
         )
         .then((res) =>{
            console.log(res.data);
            sessionStorage.setItem('myJWT',res.data)
         })
         .catch((err) => alert(err));
   };
   const deleteJWT = () => {
    sessionStorage.removeItem('myJWT')
   };

   return (
      <div>
         <input
            type="text"
            onChange={onChangeFunc}
            name="name"
            value={student.name}
         ></input>
         <br />
         <input
            type="text"
            onChange={onChangeFunc}
            name="age"
            value={student.age}
         ></input>
         <br />
         <button onClick={clickBtn}>JWT만들기</button>
         <button onClick={showStudent}>JWT확인하기</button>
         <button onClick={showStudent2}>JWT복화로풀기</button>
         <button onClick={updateJWT}>JWT갱신하기</button>
         <button onClick={deleteJWT}>JWT삭제하기</button>
      </div>
   );
};

export default Login;
