
import { useState } from 'react'
import './product.css'
const ProductBBS = () => {
    const [data, setData] = useState([
        { name: "로지텍 G PRO X Superlight", price: 179000 },
        { name: "레이저 Viper V2 Pro", price: 165000 },
        // { name: "로지텍 MX Master 3S", price: 119000 },
        // { name: "앱코 HACKER A660", price: 29900 },
        // { name: "COX CM600", price: 35000 },
        // { name: "삼성전자 SM-G100", price: 15000 },
        // { name: "마이크로소프트 Arc Mouse", price: 85000 },
        // { name: "Corsair Dark Core RGB PRO", price: 99000 },
        // { name: "ASUS ROG Gladius III Wireless", price: 139000 },
        // { name: "Xiaomi Mi Portable Mouse", price: 22000 }
    ])

    const [iptState, setIptState] = useState([
        {name:"",value:""},
        {name:"",value:0}
    ])

    const tdData = data.map((d, i) => <tr className="dataTr" key={i}><td>{d.name}</td><td>{d.price}</td></tr>)

    const changeFunc = (e) => {
        const price = e.target.value
        const name = e.target.name
        setIptState(...iptState, { name:name, price:price })
    }



    return (
        <div id="productBBS">
            품명 : <input className="txtType" name="name" value={iptState.name} onChange={changeFunc} /><br />
            가격 : <input className="txtType" name="price" value={iptState.price} onChange={changeFunc} /><br />
            <button>등록</button>
            <hr />
            <table id="productBBSTbl">
                <thead>
                    <tr>
                        <th>품명</th>
                        <th>가격</th>
                    </tr>
                </thead>
                <tbody>
                    <tr className="dataTr">
                        <td>마우스</td>
                        <td>10000</td>
                    </tr>
                    {tdData}
                </tbody>
            </table>
        </div>
    )
}

export default ProductBBS