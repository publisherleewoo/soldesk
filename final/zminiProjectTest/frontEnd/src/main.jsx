import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { BrowserRouter } from "react-router-dom";

createRoot(document.getElementById("root")).render(
   // 설정1 전역라우터 사용
   <BrowserRouter>
      <App />
   </BrowserRouter>
);
