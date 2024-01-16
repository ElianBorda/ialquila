import './App.css';
import Nav from './components/Nav';
import PrincipalContainer from './components/PrincipalContainer';
import Detail from './components/Detail';
import Landing from './components/Landing';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {

  return (
    <BrowserRouter>
      <Nav />
      <Routes>
        <Route path='/' element={<Landing/>}/>
        <Route path='/precios' element={<PrincipalContainer/>} />
        <Route path='/vivienda' element={<Detail/>}/>
        <Route path='/alquiler' />
        <Route path='/venta' />
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
