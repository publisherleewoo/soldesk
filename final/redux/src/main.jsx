import { configureStore } from "@reduxjs/toolkit";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import App from "./App.jsx";
import "./index.css";
import leeSizeSlice  from "./leeSizeSlice.js";
import leeTxtSlice  from "./leeTxtSlice.js";

//설정4. store에 등록된 slice만 사용가능
const LeeStore = configureStore({
   reducer: {
      lss: leeSizeSlice, //lss 호출해서 사용가능
      tss: leeTxtSlice
   },
});

createRoot(document.getElementById("root")).render(
  //설정5. Provider로 감싸고 스토어 등록
   <Provider store={LeeStore}>
      <App />
   </Provider>
);
