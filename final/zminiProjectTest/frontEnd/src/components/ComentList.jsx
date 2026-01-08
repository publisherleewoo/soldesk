import React from "react";

const ComentList = ({replyId,replyDate,replyContnet}) => {
   return (
      <div id="comment_list">
         <div className="comment_item">
            <div className="comment_meta">
               <span className="comment_author">{replyId}</span>
               <span className="comment_date">{replyDate}</span>
            </div>
            <p className="comment_text">{replyContnet}</p>
         </div>
      </div>
   );
};

export default ComentList;
