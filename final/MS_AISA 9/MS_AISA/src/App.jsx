import { Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./msAISA/layout/content/home/home";
import SignUpForm from "./msAISA/layout/content/member/signUpForm";
import MSAISAMain from "./msAISA/msAISAMain";

function App() {
   return (
      <Routes>
         <Route element={<MSAISAMain />}>
            <Route index element={<Home />} />
            <Route path="/sign.up.go" element={<SignUpForm />} />
         </Route>
      </Routes>
   );
}

export default App;
