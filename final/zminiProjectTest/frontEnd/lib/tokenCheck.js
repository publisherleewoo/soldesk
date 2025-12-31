import axios from "axios"
import { setLoginMember } from "../src/store/memberSlice"


export let tokenCheck = (d)=>{
   axios.get(`http://localhost:9999/member.info.get?member=${sessionStorage.getItem('loginMember')}`).then(res=>{
         d(setLoginMember(res.date.member))
         if(res.data.member ===undefined){
            //로그인풀렸으면
         }else{
            axios.get(`http://localhost:9999/sign.in.exp.refresh?member=${sessionStorage.get('loginMember')}`).then(res=>{
               sessionStorage.getItem(res.data.member)
            })
         }
      })
   }