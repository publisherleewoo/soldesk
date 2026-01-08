import { Link, useNavigate } from "react-router-dom";
import "./SignUpPage.css";
import { useEffect, useRef, useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { setLoginMember } from "../store/memberSlice";

const SignUpPage = () => {
   //  const [idValCheck] = useState(true); //False로 바꾸기
   const idInput = useRef();
   const pwdInput = useRef();
   const newPwdInput = useRef();
   const newPwdInput2 = useRef();
   const nameInput = useRef();
   const birth_select = useRef();
   const birth_select2 = useRef();
   const birth_select3 = useRef();
   const postCodeInput = useRef();
   const postCodeInput2 = useRef();
   const postCodeInput3 = useRef();
   const fileInput = useRef();
   const [fileInputVal, setFileInputVal] = useState("");
   const dispatch = useDispatch()
   const navi = useNavigate()
   useEffect(() => {
      axios
         .get(
            `http://localhost:9999/member.info.get?member=${sessionStorage.getItem(
               "loginMember"
            )}`
         )
         .then((res) => {
            idInput.current.value = res.data.member.id;
            birth_select.current.value = res.data.member.birth.split("-")[0];
            birth_select2.current.value = Number(
               res.data.member.birth.split("-")[1]
            );
            birth_select3.current.value = Number(
               res.data.member.birth.split("-")[2]
            );
            postCodeInput.current.value = res.data.member.postcode;
            postCodeInput2.current.value = res.data.member.addr.split("∴")[0];
            postCodeInput3.current.value = res.data.member.addr.split("∴")[1];
            nameInput.current.value = res.data.member.name;

            setFileInputVal(res.data.member.filename);
         });
   }, []);

   const handleUpdate = (e) => {
      e.preventDefault();
      const idCut = idInput.current;
      const pwdCut = pwdInput.current;
      const newPwdCut = newPwdInput.current;
      const newPwd2Cut = newPwdInput2.current;
      const birthCut = birth_select.current;
      const birt2hCut = birth_select2.current;
      const birth3Cut = birth_select3.current;
      const postCodeCut = postCodeInput.current;
      const postCode2Cut = postCodeInput2.current;
      const postCode3Cut = postCodeInput3.current;
      const fileCut = fileInput.current;
      const nameCut = nameInput.current;

      if (newPwdCut.value.length < 5 || newPwd2Cut.value.length < 5) {
         alert("비밀번호가 너무 짧습니다. 5글자 이상으로 해주세요.");
         return false;
      }
      if (newPwdCut.value !== newPwd2Cut.value) {
         alert("비밀번호가 다릅니다");
         return false;
      }

      if (
         idCut.value == "" ||
         pwdCut.value == "" ||
         newPwdCut.value == "" ||
         newPwd2Cut.value == "" ||
         nameCut.value == "" ||
         birthCut.value == "" ||
         birt2hCut.value == "" ||
         birth3Cut.value == "" ||
         postCodeCut.value == "" ||
         postCode2Cut.value == "" ||
         postCode3Cut.value == ""
      ) {
         alert("입력창이 비었습니다");
         return false;
      }

      const hangeulRegex = /^[ㄱ-ㅎㅏ-ㅣ가-힣]+$/;

      if (nameCut.value && !hangeulRegex.test(nameCut.value)) {
         alert("이름은 한글만 입력 가능합니다.");
         nameCut.focus();
         return false;
      }

      const fd = new FormData();
      fd.append("id", idCut.value);
      fd.append("pwd", pwdCut.value);
      fd.append("newPwd", newPwdCut.value);
      fd.append("name", nameInput.current.value);
      fd.append(
         "birthday",
         birthCut.value + "-" + birt2hCut.value + "-" + birth3Cut.value
      );
      fd.append("postCode", postCodeCut.value);
      fd.append("addr", postCode2Cut.value + "∴" + postCode3Cut.value);
      fd.append("files", fileCut.files[0]);

      axios
         .post(`http://localhost:9999/member.info.update`, fd, {
            withCredentials: true,
            headers: { "Content-Type": "multupart/form-data" },
         })
         .then((res) => {
            if (res.data.msg === "업데이트 성공") {
               alert("업데이트 성공");
               idCut.value = "";
               pwdCut.value = "";
               newPwdCut.value = "";
               newPwd2Cut.value = "";
               nameInput.current.value = "";
               birthCut.value = "";
               birt2hCut.value = "";
               birth3Cut.value = "";
               postCodeCut.value = "";
               postCode2Cut.value = "";
               postCode3Cut.value = "";
               fileCut.value = "";
            } else {
               alert(res.data.msg);
            }
         })
         .catch((err) => alert(err));
   };

   const nowDate = new Date();
   const currentYear = nowDate.getFullYear();
   const years = [];
   for (let i = currentYear; i >= 1920; i--) {
      years.push(i);
   }
   // id필수,한글x,최대10자,
   // pw필수,4자이상,숫자하나,최대10자
   const months = Array.from({ length: 12 }, (_, i) => i + 1);
   const days = Array.from({ length: 31 }, (_, i) => i + 1);
   const showAdressSearchPopup = () => {
      new window.daum.Postcode({
         oncomplete: function (data) {
            const { zonecode, address } = data;
            postCodeInput.current.value = zonecode;
            postCodeInput2.current.value = address;
         },
      }).open();
   };

   const [preview, setPreview] = useState(null);

   const handleChange = (e) => {
      const file = e.target.files[0];

      if (file) {
         const fileUrl = URL.createObjectURL(file);
         setPreview(fileUrl);
      }
   };

   const handleByd = () => {
      const memberToken = sessionStorage.getItem("loginMember");


      axios
         .get(`http://localhost:9999/member.bye?memberToken=${memberToken}`)
         .then((res) => {
            alert(res.data.msg);
            sessionStorage.removeItem('loginMember')
            dispatch(setLoginMember({}))
            navi('/')

         })
         .catch((err) => {
            alert(err);
         });
   };

   return (
      <div id="JoinWrap">
         <h3>update</h3>

         <div className="row">
            <label>ID</label>
            <input
               type="text"
               className="id_input"
               ref={idInput}
               placeholder="아이디 입력"
               readOnly
            />
         </div>
         <div className="row">
            <label>PW</label>
            <input
               type="password"
               ref={pwdInput}
               placeholder="기존 비밀번호 입력"
            />
         </div>
         <div className="row">
            <label>PW</label>
            <input
               type="password"
               ref={newPwdInput}
               placeholder="새 비밀번호 입력"
            />
         </div>
         <div className="row">
            <label>PW확인</label>
            <input
               type="password"
               ref={newPwdInput2}
               placeholder="새 비밀번호 확인"
            />
         </div>
         <div className="row">
            <label>이름</label>
            <input ref={nameInput} />
         </div>

         <div className="row">
            <label>Birth</label>

            <select ref={birth_select} className="birth_select">
               <option value="">년</option>
               {years.map((y) => (
                  <option key={y} value={y}>
                     {y}
                  </option>
               ))}
            </select>
            <select ref={birth_select2} className="birth_select">
               <option value="">월</option>
               {months.map((m) => (
                  <option key={m} value={m}>
                     {m}
                  </option>
               ))}
            </select>
            <select ref={birth_select3} className="birth_select">
               <option value="">일</option>
               {days.map((d) => (
                  <option key={d} value={d}>
                     {d}
                  </option>
               ))}
            </select>
         </div>

         <div className="row">
            <label>Addr</label>
            <input
               type="text"
               placeholder="우편 번호"
               onClick={showAdressSearchPopup}
               ref={postCodeInput}
            />
            <label>&nbsp;</label>
            <input type="text" ref={postCodeInput2} placeholder="주소" />
            <label>&nbsp;</label>

            <input type="text" ref={postCodeInput3} placeholder="상세주소" />
         </div>

         <div className="row">
            <label>Photo</label>
            {fileInputVal ? (
               <img
                  width="100px"
                  src={`http://localhost:9999/get.file/${fileInputVal}`}
               />
            ) : null}
            <input
               ref={fileInput}
               type="file"
               accept="image/*"
               onChange={handleChange}
            />
            <br />

            {preview ? (
               <img src={preview} alt="미리보기" style={{ width: "100px" }} />
            ) : null}
         </div>

         <div className="btn_area">
            <button type="button" className="submit_btn" onClick={handleUpdate}>
               수정하기
            </button>
            <Link to={-1} className="back_btn">
               뒤로가기
            </Link>
            <button type="button" className="submit_btn" onClick={handleByd}>
               회원탈퇴하기
            </button>
         </div>
      </div>
   );
};

export default SignUpPage;

//id pw 생년월일 주소 프사  유효성검사(id중복체크) 입력받고 가입
