import React from "react";

const LiComponent = ({ i, getMenu }) => {
   return (
      <li
         key={i}
         onClick={() => {
            getMenu(i);
         }}
      >
         {i}
      </li>
   );
};

export default LiComponent;
