import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { BrowserRouter } from "react-router-dom";
import memberSlice  from "./store/memberSlice.js";
import { configureStore } from "@reduxjs/toolkit";
import { Provider } from "react-redux";


const LeeStore = configureStore({
   reducer: {
      ms: memberSlice, 
   },
});

createRoot(document.getElementById("root")).render(
   <Provider store={LeeStore}>
   <BrowserRouter>
      <App />
   </BrowserRouter>
   </Provider>
);
