import { Route, Routes } from "react-router-dom";
import "./App.css";
import SiteLayout from "./layout/SiteLayout";
import ProductBBS from "./pages/productBBS";
import ProductBBS2 from "./pages/StudentBBS";
import Home from "./pages/Home";

function App() {
   return (
      <>
         <Routes>
            <Route element={<SiteLayout />}>
               <Route path="/" element={<Home />} />
               <Route path="/product.go" element={<ProductBBS />} />
               <Route path="/product2.go" element={<ProductBBS2 />} />
            </Route>
         </Routes>
      </>
   );
}

export default App;
