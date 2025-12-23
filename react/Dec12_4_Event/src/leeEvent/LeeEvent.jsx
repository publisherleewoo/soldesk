const test = () => {
   alert("ㅋ");
};

const LeeEvent = () => {
   return (
      <div>
         <input
            onClick={() => {
               alert("누름");
            }}
            onChange={test}
         />
      </div>
   );
};

export default LeeEvent;
