// import './App.css';
import LeeCssFirst from './css/LeeCssFirst';
import LeeCssSecond from './css/LeeCssSecond';
import LeeCSSThird from './css/LeeCSSThird';
import FinalLee from './statement/FinalLee';
import FinalLee0 from './statement/FinalLee0';
import FinalLee2 from './statement/FinalLee2';
import LeePropsFifth from './props/LeePropsFifth';
import LeePropsFirst from './props/LeePropsFirst';
import LeePropsSecond from './props/LeePropsSecond';
import LeePropsThird from './props/LeePropsThird';
import LeeRSFirst from './repeat_stmt/LeeRSFirst';
import LeeRSSceond from './repeat_stmt/LeeRSSceond';
import LeeRSThird from './repeat_stmt/LeeRSThird';
import LeeRSFourth from './repeat_stmt/LeeRSFourth';
import LeeRSFifth from './repeat_stmt/LeeRSFifth';
import ProductBBS from './product/ProductBBS';

function App() {
  return (
    <div className="App">
      <ProductBBS></ProductBBS>
      <hr></hr>
      <br></br>
      <LeeRSFirst></LeeRSFirst>
      <LeeRSSceond></LeeRSSceond>
      <LeeRSThird></LeeRSThird>
      <LeeRSFourth></LeeRSFourth>
      <LeeRSFifth></LeeRSFifth>
      <hr></hr>
      <br></br>
      <FinalLee0></FinalLee0>
      <FinalLee></FinalLee>
      <FinalLee2></FinalLee2>
      <hr></hr>
      <br></br>

      <LeeCssFirst></LeeCssFirst>
      <LeeCssSecond
        c="white" 
        bgc="black" 
        w="100" 
        h="50"
      >ㅋㅋㅋㅋ</LeeCssSecond>
      <LeeCSSThird></LeeCSSThird>

      <hr />
      <LeePropsFirst name="abc" age="30" />
      <LeePropsFirst name="김길동" age="20" />
      <LeePropsSecond name="초코파이" price="5000" />
      <LeePropsSecond name="빼빼로" price="3000" />
      <LeePropsThird price="15000" />
      <LeePropsThird price={3000} />
      <LeePropsFifth>홍길동</LeePropsFifth>
      
    </div>
  );
}

export default App;
