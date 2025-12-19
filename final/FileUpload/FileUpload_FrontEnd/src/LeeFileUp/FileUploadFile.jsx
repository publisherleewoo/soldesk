import axios from "axios";
import { useRef, useState } from "react";

const FileUploadFile = () => {
   const [photo, setPhoto] = useState({ title: "", file: "" });
   const [result, setResult] = useState({ title: "" });
   const fileInput = useRef();

   const changePhoto = (e) => {
      if (e.target.name === "file") {
         setPhoto({ ...photo, [e.target.name]: e.target.files[0] });
      } else {
         setPhoto({ ...photo, [e.target.name]: e.target.value });
      }
   };

   const photoFormData = new FormData();
   photoFormData.append("title", photo.title);
   photoFormData.append("file", photo.file);

   const uploadPhoto = () => {
      alert(photo.title);
      axios
         .post("http://localhost:9999/photo.upload", photoFormData, {
            withCredentials: true,
            headers: { "Content-Type": "multipart/form-data" },
         })
         .then((res) => {
            setResult(res.data);
            setPhoto({ title: "", file: "" });
            fileInput.current.value = "";
         })
         .catch((err) => {
            alert(err);
         });
   };




   return (
      <div>
         제목
         <input name="title" value={photo.title} onChange={changePhoto} />
         <br />
         <input
            type="file"
            name="file"
            ref={fileInput}
            onChange={changePhoto}
         />
         <br />
         <button onClick={uploadPhoto}>업로드</button>
         <hr />
         업로드한 사진 제목: {result.title} <br/>
         업로드한 사진 파일명 : {result.file} <br/>
         <img src={`http://localhost:9999/photo.get?filename=${result.file}`}/>
      </div>
   );
};

export default FileUploadFile;
