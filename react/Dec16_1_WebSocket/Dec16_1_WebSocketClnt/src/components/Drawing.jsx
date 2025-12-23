import { useEffect, useRef, useState } from "react";
import io from "socket.io-client";

const socket = io("http://195.168.9.86:9999");

const Drawing = () => {
   const [drawMode, setDrawMode] = useState(false);
   let paper = useRef(null);
   const startXY  = useRef({ x: 0, y: 0 });

   useEffect(() => {
      const pen = paper.current.getContext("2d");
      socket.on("drawInfoSrv", (drawInfo) => {
         pen.beginPath();
         pen.moveTo(drawInfo.sx, drawInfo.sy);
         pen.lineTo(drawInfo.ex, drawInfo.ey);
         pen.closePath();
         pen.stroke();
      });

      return () => {
         socket.off("drawInfoSrv");
      };
   }, []);

   const drawStart = (e) => {
      setDrawMode(true);
      startXY.current = { x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY };
   };

   const draw = (e) => {
      if (drawMode) {
         const endX = e.nativeEvent.offsetX;
         const endY = e.nativeEvent.offsetY;
         socket.emit("drawInfo", {
            sx: startXY.current.x,
            sy: startXY.current.y,
            ex: endX,
            ey: endY,
         });

         startXY.current ={ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY };
      }
   };
   const drawEnd = () => {
      setDrawMode(false);
   };

   const canvasBorder = { border: "2px solid black" };
   return (
      <div>
         <canvas
            ref={paper}
            onMouseDown={drawStart}
            onMouseMove={draw}
            onMouseUp={drawEnd}
            width="300"
            height="400"
            style={canvasBorder}
         ></canvas>
      </div>
   );
};

export default Drawing;
